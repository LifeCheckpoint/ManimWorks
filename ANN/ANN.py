from manimlib import *

class EduIntro(Scene):
    def construct(self) -> None:
        svg_edu = SVGMobject("./images/edu.svg", color=BLUE)
        svg_stu = SVGMobject("./images/stu.svg", color=GREEN).scale(0.7)
        stus1 = VGroup(
            svg_stu.move_to(2*RIGHT+2*UP).copy(), 
            svg_stu.move_to(2*RIGHT).copy(), 
            svg_stu.move_to(2*RIGHT+2*DOWN).copy()
        )
        stus2 = VGroup(
            svg_stu.set_color(PURPLE).move_to(4*RIGHT+2*UP).copy(), 
            svg_stu.set_color(PURPLE).move_to(4*RIGHT).copy(), 
            svg_stu.set_color(PURPLE).move_to(4*RIGHT+2*DOWN).copy()
        )
        surrond1 = SurroundingRectangle(stus1)
        surrond2 = SurroundingRectangle(stus2)

        self.play(Write(svg_edu), run_time=5)
        self.wait(1)
        self.play(
            svg_edu.animate.shift(2*LEFT).scale(0.7),
            Write(stus1),
            run_time=2
        )
        self.wait(1)
        self.play(Write(stus2), run_time=2)
        self.play(Write(surrond1), Write(surrond2))
        self.wait(0.5)
        self.play(Uncreate(surrond1), Uncreate(surrond2))
        self.wait(2.5)
        self.play(
            Uncreate(stus1),
            Uncreate(stus2),
            Uncreate(svg_edu)
        )

        svg_arrow = SVGMobject("./images/arrow.svg", color=RED)
        svg_loc = SVGMobject("./images/loc.svg", color=RED).scale(0.4).move_to(2*LEFT+3*RIGHT)
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
        roads = [Line(loc[0], loc[1], color=BLUE_E, stroke_width=15) for loc in road_locs]

        self.wait(1)
        self.play(Write(svg_arrow), run_time=3)
        self.wait(1)
        self.play(
            svg_arrow.animate.scale(0.5).move_to(RIGHT*3+UP*1.2).rotate(90*DEGREES),
            AnimationGroup(*[Write(rd) for rd in roads], run_time=2, lag_ratio=0.3)
        )
        self.play(
            Write(svg_loc),
            svg_arrow.animate.shift(LEFT*3),
            run_time=2,
            lag_ratio=1
        )
        self.wait(2)
        self.play(
            Uncreate(svg_arrow),
            Uncreate(svg_loc),
            AnimationGroup(*[Uncreate(rd) for rd in roads], run_time=2, lag_ratio=0.3)
        )

        svg_house = SVGMobject("./images/house.svg", color=WHITE)
        svg_com = SVGMobject("./images/com.svg", color=RED).scale(0.6)
        svg_search = SVGMobject("./images/search.svg", color=GREEN).scale(0.8).move_to(RIGHT*2+DOWN*6)
        img_4090 = ImageMobject("./images/4090.png").scale(0.4).move_to(RIGHT*10)

        self.wait(1.5)
        self.play(Write(svg_house), run_time=3)
        self.wait(0.5)
        self.play(
            svg_house.animate.scale(1.4),
            Write(svg_com)
        )
        self.wait(1)
        self.add(img_4090)
        self.play(
            svg_house.animate.shift(LEFT*2),
            svg_com.animate.shift(LEFT*2),
            img_4090.animate.move_to(RIGHT*2)
        )
        self.wait(1)
        self.add(svg_search)
        self.play(
            img_4090.animate.shift(UP*6),
            svg_search.animate.shift(UP*6)
        )
        self.wait(9)
        self.play(
            Uncreate(svg_search),
            Uncreate(svg_house),
            Uncreate(svg_com)
        )
        # PR 叠加透明场景 GlassIntroScene
        
        svg_bili = SVGMobject("./images/bili.svg", color=BLUE_B)
        
        self.wait(2)
        self.play(Write(svg_bili), run_time=3)
        self.wait(2)
        self.play(Uncreate(svg_bili))

        svg_lin = SVGMobject("./images/邻.svg", color=WHITE).scale(1.4)

        self.wait(3)
        self.play(FadeIn(svg_lin), run_time=3)
        self.wait(2)
        self.play(svg_lin.animate.set_color(GREY_C))
        self.wait(0.5)

        svg_stu2_1 = SVGMobject("./images/stu.svg", color=GREEN).scale(0.6).move_to(LEFT*2+UP*2)
        svg_stu2_2 = svg_stu2_1.copy().move_to(RIGHT*2+UP*2)
        svg_stu2_3 = svg_stu2_1.copy().set_color(PURPLE*2).move_to(LEFT*2+DOWN*2)
        svg_stu2_4 = svg_stu2_3.copy().move_to(RIGHT*2+DOWN*2)
        arr1 = DoubleArrow(LEFT*1+UP*2, RIGHT*1+UP*2)
        arr2 = arr1.copy().move_to(DOWN*2).rotate(180*DEGREES)
        stu_group = VGroup(svg_stu2_1, svg_stu2_2, svg_stu2_3, svg_stu2_4, arr1, arr2)
        svg_arrow2 = SVGMobject("./images/arrow.svg", color=RED).move_to(RIGHT*4).scale(0.8)

        self.play(
            Write(svg_stu2_1),
            Write(svg_stu2_2),
            Write(arr1),
            lag_ratio=1,
            run_time=2
        )
        self.wait(0.5)
        self.play(
            Write(svg_stu2_3),
            Write(svg_stu2_4),
            Write(arr2),
            lag_ratio=1,
            run_time=2
        )
        self.wait(1)
        self.play(
            stu_group.animate.shift(LEFT*3),
            Write(svg_arrow2)
        )
        self.wait(5)
        self.play(
            Uncreate(stu_group),
            Uncreate(svg_arrow2),
            svg_lin.animate.set_color(WHITE),
            run_time=2
        )
        self.wait(2)

        txt_title = Text("近邻搜索", font="微软雅黑").scale(2)

        self.play(Write(txt_title), run_time=3)
        self.wait(3)
        self.play(Uncreate(txt_title), run_time=2)

class GlassIntroScene(Scene):
    def construct(self) -> None:
        svg_gpt = SVGMobject("./images/gpt.svg", color=WHITE).scale(0.4).move_to(LEFT*3)
        svg_wxyy = SVGMobject("./images/wxyy.svg", color=BLUE).scale(0.4).move_to(LEFT*1)
        svg_tyqw = SVGMobject("./images/tyqw.svg", color=BLUE_B).scale(0.4).move_to(RIGHT*1)
        svg_clau = SVGMobject("./images/clau.svg", color=YELLOW_E).scale(0.4).move_to(RIGHT*3)
        icons = [svg_gpt, svg_wxyy, svg_tyqw, svg_clau]

        self.play(*[Write(icon) for icon in icons], lag_ratio=1, run_time=3)
        self.wait(2)
        self.play(*[Uncreate(icon) for icon in icons], lag_ratio=1, run_time=3)

class DefIntro(Scene):
    def construct(self) -> None:
        txt_title = Text("近邻搜索", font="微软雅黑").scale(2)
        txt_title_en = Text("Nearest Neighbor", font="Jetbrains Mono").scale(0.5).next_to(txt_title, DOWN).align_to(txt_title, LEFT)
        txt_title_en2 = Text("K Nearest Neighbor", font="Jetbrains Mono").scale(0.5).next_to(txt_title, DOWN).align_to(txt_title, LEFT)

        self.play(
            Write(txt_title),
            Write(txt_title_en),
            lag_ratio=1,
            run_time=2
        )
        self.wait(1)
        self.play(txt_title[1].animate.set_color(RED_B))
        self.wait(5)
        txt_title_en2[0].set_color(GREEN)
        self.play(TransformMatchingStrings(txt_title_en, txt_title_en2))
        self.wait(3)
        self.play(Uncreate(txt_title), Uncreate(txt_title_en2))
        
        
        self.wait()

class TestScene(Scene):
    def construct(self):
        txt_title = Text("近邻搜索", font="微软雅黑").scale(2)

        self.play(Write(txt_title), run_time=3)
        self.wait(2)
        self.play(Uncreate(txt_title), run_time=2)
