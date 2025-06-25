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

class DAction2:
    """
    实现一些动效
    dotWithText: 获得带文字的点
    dotsWithTexts: 获得一组带文字的点
    arrowP2P:  获取箭头，从一点射向另一点
    arrowsP2Ps:  获取一组箭头，从一组点射向另一组点
    """

    def __init__(self):
        """
        无需传入Scene
        """
        pass

    def dotWithText(self, text: str = "P", locate: ndarray = ORIGIN, sight: ndarray = UP, **kwargs) -> VGroup:
        """
        获得带文字的点，text为Tex
        text: 文字
        locate: 点坐标
        sight: 文字相对点位置
        **kwargs: 其余参数
        """
        
        g = VGroup(
            Dot(locate, **kwargs),
            Tex(text).scale(0.7)
        )
        g[1].next_to(g[0], sight)
        return g

    def dotsWithTexts(self, texts: list = ["p"], locates: list = [ORIGIN], sight: ndarray = UP, **kwargs) -> list:
        """
        获得一组dotWithText
        文字数与点数必须相同，否则抛出异常
        texts: 文字
        locates: 点坐标
        sight: 文字相对点位置
        **kwargs: 其余参数
        """

        dots = []
        if len(texts) != len(locates):
            raise Exception("text's number is not equal to locates!")
        for i in range(len(texts)):
            dots.append(self.dotWithText(
                texts[i],
                locate = locates[i],
                sight = sight,
                **kwargs
            ))
        return dots

    def arrowP2P(self, p1: Dot = Dot(), p2: Dot = Dot(), buff: float = 0.2, **kwargs):
        """
        获取箭头，从一点射向另一点
        p1: 起点
        p2: 终点
        buff: 箭头离点距离
        **kwargs: 其余箭头参数
        """

        return Arrow(p1.get_center(), p2.get_center(), buff = buff, **kwargs)

    def arrowsP2Ps(self, pMap, buff = 0.2, **kwargs):
        """
        获取一组箭头，从一组一点射向另一组一点
        pMap: Dot型list[2, n]
        p2: 终点
        buff: 箭头离点距离
        **kwargs: 其余箭头参数
        """

        arrows = []
        for i in range(len(pMap)):
            arrows.append(self.arrowP2P(
                pMap[i][0],
                pMap[i][1],
                buff = buff,
                **kwargs
            ))
        return arrows

class DGraph:
    """
    实现简单图关系的绘制
    未来可能支持Wolfram Script的自适应算法调用
    """
    def __init__(self, dots: list = [], ve: list = [], name: list = [], dotParam: dict = {}, veParam: dict = {}):
        """
        建图
        dots: 给出ndarray型list，代表节点位置
        ve: 二维int型list，给出节点有向关系
        name: 为点名称
        dotParam: 提供给Dot的参数字典
        veParam: 提供给arrow的参数字典
        """
        
        # 到时候再做（开摆）
        pass