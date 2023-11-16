from manim import *

u_rng = [-3, 3]
v_rng = [-3*PI, 0]

class ParaSurface(ThreeDScene):
    def func_1(self, u, v):
        return np.array([np.cosh(u) * np.cos(v), np.cosh(u) * np.sin(v), u])
    def func_2(self, u, v):
        return np.array([np.sinh(u) * np.sin(v), -np.sinh(u) * np.cos(v), v])

    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8, axis_config={"include_numbers": True, }, tips=False)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func_2(u, v)),
            u_range=u_rng,
            v_range=v_rng,
            resolution=20,
            fill_opacity=0.9,
            stroke_width=0.1,
            checkerboard_colors=False,
            fill_color=WHITE,
        )

        surface.set_color_by_gradient([RED, GREEN])
        surface.set_fill_by_value(axes=axes, colorscale=[RED, GREEN], axis=2)
        self.add(surface)

        rng = 4

        v_color = color_gradient([RED_A, RED_E], rng+1)
        u_color = color_gradient([BLUE_A, BLUE_E], rng+1)


        for i in range(rng+1):
            u = u_rng[0] + i * (u_rng[1] - u_rng[0])/rng
            v = v_rng[0] + i * (v_rng[1] - v_rng[0])/rng
            c = ParametricFunction(
                lambda t: axes.c2p(*self.func_2(u, t)),
                t_range=[-3*PI, 2*PI],
                stroke_opacity =0.9,
                color=PURPLE
            )

            # c2 = ParametricFunction(
            #     lambda t: axes.c2p(*self.func_2(t, v)),
            #     t_range=u_rng,
            #     color = u_color[i]
            # )
            self.add(c)

            # if i == 10 or i == 0:
            #     lab_u = MathTex(f"u = {u}").next_to(c, LEFT).set_shade_in_3d(True)
            #     # lab_v = MathTex(f"v = {v}", font_size=50).next_to(c2, UP)
            #     # self.add_fixed_in_frame_mobjects(lab_u)
            #     self.add(lab_u)

        self.set_camera_orientation(theta=0 * DEGREES, phi=80 * DEGREES)
        self.camera.set_zoom(0.3)
