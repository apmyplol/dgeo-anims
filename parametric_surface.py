from manim import *

u_rng = [-2, 2]
v_rng = [0, 2*PI]

class ParaSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([np.cosh(u) * np.cos(v), np.cosh(u) * np.sin(v), u])

    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8, axis_config={"include_numbers": True, }, tips=False)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=u_rng,
            v_range=v_rng,
            resolution=10,
            fill_opacity=0.2,
            checkerboard_colors=False,
            fill_color=WHITE
        )

        v_color = color_gradient([RED_A, RED_E], 11)
        u_color = color_gradient([BLUE_A, BLUE_E], 11)

        for i in range(11):
            u = u_rng[0] + i * (u_rng[1] - u_rng[0])/10
            v = v_rng[0] + i * (v_rng[1] - v_rng[0])/10
            c = ParametricFunction(
                lambda t: axes.c2p(*self.func(u, t)),
                t_range=v_rng,
                color = v_color[i]
            )

            c2 = ParametricFunction(
                lambda t: axes.c2p(*self.func(t, v)),
                t_range=u_rng,
                color = u_color[i]
            )
            self.add(c, c2)

            # if i == 10 or i == 0:
            #     lab_u = MathTex(f"u = {u}").next_to(c, LEFT).set_shade_in_3d(True)
            #     # lab_v = MathTex(f"v = {v}", font_size=50).next_to(c2, UP)
            #     # self.add_fixed_in_frame_mobjects(lab_u)
            #     self.add(lab_u)

        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.add(surface)
