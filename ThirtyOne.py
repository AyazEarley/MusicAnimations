from manim import *
import colorsys
import updaters
import colors
import sounds

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


config.background_color = "#121212"

titleColors = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]

cycleTime = 30
WIDTH = 7
HEIGHT = 2.5

class Run(Scene):
    def construct(self):

        title1 = Text("Take a scroll break!", font="Corbel", gradient=colors.cyanMagenta)
        title1.move_to([0,4.5,0])

        title2 = Text("Relax with me <3", font="Corbel", gradient=colors.cyanMagenta)
        #title3 = Text("subtitle 2", font="Corbel", gradient=colors.lightGreenLightBlue)
        title2.move_to([0,-4.5,0])
        #title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)

        def getAnimations(n, st):

            line = Line(start=[-WIDTH / 2, 0, 0], end=[WIDTH / 2,0,0], color=WHITE)
            line.z_index = -1
            line.set_opacity(0.2)
            self.add(line)

            step = WIDTH / (n - 1)
            x = -WIDTH / 2

            previousDot = None

            allAnimations = []

            for i in range(st, st + n):
                dot = Dot(point = [x, HEIGHT, 0], color=colors.cyanMagenta[i-st])
                path1 = Line(start = [x, HEIGHT, 0], end = [x, 0, 0])
                path1.set_opacity(0)
                path2 = Line(start = [x, 0, 0], end = [x, -HEIGHT, 0])
                path2.set_opacity(0)
                self.add(dot)
                x += step

                if(previousDot != None):
                    connector = Line(start=[-100,100,0], end = [100,-100,0], color=[dot.color, previousDot.color])
                    connector.set_opacity(0.5)
                    self.add(connector)
                    updaters.connect_line_to_dots(connector, dot, previousDot)

                previousDot = dot

                moveTime = (cycleTime / i) / 4
                t = 0
                dotSequence = []
                for d in range(i):
                    
                    t += moveTime
                    dotSequence.append(MoveAlongPath(dot, path1, run_time= moveTime, rate_func=rate_functions.ease_in_sine))
                    dotSequence.append(ApplyMethod(path1.reverse_points, run_time=0))
                    self.add_sound(sounds.EDO31sharp11[14 -(i - st)], time_offset=t, gain=0.2)

                    t += moveTime
                    dotSequence.append(MoveAlongPath(dot, path2, run_time= moveTime, rate_func=rate_functions.ease_out_sine))
                    dotSequence.append(ApplyMethod(path2.reverse_points, run_time=0))

                    t += moveTime
                    dotSequence.append(MoveAlongPath(dot, path2, run_time= moveTime,rate_func=rate_functions.ease_in_sine))
                    dotSequence.append(ApplyMethod(path2.reverse_points, run_time=0))
                    self.add_sound(sounds.EDO31sharp11[ 14 - (i - st)], time_offset=t, gain=0.2)

                    t += moveTime
                    dotSequence.append(MoveAlongPath(dot, path1, run_time= moveTime, rate_func=rate_functions.ease_out_sine))
                    dotSequence.append(ApplyMethod(path1.reverse_points, run_time=0))

                allAnimations.append(Succession(*dotSequence))


            return AnimationGroup(*allAnimations)

        self.play(getAnimations(15, 5))
        self.wait(1)
