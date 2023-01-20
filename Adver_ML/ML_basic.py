#   MANIM-Adver_ML
#   
#   L        DDDDD    DDDDD    MM         MM  IIIII       A       OOOOOOOOO
#   L        D    D   D    D   M M       M M    I        A A      O       O
#   L        D     D  D     D  M  M     M  M    I       A   A     O       O
#   L        D     D  D     D  M   M   M   M    I      AAAAAAA    O       O
#   L        D    D   D    D   M    M M    M    I     A       A   O       O
#   LLLLLLL  DDDDD    DDDDD    M     M     M  IIIII  A         A  OOOOOOOOO 
#   
#   author: LDDMiao
#   date: 2022 - 12 - 28 TO 2023 - _ - _
#
#   QAQ
#   你这代码保熟吗？

# -*- coding: UTF-8 -*-

import cmath as cm
import math as m
import random as ran
import numpy as np
import scipy as sc
import matplotlib as mat
import matplotlib.pyplot as plt

from manimlib import *
from numpy import *
from decimal import *

def set_color_by_xyz(ps: list[Dot], mode = "RG", reverse = False):
    
    x_min, x_max = -4.0, 4.0
    y_min, y_max = -4.0, 4.0
    z_min, z_max = -4.0, 4.0

    for p in ps:
        cx = (p.get_center()[0] - x_min) / (x_max - x_min)
        cy = (p.get_center()[1] - y_min) / (y_max - y_min)
        cz = (p.get_center()[2] - z_min) / (z_max - z_min)

        cx = (1 - cx) if reverse else cx
        cy = (1 - cy) if not reverse else cy

        if mode == "RG":
            p = p.set_fill(rgb_to_color([cx, cy, 0]))
        if mode == "GB":
            p = p.set_fill(rgb_to_color([0, cx, cy]))
        if mode == "RB":
            p = p.set_fill(rgb_to_color([cx, 0, cy]))
        if mode == "RGB":
            p = p.set_fill(rgb_to_color([cx, cy, cz]))
        if mode == "RAND":
            p = p.set_fill(random_bright_color())

    return ps

def rot(theta, x, y, z):
    # q = ((x, y, z)sin(θ/2), cos(θ/2))
    rx, ry, rz = m.sin(theta / 2) * x, m.sin(theta / 2) * y, m.sin(theta / 2) * z
    return [rx, ry, rz, m.cos(theta / 2)]

class test(Scene):
    def construct(self):
        axes = ThreeDAxes([-20, 20], [-20, 20])
        self.play(Write(axes))
        self.wait(2)
        camera = self.camera.frame
        self.play(camera.animate.set_orientation(Rotation(rot(PI / 3, 1, 0, 0))))
        self.wait(2)
        self.play(camera.animate.to_default_state())
        self.wait(2)

class Huigui1(Scene):
    def construct(self):
        def poly(x):
            return 0.095 * x ** 3 + 0.021 * x ** 2 - 0.469 * x - 0.019

        def logi(x):
            return 2.6928 / (1 + 0.6921 * ma.exp(-0.8828 * x))

        dots = [
            [-3.82, -2.63, -3.87],
            [-3.34, -1.6, -3.12],
            [-2.37, -1.66, -2.6],
            [-1.68, -0.67, -1.8],
            [-1.02, 0.65, -0.95],
            [-0.12, 0.58, 0],
            [1.17, 1.23, 0.67],
            [1.63, 2.03, 1.5],
            [2.0, 3.0, 2.14],
            [2.83, 3.23, 2.97]
        ]
        pre_dots = [[x, 0.85 * x + 0.85, 0.997 * x - 0.036] for x in [(ran.random() * 16 - 8) for _ in range(30)]]
        dots2 = [
            [-3.03, -1.11, 0],
            [-2.38, -0.14, 0],
            [-1.58, 0.62, 0],
            [-1.03, 0.58, 0],
            [-0.12, -0.32, 0],
            [0.96, -0.65, 0],
            [1.88, 0.27, 0],
            [3.21, 1.73, 0]
        ]
        dots3 = [
            [-3.99, 0.16, 0],
            [-3.23, 0.25, 0],
            [-2.42, 0.35, 0],
            [-1, 1, 0],
            [-0.32, 1.44, 0],
            [0.68, 1.85, 0],
            [1.64, 2.44, 0],
            [2.55, 2.52, 0],
            [3.63, 2.56, 0]
        ]
        line_point_fit = [
            [-20, 0.85 * (-20) + 0.85, 0.997 * (-20) - 0.036],
            [20, 0.85 * 20 + 0.85, 0.997 * 20 - 0.036]
        ]
        line_point_up = [
            [-20, 0.45 * (-20) + 1.2, 0],
            [20, 0.45 * 20 + 1.2, 0]
        ]
        line_point_down = [
            [-20, 1.3 * (-20) - 1.2, 0],
            [20, 1.3 * 20 - 1.2, 0]
        ]
        dot_cloud = set_color_by_xyz([Dot(d) for d in dots], mode = "RG")
        dot_cloud_pre = [Dot(d, fill_color = BLUE) for d in pre_dots]
        dot_cloud2 = set_color_by_xyz([Dot(d) for d in dots2], mode = "GB")
        dot_cloud3 = set_color_by_xyz([Dot(d) for d in dots3], mode = "RB")
        line_fit = Line(line_point_fit[0], line_point_fit[1]).set_color(WHITE)
        line_up = DashedLine(line_point_up[0], line_point_up[1]).set_color(GREY)
        line_down = DashedLine(line_point_down[0], line_point_down[1]).set_color(GREY)
        axes = ThreeDAxes([-20, 20], [-20, 20])
        poly_graph = FunctionGraph(poly, [-15, 15, 0.01]).set_color(RED)
        logi_graph = FunctionGraph(logi, [-15, 15, 0.01]).set_color(GREEN)

        camera = self.camera.frame

        self.wait(1)
        self.play(Write(axes))
        self.wait(2)
        ran.shuffle(dot_cloud)
        for d in dot_cloud:
            self.play(FadeIn(d), run_time = 0.2)
        self.wait(5)
        self.play(Write(line_up), run_time = 0.5)
        self.wait(0.5)
        self.play(Write(line_down), run_time = 0.2)
        self.wait(1)
        self.play(Write(line_fit))  #render BUG
        self.wait(3)
        self.play(
            *[d.animate.shift(LEFT * 2 + DOWN * 2) for d in dot_cloud], 
            FadeOut(line_up),
            FadeOut(line_down),
            line_fit.animate.shift(LEFT * 2 + DOWN * 2),
            axes.animate.shift(LEFT * 2 + DOWN * 2),
            camera.animate.set_height(14), 
            run_time = 2.5
        )
        self.wait(3)
        for d in dot_cloud_pre:
            self.play(FadeIn(d), run_time = 0.1)
        self.wait(3)
        self.play(
            *[d.animate.shift(RIGHT * 2 + UP * 2) for d in dot_cloud], 
            *[Uncreate(d) for d in dot_cloud_pre],
            camera.animate.set_height(8),
            line_fit.animate.shift(RIGHT * 2 + UP * 2), 
            axes.animate.shift(RIGHT * 2 + UP * 2),
            run_time = 2.5
        )
        self.play(
            camera.animate.set_orientation(Rotation(rot(PI / 3, 1, 0, 0))),
            FadeOut(line_fit)
        )
        self.play(camera.animate.set_orientation(Rotation(rot(PI, 1/6, 2/6, 3/6))), run_time = 5)
        self.wait(3)
        self.play(camera.animate.to_default_state())
        self.wait(1)
        self.play(*[d.animate.set_fill(WHITE) for d in dot_cloud])
        dot_cloud[3], dot_cloud[7] = dot_cloud[3].set_fill(RED), dot_cloud[7].set_fill(RED),
        self.play(
            dot_cloud[3].animate.shift(LEFT * 1 + UP * 2),
            dot_cloud[7].animate.shift(RIGHT * 2 + DOWN * 4)
        )
        self.wait(2)
        dot_cloud[3], dot_cloud[7] = dot_cloud[3].set_fill(WHITE), dot_cloud[7].set_fill(WHITE),
        self.play(
            dot_cloud[3].animate.shift(RIGHT * 1 + DOWN * 2),
            dot_cloud[7].animate.shift(LEFT * 2 + UP * 4)
        )
        self.wait(2)
        g1 = VGroup(*dot_cloud)
        g2 = VGroup(*dot_cloud2)
        g3 = VGroup(*dot_cloud3)
        self.play(ReplacementTransform(g1, g2), run_time = 2)
        self.wait(1)
        self.play(Write(poly_graph))
        self.wait(3)
        self.play(
            ReplacementTransform(g2, g3), 
            ReplacementTransform(poly_graph, logi_graph),
            run_time = 2
        )
        self.wait(2)
        self.play(
            FadeOut(g3), 
            FadeOut(logi_graph), 
            FadeOut(axes)
        )
        self.wait(2)
        