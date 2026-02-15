from manim import *

class Inner(Scene):
    def construct(self) -> None:
        self.play(Create(Tex("he")))
        self.next_section("ciao")
        self.play(Create(Tex("hea")))