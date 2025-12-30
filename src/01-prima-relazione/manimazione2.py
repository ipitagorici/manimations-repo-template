from manim import *

class MyScene(Scene):
    def construct(self):
        self.play(Write(Tex("Hello, Earth!")))