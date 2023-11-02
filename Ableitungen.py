from manim import *


import numpy as np

rng = np.array([0, 2*PI])

def c(u):
    return np.array([np.sin(u), np.sin(2*u), 0])

def cd(u):
    return np.array([np.cos(u), 2*np.cos(2*u), 0])

def c_dd(u):
    return np.array([-np.sin(u), -4*np.sin(2*u), 0])

class curve(Scene):

    def construct(self):

        u = ValueTracker(rng[0])

        curve = ParametricFunction(
            c,
            color=RED,
            t_range=rng,
            stroke_width=2,
            stroke_opacity=0.5
        )

        curve_d = ParametricFunction(
            cd,
            color=BLUE,
            t_range=rng,
            stroke_width=2,
            stroke_opacity=0.5
        )



        curve_dd = ParametricFunction(
            c_dd,
            color=PURPLE,
            t_range=rng,
            stroke_width=2,
            stroke_opacity=0.5
        )

        # curve_d.add_updater(lambda d: d.move_to(c(u.get_value())))
        # curve_dd.add_updater(lambda d: d.move_to(c(u.get_value())))

        l0 = NumberLine(
            x_range=rng,
            color=WHITE,
            label_direction=UP,
        ).next_to(curve_d, DOWN, buff=0.5)
        l0.add_labels({0: MathTex("0"), PI: MathTex(r"\pi"), 2*PI: MathTex(r"2\pi")})

        self.add(curve, curve_d, curve_dd, l0)

        # c3 = ParametricFunction(
        #     cs,
        #     color=PURPLE,
        #     t_range = rng
        # )


        zero = Dot(ORIGIN, color=WHITE)
        u_p = always_redraw(lambda: Dot(l0.number_to_point(u.get_value()), color=RED))
        self.add(u_p, zero)

        c_p = always_redraw(lambda: Dot(c(u.get_value()), color=RED))

        # points from center
        cd_p = always_redraw(lambda: Dot(cd(u.get_value()), color=BLUE))
        cdd_p = always_redraw(lambda: Dot(c_dd(u.get_value()), color=PURPLE))
        self.add(c_p, cd_p, cdd_p)

        # points from c_p
        # cd_p2 = always_redraw(lambda: Dot(c(u.get_value()) + cd(u.get_value()), color=BLUE))
        # cdd_p2 = always_redraw(lambda: Dot(c(u.get_value()) + c_dd(u.get_value()), color=PURPLE))
        # self.add(c_p, cd_p2, cdd_p2)


        # vectors from to c_p
        # p_cd = always_redraw(lambda: Arrow(c_p, cd_p2, stroke_width=2, color=BLUE, buff=0.05, max_tip_length_to_length_ratio=0.1))
        # p_cdd = always_redraw(lambda: Arrow(c_p, cdd_p2, stroke_width=2, color=PURPLE, buff=0.05, max_tip_length_to_length_ratio=0.1))
        # self.add(p_cd, p_cdd)


        # vectors from center
        a_c = always_redraw(lambda: Arrow(zero, c_p, stroke_width=2, color=RED, buff=0.05, max_tip_length_to_length_ratio=0.1))
        a_cd = always_redraw(lambda: Arrow(zero, cd_p, stroke_width=2, color=BLUE, buff=0.05, max_tip_length_to_length_ratio=0.1))
        a_cdd = always_redraw(lambda: Arrow(zero, cdd_p, stroke_width=2, color=PURPLE, buff=0.05, max_tip_length_to_length_ratio=0.1))
        self.add(a_c, a_cd, a_cdd)


        self.play(u.animate(rate_func=linear).set_value(rng[1]), run_time=10)



