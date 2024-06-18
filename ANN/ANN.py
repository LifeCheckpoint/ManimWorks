from manimlib import *

class IntroScene(Scene):
    def construct(self):
        road_color = BLUE_E
        road_locs = [
            [(-3, 2, 0), (-3, -5, 0)],
            [(-8, 2, 0), (8, 2, 0)],
            [(3, 2, 0), (3, 5, 0)],
            [(4, 2, 0), (4, -3, 0)],
            [(4, -3, 0), (8, -3, 0)],
            [(4, -3, 0), (1, -3, 0)],
            [(1, -3, 0), (-1, -5, 0)],
            [(-8, 0, 0), (-3, 0, 0)]
        ]
        roads = [Line(loc[0], loc[1], color=road_color, stroke_width=15) for loc in road_locs]

        self.play(AnimationGroup(*[Write(rd) for rd in roads], run_time = 2, lag_ratio = 0.3))





class TestScene(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.play(Write(circle))