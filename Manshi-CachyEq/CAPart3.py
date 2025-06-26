from manimlib import *
import re
import numpy as np
import sys
sys.path.append(".")

from extra_animation import (
    tex_typing_animate,
    animate_scaling_exponential_decay, 
    animate_scaling_smooth, 
    animate_scaling_linear, 
    animate_shift_smooth,
    homotopic_showin
)

def debugTeX(self: Scene, texm: Tex, scale_factor=0.4, text_color=PURPLE):
    for i, j in enumerate(texm):
        tex_id = Text(str(i), font="Consolas").scale(scale_factor).set_color(text_color)
        tex_id.move_to(j)
        self.add(tex_id)

class Test(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        pass
        # get the index of Tex
        # uv run manimgl CAPart1.py Test -s

        tex = tex_new1_cauchy_n = Tex("f(n\\sqrt{2})=na").scale(0.9)
        self.add(tex)
        debugTeX(self, tex)

        
class CAPart3_1(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_xy_f = {
            "x": RED,
            "y": GREEN,
            "k": YELLOW_B,
            "f": BLUE,
            "n": PINK,
            "(": WHITE,
            ")": WHITE,
            "+": WHITE,
            "-": WHITE,
            "\\left(": WHITE,
            "\\right)": WHITE
        }
        tex_cauchy = Tex("f(x)+f(y)=f(x+y)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 4.5 + UP * 3.2).scale(0.9)
        axes = Axes(
            x_range=(-8, 8),
            y_range=(-4, 4),
            height=8,
            width=16,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
        )
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        lambda_tracker = ValueTracker(0)
        delta_tracker = ValueTracker(0)
        k_tracker = ValueTracker(1)
        def kx_piecewise_homo_sin(k, x, delta, lamb):
            # if delta != 0:
            #     mask = [0 if elem else 1 for elem in np.abs(np.floor(x) - x) < 0.1]
            # else:
            #     mask = np.ones_like(x)
            # value = (k * x + np.floor(x) * delta) * lamb + (1 - lamb) * np.sin(x)
            # return mask * value
            value = (k * x + np.floor(x) * delta) * lamb + (1 - lamb) * np.sin(x)
            return value
        func_graph = axes.get_graph(
            lambda x: kx_piecewise_homo_sin(k_tracker.get_value(), x, delta_tracker.get_value(), lambda_tracker.get_value()),
            use_smoothing=False,
            color=BLUE,
            bind=True
        )
        func_label = axes.get_graph_label(func_graph, label='f(x)', x=3.5, color=BLUE, direction=UP, buff=1)
        icon_wrong = Tex("\\times").scale(2).set_color_by_tex_to_color_map({"\\times": RED_B}).move_to(DOWN * 1)
        patho_image = Rectangle(20, 20).set_color(BLUE_B).set_fill(opacity=0.5)
        text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A)
        text_axiom_choice = Text("选择公理", font="微软雅黑").scale(1).set_color_by_text_to_color_map({"选择": GREEN, "公理": WHITE}).move_to(LEFT * 2 + DOWN * 1)
        text_axion_choice_en = Text("Axiom of Choice").scale(0.5).set_color(GREY_B).move_to(DOWN * 1.4).align_to(text_axiom_choice, LEFT)
        text_hamel_basis = Text("Hamel 基", font="微软雅黑").scale(1).move_to(RIGHT * 2 + DOWN * 1)

        self.play(
            FadeIn(tex_cauchy),
            Write(axes, lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(func_graph),
            Write(func_label),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            lambda_tracker.animate.set_value(1),
            run_time=2
        )
        self.wait(1)
        self.play(
            delta_tracker.animate.set_value(0.3),
            k_tracker.animate.set_value(0.5),
            run_time=1
        )
        self.play(
            delta_tracker.animate.set_value(0),
            run_time=1
        )
        self.wait(2)
        self.play(
            tex_cauchy.animate.move_to(UP * 0.5),
            FadeOut(func_graph),
            FadeOut(func_label),
            axes.animate.set_opacity(0.3),
        )
        self.wait(1.5)
        self.play(
            FadeIn(icon_wrong),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            icon_wrong.animate.shift(DOWN * 1).set_opacity(0),
            axes.animate.set_opacity(1),
        )
        self.wait(1)
        flashtime = 0.5
        self.play(FadeIn(patho_image), run_time=flashtime)
        self.wait(0.5)
        self.play(FadeOut(patho_image), run_time=flashtime)
        self.play(FadeIn(patho_image), run_time=flashtime)
        self.wait(0.5)
        self.play(FadeOut(patho_image), run_time=flashtime)
        self.play(FadeOut(axes))
        text_continuous.next_to(tex_cauchy, DOWN).set_opacity(0).shift(UP * 0.3)
        red_del_line = Line(text_continuous.get_left() + LEFT * 0.1, text_continuous.get_right() + RIGHT * 0.1).set_color(RED).shift(DOWN * text_continuous.get_height() / 2 + DOWN * 0.05)
        self.add(text_continuous)
        self.play(
            text_continuous.animate.set_opacity(1).shift(DOWN * 0.3),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(red_del_line),
            run_time=0.5
        )
        self.wait(1.5)
        self.play(
            FadeOut(text_continuous),
            FadeOut(red_del_line),
        )
        self.play(
            Write(text_axiom_choice),
            Write(text_axion_choice_en)
        )
        self.wait(1.5)
        self.play(
            Write(text_hamel_basis),
        )
        self.wait(3)
        self.play(
            FadeOut(VGroup(
                text_axiom_choice, text_axion_choice_en, text_hamel_basis, tex_cauchy
            ))
        )
        self.wait(1)

class CAPart3_2_1(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_xy_f = {
            "x": RED, "y": GREEN, "k": YELLOW_B, "a": RED_A,
            "f": BLUE, "g": BLUE_D,
            "(": WHITE, ")": WHITE,
            "+": WHITE, "-": WHITE,
            "\\mathrm{e}": WHITE,
            "\\left(": WHITE, "\\right)": WHITE, "\\ln": WHITE
        }
        colormap_xy_1 = {
            "x": RED, "y": GREEN, "k": YELLOW_B, "a": RED_A,
            "n": PINK, "q": PINK,
            "f": BLUE, "g": BLUE_D,
            "(": WHITE, ")": WHITE,
            "+": WHITE, "-": WHITE,
            "\\mathrm{e}": WHITE,
            "\\left(": WHITE, "\\right)": WHITE, "\\ln": WHITE
        }
        tex_cauchy = Tex("f(x)+f(y)=f(x+y)").move_to(LEFT * 4.5 + UP * 3.2).scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_fx = Tex("f(x)").scale(1.1).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_f_sq2 = Tex("f(\\sqrt{2})").scale(1.1).set_color_by_tex_to_color_map(colormap_xy_f | {"\\sqrt{2}": RED})
        tex_f_sq2_eq_a = Tex("f(\\sqrt{2})=a").scale(1.1).set_color_by_tex_to_color_map(colormap_xy_f | {"\\sqrt{2}": RED})
        tex_cauchy_x_sq2 = Tex("f(\\sqrt{2})+f(y)=f(\\sqrt{2}+y)").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [2, 3, 4, 14, 15, 16]:
            tex_cauchy_x_sq2[i].set_color(RED)
        tex_cauchy_x_y_sq2 = Tex("f(\\sqrt{2})+f(\\sqrt{2})=f(\\sqrt{2}+\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [2, 3, 4, 16, 17, 18]:
            tex_cauchy_x_y_sq2[i].set_color(RED)
        for i in [9, 10, 11, 20, 21, 22]:
            tex_cauchy_x_y_sq2[i].set_color(GREEN)
        tex_cauchy_sim1 = Tex("f(\\sqrt{2})+f(\\sqrt{2})=f(2\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [2, 3, 4]:
            tex_cauchy_sim1[i].set_color(RED)
        for i in [9, 10, 11]:
            tex_cauchy_sim1[i].set_color(GREEN)
        tex_cauchy_sim2 = Tex("2f(\\sqrt{2})=f(2\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_cauchy_sim3 = Tex("f(2\\sqrt{2})=2f(\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_cauchy_sim4 = Tex("f(2\\sqrt{2})=2a").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)

        tex_new1_cauchy_x_2sq2 = Tex("f(2\\sqrt{2})+f(y)=f(2\\sqrt{2}+y)").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [2, 3, 4, 5, 15, 16, 17, 18]:
            tex_new1_cauchy_x_2sq2[i].set_color(RED)
        tex_new1_cauchy_x_y_2sq2 = Tex("f(2\\sqrt{2})+f(\\sqrt{2})=f(2\\sqrt{2}+\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [2, 3, 4, 5, 17, 18, 19, 20]:
            tex_new1_cauchy_x_y_2sq2[i].set_color(RED)
        for i in [10, 11, 12, 13, 22, 23, 24, 25]:
            tex_new1_cauchy_x_y_2sq2[i].set_color(GREEN)
        tex_new1_cauchy_sim1 = Tex("f(2\\sqrt{2})+f(\\sqrt{2})=f(3\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [2, 3, 4, 5]:
            tex_new1_cauchy_sim1[i].set_color(RED)
        for i in [10, 11, 12]:
            tex_new1_cauchy_sim1[i].set_color(GREEN)
        tex_new1_cauchy_sim2 = Tex("f(3\\sqrt{2})=f(2\\sqrt{2})+f(\\sqrt{2})").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        for i in [10, 11, 12, 13]:
            tex_new1_cauchy_sim2[i].set_color(RED)
        for i in [18, 19, 20]:
            tex_new1_cauchy_sim2[i].set_color(GREEN)
        tex_new1_cauchy_sim3 = Tex("f(3\\sqrt{2})=2a+a").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_new1_cauchy_sim4 = Tex("f(3\\sqrt{2})=3a").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_new1_cauchy_4_to_100 = [Tex("f(" + str(i) +"\\sqrt{2})=" + str(i) + "a").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_f) for i in range(4, 101)]
        tex_new1_cauchy_n = Tex("f(n\\sqrt{2})=na").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_1 | {"\\sqrt{2}": WHITE})
        tex_new1_cauchy_q = Tex("f(q\\sqrt{2})=qa").scale(0.9).set_color_by_tex_to_color_map(colormap_xy_1).set_opacity(0).shift(DOWN)

        axes = Axes(
            x_range=(-8, 8),
            y_range=(-4, 4),
            height=8,
            width=16,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
        )
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        opa = 0.1
        opa2 = 0.5
        axes.set_opacity(opa)
        line_kx = DashedLine(LEFT * 10 * np.sqrt(2) + DOWN * 10, RIGHT * 10 * np.sqrt(2) + UP * 10, color=BLUE, stroke_width=2).set_opacity(opa2)
        point_sq2s_pos = [Dot(axes.c2p(np.sqrt(2) * i, i), color=YELLOW, radius=0.08).set_opacity(opa2) for i in range(1, 20)]
        point_sq2s_neg = [Dot(axes.c2p(-np.sqrt(2) * i, -i), color=YELLOW, radius=0.08).set_opacity(opa2) for i in range(1, 20)]
        point_random = []
        for _ in range(200):
            ran_pos = random.random() * 12
            point_random.append(
                Dot(
                    axes.c2p(
                        -np.sqrt(2) * ran_pos,
                        ran_pos
                    ),
                    color=YELLOW,
                    radius=random.random() * 0.08
                ).set_opacity(opa2 * random.random()) for i in range(200)
            )

        self.play(
            Write(tex_cauchy)
        )
        self.play(
            Write(tex_fx),
            Write(line_kx),
            Write(axes, lag_ratio=0.1)
        )
        self.wait(1.5)
        self.play(
            TransformMatchingTex(tex_fx, tex_f_sq2, path_arc=PI / 2, key_map={
                "f": "f",
                "x": "\\sqrt{2}",
                "(": "(",
                ")": ")",
            })
        )
        self.play(
            TransformMatchingTex(tex_f_sq2, tex_f_sq2_eq_a, path_arc=PI / 2, key_map={
                "f(\\sqrt{2})": "f(\\sqrt{2})"
            }),
            Write(point_sq2s_pos[0]),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            tex_f_sq2_eq_a.animate.shift(UP * 1),
            TransformFromCopy(tex_cauchy, tex_cauchy_x_sq2)
        )
        self.wait(1.5)
        self.play(
            TransformMatchingTex(tex_cauchy_x_sq2, tex_cauchy_x_y_sq2, path_arc=PI / 2, key_map={
                "f(\\sqrt{2})": "f(\\sqrt{2})",
                "f(y)": "f(\\sqrt{2})",
                "f(\\sqrt{2}+y)": "f(\\sqrt{2}+\\sqrt{2})",
                "+": "+",
                "=": "=",
            })
        )
        self.wait(1.5)
        self.play(
            TransformMatchingTex(tex_cauchy_x_y_sq2, tex_cauchy_sim1, path_arc=PI / 2, key_map={
                "f(\\sqrt{2})+f(\\sqrt{2})=": "f(\\sqrt{2})+f(\\sqrt{2})=",
                "f(\\sqrt{2}": "f(2\\sqrt{2}",
                ")": ")",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_cauchy_sim1, tex_cauchy_sim2, path_arc=PI / 2, key_map={
                "f(\\sqrt{2})+f(\\sqrt{2})": "2f(\\sqrt{2})",
                "f(2\\sqrt{2})": "f(2\\sqrt{2})",
                "+": "+",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_cauchy_sim2, tex_cauchy_sim3, path_arc=PI / 2, key_map={
                "f(2\\sqrt{2})": "f(2\\sqrt{2})",
                "2f(\\sqrt{2})": "2f(\\sqrt{2})",
                "+": "+",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_cauchy_sim3, tex_cauchy_sim4, path_arc=PI / 2, key_map={
                "f(2\\sqrt{2})=2": "f(2\\sqrt{2})=2",
                "f(\\sqrt{2})": "a",
                "+": "+",
                "=": "=",
            }),
            Write(point_sq2s_pos[1])
        )
        self.wait(2)
        self.play(FadeOut(tex_cauchy_sim4))
        # new
        self.wait(1)
        self.play(
            TransformFromCopy(tex_cauchy, tex_new1_cauchy_x_2sq2)
        )
        self.wait(1.5)
        self.play(
            TransformMatchingTex(tex_new1_cauchy_x_2sq2, tex_new1_cauchy_x_y_2sq2, path_arc=PI / 2, key_map={
                "f(2\\sqrt{2})": "f(2\\sqrt{2})",
                "y": "\\sqrt{2}",
                "+": "+",
                "=": "=",
            })
        )
        self.wait(1.5)
        self.play(
            TransformMatchingTex(tex_new1_cauchy_x_y_2sq2, tex_new1_cauchy_sim1, path_arc=PI / 2, key_map={
                "f(2\\sqrt{2})+f(\\sqrt{2})=": "f(2\\sqrt{2})+f(\\sqrt{2})=",
                "f(2\\sqrt{2}": "f(3\\sqrt{2}",
                ")": ")",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_new1_cauchy_sim1, tex_new1_cauchy_sim2, path_arc=PI / 2, key_map={
                "f(2\\sqrt{2})+f(\\sqrt{2})": "f(2\\sqrt{2})+f(\\sqrt{2})",
                "f(3\\sqrt{2})": "f(3\\sqrt{2})",
                "+": "+",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_new1_cauchy_sim2, tex_new1_cauchy_sim3, path_arc=PI / 2, key_map={
                "f(2\\sqrt{2})": "2a",
                "+f(\\sqrt{2})": "+a",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_new1_cauchy_sim3, tex_new1_cauchy_sim4, path_arc=PI / 2, key_map={
                "2a": "3a",
            }),
            Write(point_sq2s_pos[2])
        )
        self.wait(2)
        # race up
        self.remove(tex_new1_cauchy_sim4)
        self.add(tex_new1_cauchy_4_to_100[0], point_sq2s_pos[3])
        self.wait(1)
        self.remove(tex_new1_cauchy_4_to_100[0])
        self.add(tex_new1_cauchy_4_to_100[1], point_sq2s_pos[4])
        self.wait(0.6)
        self.remove(tex_new1_cauchy_4_to_100[1])
        self.add(tex_new1_cauchy_4_to_100[2], point_sq2s_pos[5])
        self.wait(0.4)
        self.remove(tex_new1_cauchy_4_to_100[2])
        self.add(tex_new1_cauchy_4_to_100[3], point_sq2s_pos[6])
        self.wait(0.3)
        self.remove(tex_new1_cauchy_4_to_100[3])
        self.add(tex_new1_cauchy_4_to_100[4], point_sq2s_pos[7])
        self.wait(0.2)
        self.remove(tex_new1_cauchy_4_to_100[4])
        self.add(tex_new1_cauchy_4_to_100[5], point_sq2s_pos[8])
        self.wait(0.1)
        self.remove(tex_new1_cauchy_4_to_100[5])
        self.add(tex_new1_cauchy_4_to_100[6], point_sq2s_pos[9])
        self.wait(0.05)
        self.remove(tex_new1_cauchy_4_to_100[6])
        self.add(tex_new1_cauchy_4_to_100[7], point_sq2s_pos[10])
        self.wait(0.03)
        for i in range(8, 30):
            self.remove(tex_new1_cauchy_4_to_100[i - 1])
            self.add(tex_new1_cauchy_4_to_100[i])
            self.wait(1 / 40)
        for i in range(30, 80):
            self.remove(tex_new1_cauchy_4_to_100[i - 1])
            self.add(tex_new1_cauchy_4_to_100[i])
            self.wait(1 / 60)
        for i in range(80, 96):
            self.remove(tex_new1_cauchy_4_to_100[i - 1])
            self.add(tex_new1_cauchy_4_to_100[i])
            self.wait(1 / 20)
        self.remove(tex_new1_cauchy_4_to_100[95])
        self.add(tex_new1_cauchy_4_to_100[96])
        self.wait(0.25)
        self.play(
            TransformMatchingTex(tex_new1_cauchy_4_to_100[96], tex_new1_cauchy_n, path_arc=PI / 2, key_map={
                "100": "n"    
            }),
            FadeIn(VGroup(*point_sq2s_neg), lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(2)
        self.add(tex_new1_cauchy_q)
        self.play(
            tex_new1_cauchy_n[2].animate.shift(UP).set_opacity(0),
            tex_new1_cauchy_n[8].animate.shift(UP).set_opacity(0),
            tex_new1_cauchy_q[2].animate.shift(UP).set_opacity(1),
            tex_new1_cauchy_q[8].animate.shift(UP).set_opacity(1),
        )
        self.wait(2)
        
        sq2ii = VGroup(*[v for i, v in enumerate(tex_new1_cauchy_n) if i in [3, 4, 5]])
        sq2ll = [v for i, v in enumerate(tex_new1_cauchy_n) if i in [0, 1, 6, 7, 8, 9]]
        tex_x = Tex("x").scale(1.2).set_color_by_tex_to_color_map(colormap_xy_1).move_to(sq2ii.get_center() + DOWN * 0.12)
        tex_eq = Tex("=").scale(1.2).set_color_by_tex_to_color_map(colormap_xy_1).rotate(PI / 2).next_to(tex_x, DOWN, buff=0.24)
        tex_sq2 = Tex("\\sqrt{2}").scale(1.2).next_to(tex_eq, DOWN, buff=0.24)
        tex_pi = Tex("\\pi").scale(1.2).next_to(tex_eq, DOWN, buff=0.24).shift(RIGHT * 0.3)
        tex_e = Tex("e").scale(1.2).next_to(tex_eq, DOWN, buff=0.24).shift(RIGHT * 0.3)
        tex_phi = Tex("\\varphi").scale(1.2).next_to(tex_eq, DOWN, buff=0.24).shift(RIGHT * 0.3)
        self.play(
            tex_cauchy.animate.set_opacity(0.6),
            tex_f_sq2_eq_a.animate.set_opacity(0.6),
            tex_new1_cauchy_q[2].animate.set_opacity(0.6),
            tex_new1_cauchy_q[8].animate.set_opacity(0.6),
            *[v.animate.set_opacity(0.6) for v in sq2ll],
            sq2ii.animate.scale(1.2),
        )
        self.play(
            WiggleOutThenIn(sq2ii)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(sq2ii, tex_x),
        )
        self.wait(2)
        self.play(
            Write(tex_eq),
            Write(tex_sq2),
        )
        self.wait(1)
        self.play(
            tex_sq2.animate.shift(LEFT * 0.3).set_opacity(0),
            tex_pi.animate.set_opacity(1).shift(LEFT * 0.3),
        )
        self.wait(0.5)
        self.play(
            tex_pi.animate.shift(LEFT * 0.3).set_opacity(0),
            tex_e.animate.set_opacity(1).shift(LEFT * 0.3),
        )
        self.wait(0.5)
        self.play(
            tex_e.animate.shift(LEFT * 0.3).set_opacity(0),
            tex_phi.animate.set_opacity(1).shift(LEFT * 0.3),
        )
        self.wait(3)
        
        placeholder_rec = Rectangle(width=20, height=20).set_fill("#333333")
        self.play(FadeIn(placeholder_rec), run_time=1.5)
        self.wait(1)

class CAPart3_2_2(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_xy_f = {
            "x": RED, "y": GREEN, "k": YELLOW_B, "a": RED_A,
            "f": BLUE, "g": BLUE_D,
            "(": WHITE, ")": WHITE,
            "+": WHITE, "-": WHITE,
            "\\mathrm{e}": WHITE,
            "\\left(": WHITE, "\\right)": WHITE, "\\ln": WHITE
        }
        tex_cauchy = Tex("f(x)+f(y)=f(x+y)").move_to(LEFT * 4.5 + UP * 3.2).scale(0.8).set_color_by_tex_to_color_map(colormap_xy_f)
        tex_cauchy.fix_in_frame()
        self.camera.frame.shift(UP * 1.2 + RIGHT * 1.5)
        self.play(FadeIn(tex_cauchy))

        axes = Axes(
            x_range=(-8, 9),
            y_range=(-4, 6),
            height=10,
            width=17,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
        )
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        a = 2.25
        b = 1.69
        dot_1_0 = Dot(axes.c2p(1, 0), radius=0.08).set_color(RED)
        dot_1_a = Dot(axes.c2p(1, a), radius=0.08).set_color(RED)
        dot_pi_0 = Dot(axes.c2p(np.pi, 0), radius=0.08).set_color(GREEN)
        dot_pi_b = Dot(axes.c2p(np.pi, b), radius=0.08).set_color(GREEN)
        arrow_1_0toa = Arrow(
            start=axes.c2p(1, 0),
            end=axes.c2p(1, a),
            buff=0.05,
        ).set_color(RED)
        arrow_pi_0tob = Arrow(
            start=axes.c2p(np.pi, 0),
            end=axes.c2p(np.pi, b),
            buff=0.05,
        ).set_color(GREEN)
        tex_1_a = Tex("(1,a)").set_color_by_tex_to_color_map({"(1,a)": RED}).next_to(dot_1_a, UP * 0.2 + RIGHT * 0.2)
        tex_pi_b = Tex("(\\pi,b)").next_to(dot_pi_b, UP * 0.2 + RIGHT * 0.2)
        for t in tex_pi_b:
            t.set_color(GREEN)
        line_1a = DashedLine(
            start=axes.c2p(-20, -20 * a),
            end=axes.c2p(20, 20 * a),
            color=RED,
            stroke_width=2
        ).set_opacity(0.75)
        line_pib = DashedLine(
            start=axes.c2p(-20 * np.pi, -20 * b),
            end=axes.c2p(20 * np.pi, 20 * b),
            color=GREEN,
            stroke_width=2
        ).set_opacity(0.75)
        dots_on_line_1a = [Dot(radius=0.04).set_color(RED_B) for _ in range(6)]
        dots_on_line_pib = [Dot(radius=0.04).set_color(GREEN_B) for _ in range(6)]
        np.random.seed([114, 514, 1919])
        # # a
        # random_dot_pos_1a = np.random.uniform(-3, 5, 6)
        # group_tex_dots_1a = VGroup()
        # for i, dot in enumerate(dots_on_line_1a):
        #     dot.move_to(axes.c2p(random_dot_pos_1a[i], random_dot_pos_1a[i] * a))
        #     tex_thisp = Tex(f"({random_dot_pos_1a[i]:.2f},{random_dot_pos_1a[i]:.2f} \\cdot a)").scale(0.35).next_to(dot, UP * 0.2 + LEFT * 0.2)
        #     for t in tex_thisp:
        #         t.set_color(RED_D).set_opacity(0.75)
        #     group_tex_dots_1a.add(tex_thisp)
        # group_dots_1a = VGroup(*dots_on_line_1a)
        # # b
        # random_dot_pos_pib = np.random.uniform(-4, 12, 6)
        # group_tex_dots_pib = VGroup()
        # for i, dot in enumerate(dots_on_line_pib):
        #     dot.move_to(axes.c2p(random_dot_pos_pib[i] / np.pi, random_dot_pos_pib[i] / np.pi * b / np.pi))
        #     tex_thisp = Tex(f"({((random_dot_pos_pib[i] / np.pi)):.2f} \\cdot \\pi,{(random_dot_pos_pib[i] / np.pi):.2f} \\cdot b)").scale(0.35).next_to(dot, DOWN * 0.2 + RIGHT * 0.2)
        #     for t in tex_thisp:
        #         t.set_color(GREEN_D).set_opacity(0.75)
        #     group_tex_dots_pib.add(tex_thisp)

        # Q for Line a

        q_a_dots_div_1 = [Dot(axes.c2p(k, k * a), radius=0.05).set_color(RED) for k in range(-4, 5)]
        q_a_texs_label_1 = [Tex("M\\frac{tt}{1} \\cdot a".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(RED).scale(0.4).next_to(q_a_dots_div_1[k + 4], RIGHT + DOWN, buff=0.2) for k in range(-4, 5)]
        q_a_dash_line_1 = [DashedLine(q_a_dots_div_1[i].get_corner(RIGHT + DOWN), q_a_texs_label_1[i].get_corner(LEFT + UP)).set_stroke(width=0.4).set_color(RED) for i in range(len(q_a_dots_div_1))]

        q_a_dots_div_2 = [Dot(axes.c2p(k, k * a), radius=0.045).set_color(ORANGE) for k in [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]]
        q_a_texs_label_2 = [Tex("M\\frac{tt}{2} \\cdot a".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(ORANGE).scale(0.4).next_to(q_a_dots_div_2[i], RIGHT + DOWN, buff=0.5) for i, k in enumerate([-7, -5, -3, -1, 1, 3, 5, 7])]
        q_a_dash_line_2 = [DashedLine(q_a_dots_div_2[i].get_corner(RIGHT + DOWN), q_a_texs_label_2[i].get_corner(LEFT + UP)).set_stroke(width=0.4).set_color(ORANGE) for i in range(len(q_a_dots_div_2))]

        q_a_dots_div_3 = [Dot(axes.c2p(k, k * a), radius=0.04).set_color(YELLOW) for k in [-3.667, -3.333, -2.667, -2.333, -1.667, -1.333, -0.667, -0.333, 0.333, 0.667, 1.333, 1.667, 2.333, 2.667, 3.333, 3.667]]
        q_a_texs_label_3 = [Tex("M\\frac{tt}{3} \\cdot a".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(YELLOW).scale(0.4).next_to(q_a_dots_div_3[i], LEFT + UP, buff=0.2) for i, k in enumerate([-11, -10, -8, -7, -5, -4, -2, -1, 1, 2, 4, 5, 7, 8, 10, 11])]
        q_a_dash_line_3 = [DashedLine(q_a_dots_div_3[i].get_corner(LEFT + UP), q_a_texs_label_3[i].get_corner(RIGHT + DOWN)).set_stroke(width=0.4).set_color(YELLOW) for i in range(len(q_a_dots_div_3))]

        q_a_dots_div_4 = [Dot(axes.c2p(k, k * a), radius=0.035).set_color(GREEN) for k in [-3.75, -3.25, -2.75, -2.25, -1.75, -1.25, -0.75, -0.25, 0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75]]
        q_a_texs_label_4 = [Tex("M\\frac{tt}{4} \\cdot a".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(GREEN).scale(0.4).next_to(q_a_dots_div_4[i], LEFT + UP, buff=0.5) for i, k in enumerate([-15, -13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15])]
        q_a_dash_line_4 = [DashedLine(q_a_dots_div_4[i].get_corner(LEFT + UP), q_a_texs_label_4[i].get_corner(RIGHT + DOWN)).set_stroke(width=0.4).set_color(GREEN) for i in range(len(q_a_dots_div_4))]

        group_a_1 = VGroup(*q_a_dots_div_1, *q_a_texs_label_1, *q_a_dash_line_1)
        group_a_2 = VGroup(*q_a_dots_div_2, *q_a_texs_label_2, *q_a_dash_line_2)
        group_a_3 = VGroup(*q_a_dots_div_3, *q_a_texs_label_3, *q_a_dash_line_3)
        group_a_4 = VGroup(*q_a_dots_div_4, *q_a_texs_label_4, *q_a_dash_line_4)
        group_a = VGroup(group_a_1, group_a_2, group_a_3, group_a_4)

        # Q for Line b

        q_b_dots_div_1 = [Dot(axes.c2p(k, k * b / np.pi), radius=0.05).set_color(GREEN) for k in range(-4, 11)]
        q_b_texs_label_1 = [Tex("M\\frac{tt}{1} \\cdot b".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(GREEN).scale(0.4).next_to(q_b_dots_div_1[k + 4], RIGHT + DOWN, buff=0.2) for k in range(-4, 11)]
        q_b_dash_line_1 = [DashedLine(q_b_dots_div_1[i].get_corner(RIGHT + DOWN), q_b_texs_label_1[i].get_corner(LEFT + UP)).set_stroke(width=0.4).set_color(GREEN) for i in range(len(q_b_dots_div_1))]

        q_b_dots_div_2 = [Dot(axes.c2p(k, k * b / np.pi), radius=0.045).set_color(ORANGE) for k in [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5]]
        q_b_texs_label_2 = [Tex("M\\frac{tt}{2} \\cdot b".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(ORANGE).scale(0.4).next_to(q_b_dots_div_2[i], RIGHT + DOWN, buff=0.5) for i, k in enumerate([-7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23])]
        q_b_dash_line_2 = [DashedLine(q_b_dots_div_2[i].get_corner(RIGHT + DOWN), q_b_texs_label_2[i].get_corner(LEFT + UP)).set_stroke(width=0.4).set_color(ORANGE) for i in range(len(q_b_dots_div_2))]

        q_b_dots_div_3 = [Dot(axes.c2p(k, k * b / np.pi), radius=0.04).set_color(YELLOW) for k in [-3.667, -3.333, -2.667, -2.333, -1.667, -1.333, -0.667, -0.333, 0.333, 0.667, 1.333, 1.667, 2.333, 2.667, 3.333, 3.667, 4.333, 4.667, 5.333, 5.667, 6.333, 6.667, 7.333, 7.667, 8.333, 8.667, 9.333, 9.667, 10.333, 10.667, 11.333, 11.667]]
        q_b_texs_label_3 = [Tex("M\\frac{tt}{3} \\cdot b".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(YELLOW).scale(0.4).next_to(q_b_dots_div_3[i], LEFT + UP, buff=0.2) for i, k in enumerate([-11, -10, -8, -7, -5, -4, -2, -1, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34])]
        q_b_dash_line_3 = [DashedLine(q_b_dots_div_3[i].get_corner(LEFT + UP), q_b_texs_label_3[i].get_corner(RIGHT + DOWN)).set_stroke(width=0.4).set_color(YELLOW) for i in range(len(q_b_dots_div_3))]

        q_b_dots_div_4 = [Dot(axes.c2p(k, k * b / np.pi), radius=0.035).set_color(GREEN) for k in [-3.75, -3.25, -2.75, -2.25, -1.75, -1.25, -0.75, -0.25, 0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75, 4.25, 4.75, 5.25, 5.75, 6.25, 6.75, 7.25, 7.75, 8.25, 8.75, 9.25, 9.75, 10.25, 10.75, 11.25, 11.75]]
        q_b_texs_label_4 = [Tex("M\\frac{tt}{4} \\cdot b".replace("tt", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(GREEN).scale(0.4).next_to(q_b_dots_div_4[i], LEFT + UP, buff=0.5) for i, k in enumerate([-15, -13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47])]
        q_b_dash_line_4 = [DashedLine(q_b_dots_div_4[i].get_corner(LEFT + UP), q_b_texs_label_4[i].get_corner(RIGHT + DOWN)).set_stroke(width=0.4).set_color(GREEN) for i in range(len(q_b_dots_div_4))]

        group_b_1 = VGroup(*q_b_dots_div_1, *q_b_texs_label_1, *q_b_dash_line_1)
        group_b_2 = VGroup(*q_b_dots_div_2, *q_b_texs_label_2, *q_b_dash_line_2)
        group_b_3 = VGroup(*q_b_dots_div_3, *q_b_texs_label_3, *q_b_dash_line_3)
        group_b_4 = VGroup(*q_b_dots_div_4, *q_b_texs_label_4, *q_b_dash_line_4)
        group_b = VGroup(group_b_1, group_b_2, group_b_3, group_b_4)

        group_dots_pib = VGroup(*dots_on_line_pib)
        tex_f_1_plus_f_pi = Tex("f(1)+f(\\pi)=f(1+\\pi)").scale(0.8).set_color_by_tex_to_color_map(colormap_xy_f | {"1": RED, "\\pi": GREEN}).next_to(tex_pi_b, DOWN * 1.5 + RIGHT * 1)
        rec_hl_f1 = SurroundingRectangle(VGroup(tex_f_1_plus_f_pi[0:4]), buff=0.1, color=RED_A)
        rec_hl_fpi = SurroundingRectangle(VGroup(tex_f_1_plus_f_pi[5:9]), buff=0.1, color=GREEN_A)
        rec_hl_ca_fx = SurroundingRectangle(VGroup(tex_cauchy[0:4]), buff=0.1, color=RED_A)
        rec_hl_ca_fy = SurroundingRectangle(VGroup(tex_cauchy[5:9]), buff=0.1, color=GREEN_A)
        rec_hl_p_a = SurroundingRectangle(tex_1_a[3], buff=0.1, color=RED_A)
        rec_hl_p_b = SurroundingRectangle(tex_pi_b[3], buff=0.1, color=GREEN_A)
        tex_a = Tex("a").set_color(RED).next_to(VGroup(tex_cauchy[0:4]), DOWN, buff=0.15)
        tex_plus = Tex("+").set_color(WHITE).next_to(VGroup(tex_cauchy[4]), DOWN, buff=0.15).shift(DOWN * 0.1)
        tex_b = Tex("b").set_color(GREEN).next_to(VGroup(tex_cauchy[5:9]), DOWN, buff=0.15)
        tex_eq_apb = Tex("=a+b").next_to(VGroup(tex_cauchy[9:]), DOWN, buff=0.15).set_color_by_tex_to_color_map({
            "a": RED, "b": GREEN, "=": WHITE, "+": WHITE
        })
        tex_a.move_to(RIGHT * tex_a.get_x() + UP * tex_plus.get_y())
        tex_b.move_to(RIGHT * tex_b.get_x() + UP * tex_plus.get_y())
        tex_eq_apb.move_to(RIGHT * tex_eq_apb.get_x() + UP * tex_plus.get_y())
        VGroup(tex_a, tex_plus, tex_b, tex_eq_apb).shift(UP * 1.2 + RIGHT * 1.5)
        dot_f1 = Dot(radius = 0.1).set_color(RED).next_to(rec_hl_f1, DOWN, buff=0.15)
        dot_f2 = Dot(radius = 0.1).set_color(GREEN).next_to(rec_hl_fpi, DOWN, buff=0.15)
        show_correct = ImageMobject("right.png").scale(0.2).next_to(VGroup(tex_f_1_plus_f_pi[10:]), DOWN, buff=0.15).shift(DOWN * 0.5)

        self.wait(1)
        self.play(
            Write(axes, lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            axes.animate.set_opacity(0.3),
            Write(dot_1_0),
            Write(dot_pi_0),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(arrow_1_0toa),
            Write(arrow_pi_0tob),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(tex_1_a),
            Write(tex_pi_b),
            Write(dot_1_a),
            Write(dot_pi_b),
            run_time=1.5
        )
        self.wait(1.5)
        self.play(
            Write(line_1a),
            FadeOut(arrow_1_0toa),
            FadeOut(dot_1_0),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(group_a_1, lag_ratio=0.1),
            run_time=1
        )
        self.play(
            Write(group_a_2, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(
            Write(group_a_3, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(
            Write(group_a_4, lag_ratio=0.1),
            run_time=0.5
        )
        self.wait(2)
        self.play(FadeOut(group_a))
        self.play(
            Write(line_pib),
            FadeOut(arrow_pi_0tob),
            FadeOut(dot_pi_0),
            run_time=1.5
        )
        self.play(
            Write(group_b_1, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(
            Write(group_b_2, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(
            Write(group_b_3, lag_ratio=0.1),
            run_time=0.5
        )
        self.play(
            Write(group_b_4, lag_ratio=0.1),
            run_time=0.5
        )
        # self.wait(0.5)
        # self.play(
        #     Write(group_dots_pib, lag_ratio=0.1),
        #     run_time=2
        # )
        self.wait(2)
        self.play(
            FadeOut(group_b),
            FadeOut(group_dots_pib),
        )
        
        arrow_OA = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(1, a),
            buff=0.05,
        ).set_color(RED)
        arrow_OB = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(np.pi, b),
            buff=0.05,
        ).set_color(GREEN)
        arrow_OA_trans = Arrow(
            start=axes.c2p(np.pi, b),
            end=axes.c2p(np.pi + 1, b + a),
            buff=0.05,
        ).set_color(RED)
        arrow_OB_trans = Arrow(
            start=axes.c2p(1, a),
            end=axes.c2p(1 + np.pi, a + b),
            buff=0.05,
        ).set_color(GREEN)
        arrow_OC = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(1 + np.pi, a + b),
            buff=0.05,
        ).set_color(YELLOW)
        point_c = Dot(axes.c2p(1 + np.pi, a + b), radius=0.08).set_color(YELLOW)
        tex_appi_apb = Tex("(1+\\pi,a+b)").scale(0.8).next_to(point_c, UP * 0.2 + RIGHT * 0.2)
        tex_appi_apb[1].set_color(RED)
        tex_appi_apb[5].set_color(RED)
        tex_appi_apb[3].set_color(GREEN)
        tex_appi_apb[7].set_color(GREEN)

        self.play(
            Write(arrow_OA),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(arrow_OB),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(TransformFromCopy(
            VGroup(tex_1_a[1], tex_pi_b[1]), tex_f_1_plus_f_pi
        ))
        self.wait(1)

        dash_f_ca_1 = DashedLine(rec_hl_f1.get_left(), rec_hl_p_a.get_bottom()).set_color(GREY_A)
        dash_f_ca_pi = DashedLine(rec_hl_fpi.get_top(), rec_hl_p_b.get_bottom()).set_color(GREY_A)
        dash_ca_fx = DashedLine(rec_hl_ca_fx.get_bottom() + RIGHT * 1.5 + UP * 1, rec_hl_p_a.get_top()).set_color(GREY_A)
        dash_ca_fy = DashedLine(rec_hl_ca_fy.get_bottom() + RIGHT * 1.5 + UP * 1, rec_hl_p_b.get_top()).set_color(GREY_A)

        self.play(
            Write(rec_hl_f1),
            Write(rec_hl_ca_fx),
            Write(rec_hl_p_a),
        )
        self.play(
            Write(dash_ca_fx),
            Write(dash_f_ca_1),
        )
        self.wait(1)
        self.wait(1.5)
        rec_hl_f1_cpy = rec_hl_f1.copy(True)
        self.add(rec_hl_f1_cpy)
        self.play(
            ReplacementTransform(rec_hl_f1_cpy, tex_a),
            ReplacementTransform(rec_hl_f1, rec_hl_fpi),
            ReplacementTransform(rec_hl_ca_fx, rec_hl_ca_fy),
            ReplacementTransform(rec_hl_p_a, rec_hl_p_b),
            ReplacementTransform(dash_ca_fx, dash_ca_fy),
            ReplacementTransform(dash_f_ca_1, dash_f_ca_pi),
        )
        self.wait(1.5)
        self.play(
            FadeOut(VGroup(
                rec_hl_ca_fy, rec_hl_p_b,
                dash_ca_fy, dash_f_ca_pi
            )),
            ReplacementTransform(rec_hl_fpi, VGroup(tex_plus, tex_b)),
        )
        self.wait(1.5)
        self.play(
            TransformFromCopy(VGroup(tex_f_1_plus_f_pi[9:]), tex_eq_apb),
        )
        self.wait(1.5)
        self.play(
            TransformFromCopy(arrow_OA, arrow_OA_trans),
            TransformFromCopy(arrow_OB, arrow_OB_trans),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(point_c),
        )
        self.play(
            FadeOut(arrow_OA_trans),
            FadeOut(arrow_OB_trans),
            Write(arrow_OC),
        )
        self.wait(1)
        self.play(Write(tex_appi_apb))
        self.wait(1.5)
        self.play(Write(dot_f1))
        self.wait(1)
        self.play(Write(dot_f2))
        self.wait(1)
        self.play(FadeIn(show_correct))
        self.wait(2.5)
        self.play(FadeOut(Group(
            dot_f1, dot_f2, show_correct, tex_plus, tex_eq_apb, tex_a, tex_b,
        )))
        
        def draw_vector_addition(scene: Scene, x1, x2, wait_time=2.0, rm=True):
            """
            在两条特定直线上绘制点并展示向量加法结果
            参数:
                scene: 当前场景对象
                x1: 第一条直线上的横坐标
                x2: 第二条直线上的横坐标
                wait_time: 显示时间（秒）
            """
            # 常数定义（与CAPart3_2_2中一致）
            a = 2.25
            b = 1.69
            
            # 计算点坐标
            ori = axes.c2p(0, 0, 0)
            pointA = axes.c2p(*[x1, a * x1, 0])
            pointB = axes.c2p(*[x2, (b / np.pi) * x2, 0])
            pointC = (pointA - ori) + (pointB - ori) + ori
            
            # 创建图形元素
            dotA = Dot(pointA, radius=0.06).set_color(RED)
            dotB = Dot(pointB, radius=0.06).set_color(GREEN)
            dotC = Dot(pointC, radius=0.03).set_color(YELLOW)
            
            arrow_OA = Arrow(ori, pointA, buff=0.05).set_color(RED)
            arrow_OB = Arrow(ori, pointB, buff=0.05).set_color(GREEN)
            arrow_OC = Arrow(ori, pointC, buff=0.05).set_color(YELLOW)
            
            # 添加元素到场景
            scene.add(dotA, dotB, dotC, arrow_OA, arrow_OB, arrow_OC)
            
            # 等待指定时间
            if wait_time != 0:
                scene.wait(wait_time)
            
            # 移除元素
            if rm:
                scene.remove(dotA, dotB, dotC, arrow_OA, arrow_OB, arrow_OC)
            else:
                scene.remove(dotA, dotB, arrow_OA, arrow_OB, arrow_OC)
                return dotC

        self.remove(VGroup(tex_1_a, tex_pi_b, tex_f_1_plus_f_pi, tex_appi_apb, dot_1_a, dot_pi_b, point_c, arrow_OA, arrow_OB, arrow_OC))
        draw_vector_addition(self, 0.7, 1.3, wait_time=1.0)
        draw_vector_addition(self, 1.4, 0.5, wait_time=1.0)
        draw_vector_addition(self, 1.1, 2.9, wait_time=1.0)
        tempC_dots = VGroup()
        tempC_dots.add(draw_vector_addition(self, 0.3, 4.0, wait_time=0.4, rm=False))
        tempC_dots.add(draw_vector_addition(self, -1.0, 2.1, wait_time=0.4, rm=False))
        tempC_dots.add(draw_vector_addition(self, 2.5, -1.9, wait_time=0.3, rm=False))
        tempC_dots.add(draw_vector_addition(self, 1.0, 1.0, wait_time=0.3, rm=False))
        for _ in range(20):
            tempC_dots.add(draw_vector_addition(self, random.uniform(-1, 2), random.uniform(-1, 3), wait_time=1 / 15 + 0.00001, rm=False))
        start_yellow = 600
        end_yellow = 1000
        opacity_delta = 1 / (end_yellow - start_yellow)
        rec_yellow = Rectangle(width=20, height=20).set_fill(color=YELLOW, opacity=0)
        self.add(rec_yellow)
        group_back_dot = VGroup()
        for i in range(end_yellow):
            # tempC_dots.add(draw_vector_addition(self, random.uniform(-5, 5), random.uniform(-6, 10), wait_time=0, rm=False))
            if i % 4 == 0:
                self.wait(1 / 120 + 0.00001)
            for _ in range(10):
                group_back_dot.add(Dot(np.array([
                    random.uniform(-8, 8),
                    random.uniform(-5, 5),
                    0
                ]), radius=0.03).set_color(YELLOW))
                self.add(group_back_dot[-1])
        self.wait(2.5)
        self.play(
            FadeOut(tempC_dots, lag_ratio=0.1, run_time=1),
            FadeOut(group_back_dot, lag_ratio=0.1, run_time=1),
        )
        self.wait(1)

        # linear combination
        tex_p_1_q_pi = Tex("p \\cdot 1 + q \\cdot \\pi").move_to(UP * 1.2 + RIGHT * 1.5).scale(1.05)
        tex_p_1_q_pi[0].set_color(LIGHT_PINK).shift(DOWN * 0.3)
        tex_p_1_q_pi[2].set_color(RED)
        tex_p_1_q_pi[4].set_color(LIGHT_PINK).shift(DOWN * 0.3)
        tex_p_1_q_pi[6].set_color(GREEN)
        self.add(tex_p_1_q_pi)
        for t in tex_p_1_q_pi:
            t.set_opacity(0)
        text_linear_combination = Text("线性组合", font="微软雅黑").scale(1.1).move_to(DOWN * 0.7 + UP * 1.2 + RIGHT * 1.5).set_color_by_text_to_color_map({
            "线性": YELLOW,
            "组合": WHITE,
        })
        text_linear_combination_new = text_linear_combination.copy(True)
        text_linear_combination_new.move_to(LEFT * 4.5 + DOWN * 1 + UP * 1.2 + RIGHT * 1.5)
        text_base_1 = Text("基底", font="微软雅黑").scale(0.5).set_color(GREY_A).next_to(tex_p_1_q_pi[2], UP * 0.5)
        text_base_pi = Text("基底", font="微软雅黑").scale(0.5).set_color(GREY_A).next_to(tex_p_1_q_pi[6], UP * 0.5)
        text_base_1_new = text_base_1.copy(True)
        text_base_1_new.move_to(LEFT * 4.5 + UP * 2 + UP * 1.2 + RIGHT * 1.5)
        rect_1 = SurroundingRectangle(tex_p_1_q_pi[2], color=RED_A, buff=0.1)
        rect_pi = SurroundingRectangle(tex_p_1_q_pi[6], color=GREEN_A, buff=0.1)
        
        self.play(
            line_1a.animate.set_opacity(0.2),
            line_pib.animate.set_opacity(0.2),
            tex_p_1_q_pi[2].animate.set_opacity(1),
            tex_p_1_q_pi[6].animate.set_opacity(1),
        )
        self.play(
            tex_p_1_q_pi[0].animate.set_opacity(1).shift(UP * 0.3),
            tex_p_1_q_pi[1].animate.set_opacity(1),
            tex_p_1_q_pi[4].animate.set_opacity(1).shift(UP * 0.3),
            tex_p_1_q_pi[5].animate.set_opacity(1),
        )
        self.play(
            tex_p_1_q_pi[3].animate.set_opacity(1),
        )
        self.wait(1.5)
        self.play(
            Write(text_linear_combination),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            Write(VGroup(rect_1, rect_pi), lag_ratio=0.2, run_time=1.5),
        )
        self.wait(1)
        self.play(
            Write(text_base_1),
            Write(text_base_pi),
            run_time=1.5
        )
        self.wait(2.5)
        self.play(
            FadeOut(VGroup(tex_p_1_q_pi, rect_1, rect_pi, line_1a, line_pib, text_base_pi), lag_ratio=0.1),
            ReplacementTransform(text_linear_combination, text_linear_combination_new, path_arc=PI / 2),
            FadeOut(VGroup(text_base_pi, text_base_1)),
            run_time=1.5
        )

        arrow_vec_i = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(1, 0),
            buff=0.05,
        ).set_color(RED_A)
        arrow_vec_j = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(0, 1),
            buff=0.05,
        ).set_color(GREEN_A)
        xx = 3.51
        yy = 2.14
        zz = 1.3
        arrow_vec_xi = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(xx, 0),
            buff=0.05,
        ).set_color(RED_D)
        arrow_vec_yj = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(0, yy),
            buff=0.05,
        ).set_color(GREEN_D)
        arrow_vec_sum = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(xx, yy),
            buff=0.05,
        ).set_color(YELLOW)
        unit_len = axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0]
        arrow_vec_k = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(0, 0) + OUT * unit_len,
            buff=0.05,
        ).set_color(BLUE_A).rotate(PI / 2, axis=OUT)
        arrow_vec_kz = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(0, 0) + OUT * unit_len * zz,
            buff=0.05,
        ).set_color(BLUE_D).rotate(PI / 2, axis=OUT)
        arrow_vec_sum_3 = Arrow(
            start=axes.c2p(0, 0),
            end=axes.c2p(xx, yy) + (OUT * unit_len) * zz,
            buff=0.05,
        ).set_color(YELLOW_D)
        tex_i = Tex("i").set_color(RED_A).move_to(arrow_vec_i.get_end() + DOWN * 0.2 + RIGHT * 0.2)
        tex_j = Tex("j").set_color(GREEN_A).move_to(arrow_vec_j.get_end() + UP * 0.2 + LEFT * 0.2)
        tex_xi = Tex("xi").set_color(RED_D).move_to(arrow_vec_xi.get_end() + DOWN * 0.2 + RIGHT * 0.2)
        tex_yj = Tex("yj").set_color(GREEN_D).move_to(arrow_vec_yj.get_end() + UP * 0.2 + LEFT * 0.2)
        tex_sum = Tex("xi + yj").set_color(YELLOW).move_to(arrow_vec_sum.get_end() + UP * 0.2 + RIGHT * 0.2)
        tex_k = Tex("k").set_color(BLUE).move_to(arrow_vec_k.get_end() + UP * 0.2 + LEFT * 0.4 + IN * 0.25).scale(0.8)
        tex_k.rotate(PI / 4, axis=RIGHT, about_point=tex_k.get_center())
        tex_kz = Tex("kz").set_color(BLUE_D).move_to(arrow_vec_kz.get_end() + UP * 0.2 + LEFT * 0.4 + OUT * 0.1).scale(0.8)
        tex_kz.rotate(PI / 4, axis=RIGHT, about_point=tex_kz.get_center())
        tex_sum_3 = Tex("xi + yj + kz").set_color(YELLOW_D).move_to(arrow_vec_sum_3.get_end() + UP * 0.2 + RIGHT * 0.2 + OUT * 0.2)
        tex_sum_3.rotate(PI / 4, axis=RIGHT, about_point=tex_sum_3.get_center())
        dash_x = DashedLine(
            start=axes.c2p(0, yy),
            end=axes.c2p(xx, yy),
            color=RED_D
        ).set_opacity(0.7)
        dash_y = DashedLine(
            start=axes.c2p(xx, 0),
            end=axes.c2p(xx, yy),
            color=GREEN_D
        ).set_opacity(0.7)
        dash_z_r = DashedLine(
            start=axes.c2p(0, 0) + (OUT * unit_len) * zz,
            end=axes.c2p(xx, yy) + (OUT * unit_len) * zz,
            color=BLUE_D
        ).set_opacity(0.7)
        dash_z_xy = DashedLine(
            start=axes.c2p(xx, yy),
            end=axes.c2p(xx, yy) + (OUT * unit_len) * zz,
            color=BLUE_D
        ).set_opacity(0.7)

        self.play(Write(arrow_vec_sum))
        self.wait(2)
        self.play(
            arrow_vec_sum.animate.set_opacity(0.2),
            Write(VGroup(arrow_vec_i, arrow_vec_j), lag_ratio=0.1),
            run_time=1.5
        )
        self.play(
            Write(VGroup(tex_i, tex_j), lag_ratio=0.1, run_time=1.5)
        )
        self.wait(2)
        self.play(
            TransformFromCopy(arrow_vec_i, arrow_vec_xi, path_arc=PI / 2),
            Write(tex_xi),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            TransformFromCopy(arrow_vec_j, arrow_vec_yj, path_arc=PI / 2),
            Write(tex_yj),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            Write(dash_x),
            Write(dash_y),
        )
        self.wait(1.5)
        self.play(
            arrow_vec_sum.animate.set_opacity(1.0),
            Write(tex_sum)
        )
        self.wait(3)
        self.play(
            self.camera.frame.animate.rotate(angle=PI / 4, axis=RIGHT),
            Write(arrow_vec_k),
            Write(tex_k),
            run_time=3
        )
        self.wait(0.5)
        self.play(
            TransformFromCopy(arrow_vec_k, arrow_vec_kz),
            Write(tex_kz),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(
            Write(dash_z_r),
            Write(dash_z_xy),
        )
        self.wait(1)
        self.play(
            TransformFromCopy(arrow_vec_sum, arrow_vec_sum_3),
            Write(tex_sum_3),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(
                arrow_vec_i, arrow_vec_j, arrow_vec_xi, arrow_vec_yj, 
                tex_i, tex_j, tex_xi, tex_yj, tex_kz, dash_x, dash_y, 
                arrow_vec_k, tex_k, arrow_vec_kz, dash_z_r, dash_z_xy,
                arrow_vec_sum, tex_sum,
                arrow_vec_sum_3, tex_sum_3
            ))
        )
        self.play(
            FadeOut(VGroup(
                text_linear_combination_new, 
                axes,
                tex_cauchy
            )),
        )
        self.wait(1)