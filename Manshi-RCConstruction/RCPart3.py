from manimlib import *

class RCPart3_1(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        # 打开圆规图片
        compose = ImageMobject("compose.png").move_to(LEFT * 1).scale(0.6)
        rule = RoundedRectangle(width=0.36, height=2.2, corner_radius=0.05, color=WHITE, fill_opacity=0.5).move_to(RIGHT * 1).rotate(30 * DEGREES)

        self.play(
            FadeIn(compose, shift=UP * 0.5),
            FadeIn(rule, shift=UP * 0.5),
        )
        self.wait(1)

        rectangle_holder = Rectangle(width=5, height=6, color=GREEN, fill_opacity=0.2).move_to(RIGHT * 12)

        self.play(
            self.camera.frame.animate.shift(RIGHT * 2),
            rectangle_holder.animate.move_to(RIGHT * 2.5),
            compose.animate.move_to(LEFT * 2.5 + UP * 1).scale(0.9),
            rule.animate.move_to(LEFT * 2.5 + DOWN * 1).scale(0.9),
        )
        self.wait(4)

        arrow_0_1 = Arrow(start=ORIGIN, end=RIGHT, color=RED_A, buff=0)
        point_0 = Dot(ORIGIN, color=RED_D, radius=0.1)
        point_1 = Dot(RIGHT, color=RED_D, radius=0.1)
        tag_0 = Tex("0").next_to(point_0, DOWN, buff=0.1).set_color(RED_D).scale(0.7)
        tag_1 = Tex("1").next_to(point_1, DOWN, buff=0.1).set_color(RED_D).scale(0.7)

        self.remove(rectangle_holder)
        self.play(
            self.camera.frame.animate.move_to(UP * 1.5),
            compose.animate.move_to(LEFT * 3 + UP * 3.5).scale(0.7),
            rule.animate.move_to(LEFT * 2 + UP * 3.5).scale(0.7),
            rate_func=smooth
        )
        self.wait(0.5)
        self.play(
            Write(arrow_0_1),
            Write(point_0),
            Write(point_1),
        )
        self.play(
            Write(tag_0),
            Write(tag_1),
        )
        self.wait(1)

        # ADD

        arrow1_cp = arrow_0_1.copy()
        arrow1_cp = arrow1_cp.move_to(RIGHT*1.5).set_color(GREEN_A)
        arrow2_cp = arrow_0_1.copy()
        arrow2_cp = arrow2_cp.move_to(RIGHT*2.5).set_color(YELLOW_A)

        self.play(
            self.camera.frame.animate.move_to(UP * 1.5 + RIGHT * 1).scale(0.7),
            Write(arrow1_cp),
            Write(arrow2_cp),
            lag_ratio=0.1,
            rate_func=smooth
        )

        arrow_group = VGroup(arrow_0_1, arrow1_cp, arrow2_cp)
        brace = Brace(arrow_group, direction=UP, color=WHITE)
        brace_label = Tex("1+1+1=3", color=WHITE).next_to(brace, UP, buff=0.1)

        self.play(
            Write(brace),
            Write(brace_label),
        )

        self.wait(2)

        self.play(
            FadeOut(brace),
            FadeOut(brace_label),
        )

        # MULTIPLY

        print(RIGHT, UP)

        arrow3 = Arrow(start=ORIGIN, end=2*UP, color=GREEN_A, buff=0)
        arrow4 = Arrow(start=ORIGIN, end=1.5*RIGHT, color=YELLOW_A, buff=0)
        arrow_5_r = Arrow(start=ORIGIN, end=3*UP, color=BLUE, buff=0)

        dash_1_2 = DashedLine(start=RIGHT, end=2*UP, color=GREEN_C, dash_length=0.1, stroke_width=2)
        dash_1d5_3 = DashedLine(start=1.5*RIGHT, end=3*UP, color=YELLOW_C, dash_length=0.1, stroke_width=2)
        parallel_symbol_1 = Tex("||", color=WHITE).rotate(75 * DEGREES).move_to(dash_1_2.get_center()).scale(0.8)
        parallel_symbol_2 = Tex("||", color=WHITE).rotate(75 * DEGREES).move_to(dash_1d5_3.get_center()).scale(0.8)

        point_1d5 = Dot(1.5*RIGHT, color=RED_D, radius=0.1)
        tag_1d5 = Tex("1.5").next_to(point_1d5, DOWN, buff=0.1).set_color(RED_D).scale(0.7)
        point_y2 = Dot(2*UP, color=RED_D, radius=0.1)
        tag_y2 = Tex("2").next_to(point_y2, LEFT, buff=0.1).set_color(RED_D).scale(0.7)

        self.play(
            ReplacementTransform(arrow1_cp, arrow3),
            ReplacementTransform(arrow2_cp, arrow4),
            lag_ratio = 0.1
        )
        self.wait(0.5)
        self.play(
            self.camera.frame.animate.shift(LEFT*1).scale(1.1),
            Write(point_1d5),
            Write(tag_1d5),
            Write(point_y2),
            Write(tag_y2),
        )
        self.play(Write(dash_1_2))
        self.play(Write(parallel_symbol_1))
        self.play(TransformFromCopy(parallel_symbol_1, parallel_symbol_2))
        self.play(TransformFromCopy(dash_1_2, dash_1d5_3))
        self.wait(1)
        self.play(Write(arrow_5_r))
        self.wait(2)

        brace = Brace(arrow_5_r, direction=LEFT, color=WHITE)
        brace_label = Tex("2\\times1.5=3", color=WHITE).next_to(brace, LEFT, buff=0.7)

        self.play(
            Write(brace),
            Write(brace_label),
        )
        self.wait(3)

        self.play(
            FadeOut(brace),
            FadeOut(brace_label),
            FadeOut(arrow_5_r),
            FadeOut(arrow3),
            FadeOut(arrow4),
            FadeOut(dash_1_2),
            FadeOut(dash_1d5_3),
            FadeOut(parallel_symbol_1),
            FadeOut(parallel_symbol_2),
            FadeOut(point_1d5),
            FadeOut(tag_1d5),
            FadeOut(point_y2),
            FadeOut(tag_y2),
            FadeOut(arrow_0_1),
            FadeOut(arrow1_cp),
            
        )
