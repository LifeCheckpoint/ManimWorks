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

class TextTeX(Tex):
    """
    Form: cigar666 - MyText
    Tex下标分析方法：
    使用debugTeX, 先self.add(tex) 然后debugTeX(self, tex)
    导出最后一帧，观察每段字符上的标号，即为下标
    或使用自带的函数get_submobject_index_labels获取下标的VGroup
    然后添加
    """

    # 默认配置
    CONFIG = {
        'default_font': "等线",
        'tex_scale_factor': 1,
    }

    def __init__(self, *tex_strings, **kwargs):
        """
        初始化TeX块
        *tex_strings: 传入欲实现转换的TeX小块
        **kwargs: TeX参数
        
        例：
        formula_i = MyText(
                'f', '(', 't', ')', '=', 'x', '(', 't', ')', '+', 'y', '(', 't', ')', 'i', '=', '(', 'R', '-', 'r', ')', 'e^{', 'i', 't}', '+', 'd', 'e^{', '-', 'i', '{R', '-', 'r', '\\over', 'r}', 't}',
                default_font = someFont, 
                tex_scale_factor = 0.75
            )
        可以传入color_dict对对应的Tex上色
        formula_i.set_color_by_tex_to_color_map(color_dict)
        """

        self.tex_list = tex_strings
        Tex.__init__(self, *tex_strings, **kwargs)
        self.new_font_texs = VGroup()

    def reset_tex_with_font(self):
        self.new_font_texs = VGroup()

    def get_color_by_tex(self, tex, **kwargs):
        parts = self.get_parts_by_tex(tex, **kwargs)
        colors = []
        for part in parts:
            colors.append(part.get_color())
        return colors[0]

    def get_new_font_texs(self, replace_dict):
        """
        将载入的Tex片段转换成为一组Text后输出
        replace_dict: 无法识别的Tex片段输出形式
        
        例：
        replace_dict = {'e^{': 'e', 't}': 't', '{R': 'R', 'r}': 'r', '\\over': '-'}
        new_formula = formula_i.get_new_font_texs(replace_dict)
        """
        
        for i in range(len(self.tex_strings)):
            tex = self.tex_strings[i]
            color = self.get_color_by_tex(tex)
            if tex in replace_dict:
                tex = replace_dict[tex]
            tex_new = Text(tex, font=self.default_font, color=color)
            tex_new.set_height(self[i].get_height())
            if tex == '-' or tex == '=':
                tex_new.set_width(self[i].get_width(), stretch=True)
            tex_new.scale(self.tex_scale_factor)
            tex_new.move_to(self[i])
            self.new_font_texs.add(tex_new)
        return self.new_font_texs