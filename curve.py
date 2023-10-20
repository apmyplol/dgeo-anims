from manim import *


import numpy as np

rng = np.array([1, 100])

def curve_f(u):
    return np.array([1/np.cosh(u), u-np.tanh(u), 0])

def cd(u):
    return np.array([-1/np.sinh(u)**2, np.tanh(u)**2, 0])

def cs(u):
    l = 1
    return curve_f(u) + l * cd(u)

class curve(Scene):

    def construct(self):
        ax = Axes()
        # labels = ax.get_axis_labels(
        #     Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45)
        # )
        self.add(ax)  # , labels)

        curve = ParametricFunction(
            curve_f,
            color=RED,
            t_range=rng
        )

        curve2 = ParametricFunction(
            cd,
            color=BLUE,
            t_range=rng
        )

        c3 = ParametricFunction(
            cs,
            color=PURPLE,
            t_range = rng
        )

        # bpoint = Dot(curve_f(rng[0]), color=BLUE)
        # bpoint = Dot(curve_f(rng[1]), color=GREEN)
        
        # axes = ThreeDAxes()
        self.add(curve, curve2, c3)
        # c = Circle()
        # self.add(bpoint)
        # self.play(Write(curve), run_time=2.0)
