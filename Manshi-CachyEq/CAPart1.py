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
        # get the index of Tex
        # uv run manimgl CAPart1.py Test -s

        # tex = Tex("\\text{Solution: }f(x)=\\begin{cases}f(x)=kx\\\\?\\end{cases}")
        # self.add(tex)
        # debugTeX(self, tex)

        # tex = Tex("f(x)+f(y)=f(x+y)")
        # self.wait(1)
        # tex_typing_animate(self, tex)

        # tex = Tex("\\text{Solution: }f(x)=\\begin{cases}f(x)=kx\\\\?\\end{cases}")
        tex = Square(color=RED, side_length=2)
        self.wait(1)
        self.play(
            FadeIn(tex),
            Homotopy(homotopic_showin, tex, run_time=3),
            run_time=3,
            rate_func=smooth,
        )
        self.wait(1)

        
class CAPart1_1(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_xy = {"x": RED, "y": GREEN, "k": YELLOW_B}
        tex_fx = Tex("f(x)").set_color_by_tex_to_color_map(colormap_xy)
        tex_equation = Tex("f(x+y)", "=", "f(x)", "+", "f(y)").set_color_by_tex_to_color_map(colormap_xy)
        
        self.wait(1)
        self.camera.frame.scale(0.8)
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 2, 0.7, 0.045, "in")))
        tex_typing_animate(self, tex_fx, typing_interval=0.3)
        self.wait(1)
        self.camera.frame.clear_updaters()

        # Get the position of 3 parts of equation, then transform them
        tex_part3s_eq = [
            VGroup(*[t for t in tex_equation[0:6]]), 
            VGroup(*[t for t in tex_equation[7:11]]), 
            VGroup(*[t for t in tex_equation[12:]])
        ]
        fx_cps = [tex_fx.copy() for _ in range(3)]
        self.add(*fx_cps)
        self.remove(tex_fx)
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_smooth(now, self.time, 4.5, 0.008, "out")))
        self.play(
            *[fx.animate.move_to(tex_part3s_eq[i].get_center()) for i, fx in enumerate(fx_cps)],
            run_time=1.5,
            rate_func=smooth,
            lag_ratio=0.3
        )
        self.play(
            *[TransformMatchingShapes(fx, part) for fx, part in zip(fx_cps, tex_part3s_eq)],
            *[Write(tex_equation[i]) for i in [6, 11]],
            rate_func=smooth,
            run_time=1.5,
            lag_ratio=0.3
        )
        self.wait(2)
        self.camera.frame.clear_updaters()

        # Show the guessed solution
        fx_cpy2 = tex_part3s_eq[1].copy().shift(DOWN * 1.2)
        right_arrow = Arrow(fx_cpy2.get_right(), fx_cpy2.get_right() + RIGHT * 1)
        tex_guess_solution = Tex("x").next_to(right_arrow, RIGHT, buff=0.25).set_color_by_tex_to_color_map(colormap_xy)

        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.shift((DOWN + RIGHT) * animate_shift_smooth(now, self.time, 2.5, 0.01, "pos")))
        self.play(
            TransformFromCopy(tex_part3s_eq[1], fx_cpy2),
            run_time=1,
            rate_func=smooth,
        )
        self.play(
            Write(right_arrow),
            Write(tex_guess_solution),
            run_time=1.5,
            rate_func=smooth,
            lag_ratio=0.3
        )
        self.wait(1.5)
        self.camera.frame.clear_updaters()

        # Highlight 1 part of left and 2 parts of right
        # rec_left = SurroundingRectangle(tex_part3s_eq[0], buff=0.03).set_color_by_gradient(RED_C, GREEN_C)
        # rec_right_x = SurroundingRectangle(tex_part3s_eq[1], color=RED, buff=0.03)
        # rec_right_y = SurroundingRectangle(tex_part3s_eq[2], color=GREEN, buff=0.03)
        adapt_arrow_ups = [Tex("\\uparrow").scale(0.8).copy().move_to(tex_part3s_eq[i].get_center() + 0.5 * UP) for i in range(3)]
        adapt_recs = [SurroundingRectangle(tex_part3s_eq[i], color=WHITE, buff=0.03).copy().move_to(tex_part3s_eq[i].get_center() + 1 * UP) for i in range(3)]
        adapt_recs[0].set_color_by_gradient(RED_C, GREEN_C)
        adapt_recs[1].set_color(RED)
        adapt_recs[2].set_color(GREEN)
        tex_x_plus_y = Tex("x+y").set_color_by_tex_to_color_map(colormap_xy).move_to(tex_part3s_eq[0].get_center() + UP)
        tex_x = Tex("x").set_color_by_tex_to_color_map(colormap_xy).move_to(tex_part3s_eq[1].get_center() + UP)
        tex_y = Tex("y").set_color_by_tex_to_color_map(colormap_xy).move_to(tex_part3s_eq[2].get_center() + UP)
        tex_x_p_y_eq_x_p_y = Tex("x+y", "=", "x", "+", "y").set_color_by_tex_to_color_map(colormap_xy)
        right_img = ImageMobject("right.png", height=1).move_to(RIGHT * 1.5)

        self.play(
            Write(VGroup(adapt_arrow_ups[0], tex_x_plus_y), lag_ratio=0.3),
            run_time=1,
            rate_func=smooth,
            lag_ratio=0.3
        )
        self.play(Write(adapt_recs[0]))
        self.play(
            Write(VGroup(adapt_arrow_ups[1], tex_x), lag_ratio=0.3),
            Write(VGroup(adapt_arrow_ups[2], tex_y), lag_ratio=0.3),
            run_time=1,
            rate_func=smooth,
            lag_ratio=0.2
        )
        self.play(Write(VGroup(adapt_recs[1], adapt_recs[2])))
        self.play(WiggleOutThenIn(tex_x_plus_y), WiggleOutThenIn(tex_x), WiggleOutThenIn(tex_y), run_time = 1.5)
        self.wait(1.5)
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.shift((DOWN + RIGHT) * animate_shift_smooth(now, self.time, 2.5, 0.01, "neg")))
        self.play(
            FadeOut(VGroup(*adapt_arrow_ups)),
            FadeOut(VGroup(*adapt_recs)),
            FadeOut(fx_cpy2),
            FadeOut(right_arrow),
            FadeOut(tex_guess_solution),
            run_time=1.5,
            rate_func=smooth,
            lag_ratio=0.1
        )
        # BUG, clear the scene
        rec_cover = Rectangle(width = 30, height = 30, color="#333333", fill_opacity=1)
        self.play(FadeIn(rec_cover))
        self.clear()
        self.camera.frame.clear_updaters()
        self.camera.frame.move_to(ORIGIN).scale(1)
        self.wait(0.5)
        now = self.time
        self.camera.frame.scale(0.55)
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_smooth(now, self.time, 2, 0.025, "in")))
        self.play(FadeIn(tex_x_p_y_eq_x_p_y), run_time=1)
        self.wait(1)
        self.camera.frame.clear_updaters()
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 2.5, 0.7, 0.03, "out")))
        self.play(
            tex_x_p_y_eq_x_p_y.animate.shift(LEFT * 0.75),
            FadeIn(right_img),
            rate_func=smooth,
        )
        self.wait(1)
        self.play(
            self.camera.frame.animate.scale(1.1),
            tex_x_p_y_eq_x_p_y.animate.shift(RIGHT * 0.75),
            FadeOut(right_img),
            rate_func=smooth,
        )
        self.camera.frame.clear_updaters()

        # Show kx is also a solution
        tex_equation_new = Tex("f(x+y)", "=", "f(x)", "+", "f(y)").set_color_by_tex_to_color_map(colormap_xy)
        tex_equation_new_group = [
            VGroup(*[t for t in tex_equation_new[0:6]]), 
            VGroup(*[t for t in tex_equation_new[7:11]]), 
            VGroup(*[t for t in tex_equation_new[12:]])
        ]
        adapt_arrow_ups_2 = [Tex("\\uparrow").scale(0.8).copy().move_to(tex_equation_new_group[i].get_center() + 0.5 * UP) for i in range(3)]
        adapt_tex_kxpy = Tex("k(x+y)").set_color_by_tex_to_color_map(colormap_xy).move_to(tex_equation_new_group[0].get_center() + UP)
        adapt_tex_kx = Tex("kx").set_color_by_tex_to_color_map(colormap_xy).move_to(tex_equation_new_group[1].get_center() + UP)
        adapt_tex_ky = Tex("ky").set_color_by_tex_to_color_map(colormap_xy).move_to(tex_equation_new_group[2].get_center() + UP)
        tex_kx_equation = Tex("k(x+y)", "=", "kx", "+", "ky").set_color_by_tex_to_color_map(colormap_xy)
        tex_kx_equation_group = [
            VGroup(*[t for t in tex_kx_equation[0:6]]), 
            VGroup(*[t for t in tex_kx_equation[7:9]]), 
            VGroup(*[t for t in tex_kx_equation[10:]])
        ]
        tex_kx = Tex("kx").set_color_by_tex_to_color_map(colormap_xy).move_to(DOWN * 1)
        tex_kx_cps = [tex_kx.copy() for _ in range(3)]

        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.shift(DOWN * animate_shift_smooth(now, self.time, 2.5, 0.01, "pos")))
        self.play(
            TransformMatchingShapes(tex_x_p_y_eq_x_p_y, tex_equation_new),
            FadeIn(tex_kx),
            run_time=1.5,
            rate_func=smooth,
            lag_ratio=0.3
        )
        self.wait(0.5)
        # self.remove(tex_kx)
        # self.add(*tex_kx_cps)
        self.play(
            # *[kx_cp.animate.move_to(tex_kx_equation_group[i].get_center() + DOWN * 1).scale(0.75) for i, kx_cp in enumerate(tex_kx_cps)],
            FadeOut(tex_kx),
            # FadeOut(VGroup(tex_kx_cps)),
            Write(VGroup(*adapt_arrow_ups_2), lag_ratio=0.3),
            run_time=1.2,
        )
        self.play(
            Write(VGroup(adapt_tex_kxpy, adapt_tex_kx, adapt_tex_ky), lag_ratio=0.3),
            run_time=1,
        )
        self.wait(2)
        self.camera.frame.clear_updaters()
        # self.camera.frame.add_updater(lambda frame: frame.shift(DOWN * animate_shift_smooth(now, self.time, 2, 0.01, "neg")))
        self.play(
            *[
                TransformMatchingShapes(tex_eq_new_part, tex_k_new_part)
                for tex_eq_new_part, tex_k_new_part in zip(tex_equation_new_group, tex_kx_equation_group)
            ],
            TransformMatchingShapes(tex_equation_new[6], tex_kx_equation[6]),
            TransformMatchingShapes(tex_equation_new[11], tex_kx_equation[9]),
            run_time=2,
            rate_func=smooth,
            lag_ratio=0.2
        )
        self.play(
            *[WiggleOutThenIn(tex_k_new_part) for tex_k_new_part in tex_kx_equation_group]
        )
        self.wait(1)
        self.camera.frame.clear_updaters()
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.shift(UP * animate_shift_smooth(now, self.time, 2.5, 0.005, "pos")))
        self.play(
            # *[FadeOut(tex_kx_cp) for tex_kx_cp in tex_kx_cps],
            FadeOut(VGroup(*adapt_arrow_ups_2)),
            FadeOut(VGroup(adapt_tex_kxpy, adapt_tex_kx, adapt_tex_ky)),
            run_time=1.5,
            rate_func=smooth,
            lag_ratio=0.3
        )
        self.wait(2)

        # Show that we found a series of solutions by graphing
        solu_kx = Tex("f(x) = kx").set_color_by_tex_to_color_map(colormap_xy).move_to(LEFT * 3 + UP * 2)
        axes = Axes(
            x_range=(-10, 10),
            y_range=(-5, 5),
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
        # line_thetas = [theta * DEGREES for theta in np.linspace(80, -80, 17, endpoint=True)]
        # direction_vecs_inf = [20 * np.array([np.cos(theta), np.sin(theta), 0]) for theta in line_thetas]
        # line_color_gradient = [rgb_to_hex(np.array([255, 255, k]) / 255) for k in np.linspace(0, 200, 17, endpoint=True)] # YELLOW
        # line_strokes = [Line(
        #     start=direction_vecs_inf[i],
        #     end=-direction_vecs_inf[i],
        # ).set_color(line_color_gradient[i]) for i in range(len(line_thetas))]
        # line_dashes = [DashedLine(
        #     start=direction_vecs_inf[i],
        #     end=-direction_vecs_inf[i],
        # ).set_color(line_color_gradient[i]).set_stroke(width=0.4) for i in range(len(line_thetas))]
        adapt_line = Line(
            start=20 * UP,
            end=-20 * UP,
        ).set_color(YELLOW)
        tex_k_eq = Tex("k=").set_color_by_tex_to_color_map(colormap_xy).move_to(LEFT * 3.5 + UP * 1.5).scale(0.7)
        tex_k_num = DecimalNumber(
            0,
            show_ellipsis=False,
            num_decimal_places=2,
            include_sign=True,
        ).scale(0.7).next_to(tex_k_eq, RIGHT, buff=0.1)
        tex_k_eq_group = VGroup(tex_k_eq, tex_k_num)

        now = self.time
        self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 4, 1.5, 0.015 / 4, "out")))
        self.play(
            self.camera.frame.animate.move_to(ORIGIN),
            TransformMatchingShapes(tex_kx_equation, solu_kx, path_arc=90*DEGREES),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(0.5)
        self.play(
            Write(axes),
            FadeInFromPoint(tex_k_eq_group, solu_kx.get_center()),
        )
        self.play(
            Write(adapt_line),
            tex_k_num.animate.set_value(32)
        )
        self.camera.frame.clear_updaters()

        # draw lines
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_smooth(now, self.time, 6, 0.003, "in")))
        total_k_change_time = 3.5
        SS = lambda t: np.sin(np.arctan(5 * t))
        KT_T = lambda t: clip(np.tan(clip(SS((t - total_k_change_time / 2) / (total_k_change_time / 2)) * 90, -89.9, 89.9) * DEGREES), -99, 99) # theta -90 ~ 90
        tex_k_num.add_updater(lambda d: d.set_value(-KT_T(min(total_k_change_time, self.time - now))))
        adapt_line.add_updater(lambda line: line.put_start_and_end_on(
            RIGHT * 10 + UP * 10 * -KT_T(min(total_k_change_time, self.time - now)),
            LEFT * 10 + DOWN * 10 * -KT_T(min(total_k_change_time, self.time - now)),
        ))
          
        self.wait(total_k_change_time + 0.5)
        tex_k_num.clear_updaters()
        adapt_line.clear_updaters()
        self.wait(1)
        self.camera.frame.clear_updaters()
        now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_smooth(now, self.time, 2.5, 0.0055, "out")))
        # self.play(
        #     FadeOut(line_dashes[-4]),
        #     FadeOut(line_dashes[-3]),
        #     FadeOut(line_dashes[-2]),
        #     FadeOut(line_dashes[-1]),
        # )
        self.wait(1)
        self.play(
            FadeOut(adapt_line),
            FadeOut(axes),
            FadeOut(tex_k_eq_group),
        )
        self.wait(1)
        
        tex_k_ask = Tex("f(x)=???").set_color_by_tex_to_color_map(colormap_xy | {"?": BLUE_A})

        self.play(solu_kx.animate.move_to(ORIGIN).scale(1.2))
        self.wait(0.5)
        self.play(TransformMatchingTex(solu_kx, tex_k_ask, key_map={
            "f(x)": "f(x)",
            "k": "???",
            "=": "=",
        }, path_arc=90*DEGREES), run_time=2)
        self.wait(1)

class CAPart1_2(Scene):
    manim_config.tex.template = "ctex"
    
    def construct(self):
        colormap_xy = {"x": RED, "y": GREEN, "k": YELLOW_B}
        base_color1 = {"\\text{Solution: }": WHITE, "f(": WHITE, ")": WHITE, "?": WHITE}
        # tex_solution = Tex("\\text{Solution: }f(x)=kx").set_color_by_tex_to_color_map(colormap_xy | base_color1)
        # tex_solution_quest = Tex("\\text{Solution: }f(x)=\\begin{cases}f(x)=kx\\\\?\\end{cases}") # cannot use color_by_tex_to_color_map because BUG
        # index_color_quest = {11: RED, 17: RED, 21: RED, 20: YELLOW_B, 22: BLUE}
        # for k, v in index_color_quest.items():
            # tex_solution_quest[k].set_color(v)
        # tex_quest = Tex("?").set_color(BLUE).scale(2)

        tex_k_ask = Tex("f(x)=???").set_color_by_tex_to_color_map(colormap_xy | {"?": BLUE_A})

        self.add(tex_k_ask)
        self.wait(1)
        # self.camera.frame.scale(0.4)
        # now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 3, 0.7, 0.03, "out")))
        # tex_typing_animate(self, tex_solution, typing_interval=0.2, blinking_interval=0.8)
        # self.wait(1.5)
        # self.play(
        #     TransformMatchingShapes(tex_solution, tex_solution_quest, path_arc = 90*DEGREES),
        #     run_time=1.5,
        #     rate_func=smooth,
        # )
        # self.wait(1.5)
        # self.camera.frame.clear_updaters()
        # now = self.time
        # self.camera.frame.add_updater(lambda frame: frame.scale(animate_scaling_smooth(now, self.time, 2, 0.009, "in")))
        # shuffle_less_que_elem = [t for t in tex_solution_quest[:22]]
        # random.shuffle(shuffle_less_que_elem)
        # self.play(
        #     TransformMatchingShapes(tex_solution_quest[22], tex_quest),
        #     FadeOut(VGroup(*shuffle_less_que_elem), lag_ratio=0.3),
        #     run_time=3,
        #     rate_func=smooth,
        # )
        # self.play(WiggleOutThenIn(tex_quest))
        # self.wait(3)
        # self.camera.frame.clear_updaters()

        # Show Axes to graph the Pathological Solution
        axes = Axes(
            x_range=(-10, 10),
            y_range=(-5, 5),
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
        rec_pathos = [Rectangle(width=20, height=15, color=YELLOW_C, fill_opacity=0.16).move_to(LEFT * 8 + IN * 1).copy() for _ in range(8)]
        random_red_dot = Square(color=RED_C, side_length=0.1).move_to(RIGHT * 1 + UP * 1).set_stroke(width=0.5)
        text_axiom_choice = Text("选择公理", font="微软雅黑").scale(1.2)

        now = self.time
        # self.camera.frame.add_updater(
        #     lambda frame: frame.shift(RIGHT * animate_shift_smooth(now, self.time, 6, 0.067, "pos")).scale(animate_scaling_smooth(now, self.time, 4, 0.006, "out"))
        # )
        self.wait(1)
        self.play(
            Write(axes, lag_ratio=0.3),
            FadeOut(tex_k_ask),
            run_time=2,
            rate_func=smooth,
        )
        for i, rec_patho in enumerate(rec_pathos):
            self.play(
                rec_patho.animate.move_to(axes.get_center()),
                run_time=0.3 - i * 0.02
            )
        self.wait(2)
        self.play(
            *[FadeOut(rec_patho) for rec_patho in rec_pathos[1:]],
            Write(random_red_dot),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1)
        self.camera.frame.clear_updaters()
        now = self.time
        # self.camera.frame.add_updater(
        #     lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 4, 1.3, 0.05, "in"))
        # )
        self.play(
            # self.camera.frame.animate.move_to(RIGHT * 8 + UP * 2),
            Flash(random_red_dot, color=WHITE, run_time=1.5),
        )
        self.wait(1)
        self.play(
            FadeOut(rec_pathos[0]),
            random_red_dot.animate.set_fill(YELLOW).set_opacity(0.8).scale(1.3),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(1)
        self.camera.frame.clear_updaters()
        # self.remove(tex_quest)
        self.play(
            # self.camera.frame.animate.move_to(ORIGIN),
            FadeOut(random_red_dot),
            FadeOut(axes),
            run_time=1,
            rate_func=smooth,
            lag_ratio=0.3
        )
        self.wait(0.5)
        tex_typing_animate(self, text_axiom_choice, typing_interval=0.5, blinking_interval=0.8)
        self.play(text_axiom_choice.animate.set_color_by_text_to_color_map({
            "选择": GREEN_C,
            "公理": WHITE,
        }))
        self.wait(3)
        self.play(Uncreate(text_axiom_choice))
        self.wait(1)