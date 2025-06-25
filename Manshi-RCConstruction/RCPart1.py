from manimlib import *
import numpy as np
import random

class RCPart1(Scene):
    manim_config.tex.template = "ctex"

    def construct(self):
        # --- 定义部分 ---

        # 坐标轴设置
        axes_x = NumberLine(
            x_range=(-15, 15, 1), # Added step for clarity if needed later
            include_numbers=False,
            include_tip=True,
            color=WHITE
        )
        axes_x.shift(RIGHT * 0.11)

        axes_y = NumberLine(
            x_range=(-8, 8, 1), # Added step
            include_numbers=False,
            include_tip=True,
            color=WHITE
        ).rotate(90 * DEGREES)
        axes_y.shift(UP * 0.11)

        # 1. 明确坐标轴的含义
        q_label = Tex("\\mathbb{Q}", font_size=24, color=WHITE).shift(UP * 0.4 + RIGHT * 6.5)
        q_sqrt2_label = Tex("\\mathbb{Q}\\cdot\\sqrt{2}", font_size=30, color=WHITE).shift(UP * 3.5 + RIGHT * 1)

        # 坐标轴标签
        origin_label = Tex("0", font_size=24).next_to(axes_x.n2p(0), DOWN, buff=0.25)

        x_labels = VGroup()
        for i in range(-12, 13):
            if i == 0: continue
            label = Tex(f"{i}", font_size=24).next_to(axes_x.n2p(i), DOWN, buff=0.25)
            x_labels.add(label)

        y_labels = VGroup()
        for i in range(-6, 7):
            if i == 0: continue
            # Use axes_y.n2p for positioning relative to the rotated axis
            label = Tex(f"{i}\\sqrt{2}", font_size=24).next_to(axes_y.n2p(i), LEFT, buff=0.25)
            y_labels.add(label)

        # 4. 修正 Z 轴渲染 (将定义提前)
        axes_z = NumberLine(
            x_range=(-8, 8, 1), # Adjusted range to match y
            include_numbers=False,
            include_tip=True,
            color=WHITE
        ).rotate(90 * DEGREES, UP) # Rotate around UP vector for Z axis (Original method)

        # 恢复原始路径函数
        def get_path_point(t, time=8, include_z=False):
            # 将 t 通过 smooth 函数重映射到 (0, 6) 区间内
            t = t / time
            t = smooth(t)
            t = t * 6 # Map to 0-6 range for trigonometric functions

            # Original complex path components
            x = 5 * np.cos(t) + np.cos(2.3 * t + 1.2) + 0.5 * np.cos(4.1 * t + 0.7)
            y = 2 * np.sin(t) + np.sin(1.7 * t + 0.5) + 0.3 * np.sin(3.5 * t + 1.8)

            # Scale x to be within roughly [-7, 7] if needed, original max is ~6.5
            x_scaled = x * (7 / 6.5) # Scale slightly to ensure it reaches +/- 7

            if include_z:
                # 添加 z 坐标 (保持与原版一致)
                z = np.sin(t * 0.8) * 3 # 示例 z 坐标

                # Correct 3D point construction using vector addition
                origin_point = axes_x.n2p(0) # Assume common origin
                x_vec = axes_x.n2p(x_scaled) - origin_point
                y_vec = axes_y.n2p(y) - origin_point # y mapped to y-axis
                z_vec = axes_z.n2p(z) - origin_point # z mapped to z-axis
                return origin_point + x_vec + y_vec + z_vec
            else:
                # Return 2D coordinate using scaled x and original y mapped to axes
                # y component needs to be relative to y-axis origin
                origin_point = axes_x.n2p(0)
                x_vec = axes_x.n2p(x_scaled) - origin_point
                y_vec = axes_y.n2p(y) - origin_point
                return origin_point + x_vec + y_vec # Combine x and y vectors

        # 1. 修改一维路径函数 (基于 get_path_point 的 x 分量)
        def get_path_point_1d(t, time=8):
            t_mapped = t / time
            t_mapped = smooth(t_mapped)
            t_mapped = t_mapped * 4 # Map to 0-9 range for more oscillations

            x = 5 * np.cos(t_mapped) + np.cos(2.3 * t_mapped + 1.2) + 0.5 * np.cos(4.1 * t_mapped + 0.7)
            x_scaled = x * (7 / 6.5) # Scale to [-7, 7]
            return axes_x.n2p(x_scaled)

        # 创建移动点 (淡红色空心圆)
        dot = Circle(radius=0.1, color=RED_E, stroke_width=2, fill_opacity=0)
        initial_pos = get_path_point_1d(0) # Use new 1D path
        dot.move_to(initial_pos)

        # 创建坐标显示 (右上角)
        x_coord_display = DecimalNumber(
            axes_x.p2n(dot.get_center()), # 使用 p2n 获取数轴上的值
            num_decimal_places=3,
            include_sign=True,
            font_size=36
        )
        x_coord_display.to_corner(UR, buff=1)

        # 创建动态更新的虚线 (Part 1)
        line = always_redraw(lambda: DashedLine(
            dot.get_center(), # 起点：圆心
            np.array([dot.get_center()[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]], dtype=float), # 确保是3D float array
            color=YELLOW
        ))

        # 定义坐标文本的更新器 (Part 1)
        def update_text(mob):
            # 从点的屏幕坐标转换回数轴坐标
            current_x_val = axes_x.p2n(dot.get_center())
            mob.set_value(current_x_val)
            mob.to_corner(UR, buff=1) # 保持在角落

        # 时间追踪器 (用于所有动态路径部分)
        t_tracker = ValueTracker(0)
        # ValueTrackers for display (optional, can be removed if update_displays works)
        # rational_tracker = ValueTracker(0) # Removed unused tracker
        # sqrt2_tracker = ValueTracker(0) # Removed unused tracker

        # --- 二次扩域部分对象定义 ---
        # 创建新的红色小点
        new_dot = Circle(radius=0.08, color=RED, stroke_width=2, fill_opacity=0)
        # 初始位置将在动画部分设置

        # 3. 增强投影线的视觉效果 (Part 2 - 添加投影点)
        # 创建y轴投影虚线和点
        y_line_group = always_redraw(lambda: VGroup(
            DashedLine(
                new_dot.get_center(),
                np.array([axes_y.n2p(0)[0], new_dot.get_center()[1], axes_y.n2p(0)[2]], dtype=float),
                color=YELLOW
            ),
            Dot(
                np.array([axes_y.n2p(0)[0], new_dot.get_center()[1], axes_y.n2p(0)[2]], dtype=float),
                radius=0.05, color=YELLOW
            )
        ))

        # 创建x轴投影虚线和点
        x_line_group = always_redraw(lambda: VGroup(
            DashedLine(
                new_dot.get_center(),
                np.array([new_dot.get_center()[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]], dtype=float),
                color=YELLOW
            ),
            Dot(
                np.array([new_dot.get_center()[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]], dtype=float),
                radius=0.05, color=YELLOW
            )
        ))

        # 创建数值显示
        rational_display = DecimalNumber(
            0, num_decimal_places=3, include_sign=True, color=RED, font_size=36
        )
        sqrt2_display = DecimalNumber(
            0, num_decimal_places=3, include_sign=True, color=GREEN, font_size=36
        )
        sqrt2_sign = Tex(r"\sqrt{2}", font_size=36)

        # 组合显示
        display_group = VGroup(
            rational_display, sqrt2_display, sqrt2_sign
        ).arrange(RIGHT, buff=0.1).to_corner(UR, buff=1) # Added + sign

        brace_rational_square = Brace(rational_display, UP)
        brace_rational_square.set_color(RED)
        brace_sqrt2_square = Brace(sqrt2_display, UP)
        brace_sqrt2_square.set_color(GREEN)
        tag_a = Text("a", font_size=28)
        tag_a = tag_a.next_to(brace_rational_square, UP).set_color(RED)
        tag_b = Text("b", font_size=28)
        tag_b = tag_b.next_to(brace_sqrt2_square, UP).set_color(GREEN)

        tagging_group = VGroup(
            tag_a, tag_b, brace_rational_square, brace_sqrt2_square
        )

        # 更新函数 (Part 2 - 基于 get_center())
        def update_displays(mob): # mob is display_group
            current_pos = new_dot.get_center()
            # 从屏幕坐标转换回数轴坐标
            # Project onto x-axis first, then convert
            x_proj_point = np.array([current_pos[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]])
            x_val = axes_x.p2n(x_proj_point)

            # Project onto y-axis first, then convert
            # Need to consider the y-axis rotation and origin
            y_axis_origin = axes_y.n2p(0)
            y_axis_unit_vec = axes_y.n2p(1) - y_axis_origin
            point_vec = current_pos - y_axis_origin
            # Project point_vec onto y_axis_unit_vec
            y_val = np.dot(point_vec, y_axis_unit_vec) / np.dot(y_axis_unit_vec, y_axis_unit_vec)

            rational_display.set_value(x_val)
            sqrt2_display.set_value(y_val)
            # Keep the group in the corner
            mob.to_corner(UR, buff=1)

        # --- 动画部分 ---

        self.wait(1)
        # 1. 添加坐标轴含义标签
        self.play(
            Write(axes_x),
            Write(x_labels),
            Write(origin_label),
            Write(q_label), # Add Q label
            run_time=1.5
        )
        self.wait(1)

        # 添���初始对象到场景 (Part 1)
        self.play(
            FadeIn(dot),
            Write(line),
            Write(x_coord_display),
            run_time=1.5
        )

        # 添加更新器 (Part 1 - 使用简化路径)
        x_coord_display.add_updater(update_text)
        dot.add_updater(lambda mob: mob.move_to(get_path_point_1d(t_tracker.get_value()))) # Use new 1D path

        # 运行 8 秒动画 (Part 1)
        self.play(
            t_tracker.animate.set_value(8),
            run_time=8,
            rate_func=linear
        )

        # 清理更新器 (Part 1)
        dot.clear_updaters()
        # line is always_redraw, no need to clear
        x_coord_display.clear_updaters()
        x_line_group.clear_updaters() # Clear x_line_group updaters

        self.wait(2)

        # --- 过渡到二次扩域 ---
        # 4. 相机视角和过渡 (平滑过渡 - Step 1: Shift/Scale)
        self.play(
            FadeOut(origin_label),
            FadeOut(dot),
            FadeOut(line),
            FadeOut(x_coord_display),
            Write(axes_y),
            Write(q_sqrt2_label), # Add Q√2 label
            # Adjust camera view for y-axis - Step 1
            self.camera.frame.animate.shift(UP * 1.0 + RIGHT * 2.5).scale(0.9),
            run_time=2
        )

        x_line_group = always_redraw(lambda: VGroup(
            DashedLine(
                new_dot.get_center(),
                np.array([new_dot.get_center()[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]], dtype=float),
                color=YELLOW
            ),
            Dot(
                np.array([new_dot.get_center()[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]], dtype=float),
                radius=0.05, color=YELLOW
            )
        )) # 覆盖

        self.play(
            Write(y_labels)
        )

        self.wait(2)

        # 2. 恢复二维路径 (Part 2 - 用原始 get_path_point)
        # new_dot initial position already set during definition

        # 添加二次扩域对象到场景
        self.play(
            FadeIn(new_dot),
            Write(y_line_group), # Use group with dot
            Write(x_line_group), # Use group with dot
            Write(display_group),
            FadeIn(tagging_group),
            run_time=1.5
        )

        # 添加更新器 (Part 2 - 恢复 updater)
        new_dot.add_updater(lambda mob: mob.move_to(get_path_point(t_tracker.get_value())))
        display_group.add_updater(update_displays)

        # 2. 恢复二维路径 (Part 2 - 运行动画)
        # Reset t_tracker before animation
        t_tracker.set_value(0)
        self.play(
            t_tracker.animate.set_value(8), # Drive t from 0 to 8 (maps to 0-6 internally)
            run_time=8,
            rate_func=linear
        )

        # 清理更新器 (Part 2)
        new_dot.clear_updaters()
        # always_redraw groups don't need clearing
        display_group.clear_updaters()
        tagging_group.clear_updaters()
        x_line_group.clear_updaters() # Clear x_line_group updaters
        y_line_group.clear_updaters() # Clear y_line_group updaters

        self.wait(3)

        # --- 清理二次扩域动态点 ---
        self.play(
            FadeOut(new_dot),
            FadeOut(y_line_group),
            FadeOut(x_line_group),
            FadeOut(display_group),
            FadeOut(tagging_group),
            # Keep axes and labels for addition part
        )
        # Clear any potential leftover updaters
        if hasattr(t_tracker, 'updaters'): t_tracker.clear_updaters()
        # Removed checks for rational_tracker and sqrt2_tracker as they are no longer defined

        self.wait(1) # Wait after cleanup

        # --- 二次扩域加法可视化 ---
        # (加法部分代码保持不变，因为它未使用复杂路径或 t_tracker)
        # 2.1 场景设置 (坐标轴和标签已保留)
        title = Tex("(a_1+b_1\\sqrt{2})+(a_2+b_2\\sqrt{2})", font_size=28).move_to(UP * 3.5 + RIGHT * 6).set_color_by_tex_to_color_map({
            "a_1": RED, "a_2": RED,
            "b_1": GREEN, "b_2": GREEN,
        })
        title_2 = Tex("(a_1+a_2)+(b_1+b_2)\\sqrt{2}", font_size=28).set_color_by_tex_to_color_map({
            "a_1": RED, "a_2": RED,
            "b_1": GREEN, "b_2": GREEN,
        })
        title_2.match_x(title).match_y(title) # Ensure same position
        self.play(Write(title))
        self.wait(1)

        # 2.2 引入第一个加数 (P₁ = 2 + 3√2)
        a1, b1 = 2, 3
        p1_coord = axes_x.n2p(a1) + (axes_y.n2p(b1) - axes_y.n2p(0)) # 坐标

        vec1 = Vector(p1_coord, color=BLUE)
        dot1 = Dot(p1_coord, color=BLUE)
        # 3. 增强投影线视觉效果 (加法部分 - 添加投影点)
        lines1 = VGroup(
            DashedLine(p1_coord, axes_x.n2p(a1), color=BLUE),
            Dot(axes_x.n2p(a1), radius=0.05, color=BLUE),
            DashedLine(p1_coord, axes_y.n2p(b1), color=BLUE),
            Dot(axes_y.n2p(b1), radius=0.05, color=BLUE)
        )
        labels1 = VGroup(
            Tex(f"{a1}", font_size=24, color=BLUE).next_to(axes_x.n2p(a1), DOWN),
            Tex(f"{b1}\\sqrt{{2}}", font_size=24, color=BLUE).next_to(axes_y.n2p(b1), LEFT)
        )
        expr1 = Tex(f"{a1} + {b1}\\sqrt{{2}}", font_size=28, color=BLUE).next_to(dot1, UR).set_color_by_tex_to_color_map({
            f"{a1}": RED, f"{b1}": GREEN,
            "\\sqrt{2}": WHITE
        })

        self.play(
            GrowArrow(vec1),
            FadeIn(dot1),
            Write(lines1), # Use Write for VGroup
            Write(labels1),
            Write(expr1)
        )
        self.wait(1)

        # 2.3 引入第二个加数 (P₂ = 4 - 1√2)
        a2, b2 = 4, -1
        p2_coord = axes_x.n2p(a2) + (axes_y.n2p(b2) - axes_y.n2p(0)) # 二维坐标

        vec2 = Vector(p2_coord, color=GREEN)
        dot2 = Dot(p2_coord, color=GREEN)
        # 3. 增强投影线视觉效果 (加法部分 - 添加投影点)
        lines2 = VGroup(
            DashedLine(p2_coord, axes_x.n2p(a2), color=GREEN),
            Dot(axes_x.n2p(a2), radius=0.05, color=GREEN),
            DashedLine(p2_coord, axes_y.n2p(b2), color=GREEN),
            Dot(axes_y.n2p(b2), radius=0.05, color=GREEN)
        )
        labels2 = VGroup(
            Tex(f"{a2}", font_size=24, color=GREEN).next_to(axes_x.n2p(a2), DOWN),
            Tex(f"{b2:+}\\sqrt{{2}}", font_size=24, color=GREEN).next_to(axes_y.n2p(b2), LEFT) # 使用 {b2:+} 处理负号
        )
        expr2 = Tex(f"{a2} {b2:+}\\sqrt{{2}}", font_size=28, color=GREEN).next_to(dot2, UR).set_color_by_tex_to_color_map({
            f"{a2}": RED, f"{b2:+}": GREEN,
            "\\sqrt{2}": WHITE
        })
        expr2.shift(DOWN * 0.5)

        self.play(
            GrowArrow(vec2),
            FadeIn(dot2),
            Write(lines2),
            Write(labels2),
            Write(expr2)
        )
        self.wait(1)

        # 2.4 演示向量加法
        vec2_copy = vec2.copy()
        lines2_copy = lines2.copy()
        labels2_copy = labels2.copy()
        dot2_copy = dot2.copy()
        expr2_copy = expr2.copy()

        self.play(
            vec2_copy.animate.shift(vec1.get_end()), # Shift by vec1's vector value
            lines2_copy.animate.shift(vec1.get_end()),
            labels2_copy.animate.shift(vec1.get_end()),
            dot2_copy.animate.shift(vec1.get_end()),
            expr2_copy.animate.shift(vec1.get_end()),
            run_time=2
        )
        self.wait(0.5)

        # 2.5 显示加法结果 (P_add = 6 + 2√2)
        a_add, b_add = a1 + a2, b1 + b2
        p_add_coord = axes_x.n2p(a_add) + (axes_y.n2p(b_add) - axes_y.n2p(0)) # 二维坐标

        vec_add = Vector(p_add_coord, color=YELLOW)
        dot_add = Dot(p_add_coord, color=YELLOW)
        # 3. 增强投影线视觉效果 (加法部分 - 添加投影点)
        lines_add = VGroup(
            DashedLine(p_add_coord, axes_x.n2p(a_add), color=YELLOW),
            Dot(axes_x.n2p(a_add), radius=0.05, color=YELLOW),
            DashedLine(p_add_coord, axes_y.n2p(b_add), color=YELLOW),
            Dot(axes_y.n2p(b_add), radius=0.05, color=YELLOW)
        )
        labels_add = VGroup(
            Tex(f"{a_add}", font_size=24, color=YELLOW).next_to(axes_x.n2p(a_add), DOWN),
            Tex(f"{b_add}\\sqrt{{2}}", font_size=24, color=YELLOW).next_to(axes_y.n2p(b_add), LEFT)
        )
        expr_add = Tex(f"{a_add} + {b_add}\\sqrt{{2}}", font_size=28).next_to(dot_add, UR).set_color_by_tex_to_color_map({
            f"{a_add}": RED, f"{b_add}": GREEN,
            "\\sqrt{2}": WHITE
        })

        # Use Transform for labels for smoother transition
        self.play(
            GrowArrow(vec_add),
            FadeIn(dot_add),
            Write(lines_add),
            Transform(labels2_copy, labels_add), # Transform copied labels
            Write(expr_add),
            FadeOut(vec2_copy),
            FadeOut(lines2_copy), # Fade out original copied lines
            FadeOut(dot2_copy),
            FadeOut(expr2_copy)
        )
        self.remove(labels2_copy) # Remove the transformed label copy
        self.add(labels_add)      # Ensure the final label is added
        self.wait(1)
        self.play(
            TransformMatchingShapes(title, title_2),
        )
        self.wait(4)

        # --- 清理加法部分，准备三次扩域 ---
        self.play(
            FadeOut(vec_add), FadeOut(dot_add), FadeOut(lines_add), FadeOut(labels_add),
            FadeOut(expr_add), FadeOut(title_2),
            FadeOut(vec1), FadeOut(lines1), FadeOut(labels1), FadeOut(dot1),
            FadeOut(vec2), FadeOut(lines2), FadeOut(labels2), FadeOut(dot2),
            FadeOut(expr1), FadeOut(expr2),
            self.camera.frame.animate.shift(DOWN * 0.5 + LEFT), # Adjust camera view back
            # Keep axes and axis labels (q_label, x_labels, y_labels)
        )

        # 4. 相机视角和过渡 (平滑过渡 - Step 2: Rotate)
        self.play(self.camera.frame.animate.rotate(30 * DEGREES, RIGHT))
        self.play(
            self.camera.frame.animate.rotate(30 * DEGREES, OUT),
            self.camera.frame.animate.scale(1.2)
        )
        self.wait(1) # Wait after rotation

        # --- 三次扩域可视化 ---

        # 清除 Q√2 标签和 y 轴标签
        self.play(FadeOut(q_sqrt2_label), FadeOut(y_labels))

        q_sqrt3_2_label = Tex("\\mathbb{Q}\\cdot2^{\\frac{1}{3}}", font_size=30, color=WHITE).shift(UP * 5 + RIGHT * 0.5)
        q_sqrt3_2_2_label = Tex("\\mathbb{Q}\\cdot2^{\\frac{2}{3}}", font_size=30, color=WHITE).shift(OUT * 5 + LEFT * 0.5)

        # 定义新的 y 轴和 z 轴标签
        y_labels_cubic = VGroup()
        for i in range(-6, 7):
            if i == 0: continue
            label = Tex(str(i) + "\\times2^{\\frac{1}{3}}", font_size=24).next_to(axes_y.n2p(i), LEFT, buff=0.25)
            y_labels_cubic.add(label)

        # axes_z definition moved earlier

        z_labels_cubic = VGroup()
        for i in range(-8, 9): # Adjusted range
             if i == 0: continue
             # Position relative to Z axis. Need careful positioning in 3D.
             # Using shift relative to the point on the axis.
             label = Tex(str(i) + "\\times2^{\\frac{2}{3}}", font_size=24).next_to(axes_z.n2p(i), RIGHT, buff=0.25)
             z_labels_cubic.add(label)

        # 显示新的 y 轴坐标以及 z 轴
        self.play(
            Write(y_labels_cubic),
            Write(axes_z),
            Write(z_labels_cubic),
            Write(q_sqrt3_2_label),
            Write(q_sqrt3_2_2_label),
            lag_ratio=0.1
        )

        self.wait(2)

        # Removed unused cubic trackers
        # x_tracker_cubic = ValueTracker(0)
        # y_tracker_cubic = ValueTracker(0)
        # z_tracker_cubic = ValueTracker(0)

        # 创建数值显示 (三次扩域部分)
        x_display_cubic = DecimalNumber(0, num_decimal_places=3, include_sign=True, color=RED, font_size=36)
        y_display_cubic = DecimalNumber(0, num_decimal_places=3, include_sign=True, color=YELLOW, font_size=36)
        z_display_cubic = DecimalNumber(0, num_decimal_places=3, include_sign=True, color=GREEN, font_size=36)

        times_2_1_3 = Tex(r"\times2^{\frac{1}{3}}", font_size=36)
        times_2_2_3 = Tex(r"\times2^{\frac{2}{3}}", font_size=36)

        # 组合显示 (三次扩域部分)
        cubic_display_group = VGroup(
            x_display_cubic,
            y_display_cubic, times_2_1_3,
            z_display_cubic, times_2_2_3
        ).arrange(RIGHT, buff=0.1).to_corner(UR, buff=1) # Adjusted position

        # Brace & tag
        brace_x_cubic = Brace(x_display_cubic, UP, color=RED)
        brace_y_cubic = Brace(y_display_cubic, UP, color=YELLOW)
        brace_z_cubic = Brace(z_display_cubic, UP, color=GREEN)
        tag_x = Text("a", font_size=28).next_to(brace_x_cubic, UP).set_color(RED)
        tag_y = Text("b", font_size=28).next_to(brace_y_cubic, UP).set_color(YELLOW)
        tag_z = Text("c", font_size=28).next_to(brace_z_cubic, UP).set_color(GREEN)

        tagging_group_cubic = VGroup(
            tag_x, tag_y, tag_z,
            brace_x_cubic, brace_y_cubic, brace_z_cubic
        )

        # 创建新的红色小圆点 (三次扩域部分)
        cubic_dot = Circle(radius=0.08, color=RED, stroke_width=2, fill_opacity=0)
        # 初始位置将在动画部分设置

        # 定义原点
        origin_point = axes_x.n2p(0) # Assuming axes_x origin is the global origin

        # 3. 增强投影线的视觉效果 (Part 3 - 添加投影点)
        # 定义获取长方体边线和投影点的函数
        def get_cuboid_lines_and_dots(P, O):
            Px, Py, Pz = P[0], P[1], P[2]
            Ox, Oy, Oz = O[0], O[1], O[2] # Origin coords

            # Projection points onto planes and axes
            P_xy = np.array([Px, Py, Oz])
            P_xz = np.array([Px, Oy, Pz])
            P_yz = np.array([Ox, Py, Pz])
            P_x  = np.array([Px, Oy, Oz]) # Projection onto X-axis
            P_y  = np.array([Ox, Py, Oz]) # Projection onto Y-axis
            P_z  = np.array([Ox, Oy, Pz]) # Projection onto Z-axis

            lines = VGroup(
                # Lines from P
                DashedLine(P, P_xy, color=GREEN),
                DashedLine(P, P_xz, color=YELLOW),
                DashedLine(P, P_yz, color=RED),
                # Lines from plane projections to axis projections
                DashedLine(P_xy, P_x, color=RED), DashedLine(P_xy, P_y, color=YELLOW),
                DashedLine(P_xz, P_x, color=RED), DashedLine(P_xz, P_z, color=GREEN),
                DashedLine(P_yz, P_y, color=YELLOW), DashedLine(P_yz, P_z, color=GREEN),
            )
            dots = VGroup(
                Dot(P_x, radius=0.05, color=RED),    # X-axis projection dot
                Dot(P_y, radius=0.05, color=YELLOW), # Y-axis projection dot
                Dot(P_z, radius=0.05, color=GREEN),  # Z-axis projection dot
            )
            return VGroup(lines, dots)

        # 创建坐标投影虚线和点 (长方体)
        cubic_lines_dots_group = always_redraw(lambda: get_cuboid_lines_and_dots(cubic_dot.get_center(), origin_point))

        # 更新函数 (三次扩域部分 - 基于 get_center())
        def update_cubic_displays(mob): # mob is cubic_display_group
            current_pos = cubic_dot.get_center()

            # Project onto axes and convert
            x_proj_point = np.array([current_pos[0], axes_x.n2p(0)[1], axes_x.n2p(0)[2]])
            x_val = axes_x.p2n(x_proj_point)

            y_axis_origin = axes_y.n2p(0)
            y_axis_unit_vec = axes_y.n2p(1) - y_axis_origin
            point_vec_y = current_pos - y_axis_origin
            y_val = np.dot(point_vec_y, y_axis_unit_vec) / np.dot(y_axis_unit_vec, y_axis_unit_vec)

            # Correct Z value calculation based on Z-axis orientation
            z_axis_origin = axes_z.n2p(0)
            z_axis_unit_vec = axes_z.n2p(1) - z_axis_origin # Vector along Z axis
            point_vec_z = current_pos - z_axis_origin
            # Project point_vec_z onto z_axis_unit_vec
            z_val = np.dot(point_vec_z, z_axis_unit_vec) / np.dot(z_axis_unit_vec, z_axis_unit_vec)


            x_display_cubic.set_value(x_val)
            y_display_cubic.set_value(y_val)
            z_display_cubic.set_value(z_val)

            # Removed unused tracker updates
            # x_tracker_cubic.set_value(x_val)
            # y_tracker_cubic.set_value(y_val)
            # z_tracker_cubic.set_value(z_val)

            mob.to_corner(UR, buff=1) # 保持在角落

        # 5. 恢复三维路径 (Part 3 - 使用原始 get_path_point)
        cubic_dot.move_to(get_path_point(0, include_z=True)) # Set initial position

        # 添加三次扩域对象到场景
        self.play(
            FadeIn(cubic_dot),
            FadeIn(cubic_lines_dots_group), # Use new group with lines and dots
            Write(cubic_display_group),
            Write(tagging_group_cubic),
            run_time=1.5
        )

        # 添加更新器 (Part 3 - 恢复 updater)
        cubic_dot.add_updater(lambda mob: mob.move_to(get_path_point(t_tracker.get_value(), include_z=True)))
        cubic_display_group.add_updater(update_cubic_displays)

        def camera_shift(t):
            if t < 4.5:
                return 0.01 * LEFT * t * (4.5 - t)
            elif t < 8:
                return 0.0225 * RIGHT * (8 - t) * (t - 4.5)
            else:
                return ORIGIN

        self.camera.frame.add_updater(lambda m: m.shift(camera_shift(t_tracker.get_value())))

        # 5. 恢复三维路径 (Part 3 - 运行动画)
        # Reset t_tracker before animation
        t_tracker.set_value(0)
        self.play(
            t_tracker.animate.set_value(8), # Drive t from 0 to 8
            run_time=12,
            rate_func=smooth
        )

        # 清理更新器 (Part 3)
        cubic_dot.clear_updaters()
        # always_redraw group doesn't need clearing
        cubic_display_group.clear_updaters()
        
        self.camera.frame.clear_updaters() # Clear camera updater

        self.wait(3)

        # 清理三次扩域对象
        # 伪清除
        self.remove(cubic_lines_dots_group) # Remove the lines and dots group
        temp_group = get_cuboid_lines_and_dots(cubic_dot.get_center(), origin_point)
        self.add(temp_group)
        self.play(
            FadeOut(cubic_dot),
            FadeOut(cubic_display_group),
            FadeOut(temp_group),
            FadeOut(tagging_group_cubic),
        )
        self.wait(1)

        # Final cleanup (optional: fade out axes etc.)
        self.play(
            Uncreate(axes_x), Uncreate(axes_y), Uncreate(axes_z),
            Uncreate(x_labels), Uncreate(y_labels_cubic), Uncreate(z_labels_cubic),
            Uncreate(q_label), Uncreate(q_sqrt3_2_label), Uncreate(q_sqrt3_2_2_label),
        )
        self.wait(2)
