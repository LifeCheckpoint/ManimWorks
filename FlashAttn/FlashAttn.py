import sys
sys.path.append('D:/wroot/ManimWorks/FlashAttn')

from manimlib import *
from effect import *
import numpy as np

class SoftmaxIntroduction(Scene):
    def construct(self):
        self.show_max_function()
        self.transition_to_softmax()
        self.reveal_softmax_formula()
        self.show_key_properties()

    def show_max_function(self):
        """展示传统max函数"""
        values = [3, 1, 4, 1.5]
        boxes = VGroup(*[Rectangle(height=v/2, width=1, fill_color=BLUE_E) for v in values]).arrange(RIGHT, buff=0.5)
        boxes.to_edge(UP, buff=2)
        
        # 最大值高亮
        max_box: Rectangle = boxes[2].copy()
        max_box.set_fill(YELLOW)
        
        # 标注
        max_label = Text("max", color=RED_E).next_to(boxes, DOWN, buff=0.7)
        arrow = Arrow(max_label.get_top(), max_box.get_bottom(), color=RED_E)
        
        # 动画序列
        self.play(LaggedStartMap(FadeIn, boxes, shift=UP, lag_ratio=0.2))
        self.wait(0.5)
        self.play(
            Transform(boxes[2], max_box),
            FadeIn(arrow),
            Write(max_label),
            *[box.animate.set_fill(opacity=0.3) for i, box in enumerate(boxes) if i != 2]
        )
        for box in boxes:
            box: Rectangle
            box.add_updater(Effect.wiggle())
        self.wait(2)
        self.play(
            FadeOut(arrow),
            FadeOut(max_label)
        )

    def transition_to_softmax(self):
        """过渡到softmax的动画"""
        # 创建对比标题
        max_text = Text("max", color=RED_E).scale(1.5)
        softmax_text = Text("softmax", color=TEAL_E).scale(1.5)
        vs = Text("vs", color=GREY).scale(0.8)
        group = VGroup(max_text, vs, softmax_text).arrange(RIGHT, buff=0.5)
        
        # 动态对比动画
        self.play(Write(group))
        self.wait()
        self.play(
            group.animate.scale(0.7).to_edge(UP),
            softmax_text.animate.set_color(BLUE_D),
            max_text.animate.set_color(GREY)
        )
        self.wait()
        self.play(FadeOut(group))

    def reveal_softmax_formula(self):
        """逐步展示softmax公式"""
        # 创建公式组件
        formula = Tex(
            r"\mathrm{Softmax}(x_i) = \frac{e^{x_i}}{\sum_{j} e^{x_j}}",
            isolate=["e^{x_i}", r"\sum_{j} e^{x_j}"]
        )
        formula.set_color_by_tex("e^{x_i}", BLUE_D)
        formula.set_color_by_tex(r"\sum_{j} e^{x_j}", PURPLE)
        
        # 公式解释元素
        exp_note = Text("指数放大差异", color=BLUE_D, font="CMU Sans Serif").scale(0.7).next_to(formula, DOWN, aligned_edge=LEFT)
        sum_note = Text("归一化保证和为1", color=PURPLE, font="CMU Sans Serif").scale(0.7).next_to(formula, DOWN, aligned_edge=RIGHT)
        
        # 动态展示
        self.play(Write(formula[:5]))  # 写Softmax部分
        self.wait(0.5)
        self.play(
            Write(formula[5:8]),  # 分子部分
            FadeIn(exp_note, shift=UP)
        )
        self.wait()
        self.play(
            Write(formula[8:]),  # 分母部分
            FadeIn(sum_note, shift=UP)
        )
        self.wait(2)
        self.play(FadeOut(exp_note), FadeOut(sum_note))

    def show_key_properties(self):
        """展示三个关键特性"""
        properties = VGroup(
            self.create_property_icon("突出最大值", "arrow_up", TEAL_E),
            self.create_property_icon("保留相对差异", "wave", BLUE_D),
            self.create_property_icon("输出和为1", "sigma", PURPLE)
        ).arrange(RIGHT, buff=2)
        
        # 背景装饰
        deco_rect = SurroundingRectangle(properties, buff=1, color=GREY_A, fill_opacity=0.1)
        
        # 动画展示
        self.play(
            FadeIn(deco_rect),
            LaggedStartMap(FadeIn, properties, shift=UP, lag_ratio=0.3)
        )
        self.wait(3)

    def create_property_icon(self, text, symbol, color):
        """创建特性图标"""
        icon = VGroup()
        # 创建符号图形
        if symbol == "arrow_up":
            shape = Arrow(UP*0.5, DOWN*0.5, color=color).flip(UP)
        elif symbol == "wave":
            shape = ParametricCurve(
                lambda t: [t/2-0.7, np.sin(3*t)/4, 0],
                t_range=[-3, 3, 0.01]
            )
            shape.set_color(color)
        elif symbol == "sigma":
            shape = Tex(r"\Sigma", color=color).scale(1.5)
        
        # 文字说明
        label = Text(text, color=BLACK, font="微软雅黑").scale(0.6)
        
        return VGroup(shape, label).arrange(DOWN, buff=0.5)