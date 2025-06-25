from manimlib import *
import numpy as np
import random

class RCPart2_1(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        # 创建域的框
        domain_box = Rectangle(width=6, height=4, color=WHITE)

        # 创建有理数域的标题
        q_title = Tex("a \\in \\mathbb{Q}").move_to(UP * 3).set_color_by_tex_to_color_map({
            "a": RED,
            "\\mathbb{Q}": WHITE
        })

        self.play(Write(domain_box), Write(q_title))

        # 在框内生成并显示 5 个随机有理数
        rational_numbers = []
        for i in range(5):
            numerator = [2, 1, 3, 5, 11][i]
            denominator = [9, 8, 7, 6, 4][i]
            if denominator == 0:
                denominator = 1
            gcd_val = np.gcd(numerator, denominator)
            rational_num_str = f"\\frac{{{numerator//gcd_val}}}{{{denominator//gcd_val}}}" if denominator != 1 else f"{numerator//gcd_val}"
            rational_numbers.append(Tex(rational_num_str, color=RED).scale(0.7).set_color(RED))

        rational_group = VGroup(*rational_numbers).add(Dot(fill_opacity=0)).arrange_in_grid(n_rows=2, n_cols=3, buff=0.5) # insert a placeholder
        rational_group.move_to(domain_box.get_center())

        self.play(Write(rational_group))

        self.wait(1)

        # 演示 Q 中的加法封闭性
        num1, num2 = rational_numbers[1], rational_numbers[3]

        num1_copy = num1.copy().next_to(domain_box, LEFT, buff=1)
        num2_copy = num2.copy().next_to(num1_copy, DOWN)
        self.play(TransformFromCopy(num1, num1_copy), TransformFromCopy(num2, num2_copy))

        group_num = VGroup(num1_copy, num2_copy)
        addition_result_tex = Tex(f"{num1.get_tex()} + {num2.get_tex()} = " + "\\frac{23}{24}", color=RED).next_to(domain_box, RIGHT, buff=1).set_color_by_tex_to_color_map({
            f"{num1.get_tex()}": RED,
            f"{num2.get_tex()}": RED,
            "\\frac{23}{24}": RED
        })

        self.play(
            self.camera.frame.animate.shift(RIGHT * 2),
            ReplacementTransform(group_num, addition_result_tex)
        )

        self.wait(1)

        # 将结果移回框中
        result_copy = Tex("\\frac{23}{24}").move_to(addition_result_tex).scale(0.7).set_color(RED)
        self.play(TransformMatchingShapes(addition_result_tex, result_copy))
        self.play(result_copy.animate.move_to(rational_group[-1].get_center()))

        self.wait(2)

        self.play(
            self.camera.frame.animate.shift(LEFT * 2), 
            FadeOut(rational_group), 
            FadeOut(q_title), 
            FadeOut(num1_copy), 
            FadeOut(num2_copy), 
            FadeOut(result_copy)
        )

        # 创建 Q(sqrt(2)) 的新标题
        q_sqrt2_title = Tex("a+b\\sqrt{2} \\in \\mathbb{Q}(\\sqrt{2})").to_edge(UP).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            " \\mathbb{Q}(\\sqrt{2})": WHITE
        })

        self.play(
            Write(q_sqrt2_title)
        )

        # 生成并显示 5 个 a + b*sqrt(2) 形式的数
        q_sqrt2_numbers = []
        for i in range(5):
            a = [2, 5, 6, 3, 1][i]
            b = [-1, 2, -3, 4, 5][i]

            num_str = f"{a}+{b}" + "\\sqrt{2}"
            q_sqrt2_numbers.append(Tex(num_str).scale(0.7).set_color_by_tex_to_color_map({
                f"{a}": RED,
                f"{b}": GREEN,
                "\\sqrt{2}": WHITE
            }))

        q_sqrt2_group = VGroup(*q_sqrt2_numbers).add(Dot(fill_opacity=0)).arrange_in_grid(n_rows=2, n_cols=3, buff=0.5) # insert a placeholder
        q_sqrt2_group.move_to(domain_box.get_center())

        self.play(Write(q_sqrt2_group))

        self.wait(2)

        num_q_sqrt2_1, num_q_sqrt2_2 = q_sqrt2_group[0], q_sqrt2_group[4]
        addition_result_tex_2 = Tex(f"({num_q_sqrt2_1.get_tex()}) + ({num_q_sqrt2_2.get_tex()}) = " + "3+4\\sqrt{2}", color=RED).next_to(domain_box, RIGHT, buff=1).set_color_by_tex_to_color_map({
            "2": RED,
            "1": RED,
            "-1": GREEN,
            "5": GREEN,
            "3": RED,
            "4": GREEN,
            "\\sqrt{2}": WHITE
        }).scale(0.66).next_to(domain_box, RIGHT)

        num_q_sqrt2_1_copy = num_q_sqrt2_1.copy().next_to(domain_box, LEFT, buff=1)
        num_q_sqrt2_2_copy = num_q_sqrt2_2.copy().next_to(num_q_sqrt2_1_copy, DOWN)
        self.play(TransformFromCopy(num_q_sqrt2_1, num_q_sqrt2_1_copy), TransformFromCopy(num_q_sqrt2_2, num_q_sqrt2_2_copy))
        group_q_sqrt2_num = VGroup(num_q_sqrt2_1_copy, num_q_sqrt2_2_copy)
        self.play(
            self.camera.frame.animate.shift(RIGHT * 2),
            TransformFromCopy(group_q_sqrt2_num, addition_result_tex_2)
        )

        self.wait(1)

        # 将结果移回框中
        result_q_sqrt2_copy = Tex("3+4\\sqrt{2}").move_to(addition_result_tex_2).scale(0.7).set_color_by_tex_to_color_map({
            "3": RED,
            "4": GREEN,
            "\\sqrt{2}": WHITE
        })
        self.play(TransformMatchingShapes(addition_result_tex_2, result_q_sqrt2_copy))
        self.play(result_q_sqrt2_copy.animate.move_to(q_sqrt2_group[-1].get_center()))

        self.wait(2)

        self.play(
            FadeOut(result_q_sqrt2_copy),
            FadeOut(result_q_sqrt2_copy)
        )

        # 乘法演示

        num_q_sqrt2_1, num_q_sqrt2_2 = q_sqrt2_group[0], q_sqrt2_group[4]
        addition_result_tex_3 = Tex(f"({num_q_sqrt2_1.get_tex()}) \\times ({num_q_sqrt2_2.get_tex()}) = " + "-8+9\\sqrt{2}", color=RED).next_to(domain_box, RIGHT, buff=1).set_color_by_tex_to_color_map({
            "2": RED,
            "1": RED,
            "-1": GREEN,
            "5": GREEN,
            "-8": RED,
            "9": GREEN,
            "\\sqrt{2}": WHITE
        }).scale(0.66).next_to(domain_box, RIGHT)

        self.play(ReplacementTransform(group_q_sqrt2_num, addition_result_tex_3))
        self.wait(1)

        # 将结果移回框中
        result_q_sqrt2_copy_2 = Tex("-8+9\\sqrt{2}").move_to(addition_result_tex_3).scale(0.7).set_color_by_tex_to_color_map({
            "-8": RED,
            "9": GREEN,
            "\\sqrt{2}": WHITE
        })
        self.play(TransformMatchingShapes(addition_result_tex_3, result_q_sqrt2_copy_2))
        self.play(result_q_sqrt2_copy_2.animate.move_to(q_sqrt2_group[-1].get_center()))

        self.wait(2)

        self.play(
            self.camera.frame.animate.shift(LEFT * 2),
            FadeOut(result_q_sqrt2_copy_2),
            FadeOut(q_sqrt2_group),
            FadeOut(q_sqrt2_title),
            FadeOut(domain_box)
        )


class RCPart2_2(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        # 步骤 1: 回顾有理数域 Q
        q_title = Tex("\\mathbb{Q}").move_to(UP * 3)
        a_in_q = Tex("a \\in \\mathbb{Q}").move_to(UP * 2).set_color_by_tex_to_color_map({
            "a": RED,
            "\\mathbb{Q}": WHITE
        })
        q_degree = Tex("[\\mathbb{Q}:\\mathbb{Q}]=1").move_to(DOWN * 2)

        self.play(Write(q_title))
        self.play(Write(a_in_q))
        self.play(Write(q_degree))
        self.wait(2)
        self.play(FadeOut(VGroup(q_title, a_in_q, q_degree)))

        # 步骤 2: 引入域扩张 Q(sqrt(2))
        q_sqrt2_title = Tex("\\mathbb{Q}(\\sqrt{2})").move_to(UP * 3)
        a_b_sqrt2_in_q_sqrt2 = Tex("a+b\\cdot\\sqrt{2} \\in \\mathbb{Q}(\\sqrt{2})").move_to(UP * 2).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "\\sqrt{2}": WHITE,
            "\\mathbb{Q}(\\sqrt{2})": WHITE
        })
        q_sqrt2_degree = Tex("[\\mathbb{Q}(\\sqrt{2}):\\mathbb{Q}]=2").move_to(DOWN * 2)

        self.play(Write(q_sqrt2_title))
        self.play(Write(a_b_sqrt2_in_q_sqrt2))
        self.play(Write(q_sqrt2_degree))
        self.wait(2)
        self.play(FadeOut(VGroup(q_sqrt2_title, a_b_sqrt2_in_q_sqrt2, q_sqrt2_degree)))

        # 步骤 3: 引入域扩张 Q(cbrt(2))
        q_cbrt2_title = Tex("\\mathbb{Q}(\\sqrt[3]{2})").move_to(UP * 3)
        q_cbrt2_degree_q = Tex("[\\mathbb{Q}(\\sqrt[3]{2}):\\mathbb{Q}]").move_to(DOWN * 2)

        self.play(Write(q_cbrt2_title))
        self.play(Write(q_cbrt2_degree_q))
        self.wait(1)

        # 步骤 4: 展示 Q(cbrt(2)) 的基和扩张次数
        cbrt2_mult = Tex("2^{1/3} \\times 2^{1/3} = 2^{2/3}").move_to(UP * 0.5)
        cbrt2_basis = Tex("1, 2^{1/3}, 2^{2/3}").move_to(UP * 0.5)
        a_b_c_cbrt2_in_q_cbrt2 = Tex("a+b \\cdot 2^{1/3}+c \\cdot 2^{2/3} \\in \\mathbb{Q}(2^{1/3})").move_to(UP * 2).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": YELLOW,
            "2^{1/3}": WHITE,
            "2^{2/3}": WHITE,
            "\\mathbb{Q}(2^{1/3})": WHITE
        })
        q_cbrt2_degree = Tex("[\\mathbb{Q}(2^{1/3}):\\mathbb{Q}]=3").move_to(DOWN * 2)

        self.play(Write(cbrt2_mult))
        self.wait(2)
        self.play(FadeOut(cbrt2_mult))
        self.play(Write(cbrt2_basis))
        self.wait(1)
        arrow_cbrt2 = Arrow(cbrt2_basis.get_bottom(), q_cbrt2_degree_q.get_top())
        self.play(GrowArrow(arrow_cbrt2))
        self.wait(1)
        self.play(Write(a_b_c_cbrt2_in_q_cbrt2))
        self.play(TransformMatchingTex(q_cbrt2_degree_q, q_cbrt2_degree))
        self.wait(2)
        self.play(FadeOut(VGroup(q_cbrt2_title, a_b_c_cbrt2_in_q_cbrt2, q_cbrt2_degree, arrow_cbrt2, cbrt2_basis)))

        # 步骤 5: 引入域扩张 Q(sqrt(2), sqrt(3))
        q_sqrt2_sqrt3_title = Tex("\\mathbb{Q}(\\sqrt{2}, \\sqrt{3})").move_to(UP * 3)
        q_sqrt2_sqrt3_degree_q = Tex("[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}]").move_to(DOWN * 2)

        self.play(Write(q_sqrt2_sqrt3_title))
        self.play(Write(q_sqrt2_sqrt3_degree_q))
        self.wait(1)

        # 步骤 6: 展示 Q(sqrt(2), sqrt(3)) 的基和扩张次数
        sqrt2_sqrt3_mult = Tex("\\sqrt{2} \\times \\sqrt{3} = \\sqrt{6}").move_to(UP * 0.5)
        sqrt2_sqrt3_basis = Tex("1, \\sqrt{2}, \\sqrt{3}, \\sqrt{6}").move_to(UP * 0.5)
        q_sqrt2_sqrt3_degree = Tex("[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}]=4").move_to(DOWN * 2)
        a_b_c_d_cbrt2 = Tex("a+b \\cdot \\sqrt{2}+c \\cdot \\sqrt{3}+d \\cdot \\sqrt{6} \\in \\mathbb{Q}(\\sqrt{2},\\sqrt{3})").move_to(UP * 2).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": YELLOW,
            "d": BLUE,
            "\\sqrt{2}": WHITE,
            "\\sqrt{3}": WHITE,
            "\\sqrt{6}": WHITE,
            "\\mathbb{Q}(\\sqrt{2},\\sqrt{3})": WHITE,
            "\\cdot": WHITE
        })

        self.play(Write(sqrt2_sqrt3_mult))
        self.wait(2)
        self.play(FadeOut(sqrt2_sqrt3_mult))
        self.play(Write(sqrt2_sqrt3_basis))
        self.wait(1)
        arrow_sqrt2_sqrt3 = Arrow(sqrt2_sqrt3_basis.get_bottom(), q_sqrt2_sqrt3_degree_q.get_top())
        self.play(GrowArrow(arrow_sqrt2_sqrt3))
        self.wait(1)
        self.play(Write(a_b_c_d_cbrt2))
        self.play(TransformMatchingTex(q_sqrt2_sqrt3_degree_q, q_sqrt2_sqrt3_degree))
        self.wait(2)
        self.play(FadeOut(VGroup(q_sqrt2_sqrt3_title, q_sqrt2_sqrt3_degree, arrow_sqrt2_sqrt3, sqrt2_sqrt3_basis, a_b_c_d_cbrt2)))


class RCPart2_3(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        # 1. 表示基础域 Q
        q_box = Rectangle(width=3, height=3, color=BLUE)
        q_title = Tex("\\mathbb{Q}", font_size=36).move_to(q_box.get_center() + UP * 1.2)
        rational_elements = VGroup(
            Tex("1", font_size=28).set_color(RED),
            Tex("-\\frac{1}{2}", font_size=28).set_color(RED),
            Tex("3.14", font_size=28).set_color(RED),
            Tex("0", font_size=28).set_color(RED),
        ).arrange_in_grid(n_rows=2, n_cols=2, buff=0.3).move_to(q_box.get_center())

        q_degree = Tex("[\\mathbb{Q}:\\mathbb{Q}]=1", font_size=28).next_to(q_box, DOWN, buff=0.25)

        self.play(Write(q_box), Write(q_title))
        self.play(LaggedStart(*[Write(element) for element in rational_elements]))
        self.play(Write(q_degree))
        self.wait(2)

        # 清理 Q 的元素和次数，保留框和标题为后续动画做准备
        self.play(
            FadeOut(q_degree)
        )
        self.wait(1)

        # 2. 表示第一次扩张 Q(sqrt(2))
        q_sqrt2_box = Rectangle(width=8, height=4.5, color=GREEN).move_to(RIGHT * 1)
        q_sqrt2_title = Tex("\\mathbb{Q}(\\sqrt{2})", font_size=36).move_to(q_sqrt2_box.get_center() + UP * 1.95)
        q_q_sqrt2_arrow = Arrow(q_box.get_left(), q_sqrt2_box.get_left(), buff=0.1, stroke_width=3)

        self.play(
            self.camera.frame.animate.shift(RIGHT * 2).scale(1.2),
            Write(q_sqrt2_box), 
            Write(q_sqrt2_title), 
            GrowArrow(q_q_sqrt2_arrow)
        )
        self.wait(1)

        # 元素形式
        q_sqrt2_element_form = Tex("a+b\\sqrt{2}", font_size=36).move_to(q_sqrt2_box.get_right() + LEFT * 1.5).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": YELLOW,
            "d": BLUE,
            "\\sqrt{2}": WHITE,
            "\\sqrt{3}": WHITE,
            "\\sqrt{6}": WHITE,
            "+": WHITE
        })
        self.play(Write(q_sqrt2_element_form))
        self.wait(1)

        # 扩张次数
        q_sqrt2_degree = Tex("[\\mathbb{Q}(\\sqrt{2}):\\mathbb{Q}]=2").next_to(q_sqrt2_box, DOWN, buff=0.5)
        self.play(Write(q_sqrt2_degree))
        self.wait(2)

        # 清理 Q(sqrt(2)) 的元素形式和次数，保留框和标题
        self.play(
            FadeOut(q_sqrt2_degree)
        )
        self.wait(1)

        # 3. 表示第二次扩张 Q(sqrt(2), sqrt(3))
        q_sqrt2_sqrt3_box = Rectangle(width=15, height=6, color=YELLOW).move_to(RIGHT * 2)
        q_sqrt2_sqrt3_title = Tex("\\mathbb{Q}(\\sqrt{2}, \\sqrt{3})", font_size=36).move_to(q_sqrt2_sqrt3_box.get_center() + UP * 2.7)
        q_sqrt2_q_sqrt2_sqrt3_arrow = Arrow(q_sqrt2_box.get_left(), q_sqrt2_sqrt3_box.get_left(), buff=0.1, stroke_width=3)

        self.play(
            self.camera.frame.animate.shift(RIGHT * 2).scale(1.2),
            Write(q_sqrt2_sqrt3_box), 
            Write(q_sqrt2_sqrt3_title), 
            GrowArrow(q_sqrt2_q_sqrt2_sqrt3_arrow)
        )
        self.wait(1)

        # 动画演示元素构成和展开形式
        combined_element_2 = Tex(
            "(", "A_1", "+", "B_1", "\\sqrt{2})",
            "+",
            "(", "A_2", "+", "B_2", "\\sqrt{2})",
            "\\sqrt{3}"
        ).move_to(q_sqrt2_sqrt3_box.get_right() + RIGHT * 3.5).set_color_by_tex_to_color_map({
            "(A_1+B_1\\sqrt{2})": RED,
            "(A_2+B_2\\sqrt{2})": GREEN,
        })
        self.play(
            self.camera.frame.animate.shift(RIGHT * 3.5),
            Write(combined_element_2)
        )
        self.wait(1)

        # 展开形式
        expanded_form = Tex("a", "+", "b", "\\sqrt{2}", "+", "c", "\\sqrt{3}", "+", "d", "\\sqrt{2}\\sqrt{3}").move_to(combined_element_2.get_center())
        self.play(
            TransformMatchingTex(combined_element_2, expanded_form, key_map={
                "A_1": "a",
                "B_1": "b",
                "A_2": "c",
                "B_2": "d",
            })
        )
        self.wait(1)

        # 最终形式
        final_form = Tex("a+b\\sqrt{2}+c\\sqrt{3}+d\\sqrt{6}").move_to(combined_element_2.get_center()).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": YELLOW,
            "d": BLUE,
            "\\sqrt{2}": WHITE,
            "\\sqrt{3}": WHITE,
            "\\sqrt{6}": WHITE,
            "+": WHITE
        })
        self.play(TransformMatchingTex(expanded_form, final_form, key_map={
            "\\sqrt{2}\\sqrt{3}": "\\sqrt{6}"
        }))
        self.wait(1)

        q_sqrt2_sqrt3_element_form_ab = Tex("a+b\\sqrt{2}+c\\sqrt{3}+d\\sqrt{6}", font_size=36).move_to(q_sqrt2_sqrt3_box.get_right() + LEFT * 2).set_color_by_tex_to_color_map({
            "a": RED,
            "b": GREEN,
            "c": YELLOW,
            "d": BLUE,
            "\\sqrt{2}": WHITE,
            "\\sqrt{3}": WHITE,
            "\\sqrt{6}": WHITE,
            "+": WHITE
        })

        # 扩张次数
        q_sqrt2_sqrt3_degree = Tex("[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}(\\sqrt{2})]=2").next_to(q_sqrt2_sqrt3_box, DOWN, buff=0.25)
        self.play(
            self.camera.frame.animate.shift(LEFT * 4),
            ReplacementTransform(final_form, q_sqrt2_sqrt3_element_form_ab),
            Write(q_sqrt2_sqrt3_degree)
        )
        self.wait(2)

        # 清理 Q(sqrt(2), sqrt(3)) 的元素形式、基和次数，保留框和标题
        self.play(FadeOut(q_sqrt2_sqrt3_degree))
        self.wait(1)

        # 4. 展示域塔和次数乘法性质
        # 显示扩张次数
        q_q_sqrt2_degree_text = Tex("[\\mathbb{Q}(\\sqrt{2}):\\mathbb{Q}]=2").next_to(q_sqrt2_sqrt3_box, LEFT, buff=0.7).shift(UP * 0.5).set_color(LIGHT_PINK)
        q_sqrt2_q_sqrt2_sqrt3_degree_text = Tex("[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}(\\sqrt{2})]=2").next_to(q_sqrt2_sqrt3_box, LEFT, buff=0.7).shift(DOWN * 0.5).set_color(LIGHT_BROWN)

        self.play(
            self.camera.frame.animate.move_to(LEFT * 6).scale(0.9),
            Write(q_q_sqrt2_degree_text), 
            Write(q_sqrt2_q_sqrt2_sqrt3_degree_text)
        )
        self.wait(1)

        # 次数乘法演示
        multiplication_formula = Tex(
            "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}]", " = ", "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}(\\sqrt{2})]", " \\times ", "[\\mathbb{Q}(\\sqrt{2}):\\mathbb{Q}]"
        ).scale(0.8).next_to(q_sqrt2_q_sqrt2_sqrt3_degree_text, LEFT, buff=1).shift(UP * 0.5).set_color_by_tex_to_color_map({
            "[\\mathbb{Q}(\\sqrt{2}):\\mathbb{Q}]": LIGHT_PINK,
            "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}(\\sqrt{2})]": LIGHT_BROWN
        })
        self.play(self.camera.frame.animate.shift(LEFT * 8))
        self.play(Write(multiplication_formula))
        self.wait(3)

        # 替换数值
        multiplication_calculation = Tex(
            "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}]", " = ", "2 \\times ", "2", " = 4"
        ).move_to(multiplication_formula.get_center())
        self.play(TransformMatchingTex(multiplication_formula, multiplication_calculation, key_map={
            "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}]": "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}]",
            "[\\mathbb{Q}(\\sqrt{2}):\\mathbb{Q}]": "2",
            "[\\mathbb{Q}(\\sqrt{2}, \\sqrt{3}):\\mathbb{Q}(\\sqrt{2})]": "2 \\times"
        }))
        self.wait(2)

        # 5. 推广到一般域塔
        self.play(self.camera.frame.animate.move_to(DOWN * 9))
        self.wait(1)

        general_tower_formula = Tex("K_1 \\subseteq K_2 \\subseteq K_3 \\subseteq \\cdots \\subseteq K_n").move_to(DOWN * 6).set_color_by_tex_to_color_map({
            "K_1": BLUE_E,
            "K_2": BLUE_D,
            "K_3": BLUE_C,
            "K_n": BLUE_A,
            "\\subseteq": WHITE
        })
        general_multiplication_formula = Tex("[K_n:K_1] = [K_n:K_{n-1}] \\times [K_{n-1}:K_{n-2}] \\times \\dots \\times [K_2:K_1]").next_to(general_tower_formula, DOWN, buff=1.5).set_color_by_tex_to_color_map({
            "K_n": BLUE_A,
            "K_{n-1}": BLUE_B,
            "K_{n-2}": BLUE_C,
            "K_2": BLUE_D,
            "K_1": BLUE_E,
            "\\times": WHITE,
            "[": WHITE,
            "]": WHITE,
            ":": WHITE,
        })

        self.play(Write(general_tower_formula))
        self.play(Write(general_multiplication_formula))
        self.wait(2)
        
        self.play(
            self.camera.frame.animate.move_to(DOWN * 2).scale(1.6),
            q_box.animate.move_to(OUT * 2),
            q_sqrt2_box.animate.move_to(OUT * 1),
            q_sqrt2_sqrt3_box.animate.move_to(ORIGIN),
            q_title.animate.move_to(OUT * 2 + DOWN * 2),
            q_sqrt2_title.animate.move_to(OUT * 1 + DOWN * 3),
            q_sqrt2_sqrt3_title.animate.move_to(ORIGIN + DOWN * 4),
            general_multiplication_formula.animate.move_to(DOWN * 5 + IN),
            general_tower_formula.animate.move_to(DOWN * 5 + IN * 2),
            FadeOut(multiplication_calculation),
            FadeOut(q_q_sqrt2_degree_text),
            FadeOut(q_sqrt2_q_sqrt2_sqrt3_degree_text),
            FadeOut(rational_elements),
            FadeOut(q_sqrt2_element_form),
            FadeOut(q_sqrt2_sqrt3_element_form_ab),
            FadeOut(q_q_sqrt2_arrow),
            FadeOut(q_sqrt2_q_sqrt2_sqrt3_arrow),
        )
        self.play(
            self.camera.frame.animate.rotate(60*DEGREES, RIGHT).rotate(10*DEGREES, OUT).shift(UP * 2.5),
            q_title.animate.rotate(PI/2, RIGHT),
            q_sqrt2_title.animate.rotate(PI/2, RIGHT),
            q_sqrt2_sqrt3_title.animate.rotate(PI/2, RIGHT),
            general_multiplication_formula.animate.rotate(PI/2, RIGHT),
            general_tower_formula.animate.rotate(PI/2, RIGHT),
            run_time=2
        )

        self.wait(4)

        # 动画结束，清理所有对象
        self.play(
            FadeOut(q_box),
            FadeOut(q_sqrt2_box),
            FadeOut(q_sqrt2_sqrt3_box),
            FadeOut(q_title),
            FadeOut(q_sqrt2_title),
            FadeOut(q_sqrt2_sqrt3_title),
            FadeOut(general_multiplication_formula),
            FadeOut(general_tower_formula),
        )
        self.wait(2)