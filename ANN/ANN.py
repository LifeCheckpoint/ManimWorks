from manimlib import *
import random as ran
import math as m
import numpy as np

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
loc_pts1 = [
    (-4.62, 2.88, 0),
    (-2.18, 0.82, 0),
    (-3.6, 1.22, 0),
    (-2.58, 2.32, 0),
    (-1.42, -1.34, 0),
    (4.34, 1.34, 0),
    (2.32, 0.34, 0),
    (3.16, -1, 0),
    (3.62, 0.28, 0),
    (-5, -2.18, 0),
    (5.04, -2.58, 0)
]

def get_dash_circle(num_points=1000, color=GREY, dash_nums=3, width=0.006) -> VGroup:
    # 通过模拟虚线点进行绘制，避开 Manim DashedVMobject BUG，较慢
    is_dash = lambda idx: (idx%int(num_points/dash_nums))>num_points/dash_nums/2
    pts = [Circle().move_to((m.cos(theta), m.sin(theta), 0)).set_color(color).scale(width if is_dash(i) else 0) for i, theta in enumerate(np.arange(0, 2*PI, 1/num_points))]
    return VGroup(*pts)

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

        self.play(
            Uncreate(svg_lin),
            Write(txt_title), 
            run_time=3
        )
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
        txt_title2 = Text("K近邻搜索", font="微软雅黑").scale(2).align_to(txt_title, LEFT)
        txt_title3 = Text("K邻近近邻搜索", font="微软雅黑").scale(2).align_to(txt_title, LEFT)
        txt_title_en = Text("Nearest Neighbor", font="Jetbrains Mono").scale(0.5).next_to(txt_title, DOWN).align_to(txt_title, LEFT)
        txt_title_en2 = Text("K Nearest Neighbor", font="Jetbrains Mono").scale(0.5).next_to(txt_title, DOWN).align_to(txt_title, LEFT)
        txt_title_en3 = Text("K Approximate Nearest Neighbor", font="Jetbrains Mono").scale(0.5).next_to(txt_title, DOWN).align_to(txt_title, LEFT)
        sep = Line(UP*1,DOWN*1, stroke=1).align_to(txt_title, LEFT).shift(LEFT*0.5+DOWN*0.3)
        txt_ann = Text("ANN", font="Jetbrains Mono").scale(2)

        self.play(
            Write(sep),
            Write(txt_title),
            Write(txt_title_en),
            lag_ratio=1,
            run_time=2
        )
        self.wait(1)
        self.play(txt_title[1].animate.set_color(RED_B))
        self.wait(5)
        txt_title_en2[0].set_color(GREEN)
        txt_title2[0].set_color(GREEN)
        self.play(
            TransformMatchingStrings(txt_title_en, txt_title_en2),
            TransformMatchingStrings(txt_title, txt_title2, key_map={"近邻搜索": "近邻搜索"})
        )
        self.wait(3)
        txt_title_en3[1:12].set_color(BLUE)
        txt_title3[1:3].set_color(BLUE)
        self.play(
            TransformMatchingStrings(txt_title_en2, txt_title_en3),
            TransformMatchingStrings(txt_title2, txt_title3, key_map={"近邻搜索": "近邻搜索", "K": "K"})
        )
        self.wait(3)
        self.play(
            TransformMatchingStrings(txt_title_en3, txt_ann, key_map={"A": "A", "N": "N"}), 
            Uncreate(txt_title3), 
            Uncreate(sep)
        )
        self.wait(3)
        self.play(Uncreate(txt_ann))
        
        pts = [Circle().move_to(loc).scale(0.05).set_color(RED if loc[0]<0 else YELLOW) for loc in loc_pts1]
        loc_line = []
        for _ in range(8): loc_line.append(ran.choices(loc_pts1, k=2))
        lines = [Line(loc_line[i][0], loc_line[i][1], buff=0.2) for i in range(8)]

        self.wait(1)
        self.play(*[FadeIn(pt) for pt in pts], lag_ratio=1, run_time=3)
        self.play(*[Write(l) for l in lines], lag_ratio=1, run_time=3)
        self.wait(3)
        self.play(
            *[Uncreate(pt) for pt in pts],
            *[Uncreate(l) for l in lines],
            lag_ratio=0.6,
            run_time=2
        )
        self.wait(3)

class TraditionAlgo(Scene):
    def construct(self) -> None:
        svg_stu = SVGMobject("./images/stu.svg", color=GREEN).scale(0.5)
        svg_stus = [svg_stu.copy().set_color(rgb_to_color([ran.randint(0, 255)/255, ran.randint(0, 255)/255, ran.randint(0, 255)/255])) for _ in range(9)]
        placeholder = Rectangle(1, 1).move_to(RIGHT*1)
        grid_stu = VGroup()
        for i in range(3):
            for j in range(3):
                svg_stus[i*3 + j].move_to(np.array([j - 1, 1 - i, 0]))  # 3x3 grid
                grid_stu.add(svg_stus[i*3 + j])
        line_match = DoubleArrow(LEFT*2, RIGHT*1, buff=0.8)
        rec1 = SurroundingRectangle(svg_stu).shift(LEFT*2)
        rec2 = SurroundingRectangle(placeholder)
        
        self.play(Write(svg_stu))
        self.wait(2)
        grid_stu.shift(RIGHT * 2)
        self.play(
            Write(grid_stu),
            svg_stu.animate.scale(0.7).shift(LEFT*2),
            lag_ratio=1,
            run_time=3
        )
        self.play(Write(line_match))
        self.play(
            Write(rec1),
            Write(rec2),
            lag_ratio=1
        )
        self.wait(1)
        self.play(Uncreate(rec1), Uncreate(rec2))
        self.wait(2)
        self.play(Uncreate(grid_stu))

        score_paper = Rectangle(4, 5.5).move_to(RIGHT*3)
        svg_score = SVGMobject("./images/score.svg", color=WHITE).scale(1.3).move_to(RIGHT*3+DOWN*0.2)
        svg_APlus = SVGMobject("./images/A+.svg").set_stroke(color=RED).scale(0.5).move_to(RIGHT*4+UP*2)

        self.play(svg_stu.animate.shift(LEFT*0.5), Write(score_paper))
        self.play(
            Write(svg_score),
            Write(svg_APlus),
            lag_ratio=1
        )
        self.wait(2)
        self.play(
            Uncreate(svg_stu),
            Uncreate(score_paper),
            Uncreate(svg_APlus),
            svg_score.animate.move_to(LEFT*3).scale(0.4),
            run_time=3
        )
        
        mat_score = Matrix([
            ["", "Ch", "Ma", "En", "Ph"],
            ["A", "101", "95", "133", "65"],
            ["1", "84", "130", "107", "80"],
            ["2", "149", "146", "128", "71"],
            ["3", "98", "101", "96", "59"],
            ["4", "55", "66", "77", "25"]
        ]).move_to(RIGHT*3.5).scale(0.5).set_color(WHITE)
        ax = Axes(x_range=(0, 5), y_range=(0, 1)).scale(0.17)
        axs = [ax.copy().move_to(RIGHT*3+UP*(i-2)*1.3) for i in range(5)]
        axs_g = VGroup(*axs)
        ptss = []
        for i in range(5):
            for sub in range(4):
                loc_p = axs[i].coords_to_point(sub+1, ran.random(), 0)
                ptss.append(Circle().scale(0.025).move_to(loc_p+RIGHT*3+UP*(i-2)*1.3))

        self.wait(1)
        self.play(Write(mat_score), run_time=3)
        self.wait(3)
        self.play(TransformMatchingShapes(mat_score, axs_g), run_time=2)
        self.wait(1)
        self.play(*[Write(p) for p in ptss], lag_ratio=1, run_time=2)
        self.wait(1)
        self.play(*[p.animate.shift(UP*0.3*ran.random()) for p in ptss], lag_ratio=1, run_time=2.5)
        self.play(*[p.animate.shift(DOWN*0.3*ran.random()) for p in ptss], lag_ratio=1, run_time=2.5)
        self.play(*[p.animate.shift(UP*0.3*ran.random()) for p in ptss], lag_ratio=1, run_time=2.5)
        self.wait(2)

        txt_A = MTex("(101,95\\,,133,65\\,)").move_to(RIGHT*3+UP*2*1.3).set_color(BLUE_A)
        txt_1 = MTex("(84\\,,130,107,80\\,)").move_to(RIGHT*3+UP*1*1.3)
        txt_2 = MTex("(149,146,128,71\,)").move_to(RIGHT*3)
        txt_3 = MTex("(98\\,,101,96\\,,59\\,)").move_to(RIGHT*3+DOWN*1*1.3)
        txt_4 = MTex("(55\\,,66\\,,77\\,,25\\,)").move_to(RIGHT*3+DOWN*2*1.3)
        txt_vecs = [MTex(txt).move_to(RIGHT*2+UP*1.5) for txt in ["x=101", "y=95", "z=133", "m=65"]]
        [t.align_to(txt_vecs[0], LEFT).shift(DOWN*(i+1)) for i, t in enumerate(txt_vecs[1:4])]

        self.play(
            *[Uncreate(p) for p in ptss],
            TransformMatchingShapes(axs[4], txt_A),
            TransformMatchingShapes(axs[3], txt_1),
            TransformMatchingShapes(axs[2], txt_2),
            TransformMatchingShapes(axs[1], txt_3),
            TransformMatchingShapes(axs[0], txt_4),
            lag_ratio=1,
            run_time=2
        )
        self.wait(3)
        self.play(
            txt_A.animate.move_to(LEFT*2),
            Uncreate(svg_score),
            Uncreate(line_match),
            Uncreate(txt_1),
            Uncreate(txt_2),
            Uncreate(txt_3),
            Uncreate(txt_4),
            run_time=2
        )
        txt_A2 = txt_A.copy()
        self.add(txt_A2)
        self.play(
            *[TransformMatchingStrings(txt_A, txt_vecs[i]) for i in range(4)],
            run_time=2
        )
        self.wait(3)
        self.play(*[Uncreate(txt_vecs[i]) for i in range(4)], txt_A2.animate.move_to(ORIGIN))
        self.wait(2)
        self.play(Uncreate(txt_A2))
        mat_score.move_to(ORIGIN).scale(2)
        self.play(Write(mat_score))
        self.wait(1)
        self.play(mat_score.animate.shift(LEFT*2+UP*0.2))
        self.wait(1)
        

# continue

class TraditionAlgo2(Scene):
    def construct(self) -> None:
        mat_score = Matrix([
            ["", "Ch", "Ma", "En", "Ph"],
            ["A", "101", "95", "133", "65"],
            ["1", "84", "130", "107", "80"],
            ["2", "149", "146", "128", "71"],
            ["3", "98", "101", "96", "59"],
            ["4", "55", "66", "77", "25"]
        ]).move_to(LEFT*3+UP*0.2).set_color(WHITE)
        arrs = [Arrow(RIGHT*0.5, RIGHT*1.2).next_to(mat_score, RIGHT).shift((0.4-i*0.8)*UP) for i in range(4)]
        txt_d = [MTex(txt).next_to(arrs[i], RIGHT).match_y(arrs[i]) for i, txt in enumerate(["d=49.143", "d=70.470", "d=38.079", "d=87.710"])]
        mat_group = VGroup(mat_score, *arrs, *txt_d)
        map_d_tex = {"101": BLUE_A, "95": BLUE_A, "133": BLUE_A, "65": BLUE_A}
        txt_d1 = Tex("\\sqrt{(101-84)^2+(95-130)^2+(133-107)^2+(65-80)^2}").scale(0.6).set_color_by_tex_to_color_map(map_d_tex).move_to(RIGHT*2+DOWN*2)
        txt_d2 = Tex("\\sqrt{(101-149)^2+(95-146)^2+(133-128)^2+(65-71)^2}").scale(0.6).set_color_by_tex_to_color_map(map_d_tex).move_to(RIGHT*2+DOWN*2)
        txt_d3 = Tex("\\sqrt{(101-98)^2+(95-101)^2+(133-96)^2+(65-59)^2}").scale(0.6).set_color_by_tex_to_color_map(map_d_tex).move_to(RIGHT*2+DOWN*2)
        txt_d4 = Tex("\\sqrt{(101-55)^2+(95-66)^2+(133-77)^2+(65-25)^2}").scale(0.6).set_color_by_tex_to_color_map(map_d_tex).move_to(RIGHT*2+DOWN*2)
        highlight_rec = Rectangle(6, 0.6).set_color(GREEN_B)
        d_key_map = {"101": "101", "95": "95", "133": "133", "65": "65"}
        
        self.add(mat_score)
        self.play(
            *[Write(arr) for arr in arrs], 
            *[Write(txt) for txt in txt_d], 
            run_time=2
        )
        self.wait(1)
        self.play(mat_group.animate.scale(0.6).shift(LEFT*2+UP*2))
        self.wait(2)
        highlight_rec.move_to(arrs[0].get_center()).shift(LEFT*1.2)
        self.play(Write(highlight_rec), Write(txt_d1))
        self.wait(1)
        self.play(highlight_rec.animate.shift(0.48*DOWN), TransformMatchingShapes(txt_d1, txt_d2, key_map=d_key_map))
        self.wait(1)
        self.play(highlight_rec.animate.shift(0.48*DOWN), TransformMatchingShapes(txt_d2, txt_d3, key_map=d_key_map))
        self.wait(1)
        self.play(highlight_rec.animate.shift(0.48*DOWN), TransformMatchingShapes(txt_d3, txt_d4, key_map=d_key_map))
        self.wait(2)
        txt_d3.set_color(YELLOW)
        self.play(highlight_rec.animate.shift(0.48*UP).set_color(YELLOW), TransformMatchingShapes(txt_d4, txt_d3, key_map=d_key_map))
        self.wait(3)
        self.play(
            Uncreate(mat_group),
            Uncreate(txt_d3),
            Uncreate(highlight_rec),
            run_time=2
        )
        self.wait(3)

        txt_ann = Text("ANN", font="Jetbrains Mono").scale(3)
        svg_q = SVGMobject("./images/ask.svg", color=BLUE_B).scale(1.6)

        self.play(Write(txt_ann))
        self.wait(1)
        self.play(txt_ann.animate.set_color(GREY), FadeIn(svg_q))
        self.wait(3)
        self.play(Uncreate(txt_ann), Uncreate(svg_q))
        self.wait(2)

        txt_N = Text("N", font="Jetbrains Mono").scale(2)
        txt_K = Text("K", font="Jetbrains Mono").scale(2).move_to(RIGHT*0.5)
        txt_NtimesK = Text("N×K", font="Jetbrains Mono").scale(2)
        txt_sq = Tex("O(N^2)").scale(2).set_color(RED)
        txt_no_big = Text("大量级数据", font="微软雅黑").scale(2)

        self.play(Write(txt_N))
        self.wait(2)
        self.play(txt_N.animate.shift(LEFT*0.5), Write(txt_K))
        self.wait(2)
        self.play(TransformMatchingShapes(VGroup(txt_N, txt_K), txt_NtimesK))
        self.wait(1)
        self.play(txt_NtimesK[0].animate.set_color(RED), txt_NtimesK[2].animate.set_color(RED))
        self.wait(1.5)
        self.play(TransformMatchingShapes(txt_NtimesK, txt_sq))
        self.wait(2)
        self.play(TransformMatchingShapes(txt_sq, txt_no_big))
        self.wait(1)
        self.play(txt_no_big.animate.set_color(RED))
        self.wait(2)
        self.play(Uncreate(txt_no_big))
        self.wait(1)

loc_pts2 = [
    (2, 3, 0),
    (5, 4, 0),
    (9, 6, 0),
    (4, 7, 0),
    (8, 1, 0),
    (7, 2, 0)
]
loc_pts3=[
    (2, 4, 0),
    (3, 5, 0),
    (6, 9, 0),
    (0, 0, 1),
    (5, 5, 0),
    (4, 1, 0),
    (8, 8, 0),
    (1, 7, 0),
    (3, 6, 0)
]
loc_pts4=[
    (4, 5, 0),
    (3, 2, 0)
]

class KDTree(Scene):
    def construct(self) -> None:
        txt_tra = Text("传统算法", font="微软雅黑").set_color(GREY).scale(1.4)
        txt_kd = Text("K-D 树", font="微软雅黑").set_color(GREEN_A).scale(1.4).move_to(LEFT*2)
        txt_kd_en = Text("K-D Tree", font="Jetbrains Mono").set_color(GREEN_A).scale(0.4).next_to(txt_kd, DOWN).align_to(txt_kd, LEFT)
        txt_r = Text("R 树", font="微软雅黑").set_color(BLUE_A).scale(1.4).move_to(RIGHT*2)
        txt_r_en = Text("R Tree", font="Jetbrains Mono").set_color(BLUE_A).scale(0.4).next_to(txt_r, DOWN).align_to(txt_r, LEFT)
        txt_kd_group = VGroup(txt_kd, txt_kd_en)

        self.play(Write(txt_tra))
        self.wait(2)
        self.play(Uncreate(txt_tra))
        self.wait(1)
        self.play(Write(txt_kd))
        self.play(Write(txt_kd_en))
        self.wait(1)
        self.play(Write(txt_r))
        self.play(Write(txt_r_en))
        self.wait(2)
        self.play(
            Uncreate(txt_r), 
            Uncreate(txt_r_en),
            txt_kd_group.animate.move_to(ORIGIN).scale(1.2)
        )
        self.wait(2)
        self.play(txt_kd_group.animate.to_edge(LEFT+UP).scale(0.5))
        self.wait(2)

        txt_k_d_space = Text("K维空间", font="微软雅黑").set_color(ORANGE)
        ax = Axes(x_range=(0, 10), y_range=(0, 10), width=5, height=5)
        c2p = lambda loc1, loc2: ax.coords_to_point(loc1, loc2, 0)
        ptss = [Circle().scale(0.05).move_to(ax.coords_to_point(*loc)) for loc in loc_pts2]

        self.play(Write(txt_k_d_space))
        self.wait(3)
        self.play(
            txt_k_d_space.animate.to_edge(RIGHT+UP).scale(0.8),
            Write(ax)
        )
        self.play(*[Write(pt) for pt in ptss], lag_ratio=1, run_time=3)
        self.wait(2)

        getSepline = lambda loc1, loc2: Line(c2p(*loc1), c2p(*loc2)).set_color(YELLOW)
        seplines = [getSepline(l1, l2) for l1, l2 in [
            ((5, 0), (5, 10)),
            ((0, 4), (5, 4)),
            ((10, 2), (5, 2))
        ]]

        self.play(Write(seplines[0]))
        self.wait(1.5)
        self.play(Write(seplines[1]))
        self.wait(1.5)
        self.play(Write(seplines[2]))
        self.wait(2)

        pt_target = Square(0.08).move_to(c2p(8, 3)).set_color(GREEN_B)
        dist1 = m.sqrt(sum((c2p(8, 3)-c2p(9, 6))**2))
        target_circle = get_dash_circle().move_to(c2p(8, 3)).scale(dist1)
        mask_rec_width = abs(c2p(0, 0)[0] - c2p(5, 10)[0])
        mask_rec_height = abs(c2p(0, 0)[1] - c2p(5, 10)[1])
        mask_rec = Rectangle(fill_opacity=0.5, width=mask_rec_width, height=mask_rec_height).set_color(RED).move_to(c2p(2.5, 5))
        highlight_p1 = SurroundingRectangle(ptss[2]).set_color(PURPLE_A)
        highlight_p2 = SurroundingRectangle(ptss[4]).set_color(PURPLE_A)
        highlight_p3 = SurroundingRectangle(ptss[5]).set_color(PURPLE_A)
        res_line1 = Line(c2p(7, 2), c2p(8, 3), buff=0.2).set_color(GREEN_E)

        self.play(Write(pt_target))
        self.play(Rotate(pt_target, 45*DEGREES))
        self.wait(1)
        self.play(Write(mask_rec))
        self.wait(2)
        self.play(FadeInFromPoint(target_circle, c2p(8, 3)))
        self.play(Rotate(target_circle, 45*DEGREES), run_time=4, rate_func=linear)
        self.play(Write(highlight_p1))
        self.wait(1)
        self.play(Uncreate(highlight_p1))
        self.wait(1)
        self.play(target_circle.animate.scale(m.sqrt(2)/m.sqrt(10)))
        self.play(Rotate(target_circle, -45*DEGREES), run_time=3, rate_func=linear)
        self.play(Write(highlight_p2), Write(highlight_p3))
        self.wait(1)
        self.play(Uncreate(highlight_p2), Uncreate(highlight_p3))
        self.wait(1)
        self.play(FadeOutToPoint(target_circle, c2p(8, 3)))
        self.play(Write(res_line1))
        self.wait(4)

        txt_o_square_n = Tex("O(N^2)").scale(2).set_color(RED)
        txt_o_kd_search = Tex("O(N^{1-\\frac{1}{k}})").scale(2).set_color(GREEN)

        self.play(
            FadeOut(mask_rec),
            ax.animate.set_opacity(0.4),
            *[line.animate.set_opacity(0.4) for line in seplines],
            *[p.animate.set_opacity(0.4) for p in ptss],
            Write(txt_o_square_n),
            run_time=3
        )
        self.wait(2.5)
        self.play(TransformMatchingShapes(txt_o_square_n, txt_o_kd_search), run_time=2)
        self.wait(2.5)
        self.play(Uncreate(txt_o_kd_search))
        self.wait(3)
        self.play(Write(mask_rec))
        self.play(FadeOut(mask_rec), run_time=0.5)
        self.play(FadeIn(mask_rec), run_time=0.5)
        self.play(FadeOut(mask_rec), run_time=0.5)
        self.play(FadeIn(mask_rec), run_time=0.5)
        self.wait(3)

        txt_exact_algo = Text("精确算法", font="微软雅黑").scale(2).set_color(GREEN)
        txt_exact_algo_en = Text("exact algorithm", font="Jetbrains Mono").scale(0.6).set_color(GREEN).next_to(txt_exact_algo, DOWN).align_to(txt_exact_algo, LEFT)

        self.play(Write(txt_exact_algo), Write(txt_exact_algo_en))
        self.wait(3)
        self.play(
            ax.animate.set_opacity(1),
            *[line.animate.set_opacity(1) for line in seplines],
            *[p.animate.set_opacity(1) for p in ptss],
            Uncreate(txt_exact_algo),
            Uncreate(txt_exact_algo_en),
            run_time=2
        )

        ptss2 = [Circle().scale(0.05).move_to(ax.coords_to_point(*loc)) for loc in loc_pts3]
        svg_right = SVGMobject("./images/right.svg", color=GREEN).scale(2)
        svg_error = SVGMobject("./images/error.svg", color=RED, ).scale(0.2).move_to(ptss[3].get_center())

        self.play(*[Write(p) for p in ptss2], Uncreate(mask_rec), lag_ratio=1, run_time=3)
        self.wait(3)
        self.play(
            ax.animate.set_opacity(0.4),
            *[p.animate.set_opacity(0.4) for p in ptss],
            *[p.animate.set_opacity(0.4) for p in ptss2],
            Write(svg_right)
        )
        self.wait(2)
        self.play(
            ax.animate.set_opacity(1),
            *[p.animate.set_opacity(1) for p in ptss],
            *[p.animate.set_opacity(1) for p in ptss2],
            Uncreate(svg_right)
        )
        self.wait(2)
        self.play(FadeIn(highlight_p1), FadeIn(ptss[5]), run_time=0.5)
        self.play(FadeOut(highlight_p1), FadeOut(ptss[5]), run_time=0.5)
        self.play(FadeIn(highlight_p1), FadeIn(ptss[5]), run_time=0.5)
        self.play(FadeOut(highlight_p1), FadeOut(ptss[5]), run_time=0.5)
        self.wait(3)
        self.play(FadeIn(svg_error), run_time=0.5)
        self.play(FadeOut(svg_error), run_time=0.5)
        self.play(FadeIn(svg_error), run_time=0.5)
        self.play(FadeOut(svg_error), run_time=0.5)
        self.wait(3)

        txt_sqrt = Text("根号重构", font="微软雅黑").set_color(PINK).shift(LEFT*2)
        txt_bin = Text("二进制分组", font="微软雅黑").set_color(GOLD_A).shift(RIGHT*2)
        txt_dim = Text("维度灾难", font="微软雅黑").scale(2).set_color(RED)

        self.play(
            ax.animate.set_opacity(0.4),
            *[p.animate.set_opacity(0.4) for p in ptss],
            *[p.animate.set_opacity(0.4) for p in ptss2],
            Write(txt_sqrt)
        )
        self.play(Write(txt_bin))
        self.wait(4)
        self.play(TransformMatchingShapes(VGroup(txt_bin, txt_sqrt), txt_dim), run_time=2)
        self.wait(2)
        self.play(
            Uncreate(ax),
            Uncreate(res_line1),
            Uncreate(pt_target),
            *[Uncreate(l) for l in seplines],
            *[Uncreate(p) for p in ptss],
            *[Uncreate(p) for p in ptss2],
            Uncreate(txt_dim),
            Uncreate(txt_k_d_space)
        )
        self.wait(1)
        self.play(FadeOut(VGroup(txt_kd, txt_kd_en)))
        self.wait(1)

class RTree(Scene):
    def construct(self) -> None:
        def get_wh(loc1, loc2, buff=0.1):
            return {
                "width": abs((ax.coords_to_point(*loc1) - ax.coords_to_point(*loc2))[0]) + buff*2, 
                "height": abs((ax.coords_to_point(*loc1) - ax.coords_to_point(*loc2))[1]) + buff*2
            }
        def get_recs(locs, color, buff=0.1):
            grecs = [Rectangle(**get_wh(loc1, loc2, buff)) for loc1, loc2 in locs]
            center = lambda loc: ax.coords_to_point(*(np.array(loc[0])+np.array(loc[1]))/2)
            return [r.move_to(center(loc)).set_color(color) for r, loc in zip(grecs, locs)]

        txt_r = Text("R 树", font="微软雅黑").set_color(BLUE_A).scale(1.4)
        ax = Axes(x_range=(0, 10), y_range=(0, 10), width=5, height=5)
        loc_pts2.extend(loc_pts3)
        ptss = [Circle().scale(0.05).move_to(ax.coords_to_point(*loc)) for loc in loc_pts2]

        self.play(Write(txt_r))
        self.wait(5)
        self.play(txt_r.animate.to_edge(LEFT+UP).scale(0.5))
        self.play(Write(ax))
        self.play(*[Write(p) for p in ptss], lag_ratio=1, run_time=3)
        self.wait(2)

        rec_locs1 = [
            ((1, 7), (5, 3)),
            ((6, 9), (9, 1)),
            ((0, 0), (4, 1))
        ]
        rec_locs2 = [
            ((6, 9), (9, 6)),
            ((1, 7), (4, 6)),
            ((2, 3), (5, 5)),
            ((7, 2), (8, 1))
        ]
        rec_locs3 = [
            ((2, 3), (3, 5)),
            ((6, 9), (8, 8))
        ]
        recs1 = get_recs(rec_locs1, YELLOW)
        recs2 = get_recs(rec_locs2, GREEN, 0.07)
        recs3 = get_recs(rec_locs3, PINK, 0.04)

        self.play(*[Write(r) for r in recs1], lag_ratio=1, run_time=3)
        self.wait(2)
        self.play(*[Write(r) for r in recs2], lag_ratio=1, run_time=3)
        self.wait(2)
        self.play(*[Write(r) for r in recs3], lag_ratio=1, run_time=3)
        self.wait(2)

        svg_insert = Tex("+", font="Jetbrains Mono").set_color(GREEN_D)
        ptss_insert = [Circle().scale(0.05).move_to(ax.coords_to_point(*loc)).set_color(GREEN) for loc in loc_pts4]
        svg_error = SVGMobject("./images/error.svg", color=RED, ).scale(0.2).move_to(ptss[4].get_center())
        recs2_idx_3_new = get_recs([((7, 2), (8, 2))], GREEN, 0.07)[0]
        recs1_idx_0_new = get_recs([((1, 7), (5, 2))], YELLOW, 0.07)[0]

        self.play(Write(svg_insert))
        self.play(svg_insert.animate.move_to(ax.coords_to_point(*loc_pts4[0])))
        self.play(Write(ptss_insert[0]))
        self.wait(1)
        self.play(svg_insert.animate.move_to(ax.coords_to_point(*loc_pts4[1])))
        self.play(Write(ptss_insert[1]))
        self.play(Transform(recs1[0], recs1_idx_0_new))
        self.wait(1)
        self.play(svg_insert.animate.move_to(ORIGIN))
        self.wait(1)
        self.play(Uncreate(svg_insert))
        self.wait(2.5)
        self.play(FadeIn(svg_error))
        self.play(FadeOut(svg_error))
        self.play(FadeIn(svg_error))
        self.play(FadeOut(svg_error))
        self.play(FadeOut(ptss[4]))
        self.play(Transform(recs2[3], recs2_idx_3_new))
        self.wait(5)
        self.play(
            FadeOut(ax),
            *[FadeOut(p) for i, p in enumerate(ptss) if i!=4],
            *[FadeOut(p) for p in ptss_insert],
        )
        self.wait(1)

        # rec_screen = [r for r in self.mobjects if isinstance(r, Rectangle) and r not in [recs1[0], recs2[3]]]
        rec_screen = [r for r in self.mobjects if isinstance(r, Rectangle)]
        rec_screen.extend([recs1_idx_0_new ,recs2_idx_3_new])

        self.play(*[rect.animate.move_to((-4.5+i)*RIGHT).scale(0.5) for i, rect in enumerate(rec_screen)], lag_ratio=0.8, run_time=4)
        self.wait(1)
        self.play(*[Rotate(rec, 10*DEGREES) for rec in rec_screen])
        self.play(*[Rotate(rec, -10*DEGREES) for rec in rec_screen])
        self.wait(4)
        self.play(*[Uncreate(rec) for rec in rec_screen], Uncreate(txt_r))

class DimCAxe1(Scene):
    def construct(self) -> None:
        ax = NumberLine(x_range=[0, 10])
        pt = Circle(fill_color=RED).set_opacity(1).scale(0.1).move_to(ax.number_to_point(3)+UP*0.2)

        self.play(Write(ax))
        self.wait(1)
        self.play(Write(pt))

class DimCAxe2(Scene):
    def construct(self) -> None:
        ax = Axes(x_range=[0, 10], y_range=[0, 10], width=6, height=6)
        pt = Circle(fill_color=RED).set_opacity(1).scale(0.1).move_to(ax.coords_to_point(3, 4))

        self.play(Write(ax))
        self.wait(1)
        self.play(Write(pt))

class DimCAxe3(Scene):
    def construct(self) -> None:
        ax = ThreeDAxes(x_range=[0, 10], y_range=[0, 10], z_range=[0, 10], width=6, height=6, depth=6).scale(0.6)
        pt = Circle(fill_color=RED).set_opacity(1).scale(0.1).move_to(ax.coords_to_point(3, 4, 5))
        frame = self.camera.frame

        self.play(Write(ax))
        self.wait(1)
        self.play(Write(pt))
        self.wait(1)
        self.play(frame.animate.set_orientation(Rotation([0, 0.13, 0.13, 0.98])), run_time=2)

class DimC1(Scene):
    def construct(self) -> None:
        txt_dc = Text("维度灾难", font="微软雅黑").set_color(RED_E).scale(2)
        txt_dc2 = Text("维度诅咒", font="微软雅黑").set_color(RED_E).scale(2.48)
        txt_dc_en = Text("Curse of Dimensionality", font="Jetbrains Mono").set_color(RED).scale(0.6).next_to(txt_dc, DOWN).align_to(txt_dc, LEFT)
        txt_group = VGroup(txt_dc2, txt_dc_en)
        img_bellman = ImageMobject("./images/bellman.png").scale(0.8).shift(LEFT*8)
        txt_bellman = Text("Richard Bellman", font="Jetbrains Mono").scale(0.5)
        arr1 = SVGMobject("./images/to_right.svg").set_color(WHITE).scale(0.4).move_to(LEFT*2.5)
        arr2 = SVGMobject("./images/to_right.svg").set_color(WHITE).scale(0.4).move_to(RIGHT*2.5)

        self.play(Write(txt_dc), Write(txt_dc_en))

        self.wait(2)
        self.play(ReplacementTransform(txt_dc, txt_dc2))
        self.wait(2)
        self.add()
        self.play(txt_group.animate.scale(0.7).shift(RIGHT*2.5), img_bellman.animate.move_to(LEFT*2))
        txt_bellman.next_to(img_bellman, DOWN).align_to(img_bellman, LEFT)
        self.play(Write(txt_bellman))
        self.wait(2)
        self.play(Uncreate(txt_dc2), Uncreate(txt_dc_en), FadeOut(img_bellman), Uncreate(txt_bellman))
        self.wait(4)
        self.play(Write(arr1))
        self.wait(2)
        self.play(Write(arr2))
        self.wait(4)

        svg_bug = SVGMobject("./images/bug.svg", color=YELLOW)
        
        self.play(Write(svg_bug), arr1.animate.set_opacity(0.4), arr2.animate.set_opacity(0.4))
        self.wait(3)
        self.play(Uncreate(svg_bug), Uncreate(arr1), Uncreate(arr2))

        pt1 = Circle().scale(0.1).move_to(np.array([-2.3, 1.6, 0])).set_color(BLUE)
        pt2 = Circle().scale(0.1).move_to(np.array([1.7, -1, 0])).set_color(BLUE)
        pt3 = Circle().scale(0.1).move_to(np.array([-1.6, 2.5, 0])).set_color(RED)
        pt4 = Circle().scale(0.1).move_to(np.array([1.1, 0.9, 0])).set_color(RED)
        l1 = DashedLine(pt1.get_center(), pt2.get_center(), buff=0.2).set_color(GREY)
        l2 = DashedLine(pt1.get_center(), pt3.get_center(), buff=0.2).set_color(GREY)
        l3 = DashedLine(pt2.get_center(), pt4.get_center(), buff=0.2).set_color(GREY)
        pt_group1 = VGroup(pt1, pt2, pt3, pt4, l1, l2, l3).scale(0.8).shift(RIGHT*0.5+DOWN)
        arr3 = SVGMobject("./images/to_right.svg").set_color(BLUE).scale(0.4)
        pt5 = Circle().scale(0.1).move_to(np.array([-1.1, 1, 0])).set_color(BLUE)
        pt6 = Circle().scale(0.1).move_to(np.array([1.2, -1, 0])).set_color(BLUE)
        pt7 = Circle().scale(0.1).move_to(np.array([-0.9, -0.8, 0])).set_color(BLUE)
        pt8 = Circle().scale(0.1).move_to(np.array([1.1, 0.9, 0])).set_color(BLUE)
        l4 = DashedLine(pt5.get_center(), pt6.get_center(), buff=0.2).set_color(GREY)
        l5 = DashedLine(pt5.get_center(), pt7.get_center(), buff=0.2).set_color(GREY)
        l6 = DashedLine(pt5.get_center(), pt8.get_center(), buff=0.2).set_color(GREY)
        l7 = DashedLine(pt6.get_center(), pt7.get_center(), buff=0.2).set_color(GREY)
        l8 = DashedLine(pt6.get_center(), pt8.get_center(), buff=0.2).set_color(GREY)
        l9 = DashedLine(pt7.get_center(), pt8.get_center(), buff=0.2).set_color(GREY)
        pt_group2 = VGroup(pt5, pt6, pt7, pt8, l4, l5, l6, l7, l8, l9).move_to(RIGHT*2.5)

        self.wait(2)
        self.play(Write(pt_group1))
        self.wait(3)
        self.play(pt_group1.animate.scale(0.8).shift(LEFT*2.5))
        self.wait(1)
        self.play(Write(arr3))
        self.wait(1)
        self.play(Write(pt_group2))
        self.wait(3.5)
        self.play(Uncreate(pt_group1), Uncreate(pt_group2), Uncreate(arr3))

# 只有线条的立方体
def get_cubeLine(side_length=2, **kwargs):
    edges = [
        (0, 1), (0, 2), (0, 4),
        (1, 3), (1, 5),
        (2, 3), (2, 6),
        (3, 7),
        (4, 5), (4, 6),
        (5, 7),
        (6, 7)
    ]
    half_side = side_length / 2
    vertices, lines = [], []
    for x in [-half_side, half_side]:
        for y in [-half_side, half_side]:
            for z in [-half_side, half_side]:
                vertices.append([x, y, z])
    for edge in edges:
        lines.append(Line(vertices[edge[0]], vertices[edge[1]], **kwargs))
    return VGroup(*lines)

class DimC2(Scene):
    def construct(self) -> None:
        txt_dim_n = Text("n维空间", font="微软雅黑").set_color(YELLOW).fix_in_frame()
        cube = Cube(side_length=2).move_to(LEFT*2).set_color(BLUE).set_opacity(0.6)
        sphere = Sphere(radius=1).move_to(RIGHT*2).set_color(GREEN)
        frame = self.camera.frame
        label_cube = Text("Width = 2").scale(0.8).next_to(cube, OUT).set_color(BLUE_A)
        label_sphere = Text("diameter = 2").scale(0.8).next_to(sphere, OUT).set_color(GREEN_A)
        
        self.play(Write(txt_dim_n))
        self.wait(2)
        self.play(txt_dim_n.animate.scale(0.7).to_edge(UP+LEFT))
        self.wait(1.5)
        self.play(ShowCreation(cube))
        self.play(Write(label_cube))
        self.wait(1)
        self.play(ShowCreation(sphere))
        self.play(Write(label_sphere))
        self.wait(1)
        self.play(
            frame.animate.set_orientation(Rotation([0.774, 0.117, 0.093, 0.614])),
            Rotate(label_cube, 90*DEGREES, RIGHT),
            Rotate(label_sphere, 90*DEGREES, RIGHT),
            run_time=2
        )

        tex_vc = Tex("V_c=2^n").move_to(LEFT*2).scale(0.6).next_to(cube, IN).rotate(90*DEGREES, RIGHT).set_color(BLUE_A)
        tex_vs = Tex("V_s=\\frac{\\pi^\\frac{n}{2}}{\\Gamma\\left(\\frac{n}{2}+1\\right)}").move_to(RIGHT*2).scale(0.6).next_to(sphere, IN).rotate(90*DEGREES, RIGHT).set_color(GREEN_A)
        tex_gamma = Tex("\\Gamma\\left(x\\right)=(x-1)!\\,\\left(x\\in\\mathbb{N}\\right)").scale(0.6).next_to((sphere.get_center()+cube.get_center())/2, IN, buff=2.5).rotate(90*DEGREES, RIGHT)
        isolate_tex_frac = [
            "\\frac{\\pi^\\frac{n}{2}}{\\Gamma\\left(\\frac{n}{2}+1\\right)}",
            "2^n",
            "V_s",
            "V_c"
        ]
        tex_frac = Tex("\\frac{V_s}{V_c}="+isolate_tex_frac[0]).scale(0.6).next_to((sphere.get_center()+cube.get_center())/2, IN, buff=2.5).rotate(90*DEGREES, RIGHT)
        tex_frac_lim = Tex("\\lim_{n\\rightarrow\\infty}\\frac{V_s}{V_c}="+isolate_tex_frac[0]).scale(0.6).next_to((sphere.get_center()+cube.get_center())/2, IN, buff=2.5).rotate(90*DEGREES, RIGHT)
        tex_frac_lim2 = Tex("\\lim_{n\\rightarrow\\infty}\\frac{V_s}{V_c}\\rightarrow 0").scale(0.6).next_to((sphere.get_center()+cube.get_center())/2, IN, buff=2.5).rotate(90*DEGREES, RIGHT)
        
        self.wait(2)
        self.play(Write(tex_vc))
        self.play(Write(tex_vs))
        self.wait(2)
        self.play(Write(tex_gamma))
        self.wait(3)
        self.play(Uncreate(tex_gamma))
        self.play(Write(tex_frac))
        self.wait(2)
        self.play(ReplacementTransform(tex_frac, tex_frac_lim))
        self.wait(3)
        self.play(ReplacementTransform(tex_frac_lim, tex_frac_lim2))
        self.wait(3)
        self.play(
            frame.animate.set_orientation(Rotation([0, 0, 0, 0.001])),
            tex_frac_lim2.animate.move_to(ORIGIN),
            Rotate(tex_frac_lim2, -90*DEGREES, RIGHT),
            Uncreate(tex_vc),
            Uncreate(tex_vs),
            Uncreate(label_cube),
            Uncreate(label_sphere),
            Uncreate(cube),
            Uncreate(sphere)
        )
        self.play(tex_frac_lim2.animate.scale(2))
        self.wait(3)
        self.play(FadeOut(tex_frac_lim2), FadeOut(txt_dim_n))
        
# 以下内容正倒放两次

class DimCRatio1(Scene):
    def construct(self) -> None:
        sq = Line(LEFT*1, RIGHT*1).move_to(LEFT*2).set_color(BLUE_A)
        txt_sq = Text("Cube n=1", font="Jetbrains Mono").next_to(sq, UP).scale(0.4).set_color(BLUE_A)
        sp = Line(LEFT*1, RIGHT*1).move_to(RIGHT*2).set_color(GREEN_A)
        txt_sp = Text("Sphere n=1", font="Jetbrains Mono").next_to(sp, UP).scale(0.4).set_color(GREEN_A)
        ratio = Tex("\\frac{V_s}{V_c}=1").shift(DOWN*2)

        self.play(Write(sq), Write(txt_sq))
        self.wait(1)
        self.play(Write(sp), Write(txt_sp))
        self.wait(1)
        self.play(sq.animate.shift(RIGHT*2), sp.animate.shift(LEFT*2))
        self.wait(2)
        self.play(Write(ratio))
        self.wait(2)

class DimCRatio2(Scene):
    def construct(self) -> None:
        sq = Square().move_to(LEFT*2).set_color(BLUE_A)
        txt_sq = Text("Cube n=2", font="Jetbrains Mono").next_to(sq, UP).scale(0.4).set_color(BLUE_A)
        sp = Circle().move_to(RIGHT*2).set_color(GREEN_A)
        txt_sp = Text("Sphere n=2", font="Jetbrains Mono").next_to(sp, UP).scale(0.4).set_color(GREEN_A)
        ratio = Tex("\\frac{V_s}{V_c}=\\frac{\\pi}{4}").shift(DOWN*2)

        self.play(Write(sq), Write(txt_sq))
        self.wait(1)
        self.play(Write(sp), Write(txt_sp))
        self.wait(1)
        self.play(sq.animate.shift(RIGHT*2), sp.animate.shift(LEFT*2))
        self.wait(2)
        self.play(Write(ratio))
        self.wait(2)

class DimCRatio3(Scene):
    def construct(self) -> None:
        self.camera.frame.set_orientation(Rotation([0.15, 0.117, 0.093, 0.614]))
        sq = get_cubeLine(side_length=2).move_to(LEFT*2).set_color(BLUE_A)
        txt_sq = Text("Cube n=2", font="Jetbrains Mono").next_to(sq, OUT).scale(0.4).set_color(BLUE_A)
        sp = Sphere(radius=1).move_to(RIGHT*2).set_color(GREEN_A)
        txt_sp = Text("Sphere n=2", font="Jetbrains Mono").next_to(sp, OUT).scale(0.4).set_color(GREEN_A)
        ratio = Tex("\\frac{V_s}{V_c}=\\frac{\\pi}{6}").shift(DOWN*2)

        self.play(ShowCreation(sq), Write(txt_sq))
        self.wait(1)
        self.play(ShowCreation(sp), Write(txt_sp))
        self.wait(1)
        self.play(sq.animate.shift(RIGHT*2), sp.animate.shift(LEFT*2))
        self.wait(2)
        self.play(Write(ratio))
        self.wait(2)

def get_corner_of_sphere_and_cube(side="UL", **kwargs):
    l1 = Line(np.array([-1, 1, 0]), np.array([-1, 0, 0]), **kwargs)
    l2 = Line(np.array([-1, 1, 0]), np.array([0, 1, 0]), **kwargs)
    quarter_circle = Arc(90*DEGREES, 90*DEGREES, **kwargs)
    rotation = {"UL": 0, "DL": 90, "DR": 180, "UR": 270}
    return VGroup(l1, l2, quarter_circle).rotate(rotation[side]*DEGREES, about_point=ORIGIN)

loc_pts5 = [
    [-0.83, 0.89, 0],
    [-0.48, 0.68, 0],
    [-0.72, 0.45, 0],
    [-0.44, 0.04, 0],
    [-0.70, -0.22, 0],
    [-0.41, -0.43, 0],
    [-0.72, -0.63, 0],
    [-0.20, 0.60, 0],
    [0.40, 0.40, 0],
    [0.41, 0.04, 0],
    [-0.04, -0.29, 0],
    [0.29, -0.56, 0],
    [-0.15, -0.84, 0],
    [0.62, -0.90, 0],
    [0.83, -0.33, 0],
    [0.76, 0.02, 0],
    [0.87, 0.68, 0],
    [0.40, 0.80, 0],
    [0.20, 0.60, 0]
]

class DimC3(Scene):
    def construct(self) -> None:
        sq = Square().move_to(LEFT*2).set_color(BLUE_A)
        txt_sq = Text("Cube", font="Jetbrains Mono").next_to(sq, UP).scale(0.4).set_color(BLUE_A)
        sp = Circle().move_to(RIGHT*2).set_color(GREEN_A)
        txt_sp = Text("Sphere", font="Jetbrains Mono").next_to(sp, UP).scale(0.4).set_color(GREEN_A)
        corners = [get_corner_of_sphere_and_cube(side, color=YELLOW) for side in ["UL", "DL", "DR", "UR"]]
        corners_group = VGroup(*corners)
        ptss = [Circle().scale(0.05).move_to(loc).set_color(random_color()) for loc in loc_pts5]
        ptss_group = VGroup(*ptss)
        ptss_group2 = VGroup(*[p.copy() for p in ptss])
        ptss_group2.move_to(RIGHT*2)
        frame = self.camera.frame
        tex_r1 = Tex("Ratio=1").scale(0.6)
        tex_r2 = Tex("Ratio=\\frac{3}{19}").scale(0.6).shift(UP*1.5)
        tex_r3 = Tex("Ratio=\\frac{6}{19}").scale(0.6).shift(UP*2.5).fix_in_frame()
        sq_3 = get_cubeLine(color=BLUE_A)
        sp_3 = Sphere(color=GREEN_A, opacity=0.8)

        self.play(Write(sq), Write(sp))
        self.wait(0.5)
        self.play(Write(txt_sq), Write(txt_sp))
        self.wait(2)
        self.play(sq.animate.move_to(ORIGIN), sp.animate.move_to(ORIGIN))
        self.play(Uncreate(txt_sq), Uncreate(txt_sp))
        self.wait(2)
        self.play(*[Write(c) for c in corners])
        self.wait(2)
        self.play(
            sq.animate.shift(LEFT*2), 
            sp.animate.shift(LEFT*2), 
            corners_group.animate.shift(RIGHT*2)
        )
        self.wait(0.5)
        self.play(*[c.animate.scale(0.8) for c in corners])
        self.play(corners_group.animate.scale(1.1))
        self.wait(2)
        self.play(
            FadeOut(corners_group),
            sq.animate.shift(RIGHT*2), 
            sp.animate.shift(RIGHT*2)
        )
        self.wait(1)
        self.play(frame.animate.set_phi(90*DEGREES))
        self.wait(1)
        self.play(LaggedStart(*[Write(p.rotate(90*DEGREES, LEFT).scale(1.25)) for p in ptss_group], lag_ratio=0.1))
        self.wait(1.5)  
        self.play(Write(tex_r1.rotate(90*DEGREES, RIGHT).shift(OUT*0.5)))
        self.wait(2)
        self.play(
            frame.animate.set_phi(0.01),
            tex_r1.animate.rotate(90*DEGREES, LEFT).move_to(UP*1.5),
            LaggedStart(*[p.animate.rotate(-90*DEGREES, RIGHT).scale(0.8) for p in ptss_group], lag_ratio=0.1),
            run_time=3
        )
        self.wait(1)
        self.play(ReplacementTransform(tex_r1, tex_r2))
        self.wait(2)
        self.play(ReplacementTransform(sq, sq_3))
        self.wait(1)
        self.play(
            frame.animate.set_orientation(Rotation([0.774, 0.117, 0.093, 0.614])),
            *[p.animate.shift(OUT*(ran.random()*2-1)).rotate(90*DEGREES, LEFT) for p in ptss],
            FadeOut(tex_r2),
            run_time=3.5
        )
        self.wait(1)
        self.play(
            FadeIn(tex_r3),
            frame.animate.rotate(180*DEGREES, UP+RIGHT+OUT),
            FadeOut(sp),
            FadeIn(sp_3),
            run_time=5
        )
        self.wait(2)
        self.play(FadeOut(sp_3))
        self.play(
            FadeOut(sq_3),
            FadeOut(ptss_group),
            FadeOut(tex_r3)
        )
        
class DimC4(Scene):
    def construct(self) -> None:
        imgs_dis = [ImageMobject(f"./images/dis_{i}.png").shift(DOWN*0.5).scale(1.2) for i in range(2, 11)]
        bar = Line(UP*3+LEFT*5, UP*3+RIGHT*5)
        bar_f = [Line(UP*3+LEFT*5, UP*3+LEFT*5.01+RIGHT*i*10/8).set_color(GREEN) for i in range(9)]
        bar_button = Circle().scale(0.15).move_to(UP*3+LEFT*5).set_color(RED)
        txt_dim = [Text(f"Dim = {d}", font="Jetbrains mono").scale(0.5).shift(UP*3.3) for d in range(2, 11)]
        
        self.play(Write(bar), Write(bar_button), Write(txt_dim[0]))
        self.add(bar_f[0])
        self.play(FadeIn(imgs_dis[0]), run_time=2)
        self.wait(2)
        for i in range(len(imgs_dis)-1):
            self.play(
                FadeIn(imgs_dis[i+1]),
                TransformMatchingStrings(txt_dim[i], txt_dim[i+1]),
                bar_button.animate.shift(RIGHT*10/8),
                ReplacementTransform(bar_f[i], bar_f[i+1])
            )
            self.wait(0.5)
        self.wait(2)

        # 此处做快速回退和重放

        self.remove(bar)
        [self.remove(imgs_dis[i]) for i in range(len(imgs_dis)-1)]
        self.play(
            Uncreate(bar_f[len(bar_f)-1]), 
            Uncreate(bar_button), 
            FadeOut(imgs_dis[len(imgs_dis)-1]), 
            Uncreate(txt_dim[len(txt_dim)-1])
        )
        self.wait(2)

        txt_1 = Text("精确性", font="微软雅黑").scale(0.7).set_color(GREY)
        txt_2 = Text("暴力计算", font="微软雅黑").scale(0.7).set_color(RED_E)
        txt_3 = Tex("k>10").scale(0.7).set_color(BLUE)
        highlight = SurroundingRectangle(txt_2).set_color(YELLOW).shift(UP*0.6)

        # Use AE more...
        self.play(FadeIn(txt_1))
        self.wait(4)
        self.play(txt_1.animate.shift(UP*0.6).scale(0.9), FadeIn(txt_2))
        self.wait(3)
        self.play(txt_1.animate.shift(UP*0.6).scale(0.9), txt_2.animate.shift(UP*0.6).scale(0.9), FadeIn(txt_3))
        self.wait(3)
        self.play(Write(highlight))
        self.wait(2)
        self.play(FadeOut(txt_1), FadeOut(txt_2), FadeOut(txt_3), FadeOut(highlight))
        self.wait(1)

class LittleSummary(Scene):
    def construct(self) -> None:
        txt_1 = Text("精确性", font="微软雅黑").scale(0.7).set_color(GREY)
        ax = Axes(x_range=(0, 5), y_range=(0, 5)).scale(0.8)
        label_x, label_y = ax.get_x_axis_label("Computation").scale(0.5), ax.get_y_axis_label("Precision").scale(0.5)
        relation_line = ax.get_graph(lambda x: m.log(x+1), (0, 5)).set_color_by_gradient(GREEN, YELLOW, RED)

        self.wait(3)
        self.play(Write(txt_1))
        self.wait(2)
        self.play(
            txt_1.animate.shift(UP*3),
            Write(ax),
            Write(label_x),
            Write(label_y)
        )
        self.wait(1)
        self.play(Write(relation_line))
        self.wait(4)
        self.play(Uncreate(label_x), Uncreate(label_y), Uncreate(ax), Uncreate(relation_line), Uncreate(txt_1))

class NextPart(Scene):
    def construct(self) -> None:
        pass

class TestScene(Scene):
    def construct(self):
        pass
