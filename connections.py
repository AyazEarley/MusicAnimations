from manim import *
import colorsys
import colors
import sounds
import updaters

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

cycleTime = 16

config.background_color = "#121212"

c = colors.magentaYellow

class Run(Scene):
    def construct(self):

        title1 = Text("Title", font="Corbel", gradient=c)
        title1.move_to([0,4.5,0])

        title2 = Text("subtitle 1", font="Corbel", gradient=c)
        title3 = Text("subtitle 2", font="Corbel", gradient=c)
        title2.move_to([0,-4.5,0])
        title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)

        def getAnimations(lo, hi):

            allAnimations = []

            circle = Circle(radius = 3.4, color=WHITE)
            circle.rotate(90 * DEGREES)
            self.add(circle)

            allDots = []

            for i in range(lo, hi + 1):
                dot = Dot(point = [-100,100,0], color = c[i-lo])
                dot.set_z_index(5)
                allDots.append(dot)
                self.add(dot)

                dotSeq = []
                for j in range(i):
                    move = MoveAlongPath(dot, circle, run_time=cycleTime / i, rate_func=linear)
                    ping = Succession(FadeToColor(circle, c[i - lo], run_time= 0), FadeToColor(circle, WHITE, run_time = 0.3))
                    dotSeq.append(AnimationGroup(move, ping))
                dotSeq.append(ApplyMethod(dot.set_opacity, 0, run_time = 0))
                allAnimations.append(Succession(*dotSeq))

            numDots = len(allDots)
            for p in range(numDots - 1):
                for k in range(p + 1, numDots):
                    connector = Line(start = [-100, 100, 0], end = [-100, 99, 0], stroke_color=[allDots[p].color, allDots[k].color])
                    self.add(connector)
                    updaters.connect_line_to_dots(connector, allDots[p], allDots[k])

            return AnimationGroup(*allAnimations)

        self.play(getAnimations(1,9))
        self.wait(0.5)