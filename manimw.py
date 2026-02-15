#!/usr/bin/env python3
# WARNING: File parzialmente vibe-coded ;)
import argparse
import subprocess
import shutil
import inspect
import importlib.util
from pathlib import Path

RATEOS = {
    "16:9": "1920,1080",
    "16:10": "1920,1200",
    "9:16": "1080,1920"
}

# Mapping Manim quality flags to folder names used in the media directory
QUALITY_MAP = {
    "l": "1080p15",
    "m": "1080p30",
    "h": "1080p60"
}

def get_scene_classes(file_path):
    """
    Parses a python file and returns a list of class names 
    that likely inherit from Manim's Scene.
    """
    scenes = []
    with open(file_path, "r") as f:
        content = f.read()
        # Look for 'class Name(Scene):' or 'class Name(other):'
        # This is a simple regex approach to avoid complex imports
        import re
        matches = re.findall(r"class\s+(\w+)\s*\((?:\w*Scene\w*)\)", content)
        for m in matches:
            scenes.append(m)
    return scenes

def has_sections(file_path):
    """Checks if the file contains any section definitions."""
    with open(file_path, "r") as f:
        return "self.next_section(" in f.read()

def run_manim(source_path: Path, scene_name: str, args):
    """Handles the heavy lifting for a single scene."""
    # Check for sections logic
    use_sections = has_sections(source_path)
    
    res_args = [ 
        "-r", RATEOS.get(args.ratio, RATEOS.get("16:9")),
        f"-q{args.quality}"
    ]
    
    if use_sections:
        res_args.append("--save_sections")

    preview_flag = "-p" if not args.all else ""
    cmd = ["uv", "run", "manim", preview_flag] + res_args + [str(source_path), scene_name]
    
    print() # new line
    print(f"🔺 Rendering {scene_name} from {source_path.name} {'(with sections)' if use_sections else ''}...")
    result = subprocess.run([c for c in cmd if c], capture_output=True)

    if result.returncode == 0:
        cwd = Path.cwd()
        try:
            rel_parts = list(source_path.parent.parts)
            if rel_parts and rel_parts[0] == "src":
                rel_parts.pop(0)
            export_dir = cwd / "exports" / Path(*rel_parts)
        except ValueError:
            export_dir = cwd / "exports"
            
        export_dir.mkdir(parents=True, exist_ok=True)

        media_dir = cwd / "media"
        
        # 1. Handle Sections if they were generated
        if use_sections:
            # Path: media/videos/<filename_stem>/<quality_folder>/sections/
            quality_folder = QUALITY_MAP.get(args.quality, "1080p30")
            section_src = media_dir / "videos" / source_path.stem / quality_folder / "sections"
            if section_src.exists():
                dest_sec_dir = export_dir / scene_name
                if dest_sec_dir.exists():
                    shutil.rmtree(dest_sec_dir)
                
                # Move the entire sections folder to exports/<SceneName>/
                shutil.move(str(section_src), str(dest_sec_dir))
                print(f"✅ Saved sections to: {dest_sec_dir}")
                return
        
        # Move the latest file matching the extension
        media_dir = cwd / "media"
        candidates_ext = [ ".png", ".mp4" ]
        candidates: list[Path] = []
        for ext in candidates_ext:
            candidates.extend(media_dir.glob(f"**/*{ext}"))
        
        found_files = sorted(
            [f for f in candidates],
            key=lambda x: x.stat().st_mtime, 
            reverse=True
        )

        if found_files:
            latest_file = found_files[0]
            dest_path = export_dir / f"{scene_name}{latest_file.suffix}"
            shutil.move(str(latest_file), str(dest_path))
            print(f"✅ Saved to: {dest_path}")
    else:
        print(f"❌ Error rendering '{scene_name}'")
        print(f"Reason: {result.stderr}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", nargs="?", help="Path to the manim .py file")
    parser.add_argument("scene", nargs="?", help="Specific Scene class")
    parser.add_argument("-a", "--all", action="store_true", help="Compile everything in src/")
    parser.add_argument("-r", "--ratio", choices=["16:9", "16:10"], default="16:9")
    parser.add_argument("-q", "--quality", default="m", choices=["l", "m", "h"], help=r"Choose the quality of the rendering {l: low, m: medium, h: high}")
    parser.add_argument("-m", "--media", action="store_true", default=False, help="Choose to keep media/ folder (default: False)")
    args = parser.parse_args()
    
    if args.all:
        src_dir = Path("src")
        if not src_dir.exists():
            print("Error: 'src' directory not found.")
            return

        py_files = list(src_dir.glob("**/*.py"))
        for py_file in py_files:
            # Skip dunder files
            if py_file.name.startswith("__"): continue
            
            scenes = get_scene_classes(py_file)

            for scene in scenes:
                run_manim(py_file, scene, args)
            
    elif args.file:
        scene = args.scene if args.scene else get_scene_classes(Path(args.file))[0]
        run_manim(Path(args.file), scene, args)
    else:
        print("Please provide a file or use --all")
        return

    # Final cleanup
    if Path("media").exists() and not args.media:
        shutil.rmtree("media")
        print("\n🧹 Media folder cleared.")

if __name__ == "__main__":
    main()