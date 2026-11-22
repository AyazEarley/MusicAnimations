from manim import *
import colorsys
import colors
import sounds
import updaters

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

WIDTH = 6
HEIGHT = 1.5
BOTTOM = -1.5
cycleTime = 16

config.background_color = "#121212"

c = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]

c1 = colors.cyanMagenta
c2 = colors.redOrange


class Run(Scene):
    def construct(self):

        title1 = Text("How long until they line up?", font="Corbel", gradient=c1)
        title1.move_to([0,4,0])

        title2 = Text("Sub if you enjoyed :)", font="Corbel", gradient=c1)
        title3 = Text("subtitle 2", font="Corbel", gradient=c)
        title2.move_to([0,-4,0])
        title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)

        def getAnimations(lo, hi):
            n = hi - lo

            floor = Line(start=[(-WIDTH / 2) - 0.2, BOTTOM - 0.1, 0], end=[(WIDTH / 2) + 0.2, BOTTOM - 0.1, 0], color=WHITE)
            self.add(floor)

            x = -WIDTH / 2
            step = WIDTH / (n)
            x -= step

            allAnimations = []
            for i in range(lo, hi + 1):

                dot = Dot(point = [x,HEIGHT,0], color=c1[i-lo], radius = 0.1)
                self.add(dot)

                x += step

                path = Line(start=[x,HEIGHT,0], end=[x,BOTTOM,0])
                path.set_opacity(0)

                dotSequence = []

                t = 0
                for j in range(i):
                    dotSequence.append(AnimationGroup(
                        FadeToColor(dot, c1[i-lo], run_time=0),
                        MoveAlongPath(dot, path, run_time = (cycleTime / i) / 2, rate_func=rate_functions.ease_in_sine)
                    ))
                    dotSequence.append(ApplyMethod(path.reverse_points, run_time=0))

                    t += (cycleTime / i) / 2
                    self.add_sound(sounds.EDO31sharp11[i-lo + 1], time_offset=t)
                    t += (cycleTime / i) / 2

                    dotSequence.append(AnimationGroup(
                        FadeToColor(dot, c1[n - (i-lo)], run_time=0),
                        MoveAlongPath(dot, path, run_time = (cycleTime / i) / 2, rate_func=rate_functions.ease_out_sine)
                    ))
                    dotSequence.append(ApplyMethod(path.reverse_points, run_time=0))

                allAnimations.append(Succession(*dotSequence))

            return AnimationGroup(*allAnimations)

        self.play(getAnimations(4,17))

