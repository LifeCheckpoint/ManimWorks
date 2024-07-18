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


class TestScene(Scene):
    def construct(self):
        target_circle = SVGMobject("./images/error.svg", color=GREEN).scale(2)
        self.add(target_circle)
