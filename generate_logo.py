


from animation.transform import Transform
from mobject import Mobject
from mobject.tex_mobject import TextMobject
from topics.geometry import Circle
from topics.three_dimensions import Sphere
from scene import Scene

from helpers import *


class LogoGeneration(Scene):
    DEFAULT_CONFIG = {
        "radius"               : 1.5,
        "inner_radius_ratio"   : 0.55,
        "circle_density"       : 100,
        "circle_blue"          : "skyblue",
        "circle_brown"         : DARK_BROWN,
        "circle_repeats"       : 5,
        "sphere_density"       : 50,
        "sphere_blue"          : DARK_BLUE,
        "sphere_brown"         : LIGHT_BROWN,
        "interpolation_factor" : 0.3,
        "frame_duration"       : 0.01,
    }

    def construct(self):
        digest_config(self, {})
        circle = Circle(
            density = self.circle_density, 
            color   = self.circle_blue
        )
        circle.repeat(self.circle_repeats)
        circle.scale(self.radius)
        sphere = Sphere(
            density = self.sphere_density, 
            color   = self.sphere_blue
        )
        sphere.scale(self.radius)
        sphere.rotate(-np.pi / 7, [1, 0, 0])
        sphere.rotate(-np.pi / 7)
        iris = Mobject()
        Mobject.interpolate(
            circle, sphere, iris, 
            self.interpolation_factor
        )
        for mob, color in [(iris, self.sphere_brown), (circle, self.circle_brown)]:
            mob.highlight(color, lambda (x, y, z) : x < 0 and y > 0)
            mob.highlight(
                "black", 
                lambda point: np.linalg.norm(point) < \
                              self.inner_radius_ratio*self.radius
            )
        name = TextMobject("3Blue1Brown").center()
        name.highlight("grey")
        name.shift(2*DOWN)

        self.play(Transform(
            circle, iris, 
            run_time = DEFAULT_ANIMATION_RUN_TIME
        ))
        self.frames = drag_pixels(self.frames)
        self.set_frame_as_background()
        self.save_image()
        self.add(name)
        self.dither()
        print "Dragging pixels..."

