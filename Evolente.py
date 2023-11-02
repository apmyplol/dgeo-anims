from manim import *


import numpy as np

rng = np.array([0, 2*PI])

def c(u):
    return np.array([np.cos(u), np.sin(u), 0])

def cd(u):
    return np.array([-np.sin(u), np.cos(u), 0])

def evol(u):
    return c(u) - u * cd(u)

class curve(Scene):

    def construct(self):

        ax = Axes(x_range=[-5, 5, 1], y_range=[-5, 5, 1], axis_config={"include_numbers": True, "stroke_width":1, "tick_size": 0.05, "font_size":15}, x_length=5, y_length=5, tips=False)

        u = ValueTracker(rng[0])

        curve = ax.plot_parametric_curve(
            c,
            color=RED,
            t_range=rng,
            stroke_width=2,
            stroke_opacity=0.5
        )

        label_c = Text("Einheitskreis", color=RED).scale(0.25).next_to(curve, UP)


        evol_c = ax.plot_parametric_curve(
            evol,
            color=PURPLE,
            t_range=rng,
            stroke_width=2,
            stroke_opacity=0.5
        )

        label_e = Text("Evolente", color=PURPLE).scale(0.25).next_to(evol_c, UP)


        self.add(curve, evol_c, ax, label_c, label_e)


        # add number line
        l0 = NumberLine(
            x_range=rng,
            color=WHITE,
            label_direction=UP,
            stroke_width=1,
            font_size=15
        ).next_to(evol_c, DOWN)

        l0.add_labels({0: MathTex("0"), PI: MathTex(r"\pi"), 2*PI: MathTex(r"2\pi")})

        u_p = always_redraw(lambda: Dot(l0.n2p(u.get_value()), color=RED))
        self.add(u_p, l0)


        # point in curve
        c_p = always_redraw(lambda: Dot(ax.c2p(*c(u.get_value())), color=RED))

        evol_p = always_redraw(lambda: Dot(ax.c2p(*evol(u.get_value())), color=PURPLE))
        tang = always_redraw(lambda: Line(c_p.get_center(), evol_p.get_center(), color=BLUE, stroke_width=2, buff=0.05))

        self.add(c_p, evol_p, tang)


        self.play(u.animate(rate_func=linear).set_value(rng[1]), run_time=5)

