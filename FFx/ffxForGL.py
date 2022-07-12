#   MANIM-FFx
#   
#   L        DDDDD    DDDDD    MM         MM  IIIII       A       OOOOOOOOO
#   L        D    D   D    D   M M       M M    I        A A      O       O
#   L        D     D  D     D  M  M     M  M    I       A   A     O       O
#   L        D     D  D     D  M   M   M   M    I      AAAAAAA    O       O
#   L        D    D   D    D   M    M M    M    I     A       A   O       O
#   LLLLLLL  DDDDD    DDDDD    M     M     M  IIIII  A         A  OOOOOOOOO 
#   
#   author: LDDMiao
#   date: 2021 - 11 - 7 TO 2022 - _ - _
#
#   QAQ
#   你这代码保熟吗？

# -*- coding: UTF-8 -*-

from mods import *

###FUNCTIONS###

ad1 = DAction1()
ad2 = DAction2()

def protect_range(x: float):
    if x >= 100 or x <= -100:
        return 15
    else:
        return x

def func_itea(func, n):
    return ad1.FunctionGraphEx(
        lambda x: protect_range(func(x, n)), x_range = [-10, 10, 0.005], lineColor = BLUE
    )

###CONSTANTS###

def func_2(x, n):
    for _ in range(n):
        x = x ** 2 - 1
    return x

#--1--
text1_1 = Tex(r"f\left( f\left( x\right) \right) =ax^2+bx+c").scale(1.4)

text1_2 = [
    Tex(r"f\left( x\right) =x^2-1").scale(1.4 * 0.7).shift(DOWN * 2),
    Tex(r"f\left( f\left( x\right) \right) =\left( x^2-1\right) ^2-1=x^4-2x^2").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2),
    Tex(r"f\left( f\left( f\left( x\right) \right) \right) =\left( x^4-2x^2\right) ^2-1=x^8-4x^6+4x^4-1").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2),
    Tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right) =\text{...}").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2),
    Tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right) =\text{...}").scale(1.4 * 0.7 * 0.7).shift(DOWN * 2)
]

text1_2[0].set_color_by_tex(r"f\left( x\right)", GREEN)
text1_2[1].set_color_by_tex(r"f\left( f\left( x\right) \right)", GREEN)
text1_2[2].set_color_by_tex(r"f\left( f\left( f\left( x\right) \right) \right)", GREEN)
text1_2[3].set_color_by_tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)", GREEN)
text1_2[4].set_color_by_tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)", GREEN)

text1_3 = Tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)").scale(1.4)

text1_4 = Text("迭 代 函 数", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)

# def func_1(x, n):
#     for i in range(n):
#         x = (m.sqrt(abs(x)) - 1) ** 2
#     return x

dot1_1 = Dot([0.5 * (1 - m.sqrt(5)), 0.5 * (1 - m.sqrt(5)), 0], color = RED)
dot1_2 = Dot([0.5 * (1 + m.sqrt(5)), 0.5 * (1 + m.sqrt(5)), 0], color = RED)

#--2--
text2_1 = Tex(r"f\left( x\right)").scale(1.4)
text2_2 = Tex(r"f_0\left( x\right) =f\left( x\right)").scale(1.4).shift(DOWN * 0.5)
text2_3 = Tex(r"f_{n+1}\left( x\right) =f\left( f_n\left( x\right)\right)").scale(1.4).shift(DOWN * 1)
text2_4 = Tex(r"\Longrightarrow").scale(1.5)
text2_5 = Text(r"归 纳 定 义 函 数 的 迭 代", font = DFont_MFXingHei_Noncommercial_Bold).scale(1).shift(RIGHT * 3)

group1 = VGroup(text2_1, text2_2, text2_3)

#--3--
text3_1 = Text(r"不 动 点", font = DFont_MFLangQianNoncommercial_Bold, color = RED).scale(1.2).shift(LEFT * 10 + UP * 0.5)
text3_2 = Tex(r"f\left( x\right) =x^2-1").scale(1.4)
text3_3 = [
    Tex(r"P_1=\left( \frac{1-\sqrt{5}}{2} ,\frac{1-\sqrt{5}}{2}\right)").scale(0.6).shift(RIGHT * 3.5 + UP * 2.5),
    Tex(r"P_2=\left( \frac{1+\sqrt{5}}{2} ,\frac{1+\sqrt{5}}{2}\right)").scale(0.6).shift(RIGHT * 3.5 + UP * 1.5)
]
dashLine3_1 = DashedLine(array([-2, -2, 0]), array([6, 6, 0]), color = GREY).shift(LEFT * 1)
text3_4 = Tex(r"f_{n}\left( x \right) =x").scale(1.4).shift(DOWN * 1)
text3_5 = Text(r"不 动 点", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)
text3_6 = Text(r"一 阶 不 动 点", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4).shift(UP * 0.5)
text3_7 = Text(r"M 阶 不 动 点", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4).shift(UP * 0.5)
text3_8 = Tex(r"f_{nM}\left( x \right) =f_M\left( x \right) =x").scale(1.2).shift(DOWN * 1)
text3_9 = Tex(r"f\left( x \right) =\frac{\cos \left( x \right) -\sin \left( x \right)}{\cos \left( x \right) -e^x}").scale(1.2)

numplane_1 = NumberPlane()
numAxes_1 = Axes(
    x_min = -5,
    x_max = 5,
    y_min = -1.25,
    y_max = 5,
    number_line_config={
        "stroke_color": GREY,
        "stroke_width": 2,
        "include_tip": False,
    }
).shift(LEFT * 1)

group2 = VGroup(dot1_1, dot1_2)

#--4--
text4_1 = Text(r"轨 道 图", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)
text4_2 = [
    Tex(r"f\left( x\right) =x^2-1").scale(1).shift(UP * 0.5),
    Tex(r"f\left( f\left( x\right) \right) =\left( x^2-1\right) ^2-1=x^4-2x^2").scale(1).shift(UP * 0.5),
    Tex(r"f\left( f\left( f\left( x\right) \right) \right) =\left( x^4-2x^2\right) ^2-1=x^8-4x^6+4x^4-1").scale(1).shift(UP * 0.5),
    Tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)=\text{...}").scale(1).shift(UP * 0.5),
    Tex(r"f\left( f\left( f\left( \text{...} f\left( x\right) \text{...} \right) \right) \right)=\text{...}").scale(1).shift(UP * 0.5)
]
# text4_3 = [
#     Text(r"x = " + str(func_2(4, 1)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 2)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 3)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 4)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
#     Text(r"x = " + str(func_2(4, 5)), font = "微软雅黑").scale(1).shift(DOWN * 0.5),
# ]
text4_4 = Tex(r"f\left( x \right) \rightarrow x").scale(1.4).shift(UP * 0.5)
text4_5 = Tex(r"f\left( x_1\right) =x_2").scale(0.7).shift(DOWN * 0.5)
text4_6 = Text(r"举 个 例 子", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)
text4_7 = Tex(r"x_0=x\quad x_1=f_1\left( x \right) \quad x_2=f_2\left( x \right) \quad x_3=f_3\left( x \right) ").scale(0.8).shift(DOWN * 1)

tq4_1 = Tex(r"x_0", color = GREY).scale(1.1)
tq4_2 = Tex(r"x_1", color = GREY).scale(1.1 * 0.75)
tq4_3 = Tex(r"x_2", color = GREY).scale(1.1 * 0.75).move_to(RIGHT * 1)
tq4_4 = Tex(r"x_3", color = GREY).scale(1.1 * 0.75).move_to(RIGHT * 3)
square4_1 = Rectangle(height = 1, width = 1, color = ORANGE, fill_opacity = 1.0)
square4_2 = Rectangle(height = 1, width = 1, color = ORANGE, fill_opacity = 1.0).move_to(RIGHT * 1)
square4_3 = Rectangle(height = 1, width = 1, color = ORANGE, fill_opacity = 1.0).move_to(RIGHT * 2)

# square4_1.set_sheen(0.5, RIGHT)
# square4_2.set_sheen(0.5, RIGHT)
# square4_3.set_sheen(0.5, RIGHT)

group7 = VGroup(tq4_4, square4_1, square4_2, square4_3)

dot4_1 = [
    ad2.dotWithText("x_1", locate = DOWN * 0.5 + LEFT * 0.5, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad2.dotWithText("x_2", locate = DOWN * 0.5 + RIGHT * 0.5, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)
]
# Dot().get_center
line4_1 = [
    ad2.arrowP2P(dot4_1[0][0], dot4_1[1][0], arc_path = 0.8)
]

group3 = VGroup(ad1.list2VGroup(dot4_1), ad1.list2VGroup(line4_1), text4_5)

#--5--
text5_1 = Tex(r"f\left( x \right) =\frac{1}{x}").scale(1.4)
text5_2 = [
    Tex(r"f\left( z_1 \right) =z_2").shift(DOWN * 1),
    Tex(r"f\left( z_2 \right) =z_3").shift(DOWN * 1),
    Tex(r"f\left( z_3 \right) =z_4").shift(DOWN * 1),
    Tex(r"f\left( z_4 \right) =z_1").shift(DOWN * 1)
]
text5_3 = Text(r"轨 道 图", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4).shift(RIGHT * 4)
text5_4 = Text(r"4 - 循 环", font = DFont_MFXingHei_Noncommercial_Bold).shift(DOWN * 1.2)
text5_5 = Text(r"m - 循 环", font = DFont_MFXingHei_Noncommercial_Bold).shift(DOWN * 1.2)
text5_6 = Text(r"m - 圈", font = DFont_MFXingHei_Noncommercial_Bold).scale(1.4)

dot5_1 = dot4_1
dot5_2 = [
    ad2.dotWithText("x_1", locate = UP * 1 + LEFT * 3 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 0
    ad2.dotWithText("x_2", locate = UP * 1 + LEFT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 1
    ad2.dotWithText("x_3", locate = UP * 1 + LEFT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 2
    ad2.dotWithText("z_1", locate = UP * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 3
    ad2.dotWithText("z_2", locate = RIGHT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 4
    ad2.dotWithText("z_3", locate = DOWN * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 5
    ad2.dotWithText("z_4", locate = LEFT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 6
    ad2.dotWithText("y_1", locate = DOWN * 1 + RIGHT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 7
    ad2.dotWithText("y_2", locate = DOWN * 1 + RIGHT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0) # 8
]

color5_1, color5_2 = "#00DBDE", "#FC00FF"

dot5_3 = Dot(
    fill_opacity = 1.0, 
    radius = 0.12, 
    stroke_width = 1.0
).shift(UP * 1).shift(UP * 1)
dot5_4 = Dot(
    fill_opacity = 1.0, 
    radius = 0.12, 
    stroke_width = 1.0
).shift(UP * 1).shift(RIGHT * 1)

dot5_3.set_color(color5_1)
dot5_4.set_color(color5_2)

# dot5_3.set_sheen(0.5, RIGHT)
# dot5_4.set_sheen(0.5, RIGHT)

#Ahh...
#x_123, z_1234, y_12 -> 0 ~ 8

line5_1 = line4_1
line5_2 = [
    ad2.arrowP2P(dot5_2[0][0], dot5_2[1][0]),
    ad2.arrowP2P(dot5_2[1][0], dot5_2[2][0]),
    ad2.arrowP2P(dot5_2[2][0], dot5_2[3][0]),
    ad2.arrowP2P(dot5_2[3][0], dot5_2[4][0]),
    ad2.arrowP2P(dot5_2[4][0], dot5_2[5][0]),
    ad2.arrowP2P(dot5_2[5][0], dot5_2[6][0]),
    ad2.arrowP2P(dot5_2[6][0], dot5_2[3][0]),
    ad2.arrowP2P(dot5_2[8][0], dot5_2[5][0]),
    ad2.arrowP2P(dot5_2[7][0], dot5_2[8][0])
]

group4 = VGroup(ad1.list2VGroup(dot5_1), ad1.list2VGroup(line5_1), text5_1)
group5 = VGroup(ad1.list2VGroup(dot5_2), ad1.list2VGroup(line5_2))
group8 = VGroup()
group6 = VGroup(
    dot5_2[3][0], 
    dot5_2[4][0], 
    dot5_2[5][0], 
    dot5_2[6][0]
)

background5_1 = SurroundingRectangle(group6, opacity = 0.1, fill_color = WHITE, color = BLUE)

#--6--

color6_1 = color5_1

# "循 环 轨 道 图": color6_1
text6_1 = Text(r"循 环 轨 道 图 的 性 质", font = DFont_MFXingHei_Noncommercial_Bold, t2c = {"性 质": BLUE}).scale(1.2)
text6_2 = Text(r"多个圈？", font = DFont_MFXingHei_Noncommercial_Bold, t2c = {"多个": GREEN}).move_to(RIGHT * 2.5)
text6_2_1 = Text(r"不允许存在多个圈", font = DFont_MFXingHei_Noncommercial_Bold, t2c = {"多个": GREEN, "不允许": RED}).move_to(RIGHT * 2.5)
text6_3 = Text(r"非循环轨道图有无穷多顶点", font = DFont_MFXingHei_Noncommercial_Bold, t2c = {"无穷多": GREEN})
text6_4 = Text(r"对于函数f，其轨道图可能不止一个", font = DFont_MFXingHei_Noncommercial_Bold, t2c = {"不止一个": GREEN})
text6_5 = Tex(r"f\left( x\right) =x!").move_to(UP * 1 + LEFT * 0.5)
text6_6 = Tex(r"x_0=0").move_to(LEFT * (2.5 + 3.75) / 2)
text6_7 = Tex(r"x_0=3").move_to(RIGHT * 2)

#                      < k_2
# y_2 <-- y_1 <-- k_3     ^
#                      > k_1
dot6_1 = dot5_2
dot6_1.append(ad2.dotWithText(r"k_3", locate = DOWN * 1 + RIGHT * 3 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)) # 9
dot6_1.append(ad2.dotWithText(r"k_1", locate = DOWN * 1.5 + RIGHT * 3 * m.sqrt(2) + RIGHT, sight = DOWN, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)) # 10
dot6_1.append(ad2.dotWithText(r"k_2", locate = DOWN * 0.5 + RIGHT * 3 * m.sqrt(2) + RIGHT, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)) # 11

#          v  <
# x_0 --> x_1 ^
# 
dot6_2 = [
    ad2.dotWithText(r"x_0=0", locate = LEFT * 2 + LEFT * 1.75 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad2.dotWithText(r"x_1=1", locate = LEFT * 2 + LEFT * 0.5 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0)
]
# x_0 --> x_1 -- > x_2 --> ...
dot6_3 = [
    ad2.dotWithText(r"x_0=3", locate = RIGHT * 2 + LEFT * 2.25 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad2.dotWithText(r"x_1=6", locate = RIGHT * 2 + LEFT * 0.75 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad2.dotWithText(r"x_2=720", locate = RIGHT * 2 + RIGHT * 0.75 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
    ad2.dotWithText(r"...", locate = RIGHT * 2 + RIGHT * 2.25 + DOWN * 2, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),
]

line6_1 = line5_2
line6_1.append(ad2.arrowP2P(dot5_2[9][0], dot5_2[7][0]))
line6_1.append(ad2.arrowP2P(dot5_2[9][0], dot5_2[10][0]))
line6_1.append(ad2.arrowP2P(dot5_2[10][0], dot5_2[11][0]))
line6_1.append(ad2.arrowP2P(dot5_2[11][0], dot5_2[9][0]))
line6_2_1 = Line(
    array(
        [
            text6_2.get_center()[0] - 0.5,
            text6_2.get_center()[1],
            0
        ]
    ),
    array(
        [
            text6_2.get_center()[0] + 0.5,
            text6_2.get_center()[1],
            0
        ]
    ),
    color = RED
)
line6_2_2 = Line(
    array(
        [
            text6_2.get_center()[0] - 0.5,
            text6_2.get_center()[1],
            0
        ]
    ),
    array(
        [
            text6_2.get_center()[0] + 1,
            text6_2.get_center()[1],
            0
        ]
    ),
    color = RED
).scale(0.75)
line6_2 = [
    ad2.arrowP2P(dot6_2[0][0], dot6_2[1][0]),
    Arc(start_angle = PI + 0.4, angle = 2 * PI - 0.8, radius = 0.5).add_tip().scale(0.5).move_to(LEFT * 2.5 + RIGHT * 0.55 + DOWN * 2)
]
line6_3 = [
    ad2.arrowP2P(dot6_3[0][0], dot6_3[1][0]),
    ad2.arrowP2P(dot6_3[1][0], dot6_3[2][0]),
    ad2.arrowP2P(dot6_3[2][0], dot6_3[3][0]),
]

group6_2_1 = VGroup(
    dot6_1[9][0],
    dot6_1[10][0],
    dot6_1[11][0]
)
group6_1 = VGroup(*[i for i in dot6_1], *[i for i in line6_1])
group6_2 = VGroup(*[i for i in dot6_2], *[i for i in line6_2])
group6_3 = VGroup(*[i for i in dot6_3], *[i for i in line6_3])

rectan6_1 = Rectangle(width = 0.05, height = 2, color = WHITE, fill_opacity = 1.0).move_to(LEFT * 7 + UP * 2.25)

background6_1 = SurroundingRectangle(group6_2_1, opacity = 0.1, fill_color = WHITE, color = PURPLE)
# background6_2 = RoundedRectangle(width = 5, height = 3, opacity = 1.0, fill_color = GREY, stroke_color = WHITE).move_to(UP * 2.5 + LEFT * 5, aligned_edge = LEFT)

# --7--
text7_1 = TextTeX(
    "\\text{i: }", "f", "\\text{的一个}", "2m", "\\text{循环轨道图可分裂为两个}", "f_", "{2}", "\\text{的}", "m", "\\text{循环轨道图}",
    default_font = DFont_MFLangQianNoncommercial_Light,
    text_scale_factor = 0.77
).get_new_font_texs({
    "\\text{i: }": "i： ",
    "\\text{的一个}": "的一个",
    "\\text{循环轨道图可分裂为两个}": "循环轨道图可分裂为两个",
    "f_": "f",
    "{2}": "2",
    "\\text{的}": "的",
    "\\text{循环轨道图}": "循环轨道图"
}).scale(0.8).move_to(UP * 1 + LEFT * 6, aligned_edge = LEFT)
text7_2 = TextTeX("\\text{ii: }", "f", "\\text{的一个非循环轨道图可分裂为两个}", "f_", "{2}", "\\text{的非循环轨道图}",
    default_font = DFont_MFLangQianNoncommercial_Light,
    text_scale_factor = 0.77
).get_new_font_texs({
    "\\text{ii: }": "ii: ",
    "\\text{的一个非循环轨道图可分裂为两个}": "的一个非循环轨道图可分裂为两个",
    "f_": "f",
    "{2}": "2",
    "\\text{的非循环轨道图}": "的非循环轨道图"
}).scale(0.8).move_to(UP * 1 + LEFT * 6, aligned_edge = LEFT)
text7_3 = TextTeX("\\text{iii: }", "f", "\\text{的一个}", "2m+1", "\\text{循环轨道图可变形为一个}", "f_", "{2}", "\\text{的}", "2m+1", "\\text{循环轨道图}",
    default_font = DFont_MFLangQianNoncommercial_Light,
    text_scale_factor = 0.77
).get_new_font_texs({
    "\\text{iii: }": "iii: ",
    "\\text{的一个}": "的一个",
    "\\text{循环轨道图可变形为一个}": "循环轨道图可变形为一个",
    "f_": "f",
    "{2}": "2",
    "\\text{的}": "的",
    "\\text{循环轨道图}": "循环轨道图"
}).scale(0.8).move_to(UP * 1 + LEFT * 6, aligned_edge = LEFT)
text7_1_1 = Tex("f").move_to(LEFT * 1)
text7_1_2 = Tex("f_2").move_to(RIGHT * 1)

text7_4_1 = Tex("f_2\\left( x_1\\right) =x_3").scale(0.7).move_to(RIGHT * 5 + UP * 1.5)
text7_4_2 = Tex("f_2\\left( x_3\\right) =z_2").scale(0.7).move_to(RIGHT * 5 + UP * 0.75)
text7_4_3 = Tex("f_2\\left( z_2\\right) =z_4").scale(0.7).move_to(RIGHT * 5)
text7_4_4 = Tex("f_2\\left( z_4\\right) =z_2").scale(0.7).move_to(RIGHT * 5 + DOWN * 0.75)
text7_4_5 = Tex("f_2\\left( y_2\\right) =z_4").scale(0.7).move_to(RIGHT * 5 + DOWN * 1.5)

text7_5_1 = Tex("f_2\\left( x_2\\right) =z_1").scale(0.7).move_to(RIGHT * 5 + UP * 1.5)
text7_5_2 = Tex("f_2\\left( z_1\\right) =z_3").scale(0.7).move_to(RIGHT * 5 + UP * 0.5)
text7_5_3 = Tex("f_2\\left( z_3\\right) =z_1").scale(0.7).move_to(RIGHT * 5 + DOWN * 0.5)
text7_5_4 = Tex("f_2\\left( y_1\\right) =z_3").scale(0.7).move_to(RIGHT * 5 + DOWN * 1.5)
text7_6 = Text("4 - 循环", font = DFont_MFXingHei_Noncommercial_Bold).scale(1).move_to(UP * 0.5)
text7_7_1 = Text("2 - 循环", font = DFont_MFXingHei_Noncommercial_Bold).scale(0.8).move_to(DOWN * 2 + LEFT * 5)
text7_7_2 = Text("2 - 循环", font = DFont_MFXingHei_Noncommercial_Bold).scale(0.8).move_to(DOWN * 2 + RIGHT * 5)

text7_6.set_color_by_t2c({"4": PURPLE})
text7_7_1.set_color_by_t2c({"2": BLUE})
text7_7_2.set_color_by_t2c({"2": BLUE})

group9_1 = VGroup(text7_4_1, text7_4_2, text7_4_3, text7_4_4, text7_4_5)
group9_2 = VGroup(text7_5_1, text7_5_2, text7_5_3, text7_5_4)

# x_1 --> x_2 --> x_3 --> z_1
#                     z_4    z_2
#                         z_3 <-- y_2 <-- y_1
dot7_1 = ad2.dotsWithTexts(
    [
        "x_1",  # 0
        "x_2",  # 1
        "x_3",  # 2
        "z_1",  # 3
        "z_2",  # 4
        "z_3",  # 5
        "z_4",  # 6
        "y_1",  # 7
        "y_2"   # 8
    ],
    [
        UP * 1 + LEFT * 3 * m.sqrt(2),  # 0
        UP * 1 + LEFT * 2 * m.sqrt(2),  # 1
        UP * 1 + LEFT * 1 * m.sqrt(2),  # 2
        UP * 1,  # 3
        RIGHT * 1,  # 4
        DOWN * 1,  # 5
        LEFT * 1,  # 6
        DOWN * 1 + RIGHT * 2 * m.sqrt(2),  # 7
        DOWN * 1 + RIGHT * 1 * m.sqrt(2)    # 8
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_1a = ad2.dotsWithTexts(
    [
        "x_1",  # 0
        "x_2",  # 1
        "x_3",  # 2
        "z_1",  # 3
        "z_2",  # 4
        "z_3",  # 5
        "z_4",  # 6
        "y_1",  # 7
        "y_2"   # 8
    ],
    [
        UP * 1 + LEFT * 3 * m.sqrt(2),  # 0
        UP * 1 + LEFT * 2 * m.sqrt(2),  # 1
        UP * 1 + LEFT * 1 * m.sqrt(2),  # 2
        UP * 1,  # 3
        RIGHT * 1,  # 4
        DOWN * 1,  # 5
        LEFT * 1,  # 6
        DOWN * 1 + RIGHT * 2 * m.sqrt(2),  # 7
        DOWN * 1 + RIGHT * 1 * m.sqrt(2)    # 8
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
# dot7_1 = [
#     ad2.dotWithText("x_1", locate = UP * 1 + LEFT * 3 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 0
#     ad2.dotWithText("x_2", locate = UP * 1 + LEFT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 1
#     ad2.dotWithText("x_3", locate = UP * 1 + LEFT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 2
#     ad2.dotWithText("z_1", locate = UP * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 3
#     ad2.dotWithText("z_2", locate = RIGHT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 4
#     ad2.dotWithText("z_3", locate = DOWN * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 5
#     ad2.dotWithText("z_4", locate = LEFT * 1, fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 6
#     ad2.dotWithText("y_1", locate = DOWN * 1 + RIGHT * 2 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0),   # 7
#     ad2.dotWithText("y_2", locate = DOWN * 1 + RIGHT * 1 * m.sqrt(2), fill_opacity = 0.0, radius = 0.12, stroke_width = 1.0) # 8
# ]

#                  v     <
# x_1 --> x_3 --> z_2 > z_4 <-- y_2
# 
dot7_2 = ad2.dotsWithTexts(
    [
        "x_1",  # 0
        "x_3",  # 1
        "z_2",  # 2
        "z_4",  # 3
        "y_2"   # 4
    ],
    [
        LEFT * 3.5 + LEFT * 1.5 + UP * 0.5,  # 0
        LEFT * 3.5 + LEFT * 0.5 + UP * 0.5,  # 1
        LEFT * 3.5 + RIGHT * 0.5 + UP * 0.5,  # 2
        LEFT * 3.5 + RIGHT * 0.5 + DOWN * 0.5,  # 3
        LEFT * 3.5 + RIGHT * 1.5 + DOWN * 0.5  # 4
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_2a = ad2.dotsWithTexts(
    [
        "x_1",  # 0
        "x_3",  # 1
        "z_2",  # 2
        "z_4",  # 3
        "y_2"   # 4
    ],
    [
        LEFT * 3.5 + LEFT * 1.5 + UP * 0.5,  # 0
        LEFT * 3.5 + LEFT * 0.5 + UP * 0.5,  # 1
        LEFT * 3.5 + RIGHT * 0.5 + UP * 0.5,  # 2
        LEFT * 3.5 + RIGHT * 0.5 + DOWN * 0.5,  # 3
        LEFT * 3.5 + RIGHT * 1.5 + DOWN * 0.5  # 4
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
# dot7_2 = [
#     dot7_1[0].move_to(LEFT * 3.5 + LEFT * 1.5 + UP * 0.5),  # x_1     0
#     dot7_1[2].move_to(LEFT * 3.5 + LEFT * 0.5 + UP * 0.5),  # x_3     1
#     dot7_1[4].move_to(LEFT * 3.5 + RIGHT * 0.5 + UP * 0.5),  # z_2     2
#     dot7_1[6].move_to(LEFT * 3.5 + RIGHT * 0.5 + DOWN * 0.5),  # z_4     3
#     dot7_1[8].move_to(LEFT * 3.5 + RIGHT * 1.5 + DOWN * 0.5)   # y_2     4
# ]

#          v     <
# x_2 --> z_1 > z_3 <-- y_1
# 
dot7_3 = ad2.dotsWithTexts(
    [
        "x_2",  # 0
        "z_1",  # 1
        "z_3",  # 2
        "y_1"  # 3
    ],
    [
        RIGHT * 3.5 + LEFT * 1 + UP * 0.5,  # 0
        RIGHT * 3.5 + UP * 0.5,  # 1
        RIGHT * 3.5 + DOWN * 0.5,  # 2
        RIGHT * 3.5 + RIGHT * 1 + DOWN * 0.5  # 3
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_3a = ad2.dotsWithTexts(
    [
        "x_2",  # 0
        "z_1",  # 1
        "z_3",  # 2
        "y_1"  # 3
    ],
    [
        RIGHT * 3.5 + LEFT * 1 + UP * 0.5,  # 0
        RIGHT * 3.5 + UP * 0.5,  # 1
        RIGHT * 3.5 + DOWN * 0.5,  # 2
        RIGHT * 3.5 + RIGHT * 1 + DOWN * 0.5  # 3
    ],
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
# dot7_3 = [
#     dot7_1[1].move_to(RIGHT * 3.5 + LEFT * 1 + UP * 0.5),  # x_2     0
#     dot7_1[3].move_to(RIGHT * 3.5 + UP * 0.5),  # z_1     1
#     dot7_1[5].move_to(RIGHT * 3.5 + DOWN * 0.5),  # z_3     2
#     dot7_1[7].move_to(RIGHT * 3.5 + RIGHT * 1 + DOWN * 0.5)   # y_1     3
# ]

dot7_4 = Dot(
    UP * 1 + LEFT * 3 * m.sqrt(2),
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)
dot7_5 = Dot(
    UP * 1 + LEFT * 1 * m.sqrt(2),
    fill_opacity = 0.0,
    radius = 0.12,
    stroke_width = 1.0
)

# dot7_4.set_color(RED)
dot7_4.set_fill(RED, opacity = 1)
dot7_5.set_fill(GREEN, opacity = 1)

ad1.shiftList(dot7_2, DOWN * 2.5)
ad1.shiftList(dot7_3, DOWN * 2.5)
ad1.shiftList(dot7_2a, DOWN * 2.5)
ad1.shiftList(dot7_3a, DOWN * 2.5)

line7_1 = ad2.arrowsP2Ps([
    [dot7_1[0][0], dot7_1[1][0]],
    [dot7_1[1][0], dot7_1[2][0]],
    [dot7_1[2][0], dot7_1[3][0]],
    [dot7_1[3][0], dot7_1[4][0]],
    [dot7_1[4][0], dot7_1[5][0]],
    [dot7_1[5][0], dot7_1[6][0]],
    [dot7_1[6][0], dot7_1[3][0]],
    [dot7_1[8][0], dot7_1[5][0]],
    [dot7_1[7][0], dot7_1[8][0]],
])
# line7_1 = [
#     ad.arrowP2P(dot7_1[0][0], dot7_1[1][0]),
#     ad.arrowP2P(dot7_1[1][0], dot7_1[2][0]),
#     ad.arrowP2P(dot7_1[2][0], dot7_1[3][0]),
#     ad.arrowP2P(dot7_1[3][0], dot7_1[4][0]),
#     ad.arrowP2P(dot7_1[4][0], dot7_1[5][0]),
#     ad.arrowP2P(dot7_1[5][0], dot7_1[6][0]),
#     ad.arrowP2P(dot7_1[6][0], dot7_1[3][0]),
#     ad.arrowP2P(dot7_1[8][0], dot7_1[5][0]),
#     ad.arrowP2P(dot7_1[7][0], dot7_1[8][0])
# ]
line7_2 = [
    ad2.arrowP2P(dot7_2[0][0], dot7_2[1][0]),
    ad2.arrowP2P(dot7_2[1][0], dot7_2[2][0]),
    ad2.arrowP2P(dot7_2[2][0], dot7_2[3][0]).shift(LEFT * 0.2),
    ad2.arrowP2P(dot7_2[3][0], dot7_2[2][0]).shift(RIGHT * 0.2),
    ad2.arrowP2P(dot7_2[4][0], dot7_2[3][0])
]
line7_3 = [
    ad2.arrowP2P(dot7_3[0][0], dot7_3[1][0]),
    ad2.arrowP2P(dot7_3[1][0], dot7_3[2][0]).shift(LEFT * 0.2),
    ad2.arrowP2P(dot7_3[2][0], dot7_3[1][0]).shift(RIGHT * 0.2),
    ad2.arrowP2P(dot7_3[3][0], dot7_3[2][0])
]

group7_1 = VGroup(*[i1 for i1 in dot7_1a], *[i2 for i2 in line7_1])
group7_2 = VGroup(*[i1 for i1 in dot7_2a], *[i2 for i2 in line7_2])
group7_3 = VGroup(*[i1 for i1 in dot7_3a], *[i2 for i2 in line7_3])
group10_1 = VGroup(dot7_2a[2], dot7_2a[3])
group10_2 = VGroup(dot7_3a[1], dot7_3a[2])

background7_1 = SurroundingRectangle(group10_1, opacity = 0.1, fill_color = WHITE, color = BLUE).shift(UP * 2.5)
background7_2 = SurroundingRectangle(group10_2, opacity = 0.1, fill_color = WHITE, color = BLUE).shift(UP * 2.5)

color7_1 = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

###PROGRAMME###

class s0(Scene):
    def construct(self):
        pass

class s1(Scene):
    def construct(self):
        ad1.setScene(self)

        #--1--
        self.wait(1)
        ad1.fadeInTitle(
            "一  迭代函数", 
            subTitleText = "交叠，即是回环", 
            tex2Color = {"迭代": RED, "交叠": PINK}, 
            time = 3
        )
        # self.wait(2)
        # self.play(Write(text1_1))
        # self.wait(2)
        # self.play(FadeOut(text1_1))
        self.wait(1.5)
        self.play(Write(text1_2[0]))
        self.wait(2)
        self.play(
            text1_2[0].scale, 0.7,
            text1_2[0].move_to, DOWN * 2
        )
        self.wait(1.5)
        tmp1 = func_itea(func_2, 1)
        for i in range(5):
            if i != 0:
                tmp2 = func_itea(func_2, i + 2)
                self.play(
                    ReplacementTransform(tmp1, tmp2),
                    ReplacementTransform(text1_2[i - 1], text1_2[i])
                )
                self.wait(2)
                tmp1 = tmp2
            else:
                self.play(FadeIn(tmp1))
                # self.wait(1)
                # self.play(
                #     Write(dot1_1),
                #     Write(dot1_2)
                # )
                self.wait(1)
        self.wait(2)
        self.play(
            Uncreate(tmp2),
            text1_2[4].shift, ORIGIN,
            text1_2[4].scale, 1 / 1.4 / 0.7
        )
        self.wait(0.5)
        self.play(ReplacementTransform(text1_2[4], text1_3))
        self.wait(1.5)
        self.play(ReplacementTransform(text1_3, text1_4))
        self.wait(2.5)
        self.play(FadeOut(text1_4))
        self.wait(3)

        #--2--
        self.play(Write(text2_1))
        self.wait(1.5)
        self.play(
            FadeIn(text2_2),
            text2_1.shift, UP * 0.5
        )
        self.wait(1.5)
        self.play(
            FadeIn(text2_3),
            text2_1.shift, UP * 0.5,
            text2_2.shift, UP * 0.5
        )
        self.wait(2)
        self.play(group1.shift, LEFT * 3)
        self.wait(0.25)
        self.play(Write(text2_4))
        self.wait(0.25)
        self.play(Write(text2_5))
        self.wait(2.5)
        self.play(
            FadeOut(group1),
            FadeOut(text2_4),
            FadeOut(text2_5)
        )
        self.wait(2)

        # --3--
        ad1.fadeInTitle("二  不动点", subTitleText = "神静，方可察理", tex2Color = {"不动": RED, "静": PINK}, time = 2)
        self.wait(1)
        self.play(
            FadeIn(text3_1),
            text3_1.move_to, LEFT * 5,
            text3_1.scale, 1 / 1.4 / 1.6
        )
        self.wait(1)
        self.play(Write(text3_2))
        self.wait(1)
        tmp1 = func_itea(func_2, 1)
        self.play(
            FadeOut(text3_2), 
            FadeIn(tmp1),
            Write(numAxes_1)
        )
        self.wait(1)
        for i in range(4):
            if i != 0:
                tmp2 = func_itea(func_2, i + 2)
                tmp2.shift(LEFT * 1)
                text1_2[i].shift(LEFT * 1)
                self.play(
                    ReplacementTransform(tmp1, tmp2),
                    ReplacementTransform(text1_2[i - 1], text1_2[i])
                )
                self.wait(2)
                tmp1 = tmp2
            else:
                # self.play(FadeIn(tmp1))
                # self.wait(1)
                # self.wait(1.5)
                self.play(
                    TransformFromCopy(dot1_1, text3_3[0]),
                    TransformFromCopy(dot1_2, text3_3[1]),
                    tmp1.shift, LEFT * 1,
                    dot1_1.shift, LEFT * 1,
                    dot1_2.shift, LEFT * 1
                )
                self.wait(1.5)
                self.play(
                    Write(dot1_1),
                    Write(dot1_2)
                )
                self.wait(0.5)
                self.play(
                    FadeIn(dashLine3_1)
                )
                self.wait(1)
                text1_2[0].shift(LEFT * 1)
                self.play(Write(text1_2[0]))

        self.play(
            Uncreate(tmp1),
            Uncreate(text3_3[0]),
            Uncreate(text3_3[1]),
            Uncreate(text1_2[3]),
            Uncreate(text3_1),
            Uncreate(dashLine3_1),
            Uncreate(numAxes_1),
            ReplacementTransform(group2, text3_5)
        )
        self.wait(2)
        self.play(
            FadeIn(text3_4),
            text3_5.shift, UP * 1
        )
        self.wait(2)
        self.play(ReplacementTransform(text3_5, text3_6))
        self.wait(2)
        self.play(ReplacementTransform(text3_6, text3_7))
        self.wait(2)
        self.play(ReplacementTransform(text3_4, text3_8))
        self.wait(3)
        self.play(
            FadeOut(text3_7),
            FadeOut(text3_8)
        )
        self.wait(2)
        # self.play(Write(text3_9))
        # self.wait(2)
        # self.play(
        #     Write(numplane1),
        #     text3_9.scale, 0.7 / 1.4,
        #     text3_9.shift, RIGHT * 4
        # )
        # self.wait(1.5)

        # numplane1.prepare_for_nonlinear_transform()
        # for n in range(5):
        #     self.play(numplane1.apply_function, 
        #         lambda z: array([
        #             float(protect_range(func_3(complex(z[0], z[1]), n + 1).real)),
        #             float(protect_range(func_3(complex(z[0], z[1]), n + 1).imag)),
        #             0.0
        #             ])
        #     )
        #     self.wait(1.5)
        # self.wait(1)
        # self.play(
        #     Uncreate(numplane1), 
        #     Uncreate(text3_9)
        # )

class s2(Scene):
    def construct(self):
        ad1.setScene(self)

        #--4--
        self.wait(0.5)
        # self.play(Write(text4_1))
        # self.wait(3)
        # self.play(FadeOutAndShiftDown(text4_1))
        ad1.fadeInTitle(
            "三  函数轨道图", 
            subTitleText = "破格，不落世俗", 
            tex2Color = {"轨道": RED, "格": PINK}, 
            time = 2
        )
        self.wait(1.5)
        self.play(FadeIn(tq4_1))
        self.wait(1.5)
        self.play(
            FadeIn(square4_1),
            tq4_1.shift, LEFT * 1.5,
            tq4_1.scale, 0.75
        )
        self.wait(1.5)
        self.play(
            Rotate(square4_1, angle = PI),
            tq4_1.move_to, RIGHT * 1.5
        )
        self.wait(1)
        self.play(
            FadeIn(square4_2),
            ReplacementTransform(tq4_1, tq4_2),
            square4_1.shift, LEFT * 1,
        )
        self.wait(1.5)
        self.play(
            Rotate(square4_2, angle = PI),
            tq4_2.move_to, RIGHT * 2
        )
        self.wait(1)
        self.play(
            FadeIn(square4_3),
            ReplacementTransform(tq4_2, tq4_3),
            square4_1.shift, LEFT * 1,
            square4_2.move_to, ORIGIN,
        )
        self.wait(1)
        self.play(
            Rotate(square4_3, angle = PI),
            tq4_3.move_to, RIGHT * 3
        )
        self.wait(1)
        self.play(ReplacementTransform(tq4_3, tq4_4))
        self.wait(2)
        self.play(
            FadeIn(text4_7),
            group7.shift, UP * 1
        )
        self.wait(3)
        self.play(
            FadeOut(group7),
            text4_7.shift, UP * 1
            # FadeOut(),
        )
        self.wait()
        # self.play(
        #     Write(text4_2[0]),
        #     Write(text4_3[0])
        # )
        # for i in range(4):
        #     self.play(ReplacementTransform(text4_2[i], text4_2[i + 1]))
        #     self.play(ReplacementTransform(text4_3[i], text4_3[i + 1]))
        #     self.wait(1.5)
        # self.play(
        #     Uncreate(text4_2[4]),
        #     Uncreate(text4_3[4])
        # )
        self.wait(2)
        self.play(text4_7.shift, UP * 8)
        self.remove(text4_7)
        self.play(FadeIn(text4_4))
        self.wait(1.5)
        self.play(
            Write(dot4_1[0]),
            text4_4.shift, UP * 0.5
        )
        self.wait(0.25)
        self.play(Write(line4_1[0]))
        self.wait(0.25)
        self.play(Write(dot4_1[1]))
        self.wait(1.5)
        self.play(
            Uncreate(text4_4),
            Write(text4_5),
            dot4_1[0].shift, UP * 1,
            dot4_1[1].shift, UP * 1,
            line4_1[0].shift, UP * 1
        )
        self.wait(2.5)
        self.play(ReplacementTransform(group3, text4_6))
        self.wait(1.5)
        self.play(FadeOut(text4_6))

        #--5--
        self.play(Write(text5_1))
        self.wait(1.5)
        self.remove(text4_6)
        self.play(
            Write(dot5_1[0]),
            Write(dot5_1[1]),
            Write(line5_1[0]),
            # Write(line5_1[1]),
            text5_1.shift, UP * 1.5
        )
        self.wait(3)
        # Some BUG?
        # self.play(ReplacementTransform(group4, group5))
        self.play(FadeOut(group4))
        self.play(FadeIn(group5))
        self.wait(3)
        self.play(
            Write(text5_3),
            group5.shift, LEFT * 1
        )
        self.wait(2)
        self.play(
            Uncreate(text5_3),
            group5.shift, RIGHT * 1
        )
        self.wait(1)
        self.play(Write(background5_1))
        self.wait(2)
        # Arrow().set_color()
        self.play(
            Write(text5_2[0]),
            group5.shift, UP * 1,
            background5_1.shift, UP * 1
        )
        self.wait(0.75)
        self.play(
            Write(dot5_3),
            Write(dot5_4),
            line5_2[3].set_color_by_gradient, color5_1, color5_2
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[0], text5_2[1]),
            line5_2[3].set_color, WHITE,
            line5_2[4].set_color_by_gradient, color5_1, color5_2,
            dot5_3.move_to, RIGHT * 1 + UP * 1,
            dot5_4.move_to, DOWN * 1 + UP * 1
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[1], text5_2[2]),
            line5_2[4].set_color, WHITE,
            line5_2[5].set_color_by_gradient, color5_1, color5_2,
            dot5_3.move_to, DOWN * 1 + UP * 1,
            dot5_4.move_to, LEFT * 1 + UP * 1
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[2], text5_2[3]),
            line5_2[5].set_color, WHITE,
            line5_2[6].set_color_by_gradient, color5_1, color5_2,
            dot5_3.move_to, LEFT * 1 + UP * 1,
            dot5_4.move_to, UP * 1 + UP * 1
        )
        self.wait(0.75)
        self.play(
            ReplacementTransform(text5_2[3], text5_4),
            FadeOut(dot5_3),
            FadeOut(dot5_4),
            line5_2[3].set_color_by_gradient, color5_1, color5_2,
            line5_2[4].set_color_by_gradient, color5_1, color5_2,
            line5_2[5].set_color_by_gradient, color5_1, color5_2,
            line5_2[6].set_color_by_gradient, color5_1, color5_2
        )
        self.wait(2)
        self.play(
            ReplacementTransform(text5_4, text5_5)
        )
        self.wait(2)
        self.play(
            ReplacementTransform(group5, text5_6),
            FadeOut(text5_5),
            background5_1.shift, ORIGIN
        )
        self.wait(0.25)
        self.play(Uncreate(background5_1))
        self.wait(2)
        self.play(FadeOut(text5_6))
        self.wait(1)

class s3(Scene):
    def construct(self):
        ad1.setScene(self)

        #--6--
        self.wait(1)
        # ad1.fadeInTitle("四  循环", subTitleText = "迷途，寻觅往返", tex2Color = {"循环": RED, "往返": PINK}, time = 2)
        # self.wait(1)
        self.play(Write(text6_1))
        self.wait(0.5)
        self.play(
            # Write(background6_2),
            Write(rectan6_1),
            text6_1.scale, 0.8,
            text6_1.next_to, rectan6_1
        )
        self.play(text6_1.shift, UP * 1.5)
        self.wait(1)
        self.play(Write(group6_1))
        self.wait(1.5)
        self.play(
            Write(background6_1),
            FadeIn(text6_2)
        )
        # self.play(Write(line6_2_1))
        self.wait(1)
        self.play(ReplacementTransform(text6_2, text6_2_1))
        self.wait(3)
        self.play(
            Uncreate(group6_1),
            Uncreate(background6_1),
            # FadeOut(line6_2_1),
            text6_2_1.scale, 0.75,
            text6_2_1.next_to, rectan6_1, direction = RIGHT
        )
        self.play(text6_2_1.shift, UP * 1)
        # line6_2_2.move_to(text6_2.get_center())
        # self.play(FadeIn(line6_2_2))
        self.wait(1)
        self.play(Write(text6_3))
        self.wait(3)
        self.play(
            text6_3.scale, 0.75,
            text6_3.next_to, rectan6_1, direction = RIGHT
        )
        self.play(text6_3.shift, UP * 1 + DOWN * 0.5)
        self.wait(1)
        self.play(Write(text6_4))
        self.wait(2)
        self.play(text6_4.move_to, DOWN * 3.5)
        self.wait(1.5)
        self.play(Write(text6_5))
        self.wait(1.5)
        self.play(
            Write(text6_6),
            Write(text6_7)
        )
        self.wait(1)
        self.play(
            Write(group6_2),
            Write(group6_3)
        )
        self.wait(4)
        self.play(
            Uncreate(group6_2),
            Uncreate(group6_3),
            Uncreate(text6_6),
            Uncreate(text6_7),
            Uncreate(text6_5),
            text6_4.scale, 0.75,
            text6_4.next_to, rectan6_1, direction = RIGHT
        )
        self.play(text6_4.shift, UP * 1 + DOWN * 1)
        self.wait(3)
        self.play(
            FadeOut(text6_1),
            FadeOut(text6_2_1),
            FadeOut(text6_3),
            FadeOut(text6_4),
            # FadeOut(line6_2_2),
            FadeOut(rectan6_1)
            # FadeOut(background6_2)
        )
        self.wait(1)

        # --7--
        ad1.fadeInTitle(
            "四  轨道图的分裂", 
            subTitleText = "天灯，欲裂乾坤", 
            tex2Color = {"分裂": RED, "裂": PINK}, 
            time = 2
        )
        self.wait(3)
        self.add(
            text7_1.move_to(LEFT * 16 + UP * 1.25),
            text7_2.move_to(LEFT * 16),
            text7_3.move_to(LEFT * 16 + DOWN * 1.25)
        )
        self.play(text7_1.shift, RIGHT * 16)
        self.play(text7_2.shift, RIGHT * 16)
        self.play(text7_3.shift, RIGHT * 16)
        self.play(
            text7_1.move_to, LEFT * 1 + UP * 1,
            text7_2.move_to, ORIGIN,
            text7_3.move_to, RIGHT * 1 + DOWN * 1
        )
        self.wait(3)
        self.play(
            FadeOut(text7_1),
            FadeOut(text7_2),
            FadeOut(text7_3)
        )
        self.wait(2)
        # self.play(text7_1.shift, UP * 2)
        
        self.play(FadeIn(text7_1_1))
        self.play(FadeIn(text7_1_2))
        self.wait(3)
        self.play(
            FadeOut(text7_1_1),
            FadeOut(text7_1_2)
        )
        self.wait(1.5)
        self.play(Write(group7_1))
        self.wait(2)

        # Many BUGs......

        # 注意：t_all要设置为$TIMER_S到$TIMER_E部分的Animate总时长，dt要设置为帧率
        # self.t_all = 15
        # self.cls = []
        # self.t = 0
        # self.dt = 1 / 15
        # def changeColor(obj):
        #     if self.cls == []:
        #         self.cls = ad1.getColorGradient(int(1 / self.dt) * self.t_all, color7_1)
        #     obj.set_color(self.cls[self.t])
        #     self.t = self.t + 1

        self.play(Write(dot7_4), run_time = 1)
        self.wait(1)
        self.play(Write(text7_4_1))
        self.wait(1.5)
        self.play(Write(dot7_5), run_time = 1)
        # dot7_4.add_updater(changeColor)
        # TIMER_S
        self.wait(2)
        self.play(
            dot7_4.move_to, UP * 1 + LEFT * 1 * m.sqrt(2),
            dot7_5.move_to, RIGHT * 1,
            run_time = 2
        )
        self.wait(1)
        self.play(Write(text7_4_2))
        self.wait(1)
        self.play(
            dot7_4.move_to, RIGHT * 1,
            dot7_5.move_to, LEFT * 1,
            run_time = 2
        )
        self.wait(0.5)
        self.play(Write(text7_4_3))
        self.wait(1)
        self.play(
            dot7_4.move_to, LEFT * 1,
            dot7_5.move_to, RIGHT * 1,
            run_time = 2
        )
        self.wait(0.5)
        self.play(Write(text7_4_4))
        self.wait(1)
        self.play(
            dot7_4.move_to, DOWN * 1 + RIGHT * 1 * m.sqrt(2),
            dot7_5.move_to, LEFT * 1,
            run_time = 2
        )
        self.wait(0.5)
        self.play(Write(text7_4_5))
        self.wait(4)
        # TIMER_E
        # dot7_4.remove_updater(changeColor)
        self.play(
            FadeOut(dot7_4),
            FadeOut(dot7_5)    
        )
        
        # self.play(Uncreate(group7_1))
        self.play(
            ReplacementTransform(dot7_1[0], dot7_2[0]),
            ReplacementTransform(dot7_1[2], dot7_2[1]),
            ReplacementTransform(dot7_1[4], dot7_2[2]),
            ReplacementTransform(dot7_1[6], dot7_2[3]),
            ReplacementTransform(dot7_1[8], dot7_2[4]),
            *[FadeIn(i) for i in line7_2],
            run_time = 4
        )
        self.wait(2.5)
        self.play(
            ReplacementTransform(dot7_2[0], dot7_1a[0]),
            ReplacementTransform(dot7_2[1], dot7_1a[2]),
            ReplacementTransform(dot7_2[2], dot7_1a[4]),
            ReplacementTransform(dot7_2[3], dot7_1a[6]),
            ReplacementTransform(dot7_2[4], dot7_1a[8]),
            *[FadeOut(i) for i in line7_2],
            run_time = 1
        )
        self.play(ReplacementTransform(group9_1, group9_2))
        self.wait(1.5)
        dot7_4.move_to(UP * 1 + LEFT * 2 * m.sqrt(2))
        dot7_5.move_to(UP * 1)
        self.play(
            Write(dot7_4),
            Write(dot7_5)
        )
        self.wait(2)
        self.play(
            dot7_4.move_to, UP * 1,
            dot7_5.move_to, DOWN * 1,
        )
        self.wait(2)
        self.play(
            dot7_4.move_to, DOWN * 1,
            dot7_5.move_to, UP * 1,
        )
        self.wait(2)
        self.play(
            dot7_4.move_to, DOWN * 1 + RIGHT * 2 * m.sqrt(2),
            dot7_5.move_to, DOWN * 1,
        )
        self.wait(2.5)
        self.play(
            ReplacementTransform(dot7_1[1], dot7_3[0]),
            ReplacementTransform(dot7_1[3], dot7_3[1]),
            ReplacementTransform(dot7_1[5], dot7_3[2]),
            ReplacementTransform(dot7_1[7], dot7_3[3]),
            *[FadeIn(i) for i in line7_3],
            run_time = 3
        )
        self.wait(2)
        self.play(
            ReplacementTransform(dot7_3[0], dot7_1a[1]),
            ReplacementTransform(dot7_3[1], dot7_1a[3]),
            ReplacementTransform(dot7_3[2], dot7_1a[5]),
            ReplacementTransform(dot7_3[3], dot7_1a[7]),
            *[FadeOut(i) for i in line7_3],
            run_time = 1
        )

        self.play(
            FadeOut(dot7_4),
            FadeOut(dot7_5),
            ReplacementTransform(dot7_1a[0], dot7_2a[0]),
            ReplacementTransform(dot7_1a[2], dot7_2a[1]),
            ReplacementTransform(dot7_1a[4], dot7_2a[2]),
            ReplacementTransform(dot7_1a[6], dot7_2a[3]),
            ReplacementTransform(dot7_1a[8], dot7_2a[4]),
            *[FadeIn(i) for i in line7_2],
            run_time = 2
        )
        self.wait(1)
        self.play(
            ReplacementTransform(dot7_1a[1], dot7_3a[0]),
            ReplacementTransform(dot7_1a[3], dot7_3a[1]),
            ReplacementTransform(dot7_1a[5], dot7_3a[2]),
            ReplacementTransform(dot7_1a[7], dot7_3a[3]),
            *[FadeIn(i) for i in line7_3],
            run_time = 2
        )
        self.play(FadeOut(group9_2))
        self.wait(1)
        # self.play(*[FadeIn(i) for i in line7_3])
        self.play(
            *[FadeOut(i) for i in line7_1],
            group7_2.shift, UP * 2.5,
            group7_3.shift, UP * 2.5
        )
        # self.wait(0.5)
        # self.play(*[FadeOut(i) for i in line7_1])
        self.wait(3)
        
        self.play(Write(text7_6))
        self.wait(1.5)
        self.play(
            Write(text7_7_1),
            Write(text7_7_2),
            Write(background7_1),
            Write(background7_2)
        )
        self.wait(2.5)
        text7_1.move_to(UP * 2).scale(1.1)
        self.play(Write(text7_1))
        self.wait(4)
        self.play(
            Uncreate(group7_2), 
            Uncreate(group7_3),
            Uncreate(text7_1),
            Uncreate(text7_6),
            Uncreate(text7_7_1),
            Uncreate(text7_7_2),
            Uncreate(background7_1),
            Uncreate(background7_2)
        )
        
        

# class test(Scene):
#     def construct(self):
#         t = Tex("\\text{i: }f\\text{的一个}2m\\text{循环轨道图可分裂为两个}f_{2}\\text{的}m\\text{循环轨道图}")
#         self.add(t)
#         self.wait(3)
#         self.remove(t)
#         self.add(text7_1)
#         self.wait(3)
#         # self.add(text7_1)
#         # self.wait(5)





