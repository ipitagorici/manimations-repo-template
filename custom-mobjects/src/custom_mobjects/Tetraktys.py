from manim import *

BORDER_CLR = MAROON
DOTS_CLR = [
    ManimColor("#ffe680"), 
    GREEN, 
    TEAL, 
    ORANGE
]

class Tetraktys(Mobject):
    def __init__(self):
        super().__init__()
        circles = VGroup()
        
        for i in range(0, 4):
            layer = VGroup()
            for _ in range(0, i + 1):
                new_circ = Circle(color=DOTS_CLR[i])
                new_circ.set_fill(DOTS_CLR[i], opacity=1) 
                layer.add(new_circ)

            layer.arrange_in_grid(rows=1, buff=1)
            circles.add(layer)

        circles.arrange_in_grid(cols=1)\
            .move_to(ORIGIN)\
            .scale(.5)
        
        triangle = Polygon(
            circles.get_top(), 
            circles.get_right() + DOWN * 2, 
            circles.get_left() + DOWN * 2)\
                .scale(1.5)\
                .shift(UP * .35)\
                .set_stroke(color=MAROON)
        
        self.triangle = triangle
        self.dots = circles

        tetraktys = VGroup(circles, triangle).scale(.8)
        self.add(tetraktys)

    def get_triangle(self) -> Polygon:
        """
        Gets the border of the Tetraktys
        
        :param self: Description
        :return: A **copy** of the border.
        :rtype: Polygon
        """
        return self.triangle.copy()
    
    def get_dots(self) -> VGroup:
        """
        Gets the 10 dots of the Tetraktys
        
        :param self: Description
        :return: A **copy** of the dots.
        :rtype: VGroup
        """
        return self.dots.copy()
    
    def get_colors(self) -> set[ManimColor]:
        """
        Gets the colors of the Tetraktys (border + dots)
        
        :param self: Description
        :return: A set of colors of all the submobjects of the Tetraktys
        :rtype: set[ManimColor]
        """
        # iterates recursevely over the hierarchy of the submobjects of the Tetraktys;
        # using 'set' in order to remove duplicates (not striclty needed in this case)
        return set(
            m.get_color() 
                for m in self.get_family()   
                if hasattr(m, "get_color")
        )