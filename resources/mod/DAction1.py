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

class DAction1:
    """
    实现一些动效
    setScene: 设置动画所处Scene
    FunctionGraphEx: 高精函数图像
    fadeInTitle: 标题进入动效
    shiftList: 对list内的mobject进行整体移动
    list2VGroup: 将list内的mobject打包为VGroup
    """

    def __init__(self, thisScene: Scene):
        """
        初始化
        thisScene: 动画所处Scene
        """
        self.sc = thisScene

    def __init__(self):
        """
        无参数初始化
        """
        pass

    def setScene(self, thisScene: Scene):
        """
        设置动画所处Scene
        """
        self.sc = thisScene

    def FunctionGraphEx(self, func, x_range: list = [-8, 8, 0.01], color = WHITE, **kwargs) -> VGroup:
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


    def fadeInTitle(self, titleText: str, subTitleText: str = "", font: str = "等线", time: float = 5, rightTo: float = 6, width: float = 0.075, coverColor = DEFAULT_BACK, tex2Color: dict = {}):
        """
        标题华丽动效
        请玄学调参
        titleText: 标题
        subTitleText: 副标题，可以空
        font: 字体
        time: 动画时长
        rightTo: 控制淡入器能到达的最右边位置
        width: 淡入器的宽度
        coverColor: 遮罩颜色
        tex2Color: 标题t2c字典

        若显示DEFAULT_BACK未定义，到constants.py中加入定义：
            DEFAULT_BACK = "#333333"
        """

        textHeight = 1.8
        title = Text(titleText, font = font).scale(1.5).move_to(UP * 5, aligned_edge = RIGHT)
        dot = Dot(
            LEFT * (rightTo + 0.5),
            color = coverColor
        ).shift(UP * 5)
        sq_cover = Rectangle(
            height = textHeight + 0.5, 
            width = 32, 
            color = coverColor,
            fill_opacity = 1.0,
            stroke_color = coverColor
        ).move_to(UP * 5, aligned_edge = RIGHT)
        if subTitleText == "":
            sq_line = Rectangle(
                height = textHeight, 
                width = width, 
                color = WHITE,
                fill_opacity = 1.0,
                stroke_color = WHITE
            ).move_to(UP * 5)
            subTitleText = Text("")
        else:
            sq_line = Rectangle(
                height = textHeight, 
                width = width, 
                color = WHITE,
                fill_opacity = 1.0,
                stroke_color = WHITE
            ).move_to(UP * 5 + DOWN * 0.25)
            subTitleText = Text(subTitleText, font = font).scale(0.7).move_to(UP * 5 + DOWN * 0.5 + RIGHT * title.get_left()[0], aligned_edge = LEFT)
            # print(RIGHT * title.get_left()[0])

        if tex2Color != {}:
            title.set_color_by_t2c(tex2Color)
            subTitleText.set_color_by_t2c(tex2Color)

        self.sc.add(title)
        self.sc.add(subTitleText)
        self.sc.add(sq_cover)
        self.sc.add(dot)
        self.sc.add(sq_line)
        self.sc.play(
            sq_cover.shift, DOWN * 5,
            sq_line.shift, DOWN * 5,
            title.shift, DOWN * 5,
            subTitleText.shift, DOWN * 5,
            run_time = 1.5
        )
        self.sc.wait(0.5)
        self.sc.play(
            sq_cover.shift, LEFT * rightTo,
            sq_line.shift, RIGHT * rightTo,
            subTitleText.shift, LEFT * title.get_left()[0],
            title.move_to, ORIGIN, aligned_edge = ORIGIN,
            run_time = 1.5
        )
        self.sc.wait(0.25)
        dot.shift(DOWN * 5)
        self.sc.play(
            ShowPassingFlashAround(title),
            Flash(dot, color = WHITE),
            title.scale, 1.2,
            subTitleText.shift, DOWN * 0.3,
            sq_line.shift, LEFT * rightTo * 2,
            sq_line.set_opacity, 0.5,
            run_time = 1.5
        )

        self.sc.wait(time)

        dot.shift(UP * 5)
        self.sc.play(
            sq_line.shift, RIGHT * rightTo,
            sq_line.set_opacity, 1.0,
            sq_cover.shift, RIGHT * rightTo,
            title.move_to, LEFT * rightTo,
            subTitleText.move_to, LEFT * rightTo,
            run_time = 1.5
        )
        self.sc.wait(0.5)
        title.move_to(UP * 5)
        subTitleText.move_to(UP * 5)
        self.sc.play(
            FadeOut(sq_cover),
            FadeOut(sq_line),
            FadeOut(title),
            FadeOut(subTitleText),
            run_time = 1.5
        )
        self.sc.wait(1)

    def shiftList(self, mobjects: list = [], locate: ndarray = ORIGIN):
        """
        对list内的mobject进行整体移动
        mobjects: 物体
        locate: 移动向量
        """
        for i in mobjects:
            i.shift(locate)

    def list2VGroup(self, mobjects: list = []) -> VGroup:
        """
        将list内的mobject打包为VGroup
        mobjects: 物体
        """
        v = VGroup()
        for i in mobjects:
            v.add(i)
        return v