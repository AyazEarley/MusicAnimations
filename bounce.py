from manim import *
import colorsys
import updaters
import colors
import sounds

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

WIDTH = 7
HEIGHT = -1.5
BOUNCEHEIGHT = 1.5
cycleTime = 15

config.background_color = "#121212"

titleColors = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]

class Run(Scene):
    def construct(self):

        title1 = Text("Frame perfect loop", font="Corbel", gradient=colors.whiteRed)
        title1.move_to([0,4.5,0])

        title2 = Text("Sub if you had fun :)", font="Corbel", gradient=colors.whiteRed)
        title3 = Text("subtitle 2", font="Corbel", gradient=colors.cyanMagenta[:5])
        title2.move_to([0,-4.5,0])
        title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)

        def getAnimations(n, strt):
            allAnimations = []

            line = Line(start = [-WIDTH / 2, HEIGHT - 0.1, 0], end = [WIDTH / 2, HEIGHT - 0.1, 0])
            line.set_opacity(0.5)
            self.add(line)

            x = -WIDTH / 2
            step = WIDTH / (n - 1)

            previousDot = None

            for i in range(n):
                dotSequence = []

                dot = Dot(point=[x,BOUNCEHEIGHT,0], color = colors.whiteRed[i], radius = 0.1)
                path = Line(start=[x,BOUNCEHEIGHT,0], end = [x,HEIGHT,0])
                path.set_opacity(0)
                self.add(path)
                x+= step
                self.add(dot)

                if(previousDot != None):
                    connector = Line(start=[-100,100,0], end = [100,-100,0], color=[dot.color, previousDot.color])
                    connector.set_opacity(0.5)
                    self.add(connector)
                    updaters.connect_line_to_dots(connector, dot, previousDot)
                
                previousDot = dot

                nBounce = i + strt
                moveTime = (cycleTime / nBounce) / 2
                t = 0
                for j in range(nBounce):

                    t += moveTime
                    dotSequence.append(MoveAlongPath(dot, path, run_time=moveTime, rate_func=rate_functions.ease_in_sine))
                    dotSequence.append(ApplyMethod(path.reverse_points, run_time=0))

                    self.add_sound(sounds.EDO31sharp11[i], time_offset=t)

                    t += moveTime
                    dotSequence.append(MoveAlongPath(dot, path, run_time=moveTime, rate_func=rate_functions.ease_out_sine))
                    dotSequence.append(ApplyMethod(path.reverse_points, run_time=0))

                allAnimations.append(Succession(*dotSequence))
            return AnimationGroup(*allAnimations)
        
        self.play(getAnimations(5, 7))

