from manim import *
import numpy as np

# init functions & range
alf = 2*PI
rng = np.array([1/1000, alf])

# curve
def curve(u):
    return np.array([np.cos(u), np.sin(u), 0])

def spunkt_f(u):
    return 1/u * np.array([np.sin(u), 1 - np.cos(u), 0])

class MoveAlongPathAnimationEffect(Scene):
    def construct(self):

        # add axes and paramtric form
        ax = Axes(x_range=[-1, 1, 1/2], y_range=[-1, 1, 0.5], axis_config={"include_numbers": True}, x_length=5, y_length=5, tips=False)
        func = MathTex(r"\begin{pmatrix} \cos(t) \\ \sin(t) \end{pmatrix}, \quad t \in [0, 2 \pi]", font_size=24).next_to(ax, RIGHT)
        self.add(ax, func)

        
        u = ValueTracker(rng[0])

        # create curves for curve path and schwerpunkt curve path
        path = ax.plot_parametric_curve(
            curve,
            color=PURPLE,
            t_range=rng,
            stroke_width=2,
            stroke_opacity=0.5
        )


        s_curve = ax.plot_parametric_curve(
            spunkt_f,
            color=BLUE,
            t_range=rng,
            stroke_width=1,
            stroke_opacity=0.5,
        )

        # Add moving points on curve and schwerpunkt curve
        dot = always_redraw(lambda: Dot(ax.coords_to_point(*curve(u.get_value())), color=RED))
        spunkt = always_redraw(lambda: Dot(ax.coords_to_point(*spunkt_f(u.get_value())), color=BLUE))

        self.play(Write(VGroup(path, s_curve, dot, spunkt)))


        # Add traces to points
        c_trace = TracedPath(dot.get_center, stroke_color=PURPLE)
        s_trace = TracedPath(spunkt.get_center, stroke_color=BLUE)
        self.add(VGroup(c_trace, s_trace))


        # add some text (t = updating number)
        var_ind = MathTex("t = ", font_size=24).next_to(func, DOWN)

        # add number and updater
        decimal = DecimalNumber(
            rng[0],
            show_ellipsis=True,
            num_decimal_places=3,
            font_size=15
        ).next_to(dot)
        decimal.add_updater(lambda d: d.set_value(u.get_value()).next_to(var_ind, RIGHT))

        # add label to schwerpunkt
        label = always_redraw(lambda: Text("Schwerpunkt", font_size=18).next_to(spunkt))


        self.add(label, decimal, var_ind)
        self.play(u.animate.increment_value(rng[1]), rate_func=linear, run_time=10)
