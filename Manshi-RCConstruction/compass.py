from manimlib import *

get_angle = lambda c: np.angle(-c) + PI if not c/abs(c) == 1 else 0
convert_angle = lambda a: a if a>=0 else a + TAU

class Compass(VGroup):

    CONFIG = {
        'stroke_color': GREY_E,
        'fill_color': WHITE,
        'stroke_width': 2,
        'leg_length': 3,
        'leg_width': 0.12,
        'r': 0.2,
        'depth_test': True,
    }

    def __init__(self, span=2.5, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.span = span
        self.create_compass()
        for key, value in self.CONFIG.items():
            self.__setattr__(key, value)

    def create_compass(self):

        s, l, r, w = self.span, self.leg_length, self.r, self.leg_width
        self.theta = np.arcsin(s/2/l)

        self.c = Circle(radius=r, fill_color=self.fill_color, fill_opacity=1, stroke_color=self.stroke_color, stroke_width=self.stroke_width*5)
        c2 = Circle(radius=r+self.stroke_width*5/100/2, fill_opacity=0, stroke_color=self.fill_color, stroke_width=self.stroke_width)

        self.leg_1 = Polygon(ORIGIN, l * RIGHT, (l-w*np.sqrt(3)) * RIGHT + w * DOWN, w * DOWN,
                             stroke_width=0, stroke_color=self.fill_color, fill_color=self.stroke_color,
                             fill_opacity=1).rotate(-PI/2-self.theta, about_point=self.c.get_center())
        self.leg_2 = Polygon(ORIGIN, l * RIGHT, (l-w*np.sqrt(3)) * RIGHT + w * UP, w * UP,
                             stroke_width=0, stroke_color=self.fill_color, fill_color=self.stroke_color,
                             fill_opacity=1).rotate(-PI/2+self.theta, about_point=self.c.get_center())


        # self.leg_1, self.leg_2 = VGroup(leg_01, leg_11),  VGroup(leg_02, leg_12, pen_point)
        h = Line(UP * r, UP * (r + r * 1.8), stroke_color=self.stroke_color, stroke_width=self.stroke_width*6)

        self.head = VGroup(h, self.c, c2)
        self.add(self.leg_1, self.leg_2, self.head)
        self.move_to(ORIGIN)

        return self

    def get_niddle_tip(self):
        return self.leg_1.get_vertices()[1]

    def get_pen_tip(self):
        return self.leg_2.get_vertices()[1]

    def move_niddle_tip_to(self, pos):
        self.shift(pos-self.get_niddle_tip())
        return self

    def rotate_about_niddle_tip(self, angle=PI/2):
        self.rotate(angle=angle, about_point=self.get_niddle_tip())

    def get_span(self):
        # return self.span 如果进行了缩放而self.span没变会有问题
        return get_norm(self.get_pen_tip() - self.get_niddle_tip())

    def set_span(self, s):
        self.span = s
        l, r, w = self.leg_length, self.r, self.leg_width
        theta_new, theta_old = np.arcsin(s/2/l), self.theta
        sign = np.sign(get_angle(R3_to_complex(self.leg_2.get_vertices()[1] - self.leg_2.get_vertices()[0])) - get_angle(R3_to_complex(self.leg_1.get_vertices()[1] - self.leg_1.get_vertices()[0])))
        rotate_angle = 2 * (theta_new - theta_old) * sign
        self.leg_2.rotate(rotate_angle, about_point=self.c.get_center())
        self.theta=theta_new
        self.head.rotate(rotate_angle/2, about_point=self.c.get_center())
        self.rotate_about_niddle_tip(-rotate_angle/2)
        return self

    def set_compass(self, center, pen_tip):
        self.move_niddle_tip_to(center)
        self.set_span(get_norm(pen_tip - center))
        self.rotate_about_niddle_tip(np.angle(R3_to_complex(pen_tip - center)) - np.angle(R3_to_complex(self.get_pen_tip() - center)))
        return self

    def set_compass_to_draw_arc(self, arc):
        return self.set_compass(arc.arc_center, arc.get_start())

    def reverse_tip(self):
        return self.flip(axis=self.head[0].get_end() - self.head[0].get_start(), about_point=self.c.get_center())
