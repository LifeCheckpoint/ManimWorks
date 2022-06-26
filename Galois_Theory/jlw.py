#   MANIM-伽罗瓦理论
#   
#   L        DDDDD    DDDDD    MM         MM  IIIII       A       OOOOOOOOO
#   L        D    D   D    D   M M       M M    I        A A      O       O
#   L        D     D  D     D  M  M     M  M    I       A   A     O       O
#   L        D     D  D     D  M   M   M   M    I      AAAAAAA    O       O
#   L        D    D   D    D   M    M M    M    I     A       A   O       O
#   LLLLLLL  DDDDD    DDDDD    M     M     M  IIIII  A         A  OOOOOOOOO 
#   
#   author: LDDMiao
#   date: 2021 - 8 - 17
#   version: V1.0.0
# 
#   你这代码保熟吗？

from manimlib.imports import *
from numpy import *
import cmath as cm
import random as ran

class s(Scene):
    def construct(self):
        ###-----第一节 伽罗瓦理论-----###
        Atext1 = Text(
            "伽罗瓦理论", 
            font = "微软雅黑", 
            gradient=(BLUE, GREEN, YELLOW, RED, BLACK, WHITE)
        )
        Atext2 = Text(
            "可以从3Blue1Brown的视频了解更多有关群的知识：\nhttps://www.bilibili.com/video/BV1Rh411R7KL", 
            font = "微软雅黑", 
            gradient=(BLUE, GREEN)
        )
        Atext3 = TextMobject(
            "考虑一个n次无重根多项式$f\\left( x\\right) =a_nx^n+a_{n-1}x^{n-1}+...+a_1x+a_0$", 
            color = RED
        )
        Atext3_t = TextMobject(
            "$a_n$      $a_{n-1}$      ...      $a_1$      $a_0$", 
            color = RED
        )
        Atext4 = TextMobject(
            "记$f\\left( x\\right)$的多项式域为$\\mathbb{F}=\\mathbb{Q}\\left( a_n,a_{n-1},...,a_1,a_0\\right)$", 
            color = RED
        )
        Agird1 = NumberPlane(
            background_line_style = {
                "stroke_color": GREY, 
                "stroke_opacity": 0.3
            }
        )
        Afunc1 = FunctionGraph(
            lambda x: (x - 2) * (x - 1) * (x + 1) * (x + 2) * (x + 3) * x * 0.4
        )
        Adot1 = Dot(
            array([-3, 0, 0])
        )
        Adot2 = Dot(
            array([-2, 0, 0])
        )
        Adot3 = Dot(
            array([-1, 0, 0])
        )
        Adot4 = Dot(
            array([0, 0, 0])
        )
        Adot5 = Dot(
            array([1, 0, 0])
        )
        Adot6 = Dot(
            array([2, 0, 0])
        )
        Atext4_1 = TextMobject(
            "$\\alpha _1$", 
            color = YELLOW
        )
        Atext4_2 = TextMobject(
            "$\\alpha _2$", 
            color = YELLOW
        )
        Atext4_3 = TextMobject(
            "$\\alpha _3$", 
            color = YELLOW
        )
        Atext4_4 = TextMobject(
            "$\\alpha _4$", 
            color = YELLOW
        )
        Atext4_5 = TextMobject(
            "$\\alpha _5$", 
            color = YELLOW
        )
        Atext4_6 = TextMobject(
            "$\\alpha _6$", 
            color = YELLOW
        )
        Atext5 = TextMobject(
            "记$f\\left( x\\right)$的根分别为$\\alpha _1,\\alpha _2,...\\alpha _n$", 
            color = RED
        )
        Atext6 = TextMobject(
            "再记$\\mathbb{E}=\\mathbb{F}\\left( \\alpha _1,\\alpha _2,...\\alpha _n\\right)$为$f\\left( x\\right)$的分裂域", 
            color = RED
        )
        Atext7 = TextMobject(
            "接着研究$f\\left( x\\right)$上根的置换", 
            color = GREEN
        )
        Atext7_t = TextMobject(
            "接着研究$f\\left( x\\right)$上根的置换", 
            color = GREEN
        )
        Atext7_1 = TextMobject(
            "即，我们希望存在一个映射$\\sigma$，使得$\\sigma \\left( \\alpha _i\\right) =\\alpha _j$", 
            color = GREEN
        )
        #2(-2)-5(1) 3(-1)-6(2)
        arc1 = Arc(
            arc_center = array([-0.5, 0, 0]),
            color = PURPLE,
            start_angle = 190 * DEGREES,
            angle = 160 * DEGREES,
            radius = 1.5
        ).add_tip(at_start = True)
        arc2 = Arc(
            arc_center = array([0.5, 0, 0]),
            color = PURPLE,
            start_angle = 190 * DEGREES,
            angle = 160 * DEGREES,
            radius = 1.5
        ).add_tip(at_start = True)
        Atext7_2 = TextMobject(
            "$\\sigma$",
            color = PURPLE_C
        )
        Atext7_1_t = TextMobject(
            "即，我们希望存在一个映射$\\sigma$，使得$\\sigma \\left( \\alpha _i\\right) =\\alpha _j$", 
            color = GREEN
        )
        Atext8 = TextMobject(
            "注意到，若$\\sigma$能使$\\sigma \\left( f\\left( x\\right) \\right)=a_n{\\sigma \\left( x\\right)} ^n+a_{n-1}{\\sigma \\left( x\\right)} ^{n-1}+...+a_1{\\sigma \\left( x\\right)} +a_0$", 
            color = GREEN
        )
        Atext8_t = TextMobject(
            "注意到，若$\\sigma$能使$\\sigma \\left( f\\left( x\\right) \\right)=a_n{\\sigma \\left( x\\right)} ^n+a_{n-1}{\\sigma \\left( x\\right)} ^{n-1}+...+a_1{\\sigma \\left( x\\right)} +a_0$", 
            color = GREEN
        )
        Atext9 = TextMobject(
            "则$\\sigma \\left( f\\left( x\\right) \\right)$的根也是$\\alpha _1,\\alpha _2,...\\alpha _n$", 
            color = GREEN
        )
        Atext10 = Text(
            "可以得到一些关于σ的性质，如：", 
            font = "微软雅黑", 
            color = YELLOW
        )
        Atext11 = TexMobject(
            """
            \\begin{aligned}
            \\sigma \\left( \\mu _1+\\mu _2\\right)&=\\sigma \\left( \\mu _1\\right) +\\sigma \\left( \\mu _2\\right)\\\\
            \\sigma \\left( \\mu _1\\mu _2\\right)&=\\sigma \\left( \\mu _1\\right) \\sigma \\left( \\mu _2\\right)\\\\
            \\forall \\lambda \\in \\mathbb{F} \\subset \\mathbb{E} ,\\sigma \\left( \\lambda \\right) &=\\lambda \\text{即}\\sigma \\text{在} \\mathbb{F} \\text{中是一个恒等映射}
            \\end{aligned}
            """,
        color = YELLOW
        )
        Atext12 = TextMobject(
            "只有满足这三条才是一个合格的$\\sigma$，可以代入加以验证", 
            color = YELLOW
        )
        Atext13 = TextMobject(
            "根据第二条，可以得出$\\sigma$是$\\mathbb{E}$到$\\mathbb{E}$上的一个域同构", 
            color = YELLOW
        )
        Atext14 = TextMobject(
            "定义$\\mathbb{E}$在$\\mathbb{F}$上的伽罗瓦群$G=\\operatorname{Gal}(\\mathbb{E} / \\mathbb{F})=\\{\\sigma: \\mathbb{E} \\rightarrow \\mathbb{E} \\mid \\sigma(a)=a, \\forall a \\in \\mathbb{F}\\}$",
        color = BLUE
        )
        Atext15 = TextMobject(
            "另外，$f\\left( x\\right)$的根一共有$A_n^n=n!$种置换方式，如：",
            color = WHITE
        )
        Atext15_1 = TextMobject(
            "对换$\\alpha _1\\alpha _2\\alpha _3\\alpha _4\\alpha _5\\alpha _6$",
            color = WHITE
        )
        Atext15_2 = TextMobject(
            "对换$\\alpha _3\\alpha _2\\alpha _1\\alpha _4\\alpha _5\\alpha _6$",
            color = WHITE
        )
        Atext15_3 = TextMobject(
            "三轮换$\\alpha _1\\alpha _2\\alpha _3\\alpha _4\\alpha _5\\alpha _6$",
            color = WHITE
        )
        Atext15_4 = TextMobject(
            "三轮换$\\alpha _1\\alpha _5\\alpha _2\\alpha _4\\alpha _3\\alpha _6$",
            color = WHITE
        )
        Atext15_5 = TextMobject(
            "六轮换$\\alpha _1\\alpha _2\\alpha _3\\alpha _4\\alpha _5\\alpha _6$",
            color = WHITE
        )
        Atext15_6 = TextMobject(
            "六轮换$\\alpha _2\\alpha _3\\alpha _4\\alpha _5\\alpha _6\\alpha _1$",
            color = WHITE
        )
        Atext15_7_1 = TextMobject(
            "就像小球一样",
            color = WHITE
        )
        l = 1
        ACircle1 = []
        Agroup3 = VGroup()
        while l <= 5:
            ACircle1.append(Circle(
                arc_center = (2 + 0.5 * (l - 1)) * RIGHT + DOWN * 0.5,
                radius = 0.2,
                color = "#" + hex(ran.randint(16,255))[2:] + hex(ran.randint(16,255))[2:] + hex(ran.randint(16,255))[2:],
                fill_color = "#" + hex(ran.randint(16,255))[2:] + hex(ran.randint(16,255))[2:] + hex(ran.randint(16,255))[2:],
                fill_opacity = 1
            ))
            Agroup3.add(ACircle1[l - 1])
            l = l + 1
        Atext15_7 = TextMobject(
            "这些置换构成n次对称群$S_n$",
            color = WHITE
        )
        Agroup1 = VGroup(
            Atext15_2, 
            Atext15_4, 
            Atext15_6
        )
        Atext16 = Text(
            "可是，交换这些根，\n对解方程有什么实际作用呢？",
            font = "微软雅黑",
            color = WHITE
        )
        Atext17 = TextMobject(
            "一个一元n次方程，都有韦达定理：", 
            color = RED
        )
        Atext18 = TexMobject(
            r"""
            \begin{cases}
            &x_1+x_2+...+x_n=-\frac{\alpha _1}{\alpha _0}\\
            &x_1x_2+x_1x_3+...+x_{n-1}x_n=\frac{\alpha _2}{\alpha _0}\\
            &...\\
            &x_1x_2...x_n=\left( -1 \right) ^n\frac{\alpha _n}{\alpha _0}
            \end{cases}
            """, 
            color = RED
        )
        Atext19 = TextMobject(
            "据拉格朗日的思路，这n个多项式是对称多项式，无法直接得到方程的根", 
            color = RED
        )
        Atext19_1 = TextMobject(
            "比如，交换$x_1,x_2$，结果还是一样的", 
            color = RED
        )
        Atext20 = TextMobject(
            "需要找一个不对称的多项式，且这个表达式能由系数表示出来，才能求得解", 
            color = RED
        )
        Atext21 = Text(
            "以二次方程为例",
            font = "微软雅黑", 
            color = ORANGE
        )
        Atext22 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2=-\frac{b}{a}\\
	            x_1x_2=\frac{c}{a}\\
            \end{cases}
            """, 
            color = ORANGE
        )
        Atext23 = TexMobject(
            r"""
            \begin{cases}
            	x_2+x_1=-\frac{b}{a}\\
            	x_2x_1=\frac{c}{a}\\
            \end{cases}
            """, 
            color = ORANGE
        )
        Atext23_1 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2=-\frac{b}{a}\\
	            x_1x_2=\frac{c}{a}\\
            \end{cases}
            """, 
            color = ORANGE
        )
        Atext24 = TextMobject(
            "交换其中的变量，值不变，是对称多项式", 
            color = ORANGE
        )
        Atext25 = TextMobject(
            "但是如$x_1-x_2$一类的多项式，交换变量后其值改变", 
            color = ORANGE
        )
        Atext25_1 = TextMobject(
            "只需要知道$x_1-x_2$与系数的关系，就可以与$x_1+x_2$联立，求得$x_1$和$x_2$", 
            color = ORANGE
        )
        Atext25_2 = TextMobject(
            "这个关系，容易凑出来：$\\sqrt{\\left( x_1+x_2\\right) ^2-4x_1x_2}=x_1-x_2$", 
            color = ORANGE
        )
        Atext26 = TextMobject(
            "但是，它在$\\mathbb{F}$上没有意义！", 
            color = GREEN
        )
        Atext26_1 = TextMobject(
            "没有意义？", 
            color = GREEN
        )
        Atext27 = TextMobject(
            "试想，若只用 + - × ÷ 和$x_2+x_1$，$x_2x_1$这两个式子，能表示出$x_1-x_2$吗？", 
            color = GREEN
        )
        Atext28 = TextMobject(
            "显然不能", 
            color = GREEN
        )
        Atext29 = Text(
            "所以我们需要“扩域”",
            font = "微软雅黑"
        )
        Atext29_1 = Text(
            "扩域，就是把一个域，变得更大了",
            font = "微软雅黑"
        )
        Atext30 = TextMobject(
            "再举一个例子，三次方程$ax^3+bx^2+cx+d=0$的韦达定理", 
            color = BLUE
        )
        Atext31 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3=-\frac{b}{a}\\
            	x_1x_2+x_2x_3+x_3x_1=\frac{c}{a}\\
            	x_1x_2x_3=-\frac{d}{a}\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext32 = TextMobject(
            "可以任意交换里面的变量，构成交换对称群$S_3$", 
            color = BLUE
        )
        Atext33 = TexMobject(
            r"""
            \begin{cases}
            	x_2+x_1+x_3=-\frac{b}{a}\\
            	x_2x_1+x_1x_3+x_3x_2=\frac{c}{a}\\
            	x_2x_1x_3=-\frac{d}{a}\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext34 = TexMobject(
            r"""
            \begin{cases}
            	x_3+x_2+x_1=-\frac{b}{a}\\
            	x_3x_2+x_2x_1+x_1x_3=\frac{c}{a}\\
            	x_3x_2x_1=-\frac{d}{a}\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext35 = TexMobject(
            r"""
            \begin{cases}
	            x_1+x_3+x_2=-\frac{b}{a}\\
	            x_1x_3+x_3x_2+x_2x_1=\frac{c}{a}\\
	            x_1x_3x_2=-\frac{d}{a}\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext36 = TextMobject(
            "假如添加一个多项式$x_1+x_2-x_3$，需要“扩域”才能得到它的系数表达式", 
            color = BLUE
        )
        Atext36_1 = TextMobject(
            "需要扩张出一个什么样的域$\\mathbb{F}$呢？", 
            color = BLUE
        )
        Atext37 = TextMobject(
            r"$\mathbb{F} \left( \sqrt{\left(\frac{27}{2} \cdot \frac{2 b^{3}-9 a b c+27 a^{2} d}{27 a^{3}}\right)^{2}+27\left(\frac{2 b^{3}-9 a b c+27 a^{2} d}{27 a^{3}}\right)^{3}},\sqrt[3]{\frac{27}{2}\cdot \frac{b^2-3ac}{3a^2}+\sqrt{\left( \frac{27}{2}\cdot \frac{2b^3-9abc+27a^2d}{27a^3} \right) ^2+27\left( \frac{2b^3-9abc+27a^2d}{27a^3} \right) ^3}}\right)$", 
            color = BLUE
        )
        Atext39 = TextMobject(
            "在加入多项式$x_1+x_2-x_3$后，联立", 
            color = BLUE
        )
        Atext40 = TexMobject(
            r"""
            \begin{cases}
	            x_1+x_2+x_3\\
	            x_1+x_2-x_3\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext41 = TextMobject(
            "这时候可置换的情况变少了", 
            color = BLUE
        )
        Atext42 = TextMobject(
            "置换群也变小，成为$S_3$的子群", 
            color = BLUE
        )
        Atext43 = TexMobject(
            r"""
            \begin{cases}
	            x_2+x_1+x_3\\
	            x_2+x_1-x_3\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext44 = TexMobject(
            r"""
            \begin{cases}
	            x_1+x_2+x_3\\
	            x_1+x_2-x_3\\
            \end{cases}
            """, 
            color = BLUE
        )
        Atext46 = TexMobject(
            r"""
            \text{置换群为}\left( e,\left( \begin{matrix}
	            1&		2&		3\\
	            2&		1&		3\\
            \end{matrix} \right) \right) 
            """, 
            color = BLUE
        )
        Atext47 = TextMobject(
            "同样的，对于多项式方程$f\\left( x\\right) =0$", 
            color = GREY
        )
        Atext48 = TextMobject(
            "若增加的不对称多项式足够多，域扩的越大，则方程伽罗瓦群会越小", 
            color = GREY
        )
        Atext48_1 = TextMobject(
            "并且，当方程的伽罗瓦群只剩下恒等置换，则意味着此时方程可解，例如", 
            color = GREY
        )
        Atext49 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3\\
            	x_1+x_2-x_3\\
            	x_1-x_2+x_3\\
            \end{cases}
            """, 
            color = GREY
        )
        Atext49_1 = Text(
            "即使要进行交换\n也只能交换自身",
            font = "微软雅黑",
            color = GREY
        )
        Atext50 = TextMobject(
            "显而易见，若一方程的伽罗瓦群无法变小，则方程没有根式解", 
            color = GREY
        )
        Atext51 = Text(
            "一个方程的是否有根式解就是看\n能否在系数域中加上一些数的开方使其扩域\n有限项后将解包含起来",  
            color = GREY,
            font = "微软雅黑"
        )
        Atext52 = Text(
            "我们把这种操作定义为纯扩域",
            font = "微软雅黑",  
            color = WHITE
        )
        Atext53 = TextMobject(
            "$\\mathbb{K}=\\mathbb{F}\\left( k\\right) ,k\\in \\mathbb{K},k^m\\in\\mathbb{F}$",  
            color = WHITE
        )
        Atext54 = TextMobject(
            "将$\\mathbb{K}$称为$\\mathbb{F}$的m型扩域",  
            color = WHITE
        )
        Atext55 = TextMobject(
            "定义根式塔：由一个数域$\\mathbb{F}$不断扩域使得$\\mathbb{F}=\\mathbb{F}_0 \\subset \\mathbb{F}_1 \\subset ... \\subset \\mathbb{F}_{m+1}$",  
            color = WHITE
        )
        Atext56 = TextMobject(
            "若其中每个$\\mathbb{F}_{i+1}/\\mathbb{F}_i$都是纯扩域，则称这一列域为根式塔",  
            color = WHITE
        )
        Arec1 = Rectangle(
            height = 1,
            width = 2,
            color = '#66CCFF',
            opacity = 1.0,
            sheen_factor = 0.4,
            sheen_direction = UR
        )
        Arec2 = Rectangle(
            height = 1.2,
            width = 3,
            color = '#66CCFF',
            opacity = 0.8,
            sheen_factor = 0.4,
            sheen_direction = UR
        )
        Arec3 = Rectangle(
            height = 1.4,
            width = 4,
            color = '#66CCFF',
            opacity = 0.6,
            sheen_factor = 0.4,
            sheen_direction = UR
        )
        Arec4 = Rectangle(
            height = 1.6,
            width = 5,
            color = '#66CCFF',
            opacity = 0.4,
            sheen_factor = 0.4,
            sheen_direction = UR
        )
        Atext56_1 = TextMobject(
            "$\\mathbb{F}$",  
            color = YELLOW
        )
        Atext57 = TextMobject(
            "那么，一个方程的解是否能用根式表示就有了一个形式化的定义：",  
            color = RED
        )
        Atext58 = TextMobject(
            "$f\\left( x\\right)$有根式解$\\Leftrightarrow f\\left( x\\right)$的分裂域$\\mathbb{E} \\subset \\mathbb{F}_{m+1}$",  
            color = RED
        )
        Atext59 = TextMobject(
            "引入正规扩张的概念：若多项式环$\\mathbb{F}\\left[ x\\right]$里的一个多项式的分裂域为$\\mathbb{E}$，则称域扩张$\\mathbb{E}/\\mathbb{F}$是正规扩张",  
            color = RED
        )
        Atext60 = TextMobject(
            "若一个欲列构成根式塔，就必须要求相邻的$\\mathbb{F}_i$都是正规扩张",  
            color = RED
        )
        Atext61 = TextMobject(
            "随后，伽罗瓦证明了相邻的域扩张是正规扩域的充分必要条件是相邻的伽罗瓦群$Gal\\left( \\mathbb{E}/\\mathbb{F}_i\\right)$是$Gal\\left( \\mathbb{E}/\\mathbb{F}_{i-1}\\right)$的正规子群",  
            color = RED
        )
        Atext62 = TextMobject(
            "再引入可解群：",  
            color = PINK
        )
        Atext63 = TextMobject(
            "若一个有限群$G$存在一个递降正规子群列",  
            color = PINK
        )
        Atext64 = TextMobject(
            "$G=G_0\\rhd G_1\\rhd ...\\rhd G_n=e$",  
            color = PINK
        )
        Atext65 = TextMobject(
            "且商群$G_{i-1}/G_{i}$都是素数阶",  
            color = PINK
        )
        Atext66 = TextMobject(
            "则称$G$为一个可解群",  
            color = PINK
        )
        Atext67 = TextMobject(
            "（例如，$\\sqrt[4]{a}$可以拆成$\\sqrt{\\sqrt{a}}$，所以规定是素数阶）",  
            color = GREY
        )
        Agroup2 = VGroup(
            Atext62,
            Atext63,
            Atext64,
            Atext65,
            Atext66,
            Atext67,
        )
        Atext68 = Text(
            "可以得到伽罗瓦大定理：一个多项式方程是根式可解的当且仅当这个方程的伽罗瓦群是可解群", 
            font = "微软雅黑",  
            gradient=(BLUE, GREEN, YELLOW, RED, BLACK, WHITE)
        )

        Btext1 = TextMobject(
            "最后阶段：证明五次方程的伽罗瓦群不是可解群",  
            color = GREEN
        )
        Btext2 = TextMobject(
            "交错群$A_5$是五次方程的偶置换群",  
            color = GREEN
        )
        Btext2_1 = TextMobject(
            "而$S_5$正好可以由$C_2$（二阶循环群）和$A_5$群作用而成",  
            color = GREEN
        )
        Btext2_2 = TextMobject(
            "它可以表示成偶数个对换的乘积",  
            color = GREEN
        )
        Btext2_3 = TexMobject(
            r"""
            \left( \begin{matrix}
	            1&		2&		3&		4&		5\\
	            3&		2&		1&		5&		4\\
            \end{matrix} \right) =\left( \begin{array}{c}
            	1\\
            	3\\
            \end{array} \right) \left( \begin{array}{c}
            	4\\
            	5\\
            \end{array} \right) 
            """,  
            color = GREEN
        )
        Btext2_4 = TexMobject(
            r"""
            \left( \begin{matrix}
            	1&		2&		3&		4&		5\\
            	3&		5&		2&		4&		1\\
            \end{matrix} \right) =\left( \begin{array}{c}
            	1\\
            	5\\
            \end{array} \right) \left( \begin{array}{c}
            	2\\
            	3\\
            \end{array} \right) \left( \begin{array}{c}
            	3\\
            	1\\
            \end{array} \right) \left( \begin{array}{c}
            	5\\
            	2\\
            \end{array} \right) 
            """,  
            color = GREEN
        )
        Btext3 = TexMobject(
            r"""
            \begin{cases}
            	e&...\text{1个}\\
            	(ab)(cd)&...\text{15个}\\
            	(abc)&...\text{20个}\\
                (abcde)&...\text{24个}\\
            \end{cases}
            """,  
            color = GREEN
        )
        Btext4 = TextMobject(
            "一共有$\\frac{5!}{2}$个元素",  
            color = GREEN
        )
        Btext4_1 = TextMobject(
            "五次方程的置换有五种",  
            color = GREY
        )
        Btext5 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	            x_1x_2+x_1x_3+x_1x_4+x_1x_5+x_2x_3+x_2x_4+x_2x_5+x_3x_4+x_3x_5+x_4x_5=\frac{a_2}{a_0}\\
	            x_1x_2x_3+x_1x_2x_4+x_1x_2x_5+x_2x_3x_4+x_2x_3x_5+x_3x_4x_5=-\frac{a_3}{a_0}\\
	            x_1x_2x_3x_4+x_1x_2x_3x_5+x_2x_3x_4x_5=\frac{a_4}{a_0}\\
	            x_1x_2x_3x_4x_5=-\frac{a_5}{a_0}\\
            \end{cases} 
            """,  
            color = WHITE
        )
        Btext6 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	            x_4x_2+x_4x_3+x_4x_1+x_4x_5+x_2x_3+x_2x_1+x_2x_5+x_3x_1+x_3x_5+x_1x_5=\frac{a_2}{a_0}\\
	            x_4x_2x_3+x_4x_2x_1+x_4x_2x_5+x_2x_3x_1+x_2x_3x_5+x_3x_1x_5=-\frac{a_3}{a_0}\\
	            x_4x_2x_3x_1+x_4x_2x_3x_5+x_2x_3x_1x_5=\frac{a_4}{a_0}\\
	            x_4x_2x_3x_1x_5=-\frac{a_5}{a_0}\\
            \end{cases} 
            """,  
            color = WHITE
        )#1,4
        Btext7 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	            x_4x_3+x_4x_5+x_4x_1+x_4x_2+x_3x_5+x_3x_1+x_3x_2+x_5x_1+x_5x_2+x_1x_2=\frac{a_2}{a_0}\\
	            x_4x_3x_5+x_4x_3x_1+x_4x_3x_2+x_3x_5x_1+x_3x_5x_2+x_5x_1x_2=-\frac{a_3}{a_0}\\
	            x_4x_3x_5x_1+x_4x_3x_5x_2+x_3x_5x_1x_2=\frac{a_4}{a_0}\\
	            x_4x_3x_5x_1x_2=-\frac{a_5}{a_0}\\
            \end{cases} 
            """,  
            color = WHITE
        )   #2,3,5
        Btext8 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	            x_1x_4+x_1x_5+x_1x_2+x_1x_3+x_4x_5+x_4x_2+x_4x_3+x_5x_2+x_5x_3+x_2x_3=\frac{a_2}{a_0}\\
	            x_1x_4x_5+x_1x_4x_2+x_1x_4x_3+x_4x_5x_2+x_4x_5x_3+x_5x_2x_3=-\frac{a_3}{a_0}\\
	            x_1x_4x_5x_2+x_1x_4x_5x_3+x_4x_5x_2x_3=\frac{a_4}{a_0}\\
	            x_1x_4x_5x_2x_3=-\frac{a_5}{a_0}\\
            \end{cases} 
            """,  
            color = WHITE
        )   #1,2,3,4
        Btext9 = TexMobject(
            r"""
            \begin{cases}
            	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	            x_2x_5+x_2x_1+x_2x_3+x_2x_4+x_5x_1+x_5x_3+x_5x_4+x_1x_3+x_1x_4+x_3x_4=\frac{a_2}{a_0}\\
	            x_2x_5x_1+x_2x_5x_3+x_2x_5x_4+x_5x_1x_3+x_5x_1x_4+x_1x_3x_4=-\frac{a_3}{a_0}\\
	            x_2x_5x_1x_3+x_2x_5x_1x_4+x_5x_1x_3x_4=\frac{a_4}{a_0}\\
	            x_2x_5x_1x_3x_4=-\frac{a_5}{a_0}\\
            \end{cases} 
            """,  
            color = WHITE
        )   #1,2,3,4,5
        Btext10_1 = TextMobject(
            "恒等置换",  
            color = RED
        )
        Btext10_2 = TextMobject(
            "2-置换",  
            color = YELLOW
        )
        Btext10_3 = TextMobject(
            "3-置换",  
            color = BLUE
        )
        Btext10_4 = TextMobject(
            "4-置换",  
            color = GREEN
        )
        Btext10_5 = TextMobject(
            "5-置换",  
            color = WHITE
        )
        BPolygon1 = Polygon(
            UP * 3,
            UP * 1.5 + LEFT * 3 * np.sqrt(3) / 2,
            DOWN * 1.5 + LEFT * 3 * np.sqrt(3) / 2,
            DOWN * 3,
            DOWN * 1.5 + RIGHT * 3 * np.sqrt(3) / 2,
            UP * 1.5 + RIGHT * 3 * np.sqrt(3) / 2
        )
        Btext27 = Text(
            "根据数学家的工作\n有限单群家族共有18族另26个",
            font = "微软雅黑"
        )   # https://zhuanlan.zhihu.com/p/261013192
        Bsquare1 = []
        Bgroup1 = VGroup()
        i = 1
        j = 1
        while i <= 18:
            while j <= 6:
                Bsquare1.append(Square(
                    color = '#66CCFF'
                ))
                Bsquare1[(i - 1) * 6 + (j - 1)].set_width(0.25)
                Bsquare1[(i - 1) * 6 + (j - 1)].shift(UP * 0.4 * (i - 8.5) + RIGHT * (2.75 + 0.25 * (j - 1)) + DOWN * 0.25)
                Bgroup1.add(Bsquare1[(i - 1) * 6 + (j - 1)])
                j = j + 1
            j = 1
            i = i + 1
        Bsquare2 = []
        Bgroup2 = VGroup()
        k = 1
        while k <= 26:
            Bsquare2.append(Square(
                color = YELLOW
            ))
            Bsquare2[k - 1].set_width(0.25)
            Bsquare2[k - 1].shift(UP * 0.25 * (k - 13) + RIGHT * 5)
            Bgroup2.add(Bsquare2[k - 1])
            k = k + 1
        Btext28 = TextMobject(
            "而$A_5$是其中一族中的一个"
        )
        Btext29 = TextMobject(
            "交错群$A_n$对于所有$n\\ge 5$都是单群，从而有$\\forall N,e\\ne N\\rhd A_5,N=A_5$"
        )
        Btext30 = TextMobject(
            "那么，我们可以得到如下关系："
        )
        Btext31 = TextMobject(
            "$S_5\\overset{2}{\\rhd}A_5\\overset{60}{\\rhd}\\left\\{e\\right\\}$"
        )
        Btext32 = TextMobject(
            "由于$A_5$是单群，没有非平凡正规子群，又因为$A_5$阶是60，为非素数"
        )
        Btext33 = TextMobject(
            "所以$A_5$不是可解群"
        )
        Btext34 = Text(
            "根据伽罗瓦定理，五次方程是根式不可解的",
            font = "微软雅黑",
            color = GREY
        )
        Btext35 = TextMobject(
            "不过，这并不代表着，五次方程没有解析解...",  
            color = GREY
        )
        Btext36 = Text(
            "感谢观看",
            font = "微软雅黑",
            gradient=(BLUE, GREEN)
        )
        Btext37 = Text(
            "求三连~",
            font = "微软雅黑",
            gradient=(YELLOW, RED)
        )

        ###形态设置###
        ###多项式###
        Atext3.shift(UP * 2).scale(0.6)
        Atext3_t.shift(UP * 1 + RIGHT * 2.5).scale(0.6)
        Atext4.shift(UP * 1)
        Atext4_1.shift(array([-3.2, 0.2, 0])).scale(0.6)
        Atext4_2.shift(array([-2.2, 0.2, 0])).scale(0.6)
        Atext4_3.shift(array([-1.2, 0.2, 0])).scale(0.6)
        Atext4_4.shift(array([-0.2, 0.2, 0])).scale(0.6)
        Atext4_5.shift(array([0.8, 0.2, 0])).scale(0.6)
        Atext4_6.shift(array([1.8, 0.2, 0])).scale(0.6)
        Atext5.shift(DOWN * 0.5)
        Atext6.shift(DOWN * 1.5)

        ###映射###
        Atext7.shift(UP * 1.5)
        Atext7_1.shift(UP * 0.6)
        Atext7_2.shift(LEFT * 0.5 + DOWN * 1.25).scale(0.5)
        Atext8.shift(DOWN * 0.5).scale(0.6)
        Atext9.shift(DOWN * 1.5)
        Atext7_t.shift(UP * 0.5)
        Atext7_1_t.shift(DOWN * 0.5)
        Atext8_t.shift(DOWN * 1.5).scale(0.6)

        ###σ性质###
        Atext10.shift(UP * 1.4).set_color_by_t2c({"σ": RED})
        Atext11.shift(ORIGIN).scale(0.7)
        Atext12.shift(DOWN * 1.5)
        Atext13.shift(DOWN * 2.5)

        ###置换方式###
        Atext14.shift(ORIGIN).scale(0.5)
        Atext15.shift(UP * 1.4)
        Atext15_1.shift(UP * 0.5)
        Atext15_2.shift(UP * 0.5)
        Atext15_3.shift(UP * -0.5)
        Atext15_4.shift(UP * -0.5)
        Atext15_5.shift(UP * -1.5)
        Atext15_6.shift(UP * -1.5)
        Atext15_7_1.shift(RIGHT * 2.5).scale(0.5)
        Atext15_7.shift(UP * 0.5 + RIGHT * 2.7).scale(0.6)
        Atext16.shift(DOWN * 0.5 + RIGHT * 2.7).scale(0.6)

        ###韦达定理###
        Atext17.shift(UP * 2.5)
        Atext18.shift(UP * 1).scale(0.7)
        Atext19.shift(DOWN * 0.75).scale(0.8)
        Atext19_1.shift(DOWN * 1.25).scale(0.6)
        Atext20.shift(DOWN * 1.75).scale(0.6)
        Atext21.shift(DOWN * 2.5).set_color_by_t2c({"二次方程": PINK})
        Atext22.shift(UP * 1.25)
        Atext23.shift(UP * 1.25)
        Atext23_1.shift(UP * 1.25)
        Atext24.shift(ORIGIN)
        Atext25.shift(DOWN * 1)
        Atext25_1.shift(DOWN * 1).scale(0.6)
        Atext25_2.shift(DOWN * 1.75).scale(0.5)

        ###扩域###
        Atext26.shift(DOWN * 2.5) #To UP * 2.5
        Atext26_1.shift(UP * 1.5)
        Atext27.shift(UP * 1.5).scale(0.8)
        Atext28.shift(UP * 0.5).scale(0.8)
        Atext29.shift(DOWN * 0.5).set_color_by_t2c({"扩域": RED})
        Atext29_1.shift(ORIGIN).set_color_by_t2c({"扩域": RED, "大": YELLOW})

        ###三次方程###
        Atext30.shift(UP * 2.5).scale(0.8)
        Atext31.shift(UP * 1.5).scale(0.6)
        Atext32.shift(UP * 0.5).scale(0.8)
        Atext33.shift(UP * 1.5).scale(0.6)
        Atext34.shift(UP * 1.5).scale(0.6)
        Atext35.shift(UP * 1.5).scale(0.6)
        Atext36.shift(DOWN * 0.5).scale(0.6)
        Atext36_1.shift(DOWN * 1.5)
        Atext37.shift(DOWN * 2.75).scale(0.45)
        Atext39.shift(DOWN * 0.5)   #TO UP * 2.5
        Atext40.shift(UP * 1.25) #TO LEFT * 2.7
        Atext41.shift(UP * 1.75 + RIGHT * 2.7).scale(0.6)
        Atext42.shift(UP * 1.25 + RIGHT * 2.7).scale(0.6)
        Atext43.shift(UP * 1.25 + LEFT * 2.7)
        Atext44.shift(UP * 1.25 + LEFT * 2.7)
        Atext46.shift(DOWN * 0.5).scale(0.8)

        ###同样的多项式方程###
        Atext47.shift(UP * 2.5)
        Atext48.shift(UP * 1.5).scale(0.6)
        Atext48_1.shift(UP * 0.5).scale(0.8)
        Atext49.shift(DOWN * 0.75).scale(0.8)   #TO LEFT * 2.5
        Atext49_1.shift(DOWN * 0.75 + RIGHT * 2.5)
        Atext50.shift(DOWN * 2).scale(0.6)
        Atext51.shift(DOWN * 2.75).scale(0.6)    #TO UP * 1.5
        Atext52.shift(UP * 0.5).scale(0.8).set_color_by_t2c({"纯扩域": RED})
        Atext53.shift(DOWN * 0.5).scale(0.6)
        Atext54.shift(DOWN * 1.5).scale(0.8)

        ###根式塔###
        Atext55.shift(ORIGIN).scale(0.8)
        Atext56.shift(DOWN * 1)
        Atext56_1.shift(DOWN * 2.25)
        Arec1.shift(DOWN * 2.25)
        Arec2.shift(DOWN * 2.25)
        Arec3.shift(DOWN * 2.25)
        Arec4.shift(DOWN * 2.25)

        ###方程可解性###
        Atext57.shift(UP * 2.5).scale(0.8)
        Atext58.shift(UP * 1.5).scale(0.8)
        Atext59.shift(UP * 0.5).scale(0.6)
        Atext60.shift(DOWN * 0.5).scale(0.8)
        Atext61.shift(DOWN * 1.5).scale(0.5)
        Atext62.shift(DOWN * 2.5)   #TO UP * 2.5
        Atext63.shift(UP * 1.5 + LEFT * 3.5).scale(0.6)
        Atext64.shift(UP * 1.5 + RIGHT * 3).scale(0.6)
        Atext65.shift(UP * 0.5)
        Atext66.shift(DOWN * 0.5)
        Atext67.shift(DOWN * 1.5).scale(0.6)
        Atext68.shift(ORIGIN).scale(0.6)

        ###五次方程不可解###
        Btext1.shift(UP * 0.5)
        Btext2.shift(UP * 2.75).scale(0.6)
        Btext2_1.shift(UP * 2.25).scale(0.6)
        Btext2_2.shift(UP * 1.75).scale(0.6)
        Btext2_3.shift(UP * 1).scale(0.8)
        Btext2_4.shift(UP * 1).scale(0.8)
        Btext3.shift(DOWN * 0.75).scale(0.7)
        Btext4.shift(DOWN * 2.5)
        Btext4_1.shift(LEFT * 3).scale(0.8)
        Btext5.shift(RIGHT * 2.6).scale(0.5)    #TO UP * 3
        Btext6.shift(RIGHT * 2.6).scale(0.5)    #TO UP * 1.5 + LEFT * 3 * sqrt(3) / 2
        Btext7.shift(RIGHT * 2.6).scale(0.5)    #TO DOWN * 1.5 + LEFT * 3 * sqrt(3) / 2
        Btext8.shift(RIGHT * 2.6).scale(0.5)    #TO DOWN * 1.5 + RIGHT * 3 * sqrt(3) / 2
        Btext9.shift(RIGHT * 2.6).scale(0.5)    #TO UP * 1.5 + RIGHT * 3 * sqrt(3) / 2
        Btext10_1.shift(UP * 3 + LEFT * 3).scale(0.8),
        Btext10_2.shift(UP * 1.5 + LEFT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        Btext10_3.shift(DOWN * 1.5 + LEFT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        Btext10_4.shift(DOWN * 1.5 + RIGHT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        Btext10_5.shift(UP * 1.5 + RIGHT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        BPolygon1.shift(ORIGIN).set_fill(
            color = YELLOW, 
            opacity = 0.4
        )   #TO LEFT * 3
        Btext27.shift(UP * 0.5 + LEFT * 3).scale(0.6)
        Btext28.shift(DOWN * 0.5 + LEFT * 3).scale(0.6)
        Btext29.shift(UP * 2.5).scale(0.6)
        Btext30.shift(UP * 1.5)
        Btext31.shift(UP * 0.5).scale(0.8)
        Btext32.shift(DOWN * 0.5).scale(0.8)
        Btext33.shift(DOWN * 1.5)
        Btext34.shift(DOWN * 2.5)   #TO ORIGIN
        Btext35.shift(DOWN * 0.5).scale(0.4)

        ###结尾###
        Btext36.shift(ORIGIN).scale(0.8)    #TO UP * 0.5
        Btext37.shift(DOWN * 0.5).scale(0.8)

        ###动画设置###
        ###标题###
        self.play(Write(Atext1))
        self.wait(5)
        self.play(Uncreate(Atext1))
        self.play(Write(Atext2))
        self.wait(3)
        self.play(Uncreate(Atext2))
        self.wait(2)

        ###多项式###
        self.play(Write(Agird1), run_time = 3)
        self.play(Write(Atext3))
        self.play(Write(Afunc1), run_time = 3)
        self.wait(3)
        self.play(TransformFromCopy(Atext3, Atext3_t))
        self.wait(1)
        self.play(ReplacementTransform(Atext3_t, Atext4))
        self.wait(5)
        self.play(TransformFromCopy(Atext4, Atext5))
        self.play(
            Write(Adot1), 
            Write(Atext4_1),
            run_time = 0.2
        )
        self.play(
            Write(Adot2),
            Write(Atext4_2),
            run_time = 0.2
        )
        self.play(
            Write(Adot3), 
            Write(Atext4_3),
            run_time = 0.2
        )
        self.play(
            Write(Adot4), 
            Write(Atext4_4),
            run_time = 0.2
        )
        self.play(
            Write(Adot5), 
            Write(Atext4_5),
            run_time = 0.2
        )
        self.play(
            Write(Adot6), 
            Write(Atext4_6),
            run_time = 0.2
        )
        self.wait(3)
        self.play(TransformFromCopy(Atext5, Atext6))
        self.wait(5)
        self.play(
            Atext3.scale, 0.55, 
            Atext4.scale, 0.45, 
            Atext5.scale, 0.45, 
            Atext6.scale, 0.45
        )
        self.play(
            Atext3.move_to, UP * 3.2 + LEFT * 3.5, 
            Atext4.move_to, UP * 2.8 + LEFT * 3.5, 
            Atext5.move_to, UP * 2.4 + LEFT * 3.5, 
            Atext6.move_to, UP * 2 + LEFT * 3.5
        )

        ###映射σ###
        self.play(Write(Atext7))
        self.wait(3)
        self.play(TransformFromCopy(Atext7, Atext7_t))
        self.play(ReplacementTransform(Atext7_t, Atext7_1))
        self.wait(5)
        self.play(
            Write(arc1),
            Write(Atext7_2)
        )
        self.play(
            Atext4_2.move_to, array([0.8, 0.2, 0]),
            Atext4_5.move_to, array([-2.2, 0.2, 0])
        )
        self.wait(1)
        self.play(
            Atext4_2.move_to, array([-2.2, 0.2, 0]),
            Atext4_5.move_to, array([0.8, 0.2, 0])
        )
        self.wait(2)
        self.play(
            ReplacementTransform(arc1, arc2),
            Atext7_2.shift, RIGHT * 1,
        )
        self.play(
            Atext4_3.move_to, array([1.8, 0.2, 0]), 
            Atext4_6.move_to, array([-1.2, 0.2, 0])
        )
        self.wait(1)
        self.play(
            Atext4_3.move_to, array([-1.2, 0.2, 0]), 
            Atext4_6.move_to, array([1.8, 0.2, 0])
        )
        self.wait(3)
        self.play(
            Uncreate(arc2),
            Uncreate(Atext7_2)
        )
        self.play(TransformFromCopy(Atext7_1, Atext7_1_t))
        self.play(ReplacementTransform(Atext7_1_t, Atext8))
        self.wait(5)
        self.play(TransformFromCopy(Atext8, Atext8_t))
        self.play(ReplacementTransform(Atext8_t, Atext9))
        self.wait(5)
        self.play(
            Atext7.scale, 0.55, 
            Atext7_1.scale, 0.45, 
            Atext8.scale, 0.6, 
            Atext9.scale, 0.45
        )
        self.play(
            Uncreate(Agird1),
            Uncreate(Afunc1),
            Uncreate(Adot1),
            Uncreate(Adot2),
            Uncreate(Adot3),
            Uncreate(Adot4),
            Uncreate(Adot5),
            Uncreate(Adot6),
            Uncreate(Atext4_1),
            Uncreate(Atext4_2),
            Uncreate(Atext4_3),
            Uncreate(Atext4_4),
            Uncreate(Atext4_5),
            Uncreate(Atext4_6),
            Atext7.move_to, UP * 3.2 + RIGHT * 3.5,
            Atext7_1.move_to, UP * 2.8 + RIGHT * 3.5,
            Atext8.move_to, UP * 2.4 + RIGHT * 3.5,
            Atext9.move_to, UP * 2 + RIGHT * 3.5,
            run_time = 2
        )
        self.wait(3)

        self.play(Write(Atext10))
        self.wait(3)
        self.play(Write(Atext11))
        self.wait(7)
        self.play(Write(Atext12))
        self.wait(3)
        self.play(Write(Atext13))
        self.wait(5)
        self.play(
            Atext10.scale, 0.4,
            Atext11.scale, 0.6,
            Atext12.scale, 0.4,
            Atext13.scale, 0.4,
        )
        self.play(
            Atext10.move_to, DOWN * 2 + LEFT * 3.5,
            Atext11.move_to, DOWN * 2.6 + LEFT * 3.5,
            Atext12.move_to, DOWN * 3.2 + LEFT * 3.5,
            Atext13.move_to, DOWN * 3.6 + LEFT * 3.5,
            run_time = 2
        )
        self.wait(3)
        self.play(Write(Atext14))
        self.wait(7)
        self.play(Atext14.scale, 0.8)
        self.play(
            Atext14.move_to, DOWN * 3.6 + RIGHT * 2.75,
            run_time = 2
        )
        self.wait(3)

        self.play(Write(Atext15))
        self.wait(3)
        self.play(Write(Atext15_1))
        self.wait(2)
        self.play(ReplacementTransform(Atext15_1, Atext15_2))
        self.wait(2)
        self.play(Write(Atext15_3))
        self.wait(2)
        self.play(ReplacementTransform(Atext15_3, Atext15_4))
        self.wait(2)
        self.play(Write(Atext15_5))
        self.wait(2)
        self.play(ReplacementTransform(Atext15_5, Atext15_6))
        self.wait(3)
        self.play(
            Atext15_2.scale, 0.8,
            Atext15_4.scale, 0.8,
            Atext15_6.scale, 0.8
        )
        self.play(
            Atext15_2.shift, LEFT * 2.5,
            Atext15_4.shift, LEFT * 2.5,
            Atext15_6.shift, LEFT * 2.5,
            run_time = 2
        )
        self.wait(3)
        self.play(Write(Agroup3))
        self.wait(3)
        self.play(Write(Atext15_7_1))
        l = 1
        while l <= 5:
            ca = ran.randint(0, 4)
            cb = ran.randint(0, 4)
            while ca == cb:
                ca = ran.randint(0, 4)
                cb = ran.randint(0, 4)
            cal = ACircle1[ca].get_arc_center()
            cbl = ACircle1[cb].get_arc_center()
            self.play(
                ACircle1[ca].move_to, cbl,
                ACircle1[cb].move_to, cal,
                run_time = 0.5
            )
            self.wait(0.5)
            self.play(
                ACircle1[ca].move_to, cal,
                ACircle1[cb].move_to, cbl,
                run_time = 0.5
            )
            self.wait(0.5)
            l = l + 1
        self.wait(2.5)
        self.play(
            Uncreate(Atext15_7_1),
            Agroup3.shift, DOWN * 2
        )
        self.play(Write(Atext15_7))
        self.wait(3)
        self.play(Write(Atext16))
        self.wait(5)

        self.play(
            FadeOut(Atext15),
            FadeOut(Atext15_7),
            FadeOut(Atext16),
            Uncreate(Agroup1),
            Uncreate(Agroup3)
        )
        self.play(
            Uncreate(Atext3),
            Uncreate(Atext4),
            Uncreate(Atext5),
            Uncreate(Atext6),
            Uncreate(Atext7),
            Uncreate(Atext7_1),
            Uncreate(Atext8),
            Uncreate(Atext9),
            Uncreate(Atext10),
            Uncreate(Atext11),
            Uncreate(Atext12),
            Uncreate(Atext13),
            Uncreate(Atext14),
        )
        self.wait(3)
        self.play(Write(Atext17))
        self.wait(1)
        self.play(Write(Atext18))
        self.wait(7)
        self.play(Write(Atext19))
        self.wait(3)
        self.play(Write(Atext19_1))
        self.wait(3)
        self.play(Write(Atext20))
        self.wait(3)
        self.play(Write(Atext21))
        self.wait(1)
        self.play(
            Uncreate(Atext17),
            Uncreate(Atext18),
            Uncreate(Atext19),
            Uncreate(Atext19_1),
            Uncreate(Atext20),
            Atext21.move_to, UP * 2.5,
            run_time = 2
        )
        self.wait(3)

        self.play(Write(Atext22))
        self.wait(3)
        self.play(Write(Atext24))
        self.wait(1)
        self.play(ReplacementTransform(Atext22, Atext23))
        self.wait(3)
        self.play(ReplacementTransform(Atext23, Atext23_1))
        self.wait(3)
        self.play(Write(Atext25))
        self.wait(3)
        self.play(ReplacementTransform(Atext25, Atext25_1))
        self.wait(5)
        self.play(Write(Atext25_2))
        self.wait(5)

        self.play(Write(Atext26))
        self.wait(1)
        self.play(
            Uncreate(Atext21),
            Uncreate(Atext23_1),
            Uncreate(Atext24),
            Uncreate(Atext25_1),
            Uncreate(Atext25_2),
            Atext26.move_to, UP * 2.5
        )
        self.wait(2)
        self.play(Write(Atext26_1))
        self.wait(2)
        self.play(FadeOut(Atext26_1))
        self.play(Write(Atext27))
        self.wait(5)
        self.play(Write(Atext28))
        self.wait(3)
        self.play(Write(Atext29))
        self.wait(3)
        self.play(
            Uncreate(Atext26),
            Uncreate(Atext27),
            Uncreate(Atext28),
            Uncreate(Atext29)
        )
        self.play(Write(Atext29_1))
        self.wait(4)
        self.play(Uncreate(Atext29_1))
        self.wait(3)

        self.play(Write(Atext30))
        self.wait(3)
        self.play(Write(Atext31))
        self.wait(5)
        self.play(Write(Atext32))
        self.wait(1)
        self.play(ReplacementTransform(Atext31, Atext33))
        self.wait(1.5)
        self.play(ReplacementTransform(Atext33, Atext34))
        self.wait(1.5)
        self.play(ReplacementTransform(Atext34, Atext35))
        self.wait(1.5)
        self.play(Write(Atext36))
        self.wait(3)
        self.play(Write(Atext36_1))
        self.wait(5)
        self.play(Write(Atext37))
        self.wait(5)
        self.play(
            Uncreate(Atext30),
            Uncreate(Atext32),
            Uncreate(Atext35),
            ReplacementTransform(Atext36, Atext39),
            Uncreate(Atext36_1),
            Uncreate(Atext37),
            run_time = 2
        )
        self.play(Atext39.move_to, UP * 2.5)
        self.wait(3)
        self.play(Write(Atext40))
        self.wait(3)
        self.play(Atext40.shift, LEFT * 2.7)
        self.play(Write(Atext41))
        self.wait(3)
        self.play(Write(Atext42))
        self.wait(3)
        self.play(ReplacementTransform(Atext40, Atext43))
        self.wait(1.5)
        self.play(ReplacementTransform(Atext43, Atext44))
        self.wait(1.5)
        self.play(Write(Atext46))
        self.wait(4)

        self.play(
            Uncreate(Atext39),
            Uncreate(Atext41),
            Uncreate(Atext42),
            Uncreate(Atext44),
            Uncreate(Atext46),
        )
        self.wait(1)

        self.play(Write(Atext47))
        self.wait(3)
        self.play(Write(Atext48))
        self.wait(4)
        self.play(Write(Atext48_1))
        self.wait(4)
        self.play(Write(Atext49))
        self.wait(3)
        self.play(
            Atext49.shift, LEFT * 2.5,
            Write(Atext49_1)
        )
        self.wait(3)
        self.play(
            Uncreate(Atext49_1),
            Atext49.shift, RIGHT * 2.5
        )
        self.play(TransformFromCopy(Atext47, Atext50))
        self.wait(5)
        self.play(Write(Atext51))
        self.wait(7)
        self.play(
            FadeOut(Atext47),
            Uncreate(Atext50),
            Uncreate(Atext48),
            Uncreate(Atext48_1),
            Uncreate(Atext49),
            Uncreate(Atext51),
            run_time = 2
            )
        self.wait(3)
        self.play(Write(Atext52))
        self.wait(3)
        self.play(Write(Atext53))
        self.wait(7)
        self.play(Write(Atext54))
        self.wait(3)
        self.play(
            Atext51.move_to, UP * 3.2,
            Atext52.move_to, UP * 2.8,
            Atext53.move_to, UP * 2,
            Atext54.move_to, UP * 1,
            run_time = 2
        )

        self.wait(3)
        self.play(Write(Atext55))
        self.wait(5)
        self.play(Write(Atext56))
        self.wait(3)
        self.play(
            Write(Arec1),
            Write(Atext56_1),
            run_time = 0.4
        )
        self.play(
            Write(Arec2),
            run_time = 0.4
        )
        self.play(
            Write(Arec3),
            run_time = 0.4
        )
        self.play(
            Write(Arec4),
            run_time = 0.4
        )
        self.wait(6)
        self.play(
            Uncreate(Atext52),
            Uncreate(Atext53),
            Uncreate(Atext54),
            Uncreate(Atext55),
            Uncreate(Atext56),
            Uncreate(Atext56_1),
            Uncreate(Arec4),
            Uncreate(Arec3),
            Uncreate(Arec2),
            Uncreate(Arec1),
            run_time = 2
        )
        self.wait(3)

        self.play(Write(Atext57))
        self.wait(3)
        self.play(Write(Atext58))
        self.wait(3)
        self.play(Write(Atext59))
        self.wait(7)
        self.play(Write(Atext60))
        self.wait(5)
        self.play(Write(Atext61))
        self.wait(5)
        self.play(Write(Atext62))
        self.wait(7)
        self.play(
            Atext57.shift, UP * 6,
            Atext58.shift, UP * 6,
            Atext59.shift, UP * 6,
            Atext60.shift, UP * 6,
            Atext61.shift, UP * 6,
            Atext62.move_to, UP * 2.5,
            run_time = 2
        )
        self.wait(3)
        self.play(Write(Atext63))
        self.wait(3)
        self.play(Write(Atext64))
        self.wait(3)
        self.play(Write(Atext65))
        self.wait(5)
        self.play(Write(Atext66))
        self.wait(3)
        self.play(Write(Atext67))
        self.wait(5)
        self.play(
            ReplacementTransform(Agroup2, Atext68),
            run_time = 2
            )
        self.wait(5)
        self.play(Uncreate(Atext68))

        self.play(Write(Btext1))
        self.wait(3)
        self.play(FadeOut(Btext1))
        self.wait(1)
        self.play(Write(Btext2))
        self.wait(3)
        self.play(Write(Btext2_1))
        self.wait(3)
        self.play(Write(Btext2_2))
        self.wait(3)
        self.play(Write(Btext3))
        self.wait(3)
        self.play(Write(Btext2_3))
        self.wait(3)
        self.play(ReplacementTransform(Btext2_3, Btext2_4))
        self.wait(3)
        self.play(Uncreate(Btext2_4))
        self.play(Btext3.shift, UP * 0.5)
        self.wait(3)
        self.play(Write(Btext4))
        self.wait(5)
        self.play(
            Uncreate(Atext57),
            Uncreate(Atext58),
            Uncreate(Atext59),
            Uncreate(Atext60),
            Uncreate(Atext61),
            Uncreate(Btext2),
            Uncreate(Btext2_1),
            Uncreate(Btext2_2),
            Uncreate(Btext3),
            Uncreate(Btext4)
        )
        self.wait(3)
        self.play(
            Write(BPolygon1),
            run_time = 2
        )
        self.play(BPolygon1.shift, LEFT * 3)
        self.wait(1)
        self.play(Write(Btext4_1))
        self.wait(3)
        self.play(Uncreate(Btext4_1))
        self.wait(1)
        self.play(Write(Btext5))
        self.wait(1)
        self.play(TransformFromCopy(Btext5, Btext10_1))
        self.wait(0.75)
        self.play(ReplacementTransform(Btext5, Btext6))
        self.wait(1)
        self.play(TransformFromCopy(Btext6, Btext10_2))
        self.wait(0.75)
        self.play(ReplacementTransform(Btext6, Btext7))
        self.wait(1)
        self.play(TransformFromCopy(Btext7, Btext10_3))
        self.wait(0.75)
        self.play(ReplacementTransform(Btext7, Btext8))
        self.wait(1)
        self.play(TransformFromCopy(Btext8, Btext10_4))
        self.wait(0.75)
        self.play(ReplacementTransform(Btext8, Btext9))
        self.wait(1)
        self.play(ReplacementTransform(Btext9, Btext10_5))
        self.wait(5)
        self.play(Write(Btext27))
        self.wait(3)
        self.play(Write(Btext28))
        self.wait(3)
        i = 1
        j = 1
        while i <= 18:
            self.play(
                Write(Bsquare1[(i - 1) * 6 + 0]),
                Write(Bsquare1[(i - 1) * 6 + 1]),
                Write(Bsquare1[(i - 1) * 6 + 2]),
                Write(Bsquare1[(i - 1) * 6 + 3]),
                Write(Bsquare1[(i - 1) * 6 + 4]),
                Write(Bsquare1[(i - 1) * 6 + 5]),
                run_time = 0.1
            )
            i = i + 1
        k = 1
        while k <= 26 / 2:
            self.play(
                Write(Bsquare2[2 * (k - 1)]),
                Write(Bsquare2[2 * (k - 1) + 1]),
                run_time = 0.1
            )
            k = k + 1
        self.wait(5)
        self.play(
            Uncreate(Btext10_1),
            run_time = 0.1
        )
        self.play(
            Uncreate(Btext10_2),
            run_time = 0.1
        )
        self.play(
            Uncreate(Btext10_3),
            run_time = 0.1
        )
        self.play(
            Uncreate(Btext10_4),
            run_time = 0.1
        )
        self.play(
            Uncreate(Btext10_5),
            run_time = 0.1
        )
        self.play(
            Uncreate(Btext27),
            Uncreate(Btext28),
            Uncreate(BPolygon1),
            Uncreate(Bgroup1),
            Uncreate(Bgroup2),
            run_time = 1
        )
        self.wait(1)
        self.play(Write(Btext29))
        self.wait(7)
        self.play(Write(Btext30))
        self.wait(3)
        self.play(Write(Btext31))
        self.wait(5)
        self.play(Write(Btext32))
        self.wait(5)
        self.play(Write(Btext33))
        self.wait(3)
        self.play(Write(Btext34))
        self.wait(3)
        self.play(
            Uncreate(Btext29),
            Uncreate(Btext30),
            Uncreate(Btext31),
            Uncreate(Btext32),
            Uncreate(Btext33),
            Btext34.move_to, ORIGIN,
            run_time = 2
        )
        self.play(
            Btext34.scale, 1.25,
            run_time = 5
        )
        self.wait(3)
        self.play(
            Write(Btext35),
            run_time = 2
        )
        self.wait(5)
        self.play(
            FadeOut(Btext34),
            FadeOut(Btext35),
            run_time = 3
        )

        self.play(FadeIn(Btext36))
        self.wait(1)
        self.play(
            Btext36.shift, UP * 0.5,
            FadeIn(Btext37)
        )
        self.wait(5)
        self.play(
            FadeOut(Btext36),
            FadeOut(Btext37)
        )
        self.wait(2)

# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# class tmp(Scene):
#     def construct(self):
        # Btext5 = TexMobject(
        #     r"""
        #     \begin{cases}
        #     	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	    #         x_1x_2+x_1x_3+x_1x_4+x_1x_5+x_2x_3+x_2x_4+x_2x_5+x_3x_4+x_3x_5+x_4x_5=\frac{a_2}{a_0}\\
	    #         x_1x_2x_3+x_1x_2x_4+x_1x_2x_5+x_2x_3x_4+x_2x_3x_5+x_3x_4x_5=-\frac{a_3}{a_0}\\
	    #         x_1x_2x_3x_4+x_1x_2x_3x_5+x_2x_3x_4x_5=\frac{a_4}{a_0}\\
	    #         x_1x_2x_3x_4x_5=-\frac{a_5}{a_0}\\
        #     \end{cases} 
        #     """
        # )
        # Btext6 = TexMobject(
        #     r"""
        #     \begin{cases}
        #     	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	    #         x_4x_2+x_4x_3+x_4x_1+x_4x_5+x_2x_3+x_2x_1+x_2x_5+x_3x_1+x_3x_5+x_1x_5=\frac{a_2}{a_0}\\
	    #         x_4x_2x_3+x_4x_2x_1+x_4x_2x_5+x_2x_3x_1+x_2x_3x_5+x_3x_1x_5=-\frac{a_3}{a_0}\\
	    #         x_4x_2x_3x_1+x_4x_2x_3x_5+x_2x_3x_1x_5=\frac{a_4}{a_0}\\
	    #         x_4x_2x_3x_1x_5=-\frac{a_5}{a_0}\\
        #     \end{cases} 
        #     """
        # )#1,4
        # Btext7 = TexMobject(
        #     r"""
        #     \begin{cases}
        #     	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	    #         x_4x_3+x_4x_5+x_4x_1+x_4x_2+x_3x_5+x_3x_1+x_3x_2+x_5x_1+x_5x_2+x_1x_2=\frac{a_2}{a_0}\\
	    #         x_4x_3x_5+x_4x_3x_1+x_4x_3x_2+x_3x_5x_1+x_3x_5x_2+x_5x_1x_2=-\frac{a_3}{a_0}\\
	    #         x_4x_3x_5x_1+x_4x_3x_5x_2+x_3x_5x_1x_2=\frac{a_4}{a_0}\\
	    #         x_4x_3x_5x_1x_2=-\frac{a_5}{a_0}\\
        #     \end{cases} 
        #     """
        # )   #2,3,5
        # Btext8 = TexMobject(
        #     r"""
        #     \begin{cases}
        #     	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	    #         x_1x_4+x_1x_5+x_1x_2+x_1x_3+x_4x_5+x_4x_2+x_4x_3+x_5x_2+x_5x_3+x_2x_3=\frac{a_2}{a_0}\\
	    #         x_1x_4x_5+x_1x_4x_2+x_1x_4x_3+x_4x_5x_2+x_4x_5x_3+x_5x_2x_3=-\frac{a_3}{a_0}\\
	    #         x_1x_4x_5x_2+x_1x_4x_5x_3+x_4x_5x_2x_3=\frac{a_4}{a_0}\\
	    #         x_1x_4x_5x_2x_3=-\frac{a_5}{a_0}\\
        #     \end{cases} 
        #     """
        # )   #1,2,3,4
        # Btext9 = TexMobject(
        #     r"""
        #     \begin{cases}
        #     	x_1+x_2+x_3+x_4+x_5=-\frac{a_1}{a_0}\\
	    #         x_2x_5+x_2x_1+x_2x_3+x_2x_4+x_5x_1+x_5x_3+x_5x_4+x_1x_3+x_1x_4+x_3x_4=\frac{a_2}{a_0}\\
	    #         x_2x_5x_1+x_2x_5x_3+x_2x_5x_4+x_5x_1x_3+x_5x_1x_4+x_1x_3x_4=-\frac{a_3}{a_0}\\
	    #         x_2x_5x_1x_3+x_2x_5x_1x_4+x_5x_1x_3x_4=\frac{a_4}{a_0}\\
	    #         x_2x_5x_1x_3x_4=-\frac{a_5}{a_0}\\
        #     \end{cases} 
        #     """
        # )   #1,2,3,4,5
        # Btext10_1 = TextMobject(
        #     "恒等置换"
        # )
        # Btext10_2 = TextMobject(
        #     "2-置换"
        # )
        # Btext10_3 = TextMobject(
        #     "3-置换"
        # )
        # Btext10_4 = TextMobject(
        #     "4-置换"
        # )
        # Btext10_5 = TextMobject(
        #     "5-置换"
        # )
        # BPolygon1 = Polygon(
        #     UP * 3,
        #     UP * 1.5 + LEFT * 3 * np.sqrt(3) / 2,
        #     DOWN * 1.5 + LEFT * 3 * np.sqrt(3) / 2,
        #     DOWN * 3,
        #     DOWN * 1.5 + RIGHT * 3 * np.sqrt(3) / 2,
        #     UP * 1.5 + RIGHT * 3 * np.sqrt(3) / 2
        # )
        # Btext27 = Text(
        #     "根据数学家的工作\n有限单群家族共有18族",
        #     font = "微软雅黑"
        # )
        # Btext28 = TextMobject(
        #     "而$A_5$是其中一族中的一个"
        # )

        # Btext5.shift(RIGHT * 3).scale(0.5)    #TO UP * 3
        # Btext6.shift(RIGHT * 3).scale(0.5)    #TO UP * 1.5 + LEFT * 3 * sqrt(3) / 2
        # Btext7.shift(RIGHT * 3).scale(0.5)    #TO DOWN * 1.5 + LEFT * 3 * sqrt(3) / 2
        # Btext8.shift(RIGHT * 3).scale(0.5)    #TO DOWN * 1.5 + RIGHT * 3 * sqrt(3) / 2
        # Btext9.shift(RIGHT * 3).scale(0.5)    #TO UP * 1.5 + RIGHT * 3 * sqrt(3) / 2
        # Btext10_1.shift(UP * 3 + LEFT * 3).scale(0.8),
        # Btext10_2.shift(UP * 1.5 + LEFT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        # Btext10_3.shift(DOWN * 1.5 + LEFT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        # Btext10_4.shift(DOWN * 1.5 + RIGHT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        # Btext10_5.shift(UP * 1.5 + RIGHT * 3 * sqrt(3) / 2 + LEFT * 3).scale(0.8),
        # BPolygon1.shift(ORIGIN).set_fill(
        #     color = ORANGE, 
        #     opacity = 0.4
        # )   #TO LEFT * 3
        # Btext27.shift(UP * 0.5 + LEFT * 3).scale(0.6)
        # Btext28.shift(DOWN * 0.5 + LEFT * 3).scale(0.6)


        # self.play(
        #     Write(BPolygon1),
        #     run_time = 2
        # )
        # self.play(BPolygon1.shift, LEFT * 3)
        # self.wait(1)
        # self.play(Write(Btext5))
        # self.wait(3)
        # self.play(ReplacementTransform(Btext5, Btext10_1))
        # self.wait(3)
        # self.play(Write(Btext6))
        # self.wait(3)
        # self.play(ReplacementTransform(Btext6, Btext10_2))
        # self.wait(3)
        # self.play(Write(Btext7))
        # self.wait(3)
        # self.play(ReplacementTransform(Btext7, Btext10_3))
        # self.wait(3)
        # self.play(Write(Btext8))
        # self.wait(3)
        # self.play(ReplacementTransform(Btext8, Btext10_4))
        # self.wait(3)
        # self.play(Write(Btext9))
        # self.wait(3)
        # self.play(ReplacementTransform(Btext9, Btext10_5))
        # self.wait(5)
        # self.play(Write(Btext27))
        # self.wait(3)
        # self.play(Write(Btext28))
        # self.wait(5)
        # self.play(
        #     Uncreate(Btext10_1),
        #     run_time = 0.5
        # )
        # self.play(
        #     Uncreate(Btext10_2),
        #     run_time = 0.5
        # )
        # self.play(
        #     Uncreate(Btext10_3),
        #     run_time = 0.5
        # )
        # self.play(
        #     Uncreate(Btext10_4),
        #     run_time = 0.5
        # )
        # self.play(
        #     Uncreate(Btext10_5),
        #     run_time = 0.5
        # )
        # self.play(
        #     Uncreate(Btext27),
        #     Uncreate(Btext28),
        #     Uncreate(BPolygon1),
        #     run_time = 1
        # )
        # self.wait(1)

# class tmp2(Scene):
#     def construct(self):
#         self.play(Write(TextMobject(
#             "A",
#             color = "#" + hex(ran.randint(16,255))[2:] + hex(ran.randint(16,255))[2:] + hex(ran.randint(16,255))[2:]
#         )))