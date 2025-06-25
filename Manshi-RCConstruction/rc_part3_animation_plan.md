# 动画计划：尺规作图、域维度与倍立方体 (细化版)

**文件：** `RCPart3.py` (或其他指定文件)

**目标：** 通过简洁的视觉动画，展示尺规作图与 2 的幂次维度之间的联系，并以此简洁地证明倍立方体的不可能性。

**动画流程：**

1.  **开场：尺规作图的起点**
    *   **物件：**
        *   `Compass` 对象 (`compass = Compass()`)
        *   `NumberLine` 作为数轴 (`axes_x = NumberLine()`)
        *   `Dot` 对象表示 0 和 1 (`dot_0 = Dot(axes_x.n2p(0))`, `dot_1 = Dot(axes_x.n2p(1))`)
        *   `Tex` 对象表示标签 "0" 和 "1" (`label_0 = Tex("0")`, `label_1 = Tex("1")`)
        *   `Tex` 对象表示域 \( \mathbb{Q} \) (`label_Q = Tex("\\mathbb{Q}")`)
    *   **动画：**
        *   `FadeIn(compass)` 或 `Write(compass)`
        *   `ShowCreation(axes_x)`
        *   `FadeIn(dot_0, dot_1)`
        *   `Write(label_0, label_1)`
        *   使用 `compass.move_niddle_tip_to(axes_x.n2p(0))` 和 `compass.set_span(axes_x.get_unit(1))` 设置圆规。
        *   `ShowCreation(Circle(arc_center=axes_x.n2p(0), radius=axes_x.get_unit(1)))` 绘制单位圆。
        *   `Write(label_Q)`

2.  **有理数域 \( \mathbb{Q} \) - 基本操作**
    *   **物件：**
        *   额外的 `Dot` 对象表示有理数（例如 `dot_a`, `dot_b`）
        *   `Vector` 对象示意加法和乘法
    *   **动画：**
        *   `FadeIn(dot_a, dot_b)` 在数轴上。
        *   动画 `dot_a.animate.shift(dot_b.get_center() - axes_x.n2p(0))` 示意加法 \( a+b \)。结果点落在数轴上。
        *   动画 `Transform(Vector(axes_x.n2p(a)), Vector(axes_x.n2p(n*a)))` 示意乘法 \( n \times a \)。结果向量终点落在数轴上。
        *   `Tex` 对象表示“维度 1” (`label_dim_1 = Tex("维度: 1")`)
        *   `Write(label_dim_1)`

3.  **第一次扩域：引入 \( \sqrt{2} \)**
    *   **物件：**
        *   `Square` 对象 (边长 1)
        *   `Line` 对象表示对角线
        *   `Line` 对象表示 \( \sqrt{2} \) 长度在数轴上
        *   `Dot` 对象表示 \( \sqrt{2} \) 在数轴上 (`dot_sqrt2 = Dot(axes_x.n2p(np.sqrt(2)))`)
        *   `NumberPlane` 对象 (二维坐标系)
        *   `Tex` 对象表示二维坐��轴标签 (`label_axis_Q1 = Tex("\\mathbb{Q} \\cdot 1")`, `label_axis_Qsqrt2 = Tex("\\mathbb{Q} \\cdot \\sqrt{2}")`)
        *   `Tex` 对象表示域 \( \mathbb{Q}(\sqrt{2}) \) (`label_Qsqrt2 = Tex("\\mathbb{Q}(\\sqrt{2})")`)
        *   `Dot` 对象表示 \( a + b\sqrt{2} \) 形式的点
        *   `Vector` 对象示意向量加法
    *   **动画：**
        *   `ShowCreation(Square(side_length=1))`
        *   `ShowCreation(Line(ORIGIN, UR))` (对角线)
        *   `Transform(Line(ORIGIN, UR), Line(axes_x.n2p(0), axes_x.n2p(np.sqrt(2))))` 将对角线长度转移到数轴。
        *   `FadeIn(dot_sqrt2)`
        *   `Transform(axes_x, NumberPlane())` 或相机移动/旋转过渡到二维平面。
        *   `Write(label_axis_Q1, label_axis_Qsqrt2)`
        *   `Write(label_Qsqrt2)`
        *   动画示意点 \( a+b\sqrt{2} \) 的构造：`ShowCreation(Vector(axes_x.n2p(a)))`, `ShowCreation(Vector(axes_y.n2p(b)))`, `ShowCreation(Vector(axes_x.n2p(a) + axes_y.n2p(b)))`。展示多个点填充平面。
        *   `Tex` 对象表示“维度 2” (`label_dim_2 = Tex("维度: 2")`)
        *   `Write(label_dim_2)`

4.  **迭代扩域与维度翻倍的可视化**
    *   **物件：**
        *   抽象图形序列（例如，从线段到正方形到立方体，或不断嵌套/扩展的抽象形状）
        *   `Arrow` 对象表示扩域过程，标注 \( \sqrt{\cdot} \)
        *   `Tex` 对象表示维度数字序列 (1, 2, 4, ..., \( 2^m \))
        *   `Tex` 对象突出最终维度 \( 2^m \) (`label_dim_2m = Tex("维度: 2^m")`)
    *   **动画：**
        *   动画展示抽象图形序列的演变。
        *   `GrowArrow` 并写入 \( \sqrt{\cdot} \) 标签。
        *   动画显示维度数字序列的出现和变化，可以使用 `TransformMatchingTex` 或简单的 `FadeIn` 和 `FadeOut`。
        *   `FadeIn(label_dim_2m)` 并突出显示。

5.  **倍立方体：不可作图的挑战**
    *   **物件：**
        *   `Cube` 对象 (边长 1)
        *   `Tex` 对象表示体积 1 (`label_vol_1 = Tex("体积: 1")`)
        *   `Tex` 对象表示体积 2 (`label_vol_2 = Tex("体积: 2")`)
        *   `Cube` 对象 (边长 \( \sqrt[3]{2} \))
        *   `Tex` 对象表示边长 \( \sqrt[3]{2} \) (`label_side_cbrt2 = Tex("边长: \\sqrt[3]{2}")`)
        *   `NumberLine` (回到数轴)
        *   `Dot` 对象表示 \( \sqrt[3]{2} \) 在数轴上 (`dot_cbrt2 = Dot(axes_x.n2p(2**(1/3)))`)
    *   **动画：**
        *   `FadeIn(Cube(side_length=1), label_vol_1)`
        *   `FadeIn(label_vol_2)`
        *   `Transform(Cube(side_length=1), Cube(side_length=2**(1/3)))`
        *   `FadeIn(label_side_cbrt2)`
        *   相机移动/旋转过渡回数轴。
        *   `FadeIn(dot_cbrt2)`
        *   动画示意尺规作图尝试构造 `dot_cbrt2`，例如使用 `Compass` 和 `Line` 的组合动画，但最终点无法精确落在 `dot_cbrt2` 位置，暗示失败。

6.  **包含 \( \sqrt[3]{2} \) 的域 \( \mathbb{Q}(\sqrt[3]{2}) \) 的维度**
    *   **物件：**
        *   抽象三维图形或分为三部分的抽象图形
        *   `Tex` 对象表示域 \( \mathbb{Q}(\sqrt[3]{2}) \) (`label_Qcbrt2 = Tex("\\mathbb{Q}(\\sqrt[3]{2})")`)
        *   `Tex` 对象表示维度 3 (`label_dim_3 = Tex("维度: 3")`)
    *   **动画：**
        *   `FadeIn` 抽象图形。
        *   `Write(label_Qcbrt2, label_dim_3)`

7.  **维度矛盾：2 的幂次 vs 3 的倍数**
    *   **物件：**
        *   代表维度 \( 2^m \) 的抽象图形副本
        *   代表维度 3 的抽象图形副本
        *   `Tex` 对象突出数字 2 和 3
        *   `Tex` 对象表示“矛盾！” (`label_contradiction = Tex("矛盾！")`)
    *   **动画：**
        *   将代表维度 \( 2^m \) 和维度 3 的图形移动到一起。
        *   动画示意它们之间的��兼容性（例如，一个图形无法被另一个“整除”）。
        *   突出显示数字 2 和 3。
        *   `FadeIn(label_contradiction)` 并闪烁或放大强调。

8.  **最终结论**
    *   **物件：**
        *   `Tex` 对象表示最终结论 (`label_final = Tex("倍立方体不可作图")`)
    *   **动画：**
        *   `Write(label_final)`