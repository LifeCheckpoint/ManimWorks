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

class DAni_1:
    # 实现一些代码量较大的动画效果

    def __init__(self, thisScene: Scene):
        """
        初始化
        thisScene: 动画所处Scene
        """
        self.sc = thisScene

    def FunctionGraphEx(self, func: function, x_range: list = [-8, 8, 0.01], color = WHITE, **kwargs) -> VGroup:
        """
        以时间换取精度，绘制GL中绘制有误的函数图像
        func: 函数
        x_range: 设定绘制范围及步长：[x_min, x_max, gamma]
        color: 设定颜色
        **kwargs: 其余参数
        """

        it = x_range[0]
        endx = x_range[1]
        st = x_range[2]
        obj = VGroup()
        while it <= endx:
            obj.add(
                Line(
                    [it, func(it), 0],
                    [it + st, func(it + st), 0],
                    color = color,
                    **kwargs
                )
            )
            it = it + st
        return obj



# a = DAni_1()
# a.FunctionGraphEx()