from manim import *
from custom_mobjects.Tetraktys import Tetraktys

class Second(Scene):
    def construct(self) -> None:
        t = Tetraktys()
        self.add(t)
        self.add(ImageMobject("assets/imgs/pitagorici-aps-logo.png"))