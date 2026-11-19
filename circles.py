from manim import *
import colorsys
import colors
import updaters
import sounds

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16

RADIUS = 3.5
cycleTime = 32
PINGCOLOR = WHITE
PINGTIME = 0.35

config.background_color = "#121212"

titleColors = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]

class Run(Scene):
    def construct(self):

        title1 = Text("Sound Hypnosis", font="Corbel", gradient=colors.lightGreenLightBlue)
        title1.move_to([0,4.5,0])

        title2 = Text("Sub if you had fun :)", font="Corbel", gradient=colors.lightGreenLightBlue)
        title3 = Text("subtitle 2", font="Corbel", gradient=["#ff00cc", WHITE])
        title2.move_to([0,-4.5,0])
        title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)

        def getAnimations(min, max):
            n = max - min
            step = RADIUS / n
            r = step

            angle = 0
            angleStep = (2 * np.pi) / n

            allAnimations = []

            previousDot = None
            for i in range(max, min):
                circleSequence = []

                circle = Circle(radius = r, color = colors.lightGreenLightBlue[i - min])
                r += step
                circle.rotate(np.pi / 2)
                circle.rotate(angle)

                circleSequence.append(Create(circle))
                circleSequence.append(ApplyMethod(circle.rotate, -angle, run_time=0))


                dot = Dot(point=[-100,-100,0], color = WHITE, radius = 0.07)
                dot.set_opacity(1)
                dot.set_z_index(5)
                self.add(dot)

                if(previousDot != None):
                    connector = Line(start=[-100,100,0], end = [100,-100,0], color=[dot.color, previousDot.color])
                    connector.set_opacity(0)
                    connector.set_z_index(4)
                    self.add(connector)
                    updaters.connect_line_to_dots(connector, dot, previousDot)
                                
                previousDot = dot

                moveTime = cycleTime / i
                t = 1
                for j in range(i):

                    pingSucc = Succession(FadeToColor(circle, PINGCOLOR, run_time = 0), FadeToColor(circle, colors.lightGreenLightBlue[i - min], run_time = PINGTIME))
                    circleSequence.append(
                        AnimationGroup(MoveAlongPath(dot, circle, run_time=moveTime, rate_func=linear), pingSucc)
                        )

                    self.add_sound(sounds.EDO31harp11[(i-min)], time_offset=t)
                    t += moveTime

                self.add_sound(sounds.EDO31harp11[(i-min)], time_offset=t)
                
                circleSequence.append(ApplyMethod(dot.set_opacity, 0, run_time=PINGTIME))
                circleSequence.append(ApplyMethod(circle.rotate, angle, run_time=0))
                circleSequence.append(Uncreate(circle))
                allAnimations.append(Succession(*circleSequence))

                angle += angleStep
            return AnimationGroup(*allAnimations)

        self.play(getAnimations(13,28))