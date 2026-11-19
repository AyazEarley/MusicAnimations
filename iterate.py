from manim import *
import colorsys
import colors
import updaters
import sounds

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


config.background_color = "#121212"

titleColors = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]

class Run(Scene):
    def construct(self):

        title1 = Text("Stop Scrolling!", font="Corbel", gradient=colors.magentaYellow)
        title1.move_to([0,4.5,0])

        title2 = Text("I made this for you <3", font="Corbel", gradient=colors.magentaYellow)
        title3 = Text("and that's ok.", font="Corbel", gradient=colors.redGreenAlternate)
        title2.move_to([0,-4.5,0])
        #title3.move_to([0,4.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)

        RADIUS = 3.5

        c = colors.magentaYellow

        def getAnimations(n, cycleTime):
            allAnimations = []

            angle = 0
            angleStep = np.pi / n

            circle = Circle(radius = RADIUS, color = WHITE)
            self.add(circle)

            previousDot = None
            firstDot = None

            for i in range(n):
                line = Line(start=[-RADIUS,0,0], end = [RADIUS,0,0])
                line.set_opacity(0)
                self.add(line)
                line.rotate(angle)
                angle += angleStep

                waitTime = i * cycleTime + i * (cycleTime / (2 * n))

                dot = Dot(point = [-100,-100,0], color = c[i], radius=0.12)
                dot.set_opacity(0)
                dot.set_z_index(5)
                self.add(dot)
                dotSequence = []

                if(firstDot == None):
                    firstDot = dot

                if(previousDot != None):
                    connector = Line(start=[-100,-100,0], end=[-100,100,0], stroke_color=[ previousDot.color, dot.color])
                    self.add(connector)

                    updaters.connect_line_to_dots(connector, dot, previousDot)
                
                previousDot = dot

                if(i == n - 1):
                    connector2 = Line(start=[-100,-100,0], end=[-100,100,0], stroke_color=[firstDot.color, dot.color])
                    self.add(connector2)
                    
                    updaters.connect_line_to_dots(connector2, dot, firstDot)


                
                dotSequence.append(Wait(waitTime))
                dotSequence.append(ApplyMethod(line.set_opacity, 0.5, run_time=0))
                dotSequence.append(Create(line, run_time=cycleTime / 2))
                dotSequence.append(ApplyMethod(dot.set_opacity, 1, run_time=0))

                t = waitTime + (cycleTime / 2)
                for j in range((n + 1) * 2):
                    dSeq = []
                    dSeq.append(MoveAlongPath(dot, line, run_time = cycleTime / 2, rate_func=rate_functions.ease_in_out_sine))
                    dSeq.append(ApplyMethod(line.reverse_points, run_time=0))

                    self.add_sound(sounds.EDO31sharp11[i], time_offset= t)
                    t += cycleTime / 2

                    pSeq = []
                    pSeq.append(FadeToColor(circle, c[i], run_time=0))
                    pSeq.append(FadeToColor(circle, WHITE, run_time= (cycleTime / (2 * n))))

                    dotSequence.append(AnimationGroup(Succession(*dSeq), Succession(*pSeq)))

                self.add_sound(sounds.EDO31sharp11[i], time_offset= t)
                t += cycleTime / 2
                self.add_sound(sounds.EDO31sharp11[i], time_offset= t)
                
                pSeq = []
                pSeq.append(FadeToColor(circle, c[i], run_time=0))
                pSeq.append(FadeToColor(circle, WHITE, run_time= (cycleTime / (2 * n))))
                
                dotSequence.append(AnimationGroup(Succession(*dSeq), Succession(*pSeq)))
                dotSequence.append(ApplyMethod(dot.set_opacity, 0, run_time = 0))
                dotSequence.append(AnimationGroup(Uncreate(line, run_time=cycleTime / 2), Succession(*pSeq)))

                allAnimations.append(Succession(*dotSequence))

            return AnimationGroup(*allAnimations)

        self.play(getAnimations(15, 1))


