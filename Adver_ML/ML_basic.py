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

class Huigui1(Scene):
    def construct(self):
        dots = [
            [-3.82, -2.63, 0],
            [-3.34, -1.6, 0],
            [-2.37, -1.66, 0],
            [-1.68, -0.67, 0],
            [-1.02, 0.65, 0],
            [-0.12, 0.58, 0],
            [1.17, 1.23, 0],
            [1.63, 2.03, 0],
            [2.0, 3.0, 0],
            [2.83, 3.23, 0],
            [0.35, 1.43, 0]
        ]
        line_point = [
            [-10, 0.85 * (-10) + 0.85, 0],
            [10, 0.85 * 10 + 0.85, 0]
        ]
        dot_cloud = set_color_by_xyz([Dot(d) for d in dots], mode = "RG")

        self.wait(2)
        ran.shuffle(dot_cloud)
        for d in dot_cloud:
            self.play(FadeIn(d), run_time = 0.2)
        self.wait(5)