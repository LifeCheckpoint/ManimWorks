# RCPart2 第二部分动画计划

**目标：** 通过动画展示域扩张的次数概念，从简单的扩张到更复杂的扩张，并通过具体的例子（元素的表示和乘法）来直观地说明扩张的次数。

**动画步骤：**

1.  **回顾有理数域 $\mathbb{Q}$：**
    *   **元素：**
        *   `domain_box`: 代表域的矩形框。
        *   `q_title`: Tex 对象，显示 "$\mathbb{Q}$"。
        *   `a_in_q`: Tex 对象，显示 "$a \in \mathbb{Q}$"，其中 'a' 红色。
        *   `q_degree`: Tex 对象，显示 "$[\mathbb{Q}:\mathbb{Q}]=1$"。
    *   **动画内容：**
        *   写入 `domain_box` 和 `q_title`。
        *   写入 `a_in_q`。
        *   写入 `q_degree`。
        *   等待。
        *   淡出所有元素。

2.  **引入域扩张 $\mathbb{Q}(\sqrt{2})$：**
    *   **元素：**
        *   `domain_box_sqrt2`: 代表域的矩形框。
        *   `q_sqrt2_title`: Tex 对象，显示 "$\mathbb{Q}(\sqrt{2})$"。
        *   `a_b_sqrt2_in_q_sqrt2`: Tex 对象，显示 "$a+b\sqrt{2} \in \mathbb{Q}(\sqrt{2})$"，其中 'a' 红色，'b' 绿色，`\sqrt{2}` 白色。
        *   `q_sqrt2_degree`: Tex 对象，显示 "$[\mathbb{Q}(\sqrt{2}):\mathbb{Q}]=2$"。
    *   **动画内容：**
        *   写入 `domain_box_sqrt2` 和 `q_sqrt2_title`。
        *   写入 `a_b_sqrt2_in_q_sqrt2`。
        *   写入 `q_sqrt2_degree`。
        *   等待。
        *   淡出所有元素。

3.  **引入域扩张 $\mathbb{Q}(\sqrt[3]{2})$：**
    *   **元素：**
        *   `domain_box_cbrt2`: 代表域的矩形框。
        *   `q_cbrt2_title`: Tex 对象，显示 "$\mathbb{Q}(\sqrt[3]{2})$"。
        *   `q_cbrt2_degree_q`: Tex 对象，显示 "$[\mathbb{Q}(\sqrt[3]{2}):\mathbb{Q}]$"。
    *   **动画内容：**
        *   写入 `domain_box_cbrt2` 和 `q_cbrt2_title`。
        *   写入 `q_cbrt2_degree_q`。
        *   等待。

4.  **展示 $\mathbb{Q}(\sqrt[3]{2})$ 的基和扩张次数：**
    *   **元素：**
        *   `cbrt2_mult`: Tex 对象，显示 "$2^{1/3} \times 2^{1/3} = 2^{2/3}$"。
        *   `cbrt2_basis`: Tex 对象，显示 "$1, 2^{1/3}, 2^{2/3}$"。
        *   `a_b_c_cbrt2_in_q_cbrt2`: Tex 对象，显示 "$a+b 2^{1/3}+c 2^{2/3} \in \mathbb{Q}(2^{1/3})$"，其中 'a' 红色，'b' 绿色，'c' 黄色，幂次部分白色。
        *   `q_cbrt2_degree`: Tex 对象，显示 "$[\mathbb{Q}(2^{1/3}):\mathbb{Q}]=3$"。
    *   **动画内容：**
        *   显示 `cbrt2_mult`。
        *   等待。
        *   淡出 `cbrt2_mult`。
        *   显示 `cbrt2_basis`。
        *   等待。
        *   淡出 `cbrt2_basis`。
        *   显示 `a_b_c_cbrt2_in_q_cbrt2`。
        *   将 `q_cbrt2_degree_q` 转换为 `q_cbrt2_degree`。
        *   等待。
        *   淡出所有元素。

5.  **引入域扩张 $\mathbb{Q}(\sqrt{2}, \sqrt{3})$：**
    *   **元素：**
        *   `domain_box_sqrt2_sqrt3`: 代表域的矩形框。
        *   `q_sqrt2_sqrt3_title`: Tex 对象，显示 "$\mathbb{Q}(\sqrt{2}, \sqrt{3})$"。
        *   `q_sqrt2_sqrt3_degree_q`: Tex 对象，显示 "$[\mathbb{Q}(\sqrt{2}, \sqrt{3}):\mathbb{Q}]$"。
    *   **动画内容：**
        *   写入 `domain_box_sqrt2_sqrt3` 和 `q_sqrt2_sqrt3_title`。
        *   写入 `q_sqrt2_sqrt3_degree_q`。
        *   等待。

6.  **展示 $\mathbb{Q}(\sqrt{2}, \sqrt{3})$ 的基和扩张次数：**
    *   **元素：**
        *   `sqrt2_sqrt3_mult`: Tex 对象，显示 "$\sqrt{2} \times \sqrt{3} = \sqrt{6}$"。
        *   `sqrt2_sqrt3_basis`: Tex 对象，显示 "$1, \sqrt{2}, \sqrt{3}, \sqrt{6}$"。
        *   `q_sqrt2_sqrt3_degree`: Tex 对象，显示 "$[\mathbb{Q}(\sqrt{2}, \sqrt{3}):\mathbb{Q}]=4$"。
    *   **动画内容：**
        *   显示 `sqrt2_sqrt3_mult`。
        *   等待。
        *   淡出 `sqrt2_sqrt3_mult`。
        *   显示 `sqrt2_sqrt3_basis`。
        *   等待。
        *   淡出 `sqrt2_sqrt3_basis`。
        *   将 `q_sqrt2_sqrt3_degree_q` 转换为 `q_sqrt2_sqrt3_degree`。
        *   等待。
        *   淡出所有元素。

**域扩张关系图 (Mermaid):**

```mermaid
graph TD
    Q["Q"] --> Q_sqrt2["Q(sqrt(2))"]
    Q --> Q_cbrt2["Q(cbrt(2))"]
    Q_sqrt2 --> Q_sqrt2_sqrt3["Q(sqrt(2), sqrt(3))"]
    Q_cbrt2 --> Q_sqrt2_sqrt3