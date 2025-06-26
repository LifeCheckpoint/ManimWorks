from manimlib import *
import re
import numpy as np
import sys
from typing import Tuple, Optional, Any
sys.path.append(".")

from extra_animation import (
    tex_typing_animate,
    animate_scaling_exponential_decay, 
    animate_scaling_smooth, 
    animate_scaling_linear, 
    animate_shift_smooth,
    homotopic_showin,
    transformMatchingIndex
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
        # uv run manimgl CAPart2.py Test -s

        # tex = Tex("f\\left(\\frac{p}{q}+\\dots+\\frac{p}{q}+\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)")
        # self.add(tex)
        # debugTeX(self, tex)
        
        tex_fpqqqq_1 = Tex("f\\left(\\frac{p}{q}+\\dots+\\frac{p}{q}+\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        }).shift(UP * 2)
        [word.set_color(GREEN) for word in tex_fpqqqq_1[-4:-1]]
        tex_fpqqqq_2 = Tex("f\\left(\\frac{p}{q}+\\dots+\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        }).shift(UP * 1)
        [word.set_color(GREEN) for word in tex_fpqqqq_2[-4:-1]]
        [word.set_color(GREEN) for word in tex_fpqqqq_2[-11:-8]]
        tex_fpqqqq_3 = Tex("f\\left(\\frac{p}{q}+\\dots\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        })
        [word.set_color(GREEN) for word in tex_fpqqqq_3[-4:-1]]
        [word.set_color(GREEN) for word in tex_fpqqqq_3[-11:-8]]
        [word.set_color(GREEN) for word in tex_fpqqqq_3[-18:-15]]
        tex_fpqqqq_final = Tex("f\\left(\\frac{p}{q}\\right)+\\dots+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": GREEN,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE, "\\dots": WHITE
        }).shift(UP * -1)

        self.add(tex_fpqqqq_1)
        self.add(tex_fpqqqq_2)
        self.add(tex_fpqqqq_3)
        self.add(tex_fpqqqq_final)

        debugTeX(self, tex_fpqqqq_1)
        debugTeX(self, tex_fpqqqq_2)
        debugTeX(self, tex_fpqqqq_3)
        debugTeX(self, tex_fpqqqq_final)

class CATransparentCauchy(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        tex_cauchy = Tex("f(x+y)=f(x)+f(y)").set_color_by_tex_to_color_map({
            "x": RED, "y": GREEN, "f": BLUE,
            "+": WHITE, "=": WHITE, "(": WHITE, ")": WHITE
        })
        self.play(FadeIn(tex_cauchy))
        self.wait(20)
        self.play(FadeOut(tex_cauchy))


class CAPart2_1(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_xy = {"x": RED, "y": GREEN, "k": YELLOW_B}
        tex_equation = Tex("f(x+y)=f(x)+f(y)").set_color_by_tex_to_color_map(colormap_xy)
        tex_equation_cpy = tex_equation.copy().set_color_by_tex_to_color_map(colormap_xy | {"f": BLUE})
        axis_x = NumberLine(x_range=[-3, 3], unit_size=1, color=RED).shift(DOWN * 1)
        axis_y = NumberLine(x_range=[-3, 3], unit_size=1, color=GREEN).shift(DOWN * 1.8)
        tex_x = Tex("x").set_color(RED).scale(0.75).next_to(axis_x, LEFT, buff=0.1)
        tex_y = Tex("y").set_color(GREEN).scale(0.75).next_to(axis_y, LEFT, buff=0.1)
        control_dot_x = Circle(radius=0.1).move_to(axis_x.n2p(0)).set_color(RED)
        control_dot_y = Circle(radius=0.1).move_to(axis_y.n2p(0)).set_color(GREEN)
        decimal_num_x = DecimalNumber(0, num_decimal_places=1, color=RED).scale(0.5).next_to(control_dot_x, UP, buff=0.1)
        decimal_num_y = DecimalNumber(0, num_decimal_places=1, color=GREEN).scale(0.5).next_to(control_dot_y, UP, buff=0.1)
        decimal_x_placer_1 = DecimalNumber(0, num_decimal_places=1, color=RED)
        decimal_y_placer_1 = DecimalNumber(0, num_decimal_places=1, color=GREEN)
        decimal_x_placer_2 = DecimalNumber(0, num_decimal_places=1, color=RED)
        decimal_y_placer_2 = DecimalNumber(0, num_decimal_places=1, color=GREEN)
        groups_tex_equation_part = [
            VGroup(*tex_equation[0:2]).copy(),
            VGroup(tex_equation[3]).copy(),
            VGroup(*tex_equation[5:9]).copy(),
            VGroup(*tex_equation[10:14]).copy(),
            VGroup(tex_equation[15]).copy()
        ]
        group_decimal_tex_equation = VGroup(
            groups_tex_equation_part[0],
            decimal_x_placer_1,
            groups_tex_equation_part[1],
            decimal_y_placer_1,
            groups_tex_equation_part[2],
            decimal_x_placer_2,
            groups_tex_equation_part[3],
            decimal_y_placer_2,
            groups_tex_equation_part[4]
        )        
        group_decimal_tex_equation.arrange(RIGHT, buff=0.1)
        group_decimal_tex_equation.move_to(ORIGIN)
        text_func_equation = Text("函数方程", font="微软雅黑").move_to(UP * 1.5)
        text_func_equation_ca = Text("柯西方程", font="微软雅黑").move_to(UP * 1.5).set_color_by_text_to_color_map({
            "柯西": BLUE,
            "方程": WHITE
        })

        self.wait(1)
        self.camera.frame.scale(0.8)
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 2, 0.7, 0.02, "in")))
        tex_typing_animate(self, tex_equation, typing_interval=0.16)
        self.wait(2)
        self.camera.frame.clear_updaters()
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 2, 0.7, 0.025, "out")))
        self.play(
            FadeOut(tex_equation[2]),
            FadeOut(tex_equation[4]),
            FadeOut(tex_equation[9]),
            FadeOut(tex_equation[14]),
            Write(tex_x),
            Write(tex_y),
            Write(axis_x),
            Write(axis_y)
        )
        self.play(
            TransformMatchingShapes(VGroup(*tex_equation[0:2]), groups_tex_equation_part[0]),
            TransformMatchingShapes(tex_equation[3], groups_tex_equation_part[1]),
            TransformMatchingShapes(VGroup(*tex_equation[5:9]), groups_tex_equation_part[2]),
            TransformMatchingShapes(VGroup(*tex_equation[10:14]), groups_tex_equation_part[3]),
            TransformMatchingShapes(tex_equation[15], groups_tex_equation_part[4]),
            FadeIn(decimal_x_placer_1),
            FadeIn(decimal_y_placer_1),
            FadeIn(decimal_x_placer_2),
            FadeIn(decimal_y_placer_2),
            Write(control_dot_x),
            Write(control_dot_y),
            Write(decimal_num_x),
            Write(decimal_num_y),
        )
        self.wait(1.5)
        f_always(decimal_num_x.set_value, control_dot_x.get_x)
        f_always(decimal_num_y.set_value, control_dot_y.get_x)
        f_always(decimal_x_placer_1.set_value, control_dot_x.get_x)
        f_always(decimal_y_placer_1.set_value, control_dot_y.get_x)
        f_always(decimal_x_placer_2.set_value, control_dot_x.get_x)
        f_always(decimal_y_placer_2.set_value, control_dot_y.get_x)
        self.camera.frame.clear_updaters()
        now = self.time
        duration_shift = 8
        max_shift_distance = 3
        scale_y_value = 1.5
        destination_value = 2 * np.pi
        def timing():
            group_decimal_tex_equation.arrange(RIGHT, buff=0.1)
            return min(destination_value, destination_value * smooth((self.time - now) / duration_shift))
        x_running = lambda t: t.move_to(axis_x.n2p(max_shift_distance * np.sin(timing())))
        y_running = lambda t: t.move_to(axis_y.n2p(max_shift_distance * np.sin(scale_y_value * timing())))
        decimal_num_x.add_updater(lambda d: d.next_to(control_dot_x, UP, buff=0.1))
        decimal_num_y.add_updater(lambda d: d.next_to(control_dot_y, UP, buff=0.1))
        control_dot_x.add_updater(x_running)
        control_dot_y.add_updater(y_running)
        # self.camera.frame.add_updater(lambda frame: frame.move_to(RIGHT * 0.2 * decimal_num_x.get_value()))
        self.wait(duration_shift / 2)
        tex_typing_animate(self, text_func_equation, typing_interval=0.4)
        self.play(
            text_func_equation.animate.set_color_by_text_to_color_map({
                "函数": BLUE,
                "方程": WHITE
            }),
            # relative position
            groups_tex_equation_part[0][0].animate.set_color(BLUE),
            groups_tex_equation_part[2][2].animate.set_color(BLUE),
            groups_tex_equation_part[3][2].animate.set_color(BLUE),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(max(duration_shift / 2 - 1.5, 0))
        [mob.clear_updaters() for mob in [
            control_dot_x, control_dot_y, decimal_num_x, decimal_num_y,
            decimal_x_placer_1, decimal_y_placer_1, decimal_x_placer_2, decimal_y_placer_2,
        ]]
        self.camera.frame.clear_updaters()
        self.wait(1)
        self.play(
            # self.camera.frame.animate.shift(UP * 0.5),
            FadeOut(decimal_num_x),
            FadeOut(decimal_num_y),
            FadeOut(axis_x),
            FadeOut(axis_y),
            FadeOut(tex_x),
            FadeOut(tex_y),
            FadeOut(control_dot_x),
            FadeOut(control_dot_y),
        )
        self.play(
            TransformMatchingShapes(group_decimal_tex_equation, tex_equation_cpy),
            TransformMatchingStrings(text_func_equation, text_func_equation_ca, key_map={
                "方程": "方程",
            }, path_arc=90 * DEGREES),
            FadeOut(decimal_x_placer_1),
            FadeOut(decimal_y_placer_1),
            FadeOut(decimal_x_placer_2),
            FadeOut(decimal_y_placer_2),
        )
        self.wait(1.5)

        # Show the substitution logic For f(x+y)=f(x)+f(y)
        placer_temp_up = UP * 0.6
        x_placer_cpy_1 = tex_equation_cpy[2].copy().shift(placer_temp_up)
        y_placer_cpy_1 = tex_equation_cpy[4].copy().shift(placer_temp_up)
        x_placer_cpy_2 = tex_equation_cpy[9].copy().shift(placer_temp_up)
        y_placer_cpy_2 = tex_equation_cpy[14].copy().shift(placer_temp_up)
        tex_zero_red = Tex("0").set_color(RED).move_to(x_placer_cpy_1.get_center())
        tex_zero_green = Tex("0").set_color(GREEN).move_to(y_placer_cpy_1.get_center())
        tex_zero_red_2 = Tex("0").set_color(RED).move_to(x_placer_cpy_2.get_center())
        tex_zero_green_2 = Tex("0").set_color(GREEN).move_to(y_placer_cpy_2.get_center())
        tex_zero_red_cpy = tex_zero_red.copy().move_to(x_placer_cpy_1.get_center()).shift(-placer_temp_up + UP * 0.03) # finetune
        tex_zero_green_cpy = tex_zero_green.copy().move_to(y_placer_cpy_1.get_center()).shift(-placer_temp_up + UP * 0.08)
        tex_zero_red_2_cpy = tex_zero_red_2.copy().move_to(x_placer_cpy_2.get_center()).shift(-placer_temp_up + UP * 0.03)
        tex_zero_green_2_cpy = tex_zero_green_2.copy().move_to(y_placer_cpy_2.get_center()).shift(-placer_temp_up + UP * 0.08)
        tex_zero_red_rotate_p = x_placer_cpy_1.get_left()
        tex_zero_green_rotate_p = y_placer_cpy_1.get_left()
        tex_zero_red_2_rotate_p = x_placer_cpy_2.get_right()
        tex_zero_green_2_rotate_p = y_placer_cpy_2.get_right()
        tex_zero_red.rotate(-PI / 2, about_point=tex_zero_red_rotate_p)
        tex_zero_green.rotate(-PI / 2, about_point=tex_zero_green_rotate_p)
        tex_zero_red_2.rotate(-PI / 2, about_point=tex_zero_red_2_rotate_p)
        tex_zero_green_2.rotate(-PI / 2, about_point=tex_zero_green_2_rotate_p)
        group_zero_equation = VGroup(
            tex_zero_red_cpy, tex_zero_green_cpy, tex_zero_red_2_cpy, tex_zero_green_2_cpy,
            *tex_equation_cpy[0:2], tex_equation_cpy[3], *tex_equation_cpy[5:9], *tex_equation_cpy[10:14], tex_equation_cpy[15]
        )

        self.play(
            self.camera.frame.animate.shift(UP * 1.1),
            text_func_equation_ca.animate.shift(UP * 0.8),
            TransformFromCopy(tex_equation_cpy[2], x_placer_cpy_1),
            TransformFromCopy(tex_equation_cpy[4], y_placer_cpy_1),
            TransformFromCopy(tex_equation_cpy[9], x_placer_cpy_2),
            TransformFromCopy(tex_equation_cpy[14], y_placer_cpy_2),
        )
        self.play(
            x_placer_cpy_1.animate.rotate(PI / 2, about_point=x_placer_cpy_1.get_left()),
            y_placer_cpy_1.animate.rotate(PI / 2, about_point=y_placer_cpy_1.get_left()),
            x_placer_cpy_2.animate.rotate(PI / 2, about_point=x_placer_cpy_2.get_right()),
            y_placer_cpy_2.animate.rotate(PI / 2, about_point=y_placer_cpy_2.get_right()),
            FadeOut(x_placer_cpy_1, x_placer_cpy_1.get_center() + placer_temp_up),
            FadeOut(y_placer_cpy_1, y_placer_cpy_1.get_center() + placer_temp_up),
            FadeOut(x_placer_cpy_2, x_placer_cpy_2.get_center() + placer_temp_up),
            FadeOut(y_placer_cpy_2, y_placer_cpy_2.get_center() + placer_temp_up),
            FadeIn(tex_zero_red),
            FadeIn(tex_zero_green),
            FadeIn(tex_zero_red_2),
            FadeIn(tex_zero_green_2),
            tex_zero_red.animate.rotate(PI / 2, about_point=tex_zero_red_rotate_p),
            tex_zero_green.animate.rotate(PI / 2, about_point=tex_zero_green_rotate_p),
            tex_zero_red_2.animate.rotate(PI / 2, about_point=tex_zero_red_2_rotate_p),
            tex_zero_green_2.animate.rotate(PI / 2, about_point=tex_zero_green_2_rotate_p),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1)
        self.play(
            # self.camera.frame.animate.scale(1.1),
            TransformMatchingShapes(tex_zero_red, tex_zero_red_cpy),
            TransformMatchingShapes(tex_zero_green, tex_zero_green_cpy),
            TransformMatchingShapes(tex_zero_red_2, tex_zero_red_2_cpy),
            TransformMatchingShapes(tex_zero_green_2, tex_zero_green_2_cpy),
            FadeOut(tex_equation_cpy[2]),
            FadeOut(tex_equation_cpy[4]),
            FadeOut(tex_equation_cpy[9]),
            FadeOut(tex_equation_cpy[14]),
        )
        self.play(
            self.camera.frame.animate.move_to(ORIGIN),
            group_zero_equation.animate.move_to(ORIGIN),
            FadeOut(text_func_equation_ca),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1.5)

        # show the simplified equation processing
        group_left_0p0 = VGroup(tex_zero_red_cpy, tex_zero_green_cpy, tex_equation_cpy[3])
        rec_left_0p0 = SurroundingRectangle(group_left_0p0, buff=0.1).set_color(YELLOW)
        group_right_f0pf0 = VGroup(tex_zero_red_2_cpy, tex_zero_green_2_cpy, *tex_equation_cpy[7:9], *tex_equation_cpy[10:14], tex_equation_cpy[15])
        rec_right_f0pf0 = SurroundingRectangle(group_right_f0pf0, buff=0.1).set_color(YELLOW)
        tex_eq_simplified = Tex("f(0)=2f(0)").set_color_by_tex_to_color_map(colormap_xy | {"f": BLUE})
        tex_eq_simplified_final = Tex("f(0)=0").set_color_by_tex_to_color_map(colormap_xy | {"f": BLUE})
        tex_f1 = Tex("f(1)").set_color_by_tex_to_color_map(colormap_xy | {"f": BLUE})
        tex_f1_quest = Tex("f(1)=?").set_color_by_tex_to_color_map(colormap_xy | {"f": BLUE})

        self.play(
            Succession(Write(rec_left_0p0), Uncreate(rec_left_0p0)),
            Succession(Write(rec_right_f0pf0), Uncreate(rec_right_f0pf0)),
            run_time=1.5,
            rate_func=smooth,
        )
        self.play(TransformMatchingShapes(group_zero_equation, tex_eq_simplified))
        self.wait(1.5)
        self.play(TransformMatchingTex(tex_eq_simplified, tex_eq_simplified_final, key_map={
            "f(0)": "f(0)",
        }, path_arc=90 * DEGREES))
        self.play(WiggleOutThenIn(tex_eq_simplified_final[2]))
        self.wait(1)
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 3, 1, 0.015, "out")))
        self.play(TransformMatchingTex(tex_eq_simplified_final, tex_f1, key_map={
            "f": "f",
            "(0": "(1",
            ")": ")",
        }, path_arc=90 * DEGREES))
        self.play(TransformMatchingTex(tex_f1, tex_f1_quest, key_map={"f(1)": "f(1)"}, path_arc=90 * DEGREES))
        self.wait(1.5)
        self.camera.frame.clear_updaters()

        # Show graph of f(1)=k
        colormap_xy_f = colormap_xy | {"f": BLUE}
        tex_f1_eq_k = Tex("f(1)=k").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 4).scale(0.75)
        axes = Axes(
            x_range=(-4, 4),
            y_range=(-4, 4),
            height=8,
            width=8,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
        ).shift(RIGHT * 2.5)
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        dot_0 = Dot(axes.c2p(0, 0)).set_color(RED)
        dot_1_k = Dot(axes.c2p(1, 0)).set_color(YELLOW_C)
        dot_2 = dot_1_k.copy()
        dash_x1 = DashedLine(axes.c2p(1, -4), axes.c2p(1, 4), color=YELLOW_C).set_stroke(width=1.5)
        tex_f1p1_eq_1p1 = Tex("f(1+1)=f(1)+f(1)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 3.5 + DOWN * 0.6).scale(0.75)
        tex_f1p1_eq_1p1[2].set_color(RED)
        tex_f1p1_eq_1p1[4].set_color(GREEN)
        tex_f1p1_eq_1p1[9].set_color(RED)
        tex_f1p1_eq_1p1[14].set_color(GREEN)
        tex_f2_eq_1p1 = Tex("f(2)=f(1)+f(1)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 4 + DOWN * 0.6).scale(0.75)
        tex_f2_eq_1p1[7].set_color(RED)
        tex_f2_eq_1p1[12].set_color(GREEN)
        tex_f2_eq_2k = Tex("f(2)=2k").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 4 + DOWN * 0.6).scale(0.75)
        tex_f1pn_eq_1pn = Tex("f(1+n)=f(1)+f(n)").set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK}).move_to(LEFT * 3.85 + DOWN * 0.6).scale(0.75)
        tex_f1pn_eq_1pn[2].set_color(RED)
        tex_f1pn_eq_1pn[9].set_color(RED)
        tex_f1pn_eq_kpn = Tex("f(1+n)=k+f(n)").set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK}).move_to(LEFT * 3.85 + DOWN * 0.6).scale(0.75)
        rec_f1pn_k = SurroundingRectangle(tex_f1pn_eq_kpn[7], buff=0.1).set_color(YELLOW)

        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.shift(RIGHT * animate_shift_smooth(now, self.time, 2, 0.01, "pos")).scale(animate_scaling_smooth(now, self.time, 3, 0.01, "in")))
        self.play(
            tex_f1_quest.animate.shift(LEFT * 3.5),
            Write(axes, lag_ratio=0.1),
            Write(dot_0),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(0.5)
        self.play(FadeIn(dash_x1))
        self.play(
            TransformMatchingTex(tex_f1_quest, tex_f1_eq_k, key_map={
                "f(1)=": "f(1)=",
            }, path_arc=90 * DEGREES),
            Write(dot_1_k),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(0.5)
        self.camera.frame.clear_updaters()
        now = self.time
        def timing(duration=2.5):
            return smooth(min(duration, self.time - now) / duration)
        dot_1_k.add_updater(lambda d: d.move_to(axes.c2p(1, np.sin(timing() * 2.1 * PI) * 3)))
        self.wait(3)
        dot_1_k.clear_updaters()
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_smooth(now, self.time, 3, 0.008, "out")).shift(DOWN * animate_shift_smooth(now, self.time, 2, 0.01, "pos")))
        self.play(Write(tex_f1p1_eq_1p1))
        self.wait(0.5)
        dot_2.move_to(dot_1_k.get_center())
        self.add(dot_2)
        self.play(
            TransformMatchingTex(tex_f1p1_eq_1p1, tex_f2_eq_1p1, key_map={
                "1+1": "2",
            }, path_arc=90 * DEGREES),
            dot_2.animate.shift(UP * dot_1_k.get_y()),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(tex_f2_eq_1p1, tex_f2_eq_2k, key_map={
                "f(1)+f(1)": "2k",
            }, path_arc=90 * DEGREES),
            dot_2.animate.shift(RIGHT * (axes.c2p(1, 0) - axes.c2p(0, 0))[0]),
            FadeOut(dash_x1),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(2)
        self.play(
            tex_f1_eq_k.animate.shift(UP * 0.6),
            tex_f2_eq_2k.animate.shift(UP * 0.6),
            FadeIn(tex_f1pn_eq_1pn),
        )
        self.wait(0.5)
        self.play(
            TransformMatchingTex(tex_f1pn_eq_1pn, tex_f1pn_eq_kpn, key_map={
                "f(1+n)=": "f(1+n)=",
                "f(1)": "k",
                "+f(n)": "+f(n)",
            }, path_arc=90 * DEGREES),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1)
        new_ori = np.array([0.98, 0, 0])
        new_uni = 0.75 * (axes.c2p(1, 0)[0] - axes.c2p(0, 0)[0])
        self.play(
            axes.animate.scale(0.75).shift(LEFT * 1.5),
            dot_0.animate.move_to(new_ori),
            dot_1_k.animate.move_to(new_ori + new_uni * (UP + RIGHT)),
            dot_2.animate.move_to(new_ori + new_uni * 2 * (UP + RIGHT)),
        )
        self.wait(1)
        
        arrow_x_2_3 = Arrow(new_ori + new_uni * 2 * (UP + RIGHT), new_ori + new_uni * (2 * UP + 3 * RIGHT), buff=0).set_color(PINK)
        arrow_x_2_3_label = Tex("n\\leftarrow n+1").scale(0.5).next_to(arrow_x_2_3, DOWN, buff=0.05).set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK, "(": WHITE, ")": WHITE, "\\leftarrow": WHITE, "+": WHITE})
        arrow_f_2_k = Arrow(new_ori + new_uni * (2 * UP + 3 * RIGHT), new_ori + new_uni * 3 * (UP + RIGHT), buff=0).set_color(BLUE)
        arrow_f_2_k_label = Tex("f(n+1)\\leftarrow f(n)+k").set_color(YELLOW_C).scale(0.5).next_to(arrow_f_2_k, RIGHT, buff=0.05).set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK, "(": WHITE, ")": WHITE, "\\leftarrow": WHITE, "+": WHITE, "1": WHITE})
        dot_nk = Dot(arrow_f_2_k.get_end()).set_color(PINK)
        tex_f1pnsfnek = Tex("f(1+n)-f(n)=k").set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK}).move_to(tex_f1pn_eq_kpn.get_center()).scale(0.75)
        tex_fnef1pnsk  = Tex("f(n)=f(1+n)-k").set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK}).move_to(tex_f1pn_eq_kpn.get_center()).scale(0.75)
        arrow_x_0_m1 = Arrow(new_ori, new_ori + new_uni * LEFT, buff=0).set_color(PINK)
        arrow_x_0_m1_label = Tex("n\\leftarrow n-1").scale(0.5).next_to(arrow_x_0_m1, UP, buff=0.2).shift(LEFT * 0.3).set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK, "(": WHITE, ")": WHITE, "\\leftarrow": WHITE, "-": WHITE})
        arrow_0_mk = Arrow(new_ori + new_uni * LEFT, new_ori + new_uni * (DOWN + LEFT), buff=0).set_color(BLUE)
        arrow_0_mk_label = Tex("f(n-1)\\leftarrow f(n)-k").set_color(YELLOW_C).scale(0.5).next_to(arrow_0_mk, DOWN, buff=0.2).shift(LEFT * 0.5).set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK, "(": WHITE, ")": WHITE, "\\leftarrow": WHITE, "-": WHITE, "1": WHITE})
        dot_mk = Dot(arrow_0_mk.get_end()).set_color(PINK)
        dots_all = [Dot(new_ori + p * new_uni * (UP + RIGHT)).set_color(PINK) for p in range(-4, 5)]
        tex_fnenk = Tex("f(n)=nk").set_color_by_tex_to_color_map(colormap_xy_f | {"n": PINK}).move_to(LEFT * 3.85).scale(0.75)

        self.play(Write(rec_f1pn_k))
        self.play(Write(arrow_x_2_3))
        self.play(Write(arrow_x_2_3_label))
        self.wait(0.5)
        self.play(Write(arrow_f_2_k))
        self.play(Write(arrow_f_2_k_label))
        self.play(Write(dot_nk))
        self.wait(1.5)
        self.play(
            FadeOut(rec_f1pn_k),
            TransformMatchingTex(tex_f1pn_eq_kpn, tex_f1pnsfnek, key_map={
                "f(1+n)": "f(1+n)",
                "f(n)": "f(n)",
                "k": "k",
                "=": "=",
            })
        )
        self.wait(0.5)
        self.play(
            TransformMatchingTex(tex_f1pnsfnek, tex_fnef1pnsk, key_map={
                "f(1+n)": "f(1+n)",
                "f(n)": "f(n)",
                "k": "k",
                "=": "=",
            })
        )
        self.wait(1)
        self.play(Write(arrow_x_0_m1))
        self.play(Write(arrow_x_0_m1_label))
        self.wait(0.5)
        self.play(Write(arrow_0_mk))
        self.play(Write(arrow_0_mk_label))
        self.play(Write(dot_mk))
        self.wait(2)
        self.play(
            TransformMatchingShapes(VGroup(
                tex_f1_eq_k, tex_f2_eq_2k, tex_fnef1pnsk
            ), tex_fnenk),
            FadeOut(VGroup(
                arrow_x_2_3, arrow_f_2_k, arrow_x_0_m1, arrow_0_mk,
                arrow_x_2_3_label, arrow_f_2_k_label, arrow_x_0_m1_label, arrow_0_mk_label,
            ), lag_ratio=0.1)
        )
        self.play(Write(VGroup(
            *dots_all
        ), lag_ratio=0.1))
        self.play(WiggleOutThenIn(tex_fnenk[2]))
        self.wait(2)

        holdplace_rec = Rectangle(width=30, height=30, fill_opacity=1).set_color("#333333")
        self.play(FadeIn(holdplace_rec))
        self.wait(1)

class CAPart2_2(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_1 = {"x": RED, "y": GREEN, "k": YELLOW_B, "f": BLUE, "n": PINK}
        tex_fp = Tex("f\\left(p\\right)").set_color_by_tex_to_color_map({
            "f": BLUE, "p": RED, "\\left(": WHITE, "\\right)": WHITE
        })
        tex_fpqq = Tex("f\\left(\\frac{p}{q}\\times q\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}\\times q": RED,
            "\\left(": WHITE, "\\right)": WHITE
        })
        tex_fpqqqq = Tex("f\\left(\\frac{p}{q}+\\dots+\\frac{p}{q}+\\frac{p}{q}+\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        })
        group_fpqqqq_0_x = VGroup(*tex_fpqqqq[2:-5])
        group_fpqqqq_0_y = VGroup(*tex_fpqqqq[-4:-1])
        sr_rec_0_x = SurroundingRectangle(group_fpqqqq_0_x, buff=0.1).set_color(RED_A)
        sr_rec_0_y = SurroundingRectangle(group_fpqqqq_0_y, buff=0.1).set_color(GREEN_A)
        brace_x_0 = Brace(group_fpqqqq_0_x, UP)
        brace_y_0 = Brace(group_fpqqqq_0_y, UP)
        tex_0_x = Tex("x").set_color(RED_A).next_to(brace_x_0, UP, buff=0.1)
        tex_0_y = Tex("y").set_color(GREEN_A).next_to(brace_y_0, UP, buff=0.1)
        tex_fpqqqq_1 = Tex("f\\left(\\frac{p}{q}+\\dots+\\frac{p}{q}+\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        })
        [word.set_color(GREEN) for word in tex_fpqqqq_1[-4:-1]]
        group_fpqqqq_1_x = VGroup(*tex_fpqqqq_1[2:-12])
        group_fpqqqq_1_y = VGroup(*tex_fpqqqq_1[-11:-8])
        sr_rec_1_x = SurroundingRectangle(group_fpqqqq_1_x, buff=0.1).set_color(RED_A)
        sr_rec_1_y = SurroundingRectangle(group_fpqqqq_1_y, buff=0.1).set_color(GREEN_A)
        brace_x_1 = Brace(group_fpqqqq_1_x, UP)
        brace_y_1 = Brace(group_fpqqqq_1_y, UP)
        tex_1_x = Tex("x").set_color(RED_A).next_to(brace_x_1, UP, buff=0.1)
        tex_1_y = Tex("y").set_color(GREEN_A).next_to(brace_y_1, UP, buff=0.1)
        tex_fpqqqq_2 = Tex("f\\left(\\frac{p}{q}+\\dots+\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        })
        [word.set_color(GREEN) for word in tex_fpqqqq_2[-4:-1]]
        [word.set_color(GREEN) for word in tex_fpqqqq_2[-11:-8]]
        group_fpqqqq_2_x = VGroup(*tex_fpqqqq_2[2:9])
        group_fpqqqq_2_y = VGroup(*tex_fpqqqq_2[10:13])
        sr_rec_2_x = SurroundingRectangle(group_fpqqqq_2_x, buff=0.1).set_color(RED_A)
        sr_rec_2_y = SurroundingRectangle(group_fpqqqq_2_y, buff=0.1).set_color(GREEN_A)
        brace_x_2 = Brace(group_fpqqqq_2_x, UP)
        brace_y_2 = Brace(group_fpqqqq_2_y, UP)
        tex_2_x = Tex("x").set_color(RED_A).next_to(brace_x_2, UP, buff=0.1)
        tex_2_y = Tex("y").set_color(GREEN_A).next_to(brace_y_2, UP, buff=0.1)
        tex_fpqqqq_3 = Tex("f\\left(\\frac{p}{q}+\\dots\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": RED,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE
        })
        [word.set_color(GREEN) for word in tex_fpqqqq_3[-4:-1]]
        [word.set_color(GREEN) for word in tex_fpqqqq_3[-11:-8]]
        [word.set_color(GREEN) for word in tex_fpqqqq_3[-18:-15]]
        group_fpqqqq_3_x = VGroup(*tex_fpqqqq_3[2:5])
        group_fpqqqq_3_y = VGroup(*tex_fpqqqq_3[6:9])
        sr_rec_3_x = SurroundingRectangle(group_fpqqqq_3_x, buff=0.1).set_color(RED_A)
        sr_rec_3_y = SurroundingRectangle(group_fpqqqq_3_y, buff=0.1).set_color(GREEN_A)
        brace_x_3 = Brace(group_fpqqqq_3_x, UP)
        brace_y_3 = Brace(group_fpqqqq_3_y, UP)
        tex_3_x = Tex("x").set_color(RED_A).next_to(brace_x_3, UP, buff=0.1)
        tex_3_y = Tex("y").set_color(GREEN_A).next_to(brace_y_3, UP, buff=0.1)
        tex_fpqqqq_final = Tex("f\\left(\\frac{p}{q}\\right)+\\dots+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)+f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{p}{q}": GREEN,
            "+": WHITE,
            "\\left(": WHITE, "\\right)": WHITE, "\\dots": WHITE
        })
        brace_q1 = Brace(VGroup(tex_fpqqqq[1], tex_fpqqqq[-1]), DOWN)
        brace_q2 = Brace(VGroup(tex_fpqqqq_1[1], tex_fpqqqq_1[17]), DOWN)
        brace_q3 = Brace(VGroup(tex_fpqqqq_2[1], tex_fpqqqq_2[13]), DOWN)
        brace_q4 = Brace(VGroup(tex_fpqqqq_3[1], tex_fpqqqq_3[9]), DOWN)
        brace_final = Brace(VGroup(tex_fpqqqq_final[1], tex_fpqqqq_final[-1]), DOWN)
        tex_q = Tex("q").set_color(WHITE).scale(0.75).next_to(brace_q1, DOWN, buff=0.1)
        tex_qs1 = Tex("q-1").set_color(WHITE).scale(0.75).next_to(brace_q2, DOWN, buff=0.1)
        tex_qs2 = Tex("q-2").set_color(WHITE).scale(0.75).next_to(brace_q3, DOWN, buff=0.1)
        tex_qs3 = Tex("q-3").set_color(WHITE).scale(0.75).next_to(brace_q4, DOWN, buff=0.1)
        tex_qs_final = Tex("q").set_color(WHITE).scale(0.75).next_to(brace_final, DOWN, buff=0.1)
        tex_q_fa_pq = Tex("qf\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "q": WHITE,
            "\\frac{p}{q}": GREEN,
            "\\left(": WHITE, "\\right)": WHITE
        })
        tex_fp_e_qfapq = Tex("f\\left(p\\right)=qf\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "p": RED,
            "q": WHITE,
            "\\frac{p}{q}": GREEN,
            "\\left(": WHITE, "\\right)": WHITE
        })
        tex_kp_e_qfapq = Tex("kp=qf\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "k": YELLOW_B,
            "p": RED,
            "\\frac{p}{q}": GREEN,
            "\\left(": WHITE, "\\right)": WHITE
        })
        tex_fakpq_e_fapq = Tex("k\\frac{p}{q}=f\\left(\\frac{p}{q}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "k": YELLOW_B,
            "\\frac{p}{q}": GREEN,
            "\\left(": WHITE,
            "\\right)": WHITE
        })
        tex_ffapq_e_fakpq = Tex("f\\left(\\frac{p}{q}\\right)=k\\frac{p}{q}").set_color_by_tex_to_color_map({
            "f": BLUE,
            "k": YELLOW_B,
            "\\frac{p}{q}": GREEN,
            "\\left(": WHITE,
            "\\right)": WHITE
        })

        self.play(Write(tex_fp))
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_fp, tex_fpqq, map_index=(
                [0, 1, 2, 3],
                [0, 1, 2, 7]
            )),
            run_time=2
        )
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_fpqq, tex_fpqqqq, map_index=(
                [0, 1, 2, 3, 4, 7],
                [0, 1, 2, 3, 4, 21]
            )),
            Write(brace_q1),
            run_time=2
        )
        self.wait(1.5)
        self.play(Write(sr_rec_0_x), Write(sr_rec_0_y))
        self.play(
            Write(brace_x_0), Write(brace_y_0),
            Write(tex_0_x), Write(tex_0_y),
        )
        self.wait(0.5)
        self.play(Write(tex_q))
        self.wait(2)
        self.play(
            FadeOut(VGroup(
                sr_rec_0_x, sr_rec_0_y, brace_x_0, brace_y_0, tex_0_x, tex_0_y,
            )),
        )
        self.play(
            *transformMatchingIndex(tex_fpqqqq, tex_fpqqqq_1, map_index=(
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 17]
            )),
            TransformMatchingTex(tex_q, tex_qs1, key_map={"q": "q"}),
            ReplacementTransform(brace_q1, brace_q2),
            run_time=2
        )
        self.wait(2)
        self.play(Write(sr_rec_1_x), Write(sr_rec_1_y))
        self.play(
            Write(brace_x_1), Write(brace_y_1),
            Write(tex_1_x), Write(tex_1_y),
        )
        self.wait(1.5)
        self.play(
            FadeOut(sr_rec_1_x),
            FadeOut(sr_rec_1_y),
            FadeOut(brace_x_1),
            FadeOut(brace_y_1),
            FadeOut(tex_1_x),
            FadeOut(tex_1_y),
        )
        self.play(
            *transformMatchingIndex(tex_fpqqqq_1, tex_fpqqqq_2, map_index=(
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18, 19, 13, 22, 23, 24, 25, 26, 27]
            )),
            TransformMatchingTex(tex_qs1, tex_qs2, key_map={"q": "q"}),
            ReplacementTransform(brace_q2, brace_q3),
            run_time=2
        )
        self.wait(2)
        self.play(Write(sr_rec_2_x), Write(sr_rec_2_y))
        self.play(
            Write(brace_x_2), Write(brace_y_2),
            Write(tex_2_x), Write(tex_2_y),
        )
        self.wait(1.5)
        self.play(
            FadeOut(sr_rec_2_x),
            FadeOut(sr_rec_2_y),
            FadeOut(brace_x_2),
            FadeOut(brace_y_2),
            FadeOut(tex_2_x),
            FadeOut(tex_2_y),
        )
        self.play(
            *transformMatchingIndex(tex_fpqqqq_2, tex_fpqqqq_3, map_index=(
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 13, 14, 15, 9, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
            )),
            TransformMatchingTex(tex_qs2, tex_qs3, key_map={"q": "q"}),
            ReplacementTransform(brace_q3, brace_q4),
            run_time=2
        )
        self.wait(2)
        self.play(Write(sr_rec_3_x), Write(sr_rec_3_y))
        self.play(
            Write(brace_x_3), Write(brace_y_3),
            Write(tex_3_x), Write(tex_3_y),
        )
        self.wait(1.5)
        self.play(
            FadeOut(sr_rec_3_x),
            FadeOut(sr_rec_3_y),
            FadeOut(brace_x_3),
            FadeOut(brace_y_3),
            FadeOut(tex_3_x),
            FadeOut(tex_3_y),
        )
        self.play(
            *transformMatchingIndex(tex_fpqqqq_3, tex_fpqqqq_final, map_index=(
                [0, 1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                [0, 1, 2, 3, 4, 7, 8, 9, 5, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
            )),
            TransformMatchingTex(tex_qs3, tex_qs_final, key_map={"q": "q"}),
            ReplacementTransform(brace_q4, brace_final),
            run_time=2
        )
        self.wait(2)
        self.play(
            FadeOut(brace_final),
            FadeOut(tex_qs_final),
            *transformMatchingIndex(tex_fpqqqq_final, tex_q_fa_pq, map_index=(
                [0, 1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30],
                [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
            )),
            run_time=2
        )
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_q_fa_pq, tex_fp_e_qfapq, map_index=(
                [0, 1, 2, 3, 4, 5, 6],
                [5, 6, 7, 8, 9, 10, 11]
            )),
            run_time=2
        )
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_fp_e_qfapq, tex_kp_e_qfapq, map_index=(
                [0, 2, 4, 5, 6, 7, 8, 9, 10, 11],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            )),
            run_time=2
        )
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_kp_e_qfapq, tex_fakpq_e_fapq, map_index=(
                [0, 1, 3, 4, 5, 6, 7, 8, 9],
                [0, 1, 3, 5, 6, 7, 8, 9, 10]
            )),
            run_time=2
        )
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_fakpq_e_fapq, tex_ffapq_e_fakpq, map_index=(
                [0, 1, 2, 3, 5, 6, 7, 8, 9, 10],
                [7, 8, 9, 10, 0, 1, 2, 3, 4, 5]
            )),
            run_time=2
        )
        self.wait(1)

class CAPart2_3(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        tex_recent = Tex("f\\left(\\frac{p}{q}\\right)=k\\frac{p}{q}").set_color_by_tex_to_color_map({
            "f": BLUE,
            "k": YELLOW_B,
            "\\frac{p}{q}": GREEN,
            "\\left(": WHITE,
            "\\right)": WHITE
        })

        self.add(tex_recent)
        self.wait(1)

        axes = Axes(
            x_range=(-4, 4),
            y_range=(-4, 4),
            height=8,
            width=8,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
        ).shift(RIGHT * 2)
        axes.add_coordinate_labels(
            font_size=20,
            num_decimal_places=1,
        )
        dots_div_1 = [Dot(axes.c2p(k, k), radius=0.05).set_color(RED) for k in range(-4, 5)]
        texs_label_1 = [Tex("M\\frac{t}{1}".replace("t", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(RED).scale(0.4).next_to(dots_div_1[k + 4], RIGHT + DOWN, buff=0.2) for k in range(-4, 5)]
        dash_line_1 = [DashedLine(dots_div_1[i].get_corner(RIGHT + DOWN), texs_label_1[i].get_corner(LEFT + UP)).set_stroke(width=0.4).set_color(RED) for i in range(len(dots_div_1))]

        dots_div_2 = [Dot(axes.c2p(k, k), radius=0.045).set_color(ORANGE) for k in [-3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5]]
        texs_label_2 = [Tex("M\\frac{t}{2}".replace("t", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(ORANGE).scale(0.4).next_to(dots_div_2[i], RIGHT + DOWN, buff=0.5) for i, k in enumerate([-7, -5, -3, -1, 1, 3, 5, 7])]
        dash_line_2 = [DashedLine(dots_div_2[i].get_corner(RIGHT + DOWN), texs_label_2[i].get_corner(LEFT + UP)).set_stroke(width=0.4).set_color(ORANGE) for i in range(len(dots_div_2))]

        dots_div_3 = [Dot(axes.c2p(k, k), radius=0.04).set_color(YELLOW) for k in [-3.667, -3.333, -2.667, -2.333, -1.667, -1.333, -0.667, -0.333, 0.333, 0.667, 1.333, 1.667, 2.333, 2.667, 3.333, 3.667]]
        texs_label_3 = [Tex("M\\frac{t}{3}".replace("t", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(YELLOW).scale(0.4).next_to(dots_div_3[i], LEFT + UP, buff=0.2) for i, k in enumerate([-11, -10, -8, -7, -5, -4, -2, -1, 1, 2, 4, 5, 7, 8, 10, 11])]
        dash_line_3 = [DashedLine(dots_div_3[i].get_corner(LEFT + UP), texs_label_3[i].get_corner(RIGHT + DOWN)).set_stroke(width=0.4).set_color(YELLOW) for i in range(len(dots_div_3))]

        dots_div_4 = [Dot(axes.c2p(k, k), radius=0.035).set_color(GREEN) for k in [-3.75, -3.25, -2.75, -2.25, -1.75, -1.25, -0.75, -0.25, 0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75]]
        texs_label_4 = [Tex("M\\frac{t}{4}".replace("t", str(abs(k))).replace("M", "-" if k <= 0 else "")).set_color(GREEN).scale(0.4).next_to(dots_div_4[i], LEFT + UP, buff=0.5) for i, k in enumerate([-15, -13, -11, -9, -7, -5, -3, -1, 1, 3, 5, 7, 9, 11, 13, 15])]
        dash_line_4 = [DashedLine(dots_div_4[i].get_corner(LEFT + UP), texs_label_4[i].get_corner(RIGHT + DOWN)).set_stroke(width=0.4).set_color(GREEN) for i in range(len(dots_div_4))]

        dash_kx_line = DashedLine(axes.c2p(-6, -6), axes.c2p(6, 6), color=GREY_C).set_stroke(width=4.5)
        
        self.play(
            tex_recent.animate.shift(LEFT * 4.2).scale(0.75),
            Write(axes, lag_ratio=0.1),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1)
        self.play(
            axes.animate.set_opacity(0.3),
            Write(VGroup(*dots_div_1), lag_ratio=0.3),
            run_time=2.5,
        )
        self.play(
            Write(VGroup(*texs_label_1), lag_ratio=0.3),
            Write(VGroup(*dash_line_1), lag_ratio=0.3),
            run_time=2,
        )
        self.wait(1)
        self.play(
            Write(VGroup(*dots_div_2), lag_ratio=0.3),
            run_time=2,
        )
        self.play(
            Write(VGroup(*texs_label_2), lag_ratio=0.3),
            Write(VGroup(*dash_line_2), lag_ratio=0.3),
            run_time=1.5,
        )
        self.wait(1)
        self.play(
            Write(VGroup(*dots_div_3), lag_ratio=0.3),
            run_time=1.5,
        )
        self.play(
            Write(VGroup(*texs_label_3), lag_ratio=0.3),
            Write(VGroup(*dash_line_3), lag_ratio=0.3),
            run_time=1,
        )
        self.wait(1)
        self.play(
            Write(VGroup(*dots_div_4), lag_ratio=0.3),
            run_time=1,
        )
        self.play(
            Write(VGroup(*texs_label_4), lag_ratio=0.3),
            Write(VGroup(*dash_line_4), lag_ratio=0.3),
            run_time=1,
        )
        self.wait(1)
        self.play(FadeIn(dash_kx_line), run_time=0.5)
        self.play(FadeOut(dash_kx_line), run_time=0.5)
        self.play(FadeIn(dash_kx_line), run_time=0.5)
        self.play(FadeOut(dash_kx_line), run_time=0.5)
        self.play(FadeIn(dash_kx_line), run_time=0.5)
        self.wait(1)
        self.play(
            FadeOut(VGroup(
                *dots_div_1, *texs_label_1, *dash_line_1,
                *dots_div_2, *texs_label_2, *dash_line_2,
                *dots_div_3, *texs_label_3, *dash_line_3,
                *dots_div_4, *texs_label_4, *dash_line_4,
            ), lag_ratio=0.1),
            run_time=2.5
        )
        self.wait(0.5)

        tex_sq2 = Tex("\\sqrt{2}").move_to(axes.c2p(np.sqrt(2), -0.4)).scale(0.5).set_color(RED)
        tex_phi = Tex("\\varphi").move_to(axes.c2p((np.sqrt(5) - 1) / 2, -0.4)).scale(0.5).set_color(ORANGE)
        tex_pi = Tex("\\pi").move_to(axes.c2p(np.pi, -0.4)).scale(0.5).set_color(YELLOW)
        dot_sq2 = Dot(axes.c2p(np.sqrt(2), 0), radius=0.04).set_color(RED)
        dot_phi = Dot(axes.c2p((np.sqrt(5) - 1) / 2, 0), radius=0.04).set_color(ORANGE)
        dot_pi = Dot(axes.c2p(np.pi, 0), radius=0.04).set_color(YELLOW)
        dash_sq2_up = DashedLine(axes.c2p(np.sqrt(2), 0), axes.c2p(np.sqrt(2), np.sqrt(2)), color=GREY_C).set_stroke(width=1.5)
        dash_phi_up = DashedLine(axes.c2p((np.sqrt(5) - 1) / 2, 0), axes.c2p((np.sqrt(5) - 1) / 2, (np.sqrt(5) - 1) / 2), color=GREY_C).set_stroke(width=1.5)
        dash_pi_up = DashedLine(axes.c2p(np.pi, 0), axes.c2p(np.pi, np.pi), color=GREY_C).set_stroke(width=1.5)
        dot_sq2_k = Dot(axes.c2p(np.sqrt(2), np.sqrt(2)), radius=0.04).set_color(RED)
        dot_phi_k = Dot(axes.c2p((np.sqrt(5) - 1) / 2, (np.sqrt(5) - 1) / 2), radius=0.04).set_color(ORANGE)
        dot_pi_k = Dot(axes.c2p(np.pi, np.pi), radius=0.04).set_color(YELLOW)
        text_sq2_k = Tex("k\\sqrt{2}").set_color(RED).scale(0.5).next_to(dot_sq2_k, LEFT + UP, buff=0.1)
        text_phi_k = Tex("k\\varphi").set_color(ORANGE).scale(0.5).next_to(dot_phi_k, LEFT + UP, buff=0.1)
        text_pi_k = Tex("k\\pi").set_color(YELLOW).scale(0.5).next_to(dot_pi_k, LEFT + UP, buff=0.1)
        text_quest = Text("?").scale(1.5).move_to(RIGHT * 4 + DOWN * 2).set_color(YELLOW)
        tex_f = Tex("f\\left(x\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "x": WHITE,
            "\\left(": WHITE,
            "\\right)": WHITE
        }).move_to(LEFT * 3.5).scale(1.1)
        underline_tex_f = Underline(tex_f, color=BLUE)
        text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A).next_to(underline_tex_f, DOWN, buff=0.1).scale(0.75).align_to(underline_tex_f, LEFT)
        image_correct = ImageMobject("right.png").scale(0.25).move_to(text_quest.get_center())

        self.play(
            Write(dot_sq2),
            Write(tex_sq2),
            run_time=1
        )
        self.play(
            Write(dot_phi),
            Write(tex_phi),
            run_time=1
        )
        self.play(
            Write(dot_pi),
            Write(tex_pi),
            run_time=1
        )
        self.wait(1)
        self.play(Write(text_quest))
        self.wait(1)
        self.play(
            Write(VGroup(
                dash_sq2_up, dash_phi_up, dash_pi_up,
            ), lag_ratio=0.1),
            run_time=1.5
        )
        self.play(
            Write(VGroup(
                dot_sq2_k, dot_phi_k, dot_pi_k,
            ), lag_ratio=0.1),
            run_time=1.5
        )
        self.play(
            Write(VGroup(
                text_sq2_k, text_phi_k, text_pi_k,
            ), lag_ratio=0.1),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            *transformMatchingIndex(tex_recent, tex_f, map_index=(
                [0, 1, 2, 3, 4, 5],
                [0, 1, 2, 2, 2, 3]
            )),
            lag_ratio = 0.1,
            run_time=1.5
        )
        self.play(
            Write(underline_tex_f),
            Write(text_continuous),
            run_time=1.5
        )
        self.wait(1)
        self.play(
            FadeOutToPoint(text_quest, text_quest.get_center() + LEFT),
            FadeInFromPoint(image_correct, image_correct.get_center() + RIGHT),
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(
                text_continuous, underline_tex_f,
                dot_sq2, dot_phi, dot_pi,
                tex_sq2, tex_phi, tex_pi,
                dash_sq2_up, dash_phi_up, dash_pi_up,
                dot_sq2_k, dot_phi_k, dot_pi_k,
                text_sq2_k, text_phi_k, text_pi_k,
                axes, dash_kx_line, tex_f
            ), lag_ratio=0.1),
            FadeOut(image_correct),
            run_time=1.5
        )
        self.wait(1)


# class CAPart2_4(Scene):
#     manim_config.tex.template = "ctex"
    
#     def construct(self):
#         colormap_xy_f = {"x": RED, "y": GREEN, "k": YELLOW_B, "f": BLUE, "n": PINK, "(": WHITE, ")": WHITE, "+": WHITE, "-": WHITE, "\\left(": WHITE, "\\right)": WHITE}
        
#         tex_f = Tex("f(x)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 6 + UP * 3.2).scale(1.05)
#         underline_tex_f = Underline(tex_f, color=BLUE)
#         text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT)
#         axes = Axes(
#             x_range=(-8, 8),
#             y_range=(-4, 4),
#             height=8,
#             width=16,
#             axis_config={
#                 "stroke_color": GREY_A,
#                 "stroke_width": 2,
#             },
#         )
#         axes.add_coordinate_labels(
#             font_size=20,
#             num_decimal_places=1,
#         )
#         func = lambda x: (math.sin(1.5 * x) + x / 2) * math.exp(0.1 * x)
#         func_graph = axes.get_graph(
#             func,
#             color=BLUE,
#         )
#         func_label = axes.get_graph_label(func_graph, label='f(x)', x=3.5)
#         func_label.set_color_by_tex_to_color_map(colormap_xy_f)
#         dot_x_1 = Dot(axes.c2p(1, 0), radius=0.06).set_color(RED)
#         dot_x_1_4 = Dot(axes.c2p(1.4, 0), radius=0.06).set_color(RED)
#         dot_x_1_41 = Dot(axes.c2p(1.41, 0), radius=0.02).set_color(RED)
#         dot_x_1_414 = Dot(axes.c2p(1.414, 0), radius=0.009).set_color(RED)
#         dot_x_1_4142 = Dot(axes.c2p(1.4142, 0), radius=0.006).set_color(RED)
#         dot_y_1 = Dot(axes.c2p(0, func(1)), radius=0.06).set_color(GREEN)
#         dot_y_1_4 = Dot(axes.c2p(0, func(1.4)), radius=0.06).set_color(GREEN)
#         dot_y_1_41 = Dot(axes.c2p(0, func(1.41)), radius=0.02).set_color(GREEN)
#         dot_y_1_414 = Dot(axes.c2p(0, func(1.414)), radius=0.009).set_color(GREEN)
#         dot_y_1_4142 = Dot(axes.c2p(0, func(1.4142)), radius=0.006).set_color(GREEN)
#         dash_v_1 = DashedLine(axes.c2p(1, 0), axes.c2p(1, func(1)), color=GREY_C).set_stroke(width=1.5)
#         dash_v_1_4 = DashedLine(axes.c2p(1.4, 0), axes.c2p(1.4, func(1.4)), color=GREY_C).set_stroke(width=1.5)
#         dash_v_1_41 = DashedLine(axes.c2p(1.41, 0), axes.c2p(1.41, func(1.41)), color=GREY_C).set_stroke(width=1)
#         dash_v_1_414 = DashedLine(axes.c2p(1.414, 0), axes.c2p(1.414, func(1.414)), color=GREY_C).set_stroke(width=0.1)
#         dash_v_1_4142 = DashedLine(axes.c2p(1.4142, 0), axes.c2p(1.4142, func(1.4142)), color=GREY_C).set_stroke(width=0.02)
#         dash_h_1 = DashedLine(axes.c2p(1, func(1)), axes.c2p(0, func(1)), color=GREY_C).set_stroke(width=1.5)
#         dash_h_1_4 = DashedLine(axes.c2p(1.4, func(1.4)), axes.c2p(0, func(1.4)), color=GREY_C).set_stroke(width=1.5)
#         dash_h_1_41 = DashedLine(axes.c2p(1.41, func(1.41)), axes.c2p(0, func(1.41)), color=GREY_C).set_stroke(width=1)
#         dash_h_1_414 = DashedLine(axes.c2p(1.414, func(1.414)), axes.c2p(0, func(1.414)), color=GREY_C).set_stroke(width=0.1)
#         dash_h_1_4142 = DashedLine(axes.c2p(1.4142, func(1.4142)), axes.c2p(0, func(1.4142)), color=GREY_C).set_stroke(width=0.02)
#         tex_x_1 = Tex("1").set_color(RED).scale(0.6).next_to(dot_x_1, DOWN + RIGHT, buff=0.01)
#         tex_x_1_4 = Tex("1.4").set_color(RED).scale(0.3).next_to(dot_x_1_4, DOWN + RIGHT, buff=0.01)
#         tex_x_1_41 = Tex("1.41").set_color(RED).scale(0.25).next_to(dot_x_1_41, DOWN + RIGHT, buff=0.01)
#         tex_x_1_414 = Tex("1.414").set_color(RED).scale(0.1).next_to(dot_x_1_414, DOWN + RIGHT, buff=0.01)
#         tex_x_1_4142 = Tex("1.4142").set_color(RED).scale(0.075).next_to(dot_x_1_4142, DOWN + RIGHT, buff=0.01)
#         tex_y_1 = Tex("f(1)").set_color(GREEN).scale(0.6).next_to(dot_y_1, LEFT + DOWN, buff=0.01)
#         tex_y_1_4 = Tex("f(1.4)").set_color(GREEN).scale(0.3).next_to(dot_y_1_4, LEFT + UP, buff=0.01)
#         tex_y_1_41 = Tex("f(1.41)").set_color(GREEN).scale(0.25).next_to(dot_y_1_41, LEFT + UP, buff=0.01)
#         tex_y_1_414 = Tex("f(1.414)").set_color(GREEN).scale(0.1).next_to(dot_y_1_414, LEFT + UP, buff=0.01)
#         tex_y_1_4142 = Tex("f(1.4142)").set_color(GREEN).scale(0.075).next_to(dot_y_1_4142, LEFT + UP, buff=0.01)

#         self.play(
#             Write(tex_f),
#             Write(underline_tex_f),
#             Write(text_continuous),
#             run_time=1.5
#         )
#         self.play(
#             Write(axes, lag_ratio=0.1),
#             run_time=1.5,
#             rate_func=smooth,
#         )
#         self.play(
#             Write(func_graph),
#             Write(func_label),
#             run_time=1.5,
#         )
#         self.wait(2)
#         self.play(
#             axes.animate.set_opacity(0.3),
#             Write(dot_x_1),
#             Write(tex_x_1),
#         )
#         self.wait(1)
#         self.play(Write(dash_v_1), run_time=0.75)
#         self.play(Write(dash_h_1), run_time=0.75)
#         self.play(
#             Write(dot_y_1),
#             Write(tex_y_1),
#         )
#         self.wait(2)
#         self.play(
#             self.camera.frame.animate.scale(0.5).shift(RIGHT * 1 + UP * 1),
#             rate_func=smooth,
#         )
#         self.play(
#             ReplacementTransform(dot_x_1, dot_x_1_4),
#             TransformMatchingTex(tex_x_1, tex_x_1_4, key_map={"1": "1.4"}),
#         )
#         self.wait(1)
#         self.play(
#             Write(dash_v_1_4),
#             FadeOut(VGroup(
#                 dash_v_1, dash_h_1,
#             ), lag_ratio=0.1),
#             run_time=0.75)
#         self.play(Write(dash_h_1_4), run_time=0.75)
#         self.play(
#             ReplacementTransform(dot_y_1, dot_y_1_4),
#             TransformMatchingTex(tex_y_1, tex_y_1_4, key_map={"f(1)": "f(1.4)", "1": "1.4", "(": "(", ")": ")"}),
#         )
#         self.wait(2)
#         self.play(
#             self.camera.frame.animate.scale(0.1).move_to(axes.c2p(1.4, 0)),
#             dot_x_1_4.animate.scale(0.4),
#             dot_y_1_4.animate.scale(0.4),
#             rate_func=smooth,
#         )
#         self.play(
#             ReplacementTransform(dot_x_1_4, dot_x_1_41),
#         )
#         self.play(TransformMatchingTex(tex_x_1_4, tex_x_1_41, key_map={"1.4": "1.4"}))
#         self.wait(1)
#         self.play(
#             self.camera.frame.animate.scale(6).move_to(RIGHT * 1 + UP * 1),
#             FadeOut(VGroup(dash_h_1_4, dash_v_1_4), lag_ratio=0.1),
#             rate_func=smooth,
#         )
#         self.play(Write(dash_v_1_41), run_time=0.75)
#         self.play(Write(dash_h_1_41), run_time=0.75)
#         self.play(
#             ReplacementTransform(dot_y_1_4, dot_y_1_41),
#             TransformMatchingTex(tex_y_1_4, tex_y_1_41, key_map={"1.4": "1.4", "f": "f", "(": "(", ")": ")"}),
#         )
#         self.wait(1)
#         self.play(WiggleOutThenIn(text_continuous))
#         self.wait(2)


# class CAPart2_4_2(Scene):
#     manim_config.tex.template = "ctex"

#     def construct(self):
#         colormap_xy_f = {
#             "x": RED,
#             "y": GREEN,
#             "k": YELLOW_B,
#             "f": BLUE,
#             "n": PINK,
#             "(": WHITE,
#             ")": WHITE,
#             "+": WHITE,
#             "-": WHITE,
#             "\\left(": WHITE,
#             "\\right)": WHITE
#         }
#         tex_cauchy = Tex("f(x)+f(y)=f(x+y)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 6 + UP * 3.2).scale(0.9)
#         tex_f = Tex("f(x)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 6 + UP * 2.3).scale(1.05).fix_in_frame()
#         tex_cauchy.align_to(tex_f, LEFT).fix_in_frame()
#         underline_tex_f = Underline(tex_f, color=BLUE).fix_in_frame()
#         text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT).fix_in_frame()
#         axes = Axes(
#             x_range=(-8, 8),
#             y_range=(-4, 4),
#             height=8,
#             width=16,
#             axis_config={
#                 "stroke_color": GREY_A,
#                 "stroke_width": 2,
#             },
#         )
#         axes.add_coordinate_labels(
#             font_size=20,
#             num_decimal_places=1,
#         )

#         # 定义函数曲线
#         func = lambda x: (math.sin(1.5 * x) + x / 2) * math.exp(0.1 * x)
#         func_graph = axes.get_graph(
#             func,
#             color=BLUE,
#         )
#         func_label = axes.get_graph_label(func_graph, label='f(x)', x=3.5, color=BLUE)

#         start_x_1 = 0.5

#         x_dot = Dot(axes.c2p(start_x_1, 0), radius=0.06).set_color(RED)
#         x_label = DecimalNumber(start_x_1, num_decimal_places=3, color=RED).scale(0.6)
#         x_label.add_updater(lambda m: m.next_to(x_dot, DOWN, buff=0.6))
#         x_label.add_updater(lambda m: m.set_value(axes.p2c(x_dot.get_center())[0]))

#         y_dot = Dot(axes.c2p(0, func(start_x_1)), radius=0.06).set_color(BLUE)
#         y_label = DecimalNumber(func(start_x_1), num_decimal_places=3, color=BLUE).scale(0.6)
#         y_label.add_updater(lambda m: m.next_to(y_dot, LEFT, buff=0.8))

#         # static show special points
#         dash_holdplace = DashedLine(LEFT * 20, LEFT * 20)
#         dash_spec_1 = DashedLine(axes.c2p(1, 0), axes.c2p(1, func(1)), color=GREY_C).set_stroke(width=0.3)
#         dash_spec_2 = DashedLine(axes.c2p(1.4, 0), axes.c2p(1.4, func(1.4)), color=GREY_C).set_stroke(width=0.3)
#         dash_spec_3 = DashedLine(axes.c2p(1.41, 0), axes.c2p(1.41, func(1.41)), color=GREY_C).set_stroke(width=0.3)
#         label_spec_1 = Tex("(1,f(1))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(1, func(1)), UP + LEFT * 0.3, buff=0.1)
#         label_spec_2 = Tex("(1.4,f(1.4))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(1.4, func(1.4)), UP + LEFT * 0.2, buff=0.1)
#         label_spec_3 = Tex("(1.41,f(1.41))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(1.41, func(1.41)), UP, buff=0.25)

#         # 目标点设置
#         target_x = 1.414
#         target_y = func(target_x)
        
#         # 目标点在坐标轴上
#         target_x_dot = Dot(axes.c2p(target_x, 0), radius=0.05).set_color(RED)
#         target_y_dot = Dot(axes.c2p(0, target_y), radius=0.05).set_color(BLUE)
        
#         # 目标点标签
#         target_x_label = Tex("\\sqrt{2}").set_color(RED_A).scale(0.5)
#         target_x_label.next_to(target_x_dot, DOWN, buff=0.1)
#         target_y_label = Tex("f(\\sqrt{2})").set_color(BLUE_A).scale(0.5)
#         target_y_label.next_to(target_y_dot, LEFT, buff=0.1)

#         # 动态箭头 - 从当前点指向目标点
#         def create_arrows():
#             current_x = axes.p2c(x_dot.get_center())[0]
#             current_y = func(current_x)
            
#             # x轴上的箭头
#             arrow_x = Arrow(
#             axes.c2p(current_x, 0),
#             axes.c2p(target_x, 0),
#             buff=0.05,
#             color=YELLOW,
#             fill_color=YELLOW,
#             stroke_width=3
#             )
            
#             # y轴上的箭头
#             arrow_y = Arrow(
#             axes.c2p(0, current_y),
#             axes.c2p(0, target_y),
#             buff=0.05,
#             color=YELLOW,
#             fill_color=YELLOW,
#             stroke_width=3
#             )

#             # if distance is too small, set opacity to 0
#             if np.abs(current_x - target_x) < 0.1:
#                 arrow_x.set_opacity(0)
#             if np.abs(current_y - target_y) < 0.1:
#                 arrow_y.set_opacity(0)
            
#             return VGroup(arrow_x, arrow_y)

#         arrows = always_redraw(create_arrows)

#         y_val = func(2)
#         start = axes.c2p(2, 0)
#         end = axes.c2p(2, y_val)

#         if not np.isfinite(y_val):
#             y_val = 0

#         # 创建连接虚线 (使用 always_redraw 动态更新)
#         def create_dashed_lines():
#             x = axes.p2c(x_dot.get_center())[0]
#             y = func(x)
#             v_line = DashedLine(axes.c2p(x, 0), axes.c2p(x, y), color=GREY_C).set_stroke(width=1.5)
#             h_line = DashedLine(axes.c2p(x, y), axes.c2p(0, y), color=GREY_C).set_stroke(width=1.5)
        
#             return VGroup(v_line, h_line)

#         dashed_lines = always_redraw(create_dashed_lines)

#         # 为y_dot和y_label添加Updater
#         def update_y_dot(dot):
#             x = axes.p2c(x_dot.get_center())[0]
#             y = func(x)
#             dot.move_to(axes.c2p(0, y))

#         def update_y_label(label):
#             x = axes.p2c(x_dot.get_center())[0]
#             y = func(x)
#             label.set_value(y)

#         y_dot.add_updater(update_y_dot)
#         y_label.add_updater(update_y_label)

#         # 动画序列
#         self.play(
#             Write(tex_cauchy),
#             Write(tex_f),
#             Write(underline_tex_f),
#             Write(text_continuous),
#             run_time=1.5
#         )
#         self.play(
#             Write(axes, lag_ratio=0.1),
#             run_time=1.5,
#             rate_func=smooth,
#         )
#         self.play(
#             Write(func_graph),
#             Write(func_label),
#             run_time=1.5,
#         )
#         self.play(
#             self.camera.frame.animate.scale(0.7).shift(RIGHT * 1 + UP * 1),
#         )
#         self.play(
#             FadeIn(x_dot),
#             FadeIn(x_label),
#             FadeIn(y_dot),
#             FadeIn(y_label),
#             FadeIn(target_x_dot),
#             FadeIn(target_y_dot),
#             FadeIn(target_x_label),
#             FadeIn(target_y_label),
#             FadeIn(dashed_lines),
#             FadeIn(arrows),
#             axes.animate.set_opacity(0.3),
#             run_time=1.5
#         )
#         self.play(
#             Write(VGroup(
#                 dash_holdplace,
#                 dash_spec_1, label_spec_1,
#                 dash_spec_2, label_spec_2,
#                 dash_spec_3, label_spec_3
#             ), lag_ratio=0.2),
#             x_dot.animate.move_to(axes.c2p(1.414, 0)),
#             run_time=4,
#             rate_func=smooth,
#         )
#         self.wait(0.5)
#         self.play(
#             FadeOut(VGroup(
#                 dash_holdplace,
#                 dash_spec_1, label_spec_1,
#                 dash_spec_2, label_spec_2,
#                 dash_spec_3, label_spec_3
#             )),
#         )
#         self.wait(2)
#         self.play(
#             FadeOut(VGroup(
#                 x_dot, y_dot, x_label, y_label,
#                 target_x_dot, target_y_dot, target_x_label, target_y_label,
#                 dashed_lines, arrows
#             ), lag_ratio=0.1),
#         )
#         self.wait(1)

#         # 定义新的变量和函数 - 从0到π的极限过程

#         x_dot_new = Dot(axes.c2p(0, 0), radius=0.06).set_color(RED)
#         x_label_new = DecimalNumber(0, num_decimal_places=3, color=RED).scale(0.6)
#         x_label_new.add_updater(lambda m: m.next_to(x_dot_new, DOWN, buff=0.6))
#         x_label_new.add_updater(lambda m: m.set_value(axes.p2c(x_dot_new.get_center())[0]))

#         y_dot_new = Dot(axes.c2p(0, func(0)), radius=0.06).set_color(BLUE)
#         y_label_new = DecimalNumber(func(0), num_decimal_places=3, color=BLUE).scale(0.6)
#         y_label_new.add_updater(lambda m: m.next_to(y_dot_new, LEFT, buff=0.8))

#         # static show special points
#         dash_holdplace_new = DashedLine(LEFT * 20, LEFT * 20)
#         dash_spec_1_new = DashedLine(axes.c2p(1, 0), axes.c2p(1, func(1)), color=GREY_C).set_stroke(width=0.3)
#         dash_spec_2_new = DashedLine(axes.c2p(2, 0), axes.c2p(2, func(2)), color=GREY_C).set_stroke(width=0.3)
#         dash_spec_3_new = DashedLine(axes.c2p(3, 0), axes.c2p(3, func(3)), color=GREY_C).set_stroke(width=0.3)
#         dash_spec_4_new = DashedLine(axes.c2p(3.1, 0), axes.c2p(3.1, func(3.1)), color=GREY_C).set_stroke(width=0.3)
#         label_spec_1_new = Tex("(1,f(1))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(1, func(1)), UP + LEFT * 0.3, buff=0.1)
#         label_spec_2_new = Tex("(2,f(2))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(2, func(2)), UP + LEFT * 0.2, buff=0.1)
#         label_spec_3_new = Tex("(3,f(3))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(3, func(3)), UP + LEFT * 0.1, buff=0.1)
#         label_spec_4_new = Tex("(3.1,f(3.1))").set_color(GREY_C).scale(0.2).next_to(axes.c2p(3.1, func(3.1)), UP, buff=0.2)

#         # 目标点设置为π
#         target_x_pi = np.pi
#         target_y_pi = func(target_x_pi)

#         # 目标点在坐标轴上
#         target_x_dot_pi = Dot(axes.c2p(target_x_pi, 0), radius=0.05).set_color(RED)
#         target_y_dot_pi = Dot(axes.c2p(0, target_y_pi), radius=0.05).set_color(BLUE)

#         # 目标点标签
#         target_x_label_pi = Tex("\\pi").set_color(RED_A).scale(0.5)
#         target_x_label_pi.next_to(target_x_dot_pi, DOWN, buff=0.1)
#         target_y_label_pi = Tex("f(\\pi)").set_color(BLUE_A).scale(0.5)
#         target_y_label_pi.next_to(target_y_dot_pi, LEFT, buff=0.1)

#         # 动态箭头 - 从当前点指向π
#         def create_arrows_pi():
#             current_x_pi = axes.p2c(x_dot_new.get_center())[0]
#             current_y_pi = func(current_x_pi)
            
#             # x轴上的箭头
#             arrow_x_pi = Arrow(
#                 axes.c2p(current_x_pi, 0),
#                 axes.c2p(target_x_pi, 0),
#                 buff=0.05,
#                 color=YELLOW,
#                 fill_color=YELLOW,
#                 stroke_width=3
#             )
            
#             # y轴上的箭头
#             arrow_y_pi = Arrow(
#                 axes.c2p(0, current_y_pi),
#                 axes.c2p(0, target_y_pi),
#                 buff=0.05,
#                 color=YELLOW,
#                 fill_color=YELLOW,
#                 stroke_width=3
#             )

#             # 如果距离太小，设置透明度为0
#             if np.abs(current_x_pi - target_x_pi) < 0.1:
#                 arrow_x_pi.set_opacity(0)
#             if np.abs(current_y_pi - target_y_pi) < 0.1:
#                 arrow_y_pi.set_opacity(0)
            
#             return VGroup(arrow_x_pi, arrow_y_pi)

#         arrows_pi = always_redraw(create_arrows_pi)

#         # 创建连接虚线 (使用 always_redraw 动态更新)
#         def create_dashed_lines_pi():
#             x_pi = axes.p2c(x_dot_new.get_center())[0]
#             y_pi = func(x_pi)
#             v_line_pi = DashedLine(axes.c2p(x_pi, 0), axes.c2p(x_pi, y_pi), color=GREY_C).set_stroke(width=1.5)
#             h_line_pi = DashedLine(axes.c2p(x_pi, y_pi), axes.c2p(0, y_pi), color=GREY_C).set_stroke(width=1.5)

#             return VGroup(v_line_pi, h_line_pi)

#         dashed_lines_pi = always_redraw(create_dashed_lines_pi)

#         # 为y_dot_new和y_label_new添加Updater
#         def update_y_dot_pi(dot):
#             x_pi = axes.p2c(x_dot_new.get_center())[0]
#             y_pi = func(x_pi)
#             dot.move_to(axes.c2p(0, y_pi))

#         def update_y_label_pi(label):
#             x_pi = axes.p2c(x_dot_new.get_center())[0]
#             y_pi = func(x_pi)
#             label.set_value(y_pi)

#         y_dot_new.add_updater(update_y_dot_pi)
#         y_label_new.add_updater(update_y_label_pi)

#         # 动画序列 - 从0到π
#         self.play(
#             FadeIn(x_dot_new),
#             FadeIn(x_label_new),
#             FadeIn(y_dot_new),
#             FadeIn(y_label_new),
#             FadeIn(target_x_dot_pi),
#             FadeIn(target_y_dot_pi),
#             FadeIn(target_x_label_pi),
#             FadeIn(target_y_label_pi),
#             FadeIn(dashed_lines_pi),
#             FadeIn(arrows_pi),
#             axes.animate.set_opacity(0.3),
#             run_time=1.5
#         )
#         self.play(
#             Write(VGroup(
#                 dash_holdplace_new,
#                 dash_spec_1_new, label_spec_1_new,
#                 dash_spec_2_new, label_spec_2_new,
#                 dash_spec_3_new, label_spec_3_new,
#                 dash_spec_4_new, label_spec_4_new
#             ), lag_ratio=0.2),
#             x_dot_new.animate.move_to(axes.c2p(np.pi, 0)),
#             run_time=5,
#             rate_func=smooth,
#         )
#         self.wait(0.5)
#         self.play(
#             FadeOut(VGroup(
#                 dash_holdplace_new,
#                 dash_spec_1_new, label_spec_1_new,
#                 dash_spec_2_new, label_spec_2_new,
#                 dash_spec_3_new, label_spec_3_new,
#                 dash_spec_4_new, label_spec_4_new
#             )),
#         )
#         self.wait(2)
#         self.play(
#             FadeOut(VGroup(
#                 x_dot_new, y_dot_new, x_label_new, y_label_new,
#                 target_x_dot_pi, target_y_dot_pi, target_x_label_pi, target_y_label_pi,
#                 dashed_lines_pi, arrows_pi
#             ), lag_ratio=0.1),
#         )
#         self.play(
#             FadeOut(VGroup(
#                 axes, func_graph, func_label,
#                 tex_cauchy, tex_f, underline_tex_f, text_continuous,
#             ), lag_ratio=0.1),
#         )


class CAPart2_4_3(Scene):
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
        tex_cauchy = Tex("f(x)+f(y)=f(x+y)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 6 + UP * 3.2).scale(0.9)
        tex_f = Tex("f(x)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(LEFT * 6 + UP * 2.3).scale(1.05).fix_in_frame()
        tex_cauchy.align_to(tex_f, LEFT).fix_in_frame()
        underline_tex_f = Underline(tex_f, color=BLUE).fix_in_frame()
        text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT).fix_in_frame()
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
        self.play(
            Write(tex_cauchy),
            Write(tex_f),
            Write(underline_tex_f),
            Write(text_continuous),
            run_time=1.5
        )
        self.play(
            Write(axes, lag_ratio=0.1),
            run_time=1.5,
            rate_func=smooth,
        )

        # Dots contruction
        func = lambda x: (math.sin(1.5 * x) + x / 2) * math.exp(0.1 * x)
        func_interpolate: Callable[[Callable[[float], float], Callable[[float], float], float, float], float] = lambda f1, f2, x, t: f1(x) * (1 - t) + f2(x) * t
        func_no_smooth = lambda x: (math.sin(1.5 * x) + x / 2) * math.exp(0.1 * x) + ((x + 1) - 2 * int((x + 1) / 2))
        color_func = lambda x, min_val, max_val: interpolate_color(BLUE_B, GREEN_B, (x - min_val) / (max_val - min_val))
        dots = VGroup(*[
            Dot(axes.c2p(x, func(x)), radius=0.025).set_color(color_func(x, -8, 5))
            for x in np.linspace(-8, 5, 10000)
        ])
        dots_sq2_patch = VGroup(*[
            Dot(axes.c2p(x, func(x)), radius=0.004).set_color(color_func(x, -8, 5))
            for x in np.linspace(-np.sqrt(2) - 0.8, np.sqrt(2) + 0.8, 10000)
        ])
        func_label = Tex("f(x)").set_color(BLUE_A).scale(0.9).move_to(RIGHT * 6 + UP * 2)

        # Draw dots
        self.play(
            FadeIn(dots, lag_ratio=0.01),
            run_time=2,
            rate_func=smooth,
        )
        self.play(Write(func_label))
        self.wait(1)

        # def start point and end point
        start_x_1 = 0.5
        end_x_1 = np.sqrt(2)
        start_x_2 = np.sqrt(2)
        end_x_2 = 2.9999

        dash_end_x_1 = DashedLine(axes.c2p(0, func(start_x_1)), axes.c2p(start_x_1, func(start_x_1)), color=GREY_C).set_stroke(width=0.3)
        dash_end_y_1 = DashedLine(axes.c2p(end_x_1, 0), axes.c2p(end_x_1, func(end_x_1)), color=GREY_C).set_stroke(width=0.3)

        # position for the moving dot
        def pos_func_log_smooth(
            t, min_val, max_val,
            from_val = None, to_val = None,
            smooth_recursion: int = 5
        ) -> float | Tuple[float, Any]:
            alpha = (t - min_val) / (max_val - min_val)
            # log to scale
            log_val = np.log10(1 + alpha * 9)
            
            # smooth the log value
            if smooth_recursion >= 1:
                smooth_val = double_smooth(log_val)
                # for _ in range(smooth_recursion - 1):
                #     smooth_val = smooth(smooth_val)
                smooth_val = np.clip(smooth_val, 0, 1)  # Ensure smooth_val is between 0 and 1
            else:
                smooth_val = smooth(log_val)
                smooth_val = np.clip(log_val, 0, 1)

            if from_val is None or to_val is None:
                return smooth_val
            return smooth_val, smooth_val * (to_val - from_val) + from_val
        
        point_dot = Dot(axes.c2p(start_x_1, func(start_x_1)), radius=0.06).set_color(YELLOW)
        point_label = VGroup(
            Tex("(").scale(0.8),
            DecimalNumber(start_x_1, num_decimal_places=4, color=BLUE).scale(0.6),
            Tex(",").scale(0.8),
            DecimalNumber(func(start_x_1), num_decimal_places=4, color=RED).scale(0.6),
            Tex(")").scale(0.8)
        ).arrange_in_grid(n_rows=1, buff=0).move_to(point_dot.get_corner(RIGHT + DOWN), aligned_edge=LEFT + UP)
        for i, elem in enumerate(point_label):
            if i >= 1:
                elem.move_to(point_label[i - 1].get_right(), aligned_edge=LEFT)
        point_label[2].shift(DOWN * 0.1 + RIGHT * 0.05)
        point_label[3].shift(RIGHT * 0.15)
        point_label[4].shift(RIGHT * 0.15)

        final_dot = Dot(axes.c2p(end_x_1, func(end_x_1)), radius=0.003).set_color(YELLOW_A)
        x_dot = Dot(axes.c2p(start_x_1, 0), radius=0.06).set_color(RED).move_to(RIGHT * point_dot.get_x())
        x_label = DecimalNumber(start_x_1, num_decimal_places=3, color=RED).scale(0.6).next_to(x_dot, DOWN, buff=0.6)
        y_dot = Dot(axes.c2p(0, func(start_x_1)), radius=0.06).set_color(BLUE).move_to(UP * point_dot.get_y())
        y_label = DecimalNumber(func(start_x_1), num_decimal_places=3, color=BLUE).scale(0.6).next_to(y_dot, LEFT, buff=0.8)

        # Write dots
        self.play(
            FadeIn(x_dot),
            FadeIn(x_label),
            FadeIn(y_dot),
            FadeIn(y_label),
            run_time=1.5
        )
        self.play(
            self.camera.frame.animate.move_to(point_dot.get_center()),
        )
        self.play(
            Write(point_dot),
            Write(point_label),
            Write(dash_end_x_1),
            Write(dash_end_y_1),
        )
        self.wait(1)

        # add a arrow
        arrow_start_to_end = Arrow(start=point_dot.get_center(), end=dash_end_y_1.get_end(), buff=0.01).set_color(LIGHT_BROWN).set_stroke(width=0.5)
        self.play(Write(arrow_start_to_end))

        full_play_time = 7
        time_start = self.time

        # Create dashed lines to indicate position
        def create_position_lines():
            x = axes.p2c(point_dot.get_center())[0]
            y = func(x)
            vertical_line = DashedLine(
                axes.c2p(x, 0), 
                axes.c2p(x, y), 
                color=BLUE
            ).set_stroke(width=1)
            horizontal_line = DashedLine(
                axes.c2p(0, y), 
                axes.c2p(x, y), 
                color=RED
            ).set_stroke(width=1)
            return VGroup(vertical_line, horizontal_line)

        position_lines = always_redraw(create_position_lines)
        self.add(position_lines)

        point_dot.add_updater(lambda m: m.move_to(axes.c2p(
            pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time,
                from_val=start_x_1, to_val=end_x_1
            )[1],
            func(pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time,
                from_val=start_x_1, to_val=end_x_1
            )[1]    
        ))))
        point_dot.add_updater(lambda m: m.scale(pos_func_log_smooth(
            self.time, time_start, time_start + full_play_time,
            from_val=1, to_val=0.995
        )[1]))

        self.camera.frame.add_updater(lambda m: 
            m.move_to(point_dot.get_center()).scale(s := pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time,
                from_val=1, to_val=0.992
            )[1]))

        arrow_start_to_end.add_updater(lambda m: m.put_start_and_end_on(point_dot.get_center(), np.array([1.4142, 1.7962, 0])))
        arrow_start_to_end.add_updater(lambda m: m.set_stroke(width=0.5 * pos_func_log_smooth(
            self.time, time_start, time_start + full_play_time,
            from_val=1, to_val=0.1
        )[1]))
        point_label[1].add_updater(lambda m: m.set_value(axes.p2c(point_dot.get_center())[0]))
        point_label[3].add_updater(lambda m: m.set_value(func(axes.p2c(point_dot.get_center())[0])))
        x_dot.add_updater(lambda m: m.move_to(RIGHT * point_dot.get_x()))
        y_dot.add_updater(lambda m: m.move_to(UP * point_dot.get_y()))
        x_label.add_updater(lambda m: m.next_to(x_dot, DOWN, buff=0.6))
        x_label.add_updater(lambda m: m.set_value(axes.p2c(x_dot.get_center())[0]))
        y_label.add_updater(lambda m: m.next_to(y_dot, LEFT, buff=0.8))
        y_label.add_updater(lambda m: m.set_value(func(axes.p2c(x_dot.get_center())[0])))
        point_label.add_updater(lambda m: m.move_to(point_dot.get_corner(RIGHT + DOWN), aligned_edge=LEFT + UP))
        point_label.add_updater(lambda m: m.scale(pos_func_log_smooth(
            self.time, time_start, time_start + full_play_time,
            from_val=1, to_val=0.992
        )[1]))
        for func_point in dots:
            func_point.add_updater(lambda m: m.scale(pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time,
                from_val=1, to_val=0.99
            )[1]))
        
        self.wait(full_play_time / 2 - 0.5)
        # write patch
        self.play(
            Write(dots_sq2_patch),
            Write(final_dot),
            rate_func=smooth,
            run_time=1
        )
        for func_point in dots_sq2_patch:
            func_point.add_updater(lambda m: m.scale(pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time / 2 - 0.5,
                from_val=1, to_val=0.988
            )[1]))
        self.wait(full_play_time / 2 - 0.5)

        # clear all updaters
        point_dot.clear_updaters()
        x_dot.clear_updaters()
        y_dot.clear_updaters()
        x_label.clear_updaters()
        y_label.clear_updaters()
        point_label.clear_updaters()
        for func_point in dots:
            func_point.clear_updaters()
        for func_point in dots_sq2_patch:
            func_point.clear_updaters()
        arrow_start_to_end.clear_updaters()
        position_lines.clear_updaters()
        self.camera.frame.clear_updaters()

        self.wait(2)
        self.remove(position_lines)

        # scale to origin
        
        self.play(
            self.camera.frame.animate.scale(100),
            FadeOut(VGroup(*dots_sq2_patch), lag_ratio=0.1),
            *[dot.animate.scale(100) for dot in dots],
            FadeOut(arrow_start_to_end),
            point_dot.animate.scale(25),
            point_label.animate.scale(80).move_to(point_dot.get_corner(DOWN), aligned_edge=LEFT + UP),
            run_time=2,
        )
        self.play(self.camera.frame.animate.move_to(ORIGIN))

        # transform func points

        point_label.add_updater(lambda m: m.move_to(point_dot.get_corner(RIGHT + DOWN), aligned_edge=LEFT + UP))
        point_label[1].add_updater(lambda m: m.set_value(axes.p2c(point_dot.get_center())[0]))
        point_label[3].add_updater(lambda m: m.set_value(func_no_smooth(axes.p2c(point_dot.get_center())[0])))
        self.play(
            *[
                dot.animate.move_to(axes.c2p(
                    axes.p2c(dot.get_center())[0],
                    func_no_smooth(axes.p2c(dot.get_center())[0])
                ))
                for dot in dots
            ],
            point_dot.animate.move_to(axes.c2p(
                axes.p2c(point_dot.get_center())[0],
                func_no_smooth(axes.p2c(point_dot.get_center())[0])
            )),
            run_time=1.5
        )
        self.play(
            x_dot.animate.move_to(RIGHT * point_dot.get_x()),
            y_dot.animate.move_to(UP * point_dot.get_y()),
            x_label.animate.next_to(x_dot, DOWN, buff=0.6).set_value(axes.p2c(x_dot.get_center())[0]),
            y_label.animate.next_to(y_dot, LEFT, buff=0.8).set_value(func_no_smooth(axes.p2c(x_dot.get_center())[0])),
        )
        self.wait(2)

        # play animate 2

        target_point_2 = Dot(axes.c2p(end_x_2 + 0.01, func_no_smooth(end_x_2 + 0.01)), radius=0.1).set_color(YELLOW)
        arrow_start_to_end_2 = Arrow(
            start=point_dot.get_center(),
            end=axes.c2p(end_x_2 + 0.01, func_no_smooth(end_x_2 + 0.01)),
            buff=0,
        ).set_color(LIGHT_BROWN).set_stroke(width=0.5)
        self.play(Write(target_point_2))
        self.play(Write(arrow_start_to_end_2))
        full_play_time = 4
        time_start = self.time
        point_dot.add_updater(lambda m: m.move_to(axes.c2p(
            pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time,
                from_val=start_x_2, to_val=end_x_2, smooth_recursion=0
            )[1],
            func_no_smooth(pos_func_log_smooth(
                self.time, time_start, time_start + full_play_time,
                from_val=start_x_2, to_val=end_x_2, smooth_recursion=0
            )[1]
        ))))
        point_label.add_updater(lambda m: m.move_to(point_dot.get_corner(DOWN), aligned_edge=LEFT + UP))
        point_label[1].add_updater(lambda m: m.set_value(axes.p2c(point_dot.get_center())[0]))
        point_label[3].add_updater(lambda m: m.set_value(func_no_smooth(axes.p2c(point_dot.get_center())[0])))
        arrow_start_to_end_2.add_updater(lambda m: m.put_start_and_end_on(
            point_dot.get_center(),
            axes.c2p(end_x_2 + 0.01, func_no_smooth(end_x_2 + 0.01))
        ))

        self.wait(full_play_time)
        point_dot.clear_updaters()
        point_label.clear_updaters()
        arrow_start_to_end_2.clear_updaters()
        point_label[1].clear_updaters()
        point_label[3].clear_updaters()
        self.wait(1.5)
        text_limit = Text("极限", font="微软雅黑").set_color(BLUE_A)
        self.play(
            Write(text_limit),
            *[dot.animate.set_opacity(0.2) for dot in dots],
            axes.animate.set_opacity(0.2),
            x_dot.animate.set_opacity(0.2),
            y_dot.animate.set_opacity(0.2),
            func_label.animate.set_opacity(0.2),
            x_label.animate.set_opacity(0.2),
            y_label.animate.set_opacity(0.2),
            point_dot.animate.set_opacity(0.2),
            point_label.animate.set_opacity(0.2),
            arrow_start_to_end_2.animate.set_opacity(0.2),
        )
        self.wait(2)
        self.play(FadeOut(VGroup(
            tex_cauchy, tex_f, underline_tex_f, text_continuous,
            axes, func_label,
            point_dot, point_label, x_dot, y_dot, x_label, y_label,
            target_point_2, arrow_start_to_end_2,
            dash_end_x_1, dash_end_y_1,
            *dots_sq2_patch, *dots,
        )))
        self.wait(1)

class CAPart2_5(Scene):
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
        tex_cauchy = Tex("f(x)+f(y)=f(x+y)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(UP * 2.2).scale(0.9)
        tex_f = Tex("f(x)").set_color_by_tex_to_color_map(colormap_xy_f).move_to(UP * 1.3).scale(1.05)
        underline_tex_f = Underline(tex_f, color=BLUE)
        text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT)
        text_continuous_1 = text_continuous.copy()
        text_dandiao_1 = Text("单调", font="微软雅黑").set_color(GREEN_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT)
        text_youjie_1 = Text("有界", font="微软雅黑").set_color(RED_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT)
        text_dandianlianxu_1 = Text("单点连续", font="微软雅黑").set_color(YELLOW_A).scale(0.55).next_to(underline_tex_f, DOWN, buff=0.1).align_to(underline_tex_f, LEFT)
        # gird align above
        group_texts = VGroup(
            text_continuous_1, text_dandiao_1, text_youjie_1, text_dandianlianxu_1
        ).arrange_in_grid(
            n_rows=1,
            n_cols=4,
            buff=0.8
        )
        right_img = ImageMobject("right.png", height=1).move_to(DOWN * 1.5)

        self.play(
            FadeIn(VGroup(
                tex_cauchy, tex_f, underline_tex_f, text_continuous
            )),
            rate_func=smooth,
            run_time=2
        )
        self.wait(1.5)
        group_texts.next_to(underline_tex_f, DOWN, buff=0.1).shift(DOWN * 1)
        self.play(
            TransformFromCopy(
                text_continuous, group_texts[0],
                path_arc=PI / 2,
            ),
        )
        self.play(
            TransformFromCopy(
                text_continuous, group_texts[1],
                path_arc=PI / 2,
            ),
        )
        self.play(
            TransformFromCopy(
                text_continuous, group_texts[2],
                path_arc=PI / 2,
            ),
        )
        self.play(
            TransformFromCopy(
                text_continuous, group_texts[3],
                path_arc=PI / 2,
            ),
        )
        self.wait(1)
        self.play(FadeIn(right_img))
        self.wait(2)
        self.play(
            FadeOut(Group(
                tex_cauchy, tex_f, underline_tex_f, group_texts, text_continuous,
                right_img,
            )),
            run_time=1.5
        )


class CAPart2_6(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        colormap_xy_f = {
            "x": RED, "y": GREEN, "k": YELLOW_B, "a": RED_A,
            "n": PINK,
            "f": BLUE, "g": BLUE_D,
            "(": WHITE, ")": WHITE,
            "+": WHITE, "-": WHITE,
            "\\mathrm{e}": WHITE,
            "\\left(": WHITE, "\\right)": WHITE, "\\ln": WHITE
        }
        tex_cauchy = Tex("f(x+y)=f(x)+f(y)")
        text_continuous = Text("连续", font="微软雅黑").set_color(BLUE_A).scale(0.55).move_to(DOWN * 0.8)
        tex_muilt_cauchy = Tex("f(x+y)=f(x)f(y)")
        tex_f_ge_0 = Tex("f(x)>0")
        tex_log_muilt_cauchy = Tex("\\ln f(x+y)=\\ln f(x)+\\ln f(y)")
        parts_tex_muilt_cauchy = [
            VGroup(tex_log_muilt_cauchy[0:8]),
            VGroup(tex_log_muilt_cauchy[9:15]),
            VGroup(tex_log_muilt_cauchy[16:22]),
        ]
        arrows_up = [
            Arrow(parts_tex_muilt_cauchy[i].get_top(), parts_tex_muilt_cauchy[i].get_top() + UP * 1, buff=0.1, color=WHITE)
            for i in range(0, len(parts_tex_muilt_cauchy))
        ]
        tex_g_xpy = Tex("g(x+y)").move_to(parts_tex_muilt_cauchy[0].get_top() + UP * 1.2)
        tex_g_x = Tex("g(x)").move_to(parts_tex_muilt_cauchy[1].get_top() + UP * 1.2)
        tex_g_y = Tex("g(y)").move_to(parts_tex_muilt_cauchy[2].get_top() + UP * 1.2)
        tex_cauchy_g = Tex("g(x+y)=g(x)+g(y)")
        tex_g_eq_kx = Tex("g(x)=kx").shift(DOWN * 0.8)
        tex_logf_eq_kx = Tex("\\ln f(x)=kx").shift(DOWN * 0.8)
        tex_f_eq_exp_kx = Tex("f(x)=e^{kx}").shift(DOWN * 0.8)
        rec_ek = SurroundingRectangle(VGroup(tex_f_eq_exp_kx[5:7]), buff=0.05).set_stroke(width=0.1)
        tex_a_eq_a_power_x = Tex("a=e^k").shift(DOWN * 1.6)
        tex_f_eq_a_power_x = Tex("f(x)=a^x").shift(DOWN * 0.8)
        tex_apower_xpy = Tex("f(x+y)=a^{x+y}").shift(UP * 0.8)
        tex_apowerx_times_apowery = Tex("f(x)f(y)=a^x\\times a^y").shift(UP * 0.8)
        background_rec = Rectangle(width=20, height=20, color="#333333", fill_opacity=1).set_opacity(1)
        tex_f_xy_eq_fxfy = Tex("f(xy)=f(x)f(y)").shift(LEFT * 3)
        tex_f_xtimesy_fxpfy = Tex("f(xy)=f(x)+f(y)").shift(RIGHT * 3)
        tex_x_y_ge_0 = Tex("x,y>0")
        for tex in [
            tex_cauchy, tex_muilt_cauchy,
            tex_f_ge_0, tex_log_muilt_cauchy, tex_g_xpy,
            tex_g_x, tex_g_y, tex_cauchy_g, tex_g_eq_kx,
            tex_logf_eq_kx, tex_f_eq_exp_kx, tex_a_eq_a_power_x,
            tex_f_eq_a_power_x, tex_apower_xpy, tex_apowerx_times_apowery,
            tex_f_xy_eq_fxfy, tex_f_xtimesy_fxpfy, tex_x_y_ge_0
        ]:
            tex.set_color_by_tex_to_color_map(colormap_xy_f).scale(0.8)
        tex_f_ge_0.set_color(GREY_C).scale(0.6).next_to(tex_muilt_cauchy, RIGHT, buff=0.5)

        self.play(FadeIn(tex_cauchy))
        self.wait(3)
        self.play(
            TransformFromCopy(tex_cauchy, text_continuous),
        )
        self.play(WiggleOutThenIn(text_continuous))
        self.wait(1)
        self.play(
            FadeOut(text_continuous),
            TransformMatchingTex(
                tex_cauchy, tex_muilt_cauchy,
                key_map={"f(x)": "f(x)", "f(y)": "f(y)", "f(x+y)": "f(x+y)", "=": "="},
                path_arc = 90 * DEGREES
            ),
            run_time=2
        )
        self.play(Write(tex_f_ge_0))
        self.wait(1.5)
        self.play(
            tex_f_ge_0.animate.next_to(tex_log_muilt_cauchy, RIGHT, buff=0.5),
            TransformMatchingTex(
                tex_muilt_cauchy, tex_log_muilt_cauchy,
                key_map={"f(x)": "f(x)", "f(y)": "f(y)", "f(x+y)": "f(x+y)", "=": "="},
                path_arc = 90 * DEGREES
            ),
            run_time=2
        )
        self.wait(1.5)
        self.play(
            Write(VGroup(*arrows_up), lag_ratio=0.2),
        )
        self.play(
            TransformFromCopy(parts_tex_muilt_cauchy[0], tex_g_xpy),
            TransformFromCopy(parts_tex_muilt_cauchy[1], tex_g_x),
            TransformFromCopy(parts_tex_muilt_cauchy[2], tex_g_y),
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(*arrows_up), lag_ratio=0.1),
            FadeOut(tex_log_muilt_cauchy, lag_ratio=0.1),
            FadeOut(tex_f_ge_0, lag_ratio=0.1),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(
                VGroup(tex_g_xpy, tex_g_x, tex_g_y),
                tex_cauchy_g,
                lag_ratio=0.1,
            ),
            run_time=1.5
        )
        self.play(
            tex_cauchy_g.animate.scale(11 / 10),
            ShowCreationThenDestructionAround(tex_cauchy_g, buff=0.3)
        )
        self.wait(1)
        tex_typing_animate(self, tex_g_eq_kx, typing_interval=0.1)
        self.wait(2)
        self.play(
            TransformMatchingTex(
                tex_g_eq_kx, tex_logf_eq_kx,
                key_map={"g(x)": "f(x)", "=kx": "=kx"},
                path_arc=90 * DEGREES
            ),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            TransformMatchingTex(
                tex_logf_eq_kx, tex_f_eq_exp_kx,
                key_map={"f(x)": "f(x)", "=": "=", "\\ln": "e", "kx": "^{kx}"},
                path_arc=90 * DEGREES
            ),
            run_time=1.5
        )
        self.wait(2)
        self.play(Write(rec_ek))
        self.wait(1)
        tex_f_eq_exp_kx_cpy = tex_f_eq_exp_kx.copy()
        self.add(tex_f_eq_exp_kx_cpy)
        self.play(
            FadeOut(rec_ek),
            TransformMatchingTex(tex_f_eq_exp_kx_cpy, tex_a_eq_a_power_x,
                key_map={"e^{k}": "e^k"},
                path_arc=90 * DEGREES
            ),
        )
        self.wait(1)
        self.play(
            TransformMatchingTex(
                tex_f_eq_exp_kx, tex_f_eq_a_power_x,
                key_map={"f(x)": "f(x)", "e^{kx}": "a^x", "=": "="},
                path_arc=90 * DEGREES
            )
        )
        self.wait(2)
        self.play(
            Write(tex_apower_xpy)
        )
        self.wait(1)
        self.play(
            tex_apower_xpy.animate.shift(LEFT * 1.6),
        )
        tex_apower_xpy_cpy = tex_apower_xpy.copy()
        tex_apowerx_times_apowery.next_to(tex_apower_xpy, RIGHT, buff=0.4)
        self.add(tex_apower_xpy_cpy)
        self.play(
            TransformMatchingTex(
                tex_apower_xpy, tex_apowerx_times_apowery,
                key_map={"a": "a","x": "x", "y": "y", "=": "="},
                path_arc=90 * DEGREES
            ),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeIn(background_rec))
        self.play(Write(
            VGroup(tex_f_xy_eq_fxfy, tex_f_xtimesy_fxpfy),
            lag_ratio=0.2
        ))
        self.wait(0.5)
        self.play(
            ShowCreationThenDestructionAround(tex_f_xy_eq_fxfy, buff=0.3, stroke_color=BLUE_B),
            ShowCreationThenDestructionAround(tex_f_xtimesy_fxpfy, buff=0.3, stroke_color=BLUE_B),
            run_time=1.5
        )
        self.wait(2)
        self.play(
            FadeOut(VGroup(
                tex_f_xy_eq_fxfy,
                tex_f_xtimesy_fxpfy
            ))
        )
        self.wait(1)
        