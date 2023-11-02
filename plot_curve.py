from manim import *
from manim.opengl import *


import numpy as np

rng = np.array([-5, 5])

def curve_f(u):
    return np.array([u, u**2])

def cd(u):
    return 1/np.sqrt(1 + 4*u**2) * np.array([-2*u, 1])

def parallelkurve(u, l):
    return curve_f(u) + l * cd(u)

class curve(Scene):

    def construct(self):
        # labels = ax.get_axis_labels(
        #     Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45)
        # )
        ax = Axes(axis_config={"include_numbers": True, "stroke_width":1, "tick_size": 0.05, "font_size":15}, tips=False, x_range=[-10, 10], y_range=[-5, 25])
        self.add(ax)  # , labels)


        # label_c = Text("Einheitskreis", color=PINK).scale(0.25).next_to(curve, UP)

        colors = [RED_A, RED_C, RED_E, PINK, BLUE_E, BLUE_C, BLUE_A]

        # pcurves = []
        # labels = []
        for i in range(-3, 4):
            temp_curve = ax.plot_parametric_curve(
                lambda u: parallelkurve(u, i),
                color=colors[i+3],
                t_range = rng
                
            )

            lab = MathTex(f"d = {i}", color=colors[i+3]).scale(0.30)
            lab.shift(ax.c2p(*parallelkurve(rng[0], i))).shift([0, 0.25, 0])
            self.add(temp_curve, lab)
            # pcurves.append(temp_curve)
