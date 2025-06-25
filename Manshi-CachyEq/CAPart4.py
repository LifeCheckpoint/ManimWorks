from manimlib import *
import numpy as np
import sys
sys.path.append(".")
from phy_cube import ManimPybulletSimulator, SHAPE_TYPE_BOX, SHAPE_TYPE_PLANE

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

        tex = tex_f_x_eq_fafbfc_final = Tex("f(x) = \\frac{a}{n}\\cdot f\\left(1\\right) + \\frac{b}{n}\\cdot f\\left(\\pi\\right) + \\frac{c}{n}\\cdot f\\left(\\sqrt{2}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{a}{n}\\cdot ": RED_A,
            "\\frac{b}{n}\\cdot ": GREEN_A,
            "\\frac{c}{n}\\cdot ": BLUE_A,
            "1": RED_A,
            "\\pi": GREEN_A,
            "\\sqrt{2}": BLUE_A,
            "(x) =": WHITE
        }).move_to(UP * 1)
        self.add(tex)
        debugTeX(self, tex)

def extract_xz_plane_rotation_angle(quat_manim: np.ndarray) -> float:
    """
    Extracts the rotation angle around the Manim Y-axis (UP)
    from a Manim-coordinate quaternion (x, y, z, w).
    This corresponds to the rotation in the XZ plane (ground plane).
    """
    x, y, z, w = quat_manim
    angle = math.atan2(2*x*z + 2*y*w, 1 - 2*y*y - 2*z*z)
    return angle

class CAPart4_1(Scene):
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
        self.wait(1)
        self.play(Write(tex_cauchy, run_time=1.5))
        self.wait(1)

        balancer = SVGMobject("balancer.svg").move_to(DOWN * 8.05).scale(2.75).set_opacity(0.75)
        fama_red = SVGMobject("fama.svg").scale(0.25).set_color(RED_A)
        fama_green = SVGMobject("fama.svg").scale(0.25).set_color(GREEN_A)
        fama_blue = SVGMobject("fama.svg").scale(0.25).set_color(BLUE_A)
        tex_1 = Tex("1").set_color(RED_A)
        tex_pi = Tex("\\pi").set_color(GREEN_A)
        tex_sq2 = Tex("\\sqrt{2}").set_color(BLUE_A)
        tex_eq = Tex("=")
        group_fama_1 = VGroup(fama_red, tex_eq.copy(True), tex_1).arrange(RIGHT, buff=0.2).move_to(UP * 1 + LEFT * 2.5)
        group_fama_pi = VGroup(fama_green, tex_eq.copy(True), tex_pi).arrange(RIGHT, buff=0.2).move_to(UP * 1 + LEFT * 0.5)
        group_fama_sq2 = VGroup(fama_blue, tex_eq.copy(True), tex_sq2).arrange(RIGHT, buff=0.2).move_to(UP * 1 + RIGHT * 1.5)

        self.play(
            Write(group_fama_1, lag_ratio=0.2),
        )
        self.play(
            Write(group_fama_pi, lag_ratio=0.2),
        )
        self.play(
            Write(group_fama_sq2, lag_ratio=0.2),
        )
        self.wait(2)
        self.add(balancer)
        self.wait(0.5)
        self.play(
            balancer.animate.move_to(DOWN * 2.3),
            group_fama_1.animate.scale(0.8).move_to(LEFT * 6.5 + UP * 2.5, aligned_edge=LEFT),
            group_fama_pi.animate.scale(0.8).move_to(LEFT * 6.5 + UP * 2, aligned_edge=LEFT),
            group_fama_sq2.animate.scale(0.8).move_to(LEFT * 6.5 + UP * 1.5, aligned_edge=LEFT),
            rate_func=exponential_decay,
            run_time=2
        )
        
        # stimulate the dropping of fama
        self.play(balancer.animate.set_opacity(0.2))
        def update_manim_objects(mob):
            self.simulator.update_simulation(self.time)
            current_states = self.simulator.get_states()

            for name, state in current_states.items():
                if name in self.manim_objects:
                    manim_obj = self.manim_objects[name]
                    manim_obj: Mobject

                    manim_obj.move_to(state['pos'])
                    # angle_2d = extract_xz_plane_rotation_angle(state['quat'])
                    # manim_obj.rotate(angle_2d, axis=OUT)

        self.simulator = ManimPybulletSimulator(sim_time_step=1.0/240.0)
        ground_y_axis = -3.2
        ground_balancers = [
            self.simulator.add_body(
                name="balancer0",
                shape_type=SHAPE_TYPE_PLANE,
                mass=0, # static
                initial_pos_manim=np.array([0, ground_y_axis, 0]),
                restitution=0.3
            ),
        ]
        self.manim_objects = {
            ground_balancer: VMobject() for ground_balancer in ground_balancers
        }

        self.camera.frame.add_updater(update_manim_objects)
        self.wait(0.2)

        # little squares
        little_square_n = 6
        little_square_size = [0.2] * 3
        little_square_names = []
        little_square_manim = []
        for index in range(little_square_n):
            little_square_rotates = random.uniform(0, 1)
            pos = np.array([-3 + random.uniform(-0.05, 0.05), 2, 0])
            little_square_names.append(self.simulator.add_body(
                name="little_square_" + str(index),
                shape_type=SHAPE_TYPE_BOX,
                size=little_square_size,
                mass=1.0,
                initial_pos_manim=pos,
                initial_quat_manim=np.array([little_square_rotates, 0, 0, little_square_rotates]),
                restitution=0.2
            ))
            little_square_manim.append(VGroup(
                Square(side_length=0.4).rotate(
                    extract_xz_plane_rotation_angle([little_square_rotates, 0, 0, little_square_rotates]),
                    axis=OUT
                ).set_color(WHITE).move_to(pos),
                Tex("x").scale(0.7).move_to(pos)
            ))

            self.manim_objects = self.manim_objects | {little_square_names[-1]: little_square_manim[-1]}
            self.add(little_square_manim[-1])
            self.wait(0.25)

        self.wait(0.5)

        # famas
        fama_abc = {"a": 3, "b": 5, "c": 2}
        fama_manim = []
        fama_names = []
        for fama_type in fama_abc.keys():
            for index in range(fama_abc[fama_type]):
                base_delta = {"a": -0.5, "b": 0, "c": 0.5}[fama_type]
                pos = np.array([3 + base_delta + random.uniform(-0.025, 0.025), 2, 0])
                fama_obj = VGroup(fama_red.copy(True)).set_color({
                    "a": RED_A,
                    "b": GREEN_A,
                    "c": BLUE_A
                }[fama_type]).move_to(pos)
                fama_names.append(self.simulator.add_body(
                    name="fama_" + fama_type + str(index),
                    shape_type=SHAPE_TYPE_BOX,
                    size=[fama_obj.get_width() / 2, fama_obj.get_height() / 2, fama_obj.get_height() / 2],
                    mass=1.0,
                    initial_pos_manim=pos,
                    restitution=0.1
                ))
                fama_manim.append(fama_obj)

                self.manim_objects = self.manim_objects | {fama_names[-1]: fama_obj[-1]}
                self.add(fama_obj[-1])
                self.wait(0.25)
                
        tex_left_n = Tex("n=6").set_color(WHITE).move_to(LEFT * 3 + DOWN * 0.5).scale(0.8)
        tex_fama_1_num = Tex("a=3").set_color(RED_A).move_to(-1.8 * UP + RIGHT * 2.4).scale(0.5)
        tex_fama_pi_num = Tex("b=5").set_color(GREEN_A).move_to(UP * -1 + RIGHT * 3).scale(0.5)
        tex_fama_sq2_num = Tex("c=2").set_color(BLUE_A).move_to(UP * -2.2 + RIGHT * 3.6).scale(0.5)
        group_famas = VGroup(
            VGroup(*fama_manim), tex_fama_1_num, tex_fama_pi_num, tex_fama_sq2_num
        )
        group_squares = VGroup(
            *little_square_manim, tex_left_n
        )
        tex_nx_eq_abc = Tex("nx = a\\cdot 1 + b\\cdot \\pi + c\\cdot \\sqrt{2}").set_color_by_tex_to_color_map({
            "a\\cdot 1": RED_A,
            "b\\cdot \\pi": GREEN_A,
            "c\\cdot \\sqrt{2}": BLUE_A,
            "nx =": WHITE
        }).move_to(UP * 1)
        tex_nx_eq_abc_new1 = Tex("nx + a\\cdot 1 = b\\cdot \\pi + c\\cdot \\sqrt{2}").set_color_by_tex_to_color_map({
            "a\\cdot 1": RED_A,
            "b\\cdot \\pi": GREEN_A,
            "c\\cdot \\sqrt{2}": BLUE_A,
            "nx +": WHITE
        }).move_to(UP * 1)
        tex_nx_eq_abc_new2 = Tex("nx + a\\cdot 1 + b\\cdot \\pi = c\\cdot \\sqrt{2}").set_color_by_tex_to_color_map({
            "a\\cdot 1": RED_A,
            "b\\cdot \\pi": GREEN_A,
            "c\\cdot \\sqrt{2}": BLUE_A,
            "nx +": WHITE
        }).move_to(UP * 1)
        tex_nx_plus_abc_eq_0 = Tex("nx + a\\cdot 1 + b\\cdot \\pi + c\\cdot \\sqrt{2} = 0").set_color_by_tex_to_color_map({
            "a\\cdot 1": RED_A,
            "b\\cdot \\pi": GREEN_A,
            "c\\cdot \\sqrt{2}": BLUE_A,
            "nx +": WHITE,
            " = 0": WHITE
        }).move_to(UP * 1)
        tex_nx_eq_minus_abc = Tex("nx = -a\\cdot 1 + -b\\cdot \\pi + -c\\cdot \\sqrt{2}").set_color_by_tex_to_color_map({
            "-a\\cdot 1": RED_A,
            "-b\\cdot \\pi": GREEN_A,
            "-c\\cdot \\sqrt{2}": BLUE_A,
            "nx =": WHITE
        }).move_to(UP * 1)
        tex_nx_eq_abc_new = tex_nx_eq_abc.copy(True)
        tex_x_eq_abc = Tex("x = \\frac{a}{n}\\cdot 1 + \\frac{b}{n}\\cdot \\pi + \\frac{c}{n}\\cdot \\sqrt{2}").set_color_by_tex_to_color_map({
            "\\frac{a}{n}\\cdot 1": RED_A,
            "\\frac{b}{n}\\cdot \\pi": GREEN_A,
            "\\frac{c}{n}\\cdot \\sqrt{2}": BLUE_A,
            "x =": WHITE
        }).move_to(UP * 1)
        text_linear_combination = Text("线性组合", font="微软雅黑").move_to(UP * 1.85).scale(0.8).set_color_by_text_to_color_map(
            {
                "线性": YELLOW,
                "组合": WHITE
            }
        )
        tex_q_linear_combination = Text("有理线性组合", font="微软雅黑").move_to(UP * 1.85).scale(0.8).set_color_by_text_to_color_map(
            {
                "有理": BLUE,
                "线性": YELLOW,
                "组合": WHITE
            }
        )
        tex_f_x_eq_f_abc = Tex("f(x) = f\\left(\\frac{a}{n}\\cdot 1 + \\frac{b}{n}\\cdot \\pi + \\frac{c}{n}\\cdot \\sqrt{2}\\right)").set_color_by_tex_to_color_map({
            "\\frac{a}{n}\\cdot 1": RED_A,
            "\\frac{b}{n}\\cdot \\pi": GREEN_A,
            "\\frac{c}{n}\\cdot \\sqrt{2}": BLUE_A,
            "f": BLUE,
            "x =": WHITE
        }).move_to(UP * 1)
        tex_f_x_eq_fafbfc = Tex("f(x) = f\\left(\\frac{a}{n}\\cdot 1\\right) + f\\left(\\frac{b}{n}\\cdot \\pi\\right) + f\\left(\\frac{c}{n}\\cdot \\sqrt{2}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{a}{n}\\cdot 1": RED_A,
            "\\frac{b}{n}\\cdot \\pi": GREEN_A,
            "\\frac{c}{n}\\cdot \\sqrt{2}": BLUE_A,
            "(x) =": WHITE
        }).move_to(UP * 1)
        tex_f_x_eq_fafbfc_final = Tex("f(x) = \\frac{a}{n}\\cdot f\\left(1\\right) + \\frac{b}{n}\\cdot f\\left(\\pi\\right) + \\frac{c}{n}\\cdot f\\left(\\sqrt{2}\\right)").set_color_by_tex_to_color_map({
            "f": BLUE,
            "\\frac{a}{n}\\cdot ": RED_A,
            "\\frac{b}{n}\\cdot ": GREEN_A,
            "\\frac{c}{n}\\cdot ": BLUE_A,
            "1": RED_A,
            "\\pi": GREEN_A,
            "\\sqrt{2}": BLUE_A,
            "(x) =": WHITE
        }).move_to(UP * 1)
        recs_hl_final = VGroup(
            SurroundingRectangle(VGroup(*tex_f_x_eq_fafbfc_final[9: 13]), color=RED_A, buff=0.05),
            SurroundingRectangle(VGroup(*tex_f_x_eq_fafbfc_final[18: 22]), color=GREEN_A, buff=0.05),
            SurroundingRectangle(VGroup(*tex_f_x_eq_fafbfc_final[27: ]), color=BLUE_A, buff=0.05)
        )

        self.wait(1)
        self.play(
            Write(VGroup(
                tex_left_n,
                tex_fama_1_num, 
                tex_fama_pi_num,
                tex_fama_sq2_num
            ), lag_ratio=0.2),
            run_time=1.5
        )
        self.camera.frame.remove_updater(update_manim_objects)
        self.wait(1)
        self.play(Write(tex_nx_eq_abc))
        self.wait(2)
        sqauare_g_down, fama_g_down = group_squares.get_bottom(), group_famas.get_bottom()
        # move famas
        famas_a_group = VGroup(group_famas[0][0:fama_abc["a"]])
        famas_b_group = VGroup(group_famas[0][fama_abc["a"]:fama_abc["a"] + fama_abc["b"]])
        famas_c_group = VGroup(group_famas[0][fama_abc["a"] + fama_abc["b"]:])
        famas_a_pos = np.array(famas_a_group.get_center())
        famas_b_pos = np.array(famas_b_group.get_center())
        famas_c_pos = np.array(famas_c_group.get_center())
        famas_a_label_pos = np.array(group_famas[1].get_center())
        famas_b_label_pos = np.array(group_famas[2].get_center())
        famas_c_label_pos = np.array(group_famas[3].get_center())
        self.play(
            group_squares.animate.shift(LEFT * 0.7),
            famas_a_group.animate.move_to(sqauare_g_down + RIGHT * 0.4, aligned_edge=DOWN),
            FadeOut(group_famas[1]),
            TransformMatchingTex(
                tex_nx_eq_abc, tex_nx_eq_abc_new1,
                path_arc=PI/2, run_time=1.5
            )
        )
        group_famas[1].next_to(famas_a_group, UP)
        self.play(FadeIn(group_famas[1], shift=DOWN * 0.5))
        self.wait(1)
        self.play(
            famas_a_group.animate.shift(LEFT * 0.5),
            group_famas[1].animate.shift(LEFT * 0.5),
            famas_b_group.animate.move_to(sqauare_g_down + RIGHT * 0.4, aligned_edge=DOWN),
            FadeOut(group_famas[2]),
            TransformMatchingTex(
                tex_nx_eq_abc_new1, tex_nx_eq_abc_new2,
                path_arc=PI/2, run_time=1.5
            )
        )
        group_famas[2].next_to(famas_b_group, UP)
        self.play(FadeIn(group_famas[2], shift=DOWN * 0.5))
        self.wait(1)
        self.play(
            famas_a_group.animate.shift(LEFT * 0.2),
            group_famas[1].animate.shift(LEFT * 0.2),
            famas_b_group.animate.shift(LEFT * 0.2),
            group_famas[2].animate.shift(LEFT * 0.2),
            famas_c_group.animate.move_to(sqauare_g_down + RIGHT * 0.7, aligned_edge=DOWN),
            FadeOut(group_famas[3]),
            TransformMatchingTex(
                tex_nx_eq_abc_new2, tex_nx_plus_abc_eq_0,
                path_arc=PI/2, run_time=1.5
            )
        )
        group_famas[3].next_to(famas_c_group, UP)
        self.play(FadeIn(group_famas[3], shift=DOWN * 0.5))
        self.wait(1.5)
        self.play(
            TransformMatchingTex(
                tex_nx_plus_abc_eq_0, tex_nx_eq_minus_abc,
                path_arc=PI/2, run_time=1.5
            )
        )
        self.wait(2)
        self.play(
            group_squares.animate.shift(RIGHT * 0.7),
            famas_a_group.animate.move_to(famas_a_pos),
            famas_b_group.animate.move_to(famas_b_pos),
            famas_c_group.animate.move_to(famas_c_pos),
            group_famas[1].animate.move_to(famas_a_label_pos),
            group_famas[2].animate.move_to(famas_b_label_pos),
            group_famas[3].animate.move_to(famas_c_label_pos),
            TransformMatchingTex(
                tex_nx_eq_minus_abc, tex_nx_eq_abc_new,
                path_arc=PI/2, run_time=1.5
            )
        )
        self.camera.frame.add_updater(update_manim_objects)
        self.wait(2.5)
        self.play(TransformMatchingTex(
            tex_nx_eq_abc_new, tex_x_eq_abc,
            path_arc=PI/2, run_time=1.5
        ))
        self.wait(1.5)
        tex_typing_animate(self, text_linear_combination)
        self.wait(1.5)
        self.play(TransformMatchingStrings(text_linear_combination, tex_q_linear_combination, path_arc=PI/2, run_time=1.5))
        self.wait(2)
        self.play(
            FadeOut(tex_q_linear_combination, shift=UP * 0.5),
        )
        self.wait(1)
        self.play(WiggleOutThenIn(tex_cauchy))
        self.wait(1)
        self.play(TransformMatchingTex(tex_x_eq_abc, tex_f_x_eq_f_abc, path_arc=PI/2, run_time=1.5))
        self.wait(1.5)
        self.play(TransformMatchingTex(tex_f_x_eq_f_abc, tex_f_x_eq_fafbfc, path_arc=PI/2, run_time=1.5))
        self.wait(1.5)
        self.play(TransformMatchingTex(tex_f_x_eq_fafbfc, tex_f_x_eq_fafbfc_final, path_arc=PI/2, run_time=1.5))
        self.wait(1.5)
        self.play(
            Write(recs_hl_final, lag_ratio=0.2),
            run_time=2
        )
        self.wait(1)
        self.play(
            Uncreate(recs_hl_final, lag_ratio=0.1),
        )
        self.wait(2.5)
        
        self.play(FadeOut(VGroup(
            group_fama_1, group_fama_pi, group_fama_sq2,
            tex_left_n, tex_fama_1_num, tex_fama_pi_num, tex_fama_sq2_num,
            tex_f_x_eq_fafbfc_final
        )))
        
        # many famas
        # famas
        for index in range(25):
            base_delta = random.uniform(-0.6, 0.6)
            pos = np.array([3 + base_delta, 2, 0])
            fama_obj = VGroup(fama_red.copy(True)).set_color(
                random.choice([RED_A, BLUE_A, GREEN_A, YELLOW_A, PURPLE_A, ORANGE, GREY_A, TEAL_A, LIGHT_PINK, WHITE])
            ).move_to(pos)
            fama_names.append(self.simulator.add_body(
                name="fama2_" + str(index),
                shape_type=SHAPE_TYPE_BOX,
                size=[fama_obj.get_width() / 2, fama_obj.get_height() / 2, fama_obj.get_height() / 2],
                mass=1.0,
                initial_pos_manim=pos,
                restitution=0
            ))
            fama_manim.append(fama_obj)

            self.manim_objects = self.manim_objects | {fama_names[-1]: fama_obj[-1]}
            self.add(fama_obj[-1])
            self.wait(0.10)
        self.wait(2)
        self.camera.frame.remove_updater(update_manim_objects)

        color_set = [RED_A, BLUE_A, GREEN_A, YELLOW_A, PURPLE_A, ORANGE, GREY_A, TEAL_A, LIGHT_PINK, WHITE]
        random_color = lambda: random.choice(color_set)
        fama_limited_num = 15
        limit_fama_objs = [VGroup(fama_red.copy(True)).set_color(random_color()) for _ in range(fama_limited_num)]
        tex_dots = Tex("\\cdots").set_color(WHITE)
        limit_fama_objs.append(tex_dots)
        group_limited_famas = VGroup(*limit_fama_objs).arrange_in_grid(n_rows=1, buff=0.07).scale(1.5)
        tex_list_bi = [Tex("b_{" + str(i) + "}").scale(0.6) for i in range(len(group_limited_famas) - 1)]
        tex_list_bi.append(tex_dots.copy(True).scale(0.57))
        group_limited_famas_label = VGroup(*tex_list_bi).arrange(RIGHT, buff=0.215).scale(1.8).next_to(group_limited_famas, DOWN, buff=0.1)
        # re arrange
        for i in range(len(group_limited_famas) - 1):
            group_limited_famas_label[i].move_to(group_limited_famas[i].get_bottom() + DOWN * 0.35)
        for i, label in enumerate(group_limited_famas_label[:-1]):
            label.set_color(group_limited_famas[i].get_color())
        tex_x_eq_q1b1 = Tex("x = q_1 b_1 + q_2 b_2 + \\cdots + q_n b_n").set_color_by_tex_to_color_map({
            "q_1 b_1": RED_A,
            "q_2 b_2": GREEN_A,
            "q_n b_n": BLUE_A,
            "x =": WHITE
        }).move_to(DOWN * 1.5)
        tex_RR = Tex("\\mathbb{R}").set_color(YELLOW).move_to(DOWN + LEFT * 1)
        tex_QQ = Tex("\\mathbb{Q}").set_color(LIGHT_PINK).move_to(DOWN + RIGHT * 1)
        arrow_R2Q = Arrow(
            start=tex_RR.get_right(),
            end=tex_QQ.get_left(),
            buff=0.1, color=WHITE
        )
        text_hamel_basis = Text("Hamel 基", font="微软雅黑").move_to(arrow_R2Q.get_center()).scale(0.6).set_color_by_text_to_color_map({
            "Hamel": LIGHT_PINK,
            "基": WHITE
        })
        
        self.play(
            TransformMatchingShapes(VGroup(*fama_manim), group_limited_famas),
            VGroup(*little_square_manim).animate.set_opacity(0.1),
            balancer.animate.set_opacity(0.1),
            run_time=1.5,
        )
        self.wait(1.5)
        self.play(
            Write(group_limited_famas_label, run_time=1.5),
        )
        self.wait(1.5)
        self.play(Write(tex_x_eq_q1b1, run_time=1.5))
        self.wait(2)
        self.play(
            FadeOut(VGroup(
                group_limited_famas, *little_square_manim, balancer
            )),
            tex_x_eq_q1b1.animate.shift(UP * 1.5),
            group_limited_famas_label.animate.shift(UP * 1.5),
            run_time=1.5
        )
        self.wait(0.5)
        self.play(Write(tex_RR))
        self.wait(1)
        self.play(Write(tex_QQ))
        self.wait(0.5)
        self.play(Write(arrow_R2Q))
        self.wait(1.5)
        self.play(
            arrow_R2Q.animate.shift(DOWN * 0.3),
            tex_RR.animate.shift(DOWN * 0.15),
            tex_QQ.animate.shift(DOWN * 0.15),
            Write(text_hamel_basis),
            run_time=1.5
        )
        self.wait(2)
        
        # choose 1, 4, 6 to show the Hamel basis
        recs_146 = VGroup(
            SurroundingRectangle(group_limited_famas_label[i], color=YELLOW, buff=0.05) for i in [1, 4, 6]
        )
        group_label146 = VGroup(
            group_limited_famas_label[1].copy(True),
            group_limited_famas_label[4].copy(True),
            group_limited_famas_label[6].copy(True)
        )
        tex_146_p123 = Tex("q_1 b_1 + q_4 b_4 + q_6 b_6")

        self.play(Write(recs_146))
        self.wait(1)
        self.play(FadeOut(recs_146))
        self.wait(1)
        self.add(group_label146)
        self.play(
            FadeOut(group_limited_famas_label),
            FadeOut(tex_x_eq_q1b1),
            FadeOut(VGroup(tex_RR, tex_QQ, arrow_R2Q, text_hamel_basis)),
            group_label146.animate.arrange_in_grid(n_rows=1, buff=0.6).move_to(ORIGIN)
        )
        self.wait(1.5)
        self.play(ReplacementTransform(group_label146, tex_146_p123))
        self.wait(1.5)
        self.play(FadeOut(tex_cauchy), FadeOut(tex_146_p123))

class CAPart4_2(Scene):
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
        self.wait(1)
        self.play(Write(tex_cauchy, run_time=1.5))
        self.wait(1)

        tex_x_eq_sum_qb = Tex("x = \\sum_{i=1}^{n} q_i b_i").set_color_by_tex_to_color_map({
            "x =": WHITE,
            "\\sum_{i=1}^{n}": WHITE,
            "q_i": LIGHT_PINK,
            "b_i": RED_A
        }).move_to(UP * 1.5)
        tex_fx_eq_sum_fqb = Tex("f(x) = \\sum_{i=1}^{n} q_i f(b_i)").set_color_by_tex_to_color_map({
            "f(x) =": WHITE,
            "\\sum_{i=1}^{n}": WHITE,
            "q_i": LIGHT_PINK,
            "f": BLUE,
            "b_i": RED_A
        }).move_to(UP * 1.5)
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
        axes.set_opacity(0.2)
        rec_plot = Rectangle(width=20, height=20, color=YELLOW_B).set_opacity(0.1)
        tex_image_set = Tex("\\{ (x,f(x)) | x \\in \\mathbb{R} \\}").move_to(DOWN)
        tex_image_set[2].set_color(RED)
        tex_image_set[4].set_color(BLUE)
        tex_image_set[6].set_color(RED)
        tex_image_set[10].set_color(RED)
        tex_image_set[12].set_color(YELLOW)
        tex_center = Tex("+").set_color(GREEN)
        quat_arc = Circle(radius=0.1).set_color(GREY_A).set_opacity(0)
        dots_in_arc = VGroup()
        ras = [1 / i for i in range(1, 21)] + [0.01]
        for r in ras:
            for angle in np.arange(0 + r * 0.5, 2 * PI + r * 0.5, PI / 20):
                dot = Dot(
                    radius=0.015,
                ).set_color(YELLOW).move_to(axes.c2p(3, 2.5) + r * np.array([np.cos(angle), np.sin(angle), 0]))
                dots_in_arc.add(dot)

        self.play(Write(tex_x_eq_sum_qb))
        self.wait(2)
        self.play(TransformMatchingTex(
            tex_x_eq_sum_qb, tex_fx_eq_sum_fqb,
            path_arc=PI/2, run_time=1.5
        ))
        self.wait(1.5)
        self.play(
            Write(axes)
        )
        self.play(Write(rec_plot))
        self.wait(1.5)
        self.play(
            Write(tex_image_set)
        )
        self.wait(2)
        self.play(Write(tex_center))
        self.wait(0.5)
        self.play(
            tex_center.animate.move_to(axes.c2p(3, 2.5)),
        )
        quat_arc.move_to(axes.c2p(3, 2.5))
        self.wait(1.5)
        now = self.time
        self.camera.frame.add_updater(
            lambda frame: frame.shift((RIGHT + UP) * animate_shift_smooth(now, self.time, 2, 0.023, "pos"))
        )
        self.play(
            quat_arc.animate.set_stroke(opacity=1).scale(11),
        )
        self.play(
            quat_arc.animate.rotate(2 * PI, about_point=axes.c2p(3, 2.5)),
            Write(dots_in_arc, lag_ratio=0.1),
            run_time=2.0
        )
        self.wait(1.5)
        self.camera.frame.clear_updaters()
        now = self.time
        self.camera.frame.add_updater(
            lambda frame: frame.shift((LEFT + DOWN) * animate_shift_smooth(now, self.time, 2, 0.023, "pos"))
        )
        self.play(
            FadeOut(dots_in_arc, lag_ratio=0.1),
            quat_arc.animate.set_opacity(0).scale(0.1),
            FadeOut(tex_center),
        )
        self.wait(1)
        self.play(
            FadeOut(tex_image_set, shift=UP * 0.5),
            FadeOut(axes, shift=UP * 0.5),
            FadeOut(rec_plot, shift=UP * 0.5),
            FadeOut(tex_fx_eq_sum_fqb, shift=UP * 0.5),
        )
        self.wait(1)

class CAPart4_3(Scene):
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
        self.add(tex_cauchy)
        self.wait(1)

        text_axiom_of_choice = Text("选择公理", font="微软雅黑").move_to(UP * 2.5).scale(0.8).set_color_by_text_to_color_map({
            "选择": YELLOW,
            "公理": WHITE
        }).move_to(UP * 0.5)
        group_sets = VGroup()
        choice_indexes = []
        choice_rects_from = VGroup()
        choice_rects_to = VGroup()
        color = [RED_A, GREEN_A, BLUE_A, YELLOW_A, PURPLE_A, ORANGE, GREY_A, TEAL_A, LIGHT_PINK, WHITE]
        n_rows = 15
        n_cols = 12
        for i in range(n_rows * n_cols):
            elem_num = random.randint(2, 5)
            elems = []
            choice_indexes.append(random.randint(0, elem_num - 1))
            for j in range(elem_num):
                elem_name_1 = random.choice(list(enumerate(["A", "B", "C", "D", "E", "F", "G", "H"])))
                elem_name_2 = str(random.randint(1, 9))
                elem_name = elem_name_1[1] + "_" + elem_name_2
                elem_color = color[elem_name_1[0] % len(color)]
                elems.append((elem_name, elem_color))
            set_str = ", ".join([f"{elem_name}" for elem_name, _ in elems])
            set_tex = Tex(set_str).set_color_by_tex_to_color_map({
                elem_name: elem_color for elem_name, elem_color in elems
            })
            left_brace = Tex("\\{").move_to(set_tex.get_left() + LEFT * 0.2)
            right_brace = Tex("\\}").move_to(set_tex.get_right() + RIGHT * 0.2)
            group_sets.add(VGroup(
                left_brace,
                set_tex,
                right_brace,
            ).scale(0.7))
        group_sets.arrange_in_grid(n_rows=n_rows, n_cols=n_cols, buff=0.45).set_opacity(0.8)
        for i, tex_group in enumerate(group_sets):
            set_tex = tex_group[1]
            # (0,1) -> 1; (3,4) -> 2; ...; (3k, 3k+1) -> k+1
            choice_rects_from.add(SurroundingRectangle(
                VGroup(set_tex[0], set_tex[1]), 
                color=YELLOW, 
                buff=0.04,
                stroke_width=1
            ))
            choice_rects_to.add(SurroundingRectangle(
                VGroup(set_tex[3 * choice_indexes[i]], set_tex[3 * choice_indexes[i] + 1]), 
                color=BLUE, 
                buff=0.04,
                stroke_width=1
            ))
        group_chosen_sets = VGroup()
        for i, tex_group in enumerate(group_sets):
            set_tex = tex_group[1]
            group_chosen_sets.add(VGroup(set_tex[3 * choice_indexes[i]], set_tex[3 * choice_indexes[i] + 1]))
        group_chosen_sets = group_chosen_sets.copy(True)

        tex_typing_animate(self, text_axiom_of_choice)
        self.wait(1.5)
        now = self.time
        self.camera.frame.add_updater(
            lambda frame: frame.scale(animate_scaling_exponential_decay(now, self.time, 3, 1, 0.002, "out")),
        )
        self.play(
            FadeOut(tex_cauchy),
            Write(group_sets, lag_ratio=0.1),
            run_time=3,
        )
        self.wait(1.5)
        self.play(
            Write(choice_rects_from, lag_ratio=0.1),
            run_time=2,
        )
        self.wait(1)
        self.play(
            *[ReplacementTransform(choice_rects_from[i], choice_rects_to[i]) for i in range(len(choice_rects_from))],
        )
        self.wait(1.5)
        self.add(group_chosen_sets)
        self.play(
            text_axiom_of_choice.animate.move_to(UP * 3.5).scale(1.1),
            FadeOut(group_sets),
            Uncreate(choice_rects_to),
            group_chosen_sets.animate.arrange_in_grid(n_rows=n_rows, n_cols=n_cols, buff=0.25).set_opacity(1).move_to(DOWN * 1),
            run_time=2
        )
        self.wait(0.5)

        big_braces = VGroup(
            Brace(group_chosen_sets, LEFT, buff=0.1),
            Brace(group_chosen_sets, RIGHT, buff=0.1)
        )

        self.play(Write(big_braces))
        self.wait(1.5)

        shelfs = VGroup(*[
            SVGMobject("shelf.svg").scale(0.4) for _ in range(n_rows * n_cols)
        ]).arrange_in_grid(n_rows=n_rows, n_cols=n_cols, buff=1.5)
        sorts = VGroup(*[
            SVGMobject("sort.svg").scale(0.4).set_color(color[i % len(color)])
            for i in range(n_rows * n_cols)
        ]).arrange_in_grid(n_rows=n_rows, n_cols=n_cols, buff=1.5).set_opacity(0.5)
        one_shelf = SVGMobject("shelf.svg").scale(0.6).set_color(YELLOW)
        text_choiceable = Text("可选的", font="微软雅黑").move_to(UP * 3.5).scale(0.8).set_color_by_text_to_color_map({
            "可选": GREEN,
            "的": WHITE
        }).move_to(DOWN * 0.5 + LEFT * 1)
        text_howtochoose = Text("如何选", font="微软雅黑").move_to(UP * 2.5).scale(0.8).set_color_by_text_to_color_map({
            "如何": RED,
            "选": WHITE
        }).move_to(DOWN * 0.5 + RIGHT * 1)

        self.play(
            *[ReplacementTransform(group_chosen_sets[i], shelfs[i]) for i in range(len(group_chosen_sets))],
            FadeOut(big_braces[0], shift=LEFT * 3),
            FadeOut(big_braces[1], shift=RIGHT * 3),
            run_time=2
        )
        self.wait(1.5)
        self.play(
            FadeIn(sorts, lag_ratio=0.1, run_time=2)
        )
        self.play(
            sorts.animate.shift(RIGHT * 0.75)
        )
        self.wait(1.5)
        self.play(
            ReplacementTransform(sorts, one_shelf),
            FadeOut(shelfs)
        )
        self.wait(1.5)
        self.play(
            one_shelf.animate.move_to(UP * 1),
            Write(text_choiceable)
        )
        self.wait(1.5)
        self.play(
            Write(text_howtochoose)
        )
        group_chosen_sets.set_opacity(0)
        self.play(group_chosen_sets.animate.set_opacity(0.1))
        self.wait(1.5)
        self.play(group_chosen_sets.animate.set_opacity(0))
        
        ball_1 = Sphere(radius=0.4, color=GREEN_A).move_to(DOWN * 2 + LEFT * 1.3)
        ball_2 = Sphere(radius=0.4, color=RED_A).move_to(DOWN * 1.5 + RIGHT * 1.3)
        ball_3 = Sphere(radius=0.4, color=BLUE_A).move_to(DOWN * 2.5 + RIGHT * 1.3)
        text_zorn_lemma = Text("Zorn 引理", font="微软雅黑").scale(0.4).next_to(text_axiom_of_choice, RIGHT).shift(DOWN * 0.15).set_color_by_text_to_color_map({
            "Zorn": ORANGE,
            "引理": WHITE
        })

        self.play(FadeIn(ball_1))
        self.wait(1.5)
        self.play(FadeIn(ball_2), FadeIn(ball_3))
        self.wait(2)
        self.play(
            Write(text_zorn_lemma)
        )
        self.wait(3)
        self.play(
            FadeOut(VGroup(
                text_zorn_lemma, text_choiceable, text_howtochoose,
                one_shelf, group_chosen_sets
            )),
            FadeOut(Group(ball_1, ball_2, ball_3)),
            run_time=1.5
        )
        self.play(FadeOut(text_axiom_of_choice))
        self.wait(1)