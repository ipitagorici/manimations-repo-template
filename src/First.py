from manim import Tex, Scene

class First(Scene):
    def construct(self) -> None:
        self.add(Tex("Everything should be working!"))