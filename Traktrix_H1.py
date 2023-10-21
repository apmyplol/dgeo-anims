from manim import *
import numpy as np

# init functions & range
rng = np.array([1/1000, 5])

# curve
def curve_f(u):
    return np.array([1/np.cosh(u), u-np.tanh(u), 0])

# derivative
def cd(u):
    return np.array([-np.sinh(u)/(np.cosh(u)**2), np.tanh(u)**2, 0])

# tangent function
def cs(u, x):
    return curve_f(u) + x * cd(u)

# value of x in cs such that the point is on the y-axis, i.e. x = 0
def l(u):
    return np.cosh(u) / np.sinh(u)


class MoveAlongPathAnimationEffect(Scene):
    def construct(self):

        # add axes and paramtric form
        ax = Axes(x_range=[0, 3, 1], y_range=[0, 5, 1], axis_config={"include_numbers": True}, x_length=3, y_length=5, tips=False)
        func = MathTex(r"\begin{pmatrix} \frac{1}{\cosh(u)} \\ u - \tanh(u) \end{pmatrix}, \quad u \in (0, \infty)", font_size=24).next_to(ax, RIGHT)
        self.add(ax, func)



        # init value tracker which is used to update Dots
        u = ValueTracker(rng[0])


        # plot parametric curve
        curve = ax.plot_parametric_curve(
            curve_f,
            color=RED,
            t_range=rng,
            stroke_width=2
        )

        self.play(Write(curve))
        self.wait()

        # draw dot on curve based on value tracker
        # and dot which is on the tangent & y axis
        dot = always_redraw(lambda: Dot(ax.coords_to_point(*curve_f(u.get_value())), color=BLUE))
        sp = always_redraw(lambda: Dot(ax.coords_to_point(*cs(u.get_value(), l(u.get_value()))), color=PURPLE))

        # draw line between these two points = tangent line in dot
        vec = always_redraw(lambda: Line(dot, sp, stroke_width=2))


        # add some text that |dot - sp| = 1
        br = Text("|", font_size=24).next_to(func, DOWN)
        pdot = Dot(color=PURPLE).next_to(br, RIGHT)
        t = Text("-", font_size=24).next_to(pdot)
        bdot = Dot(color=BLUE).next_to(t, RIGHT)
        br2 = Text("|", font_size=24).next_to(bdot, RIGHT)
        sol = Text("= 1", font_size=24).next_to(br2, RIGHT)


        # write & play
        self.play(Write(VGroup(dot, vec, sp, bdot, pdot, t, sol, br, br2)))
        self.play(u.animate.increment_value(rng[1]), rate_func=linear, run_time=10)
        self.wait()
