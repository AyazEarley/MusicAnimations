from manim import *
import colorsys
import colors
import sounds
import updaters

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


config.background_color = "#121212"

c = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]

class Run(Scene):
    def construct(self):

        title1 = Text("Title", font="Corbel", gradient=c)
        title1.move_to([0,4.5,0])

        title2 = Text("subtitle 1", font="Corbel", gradient=c)
        title3 = Text("subtitle 2", font="Corbel", gradient=["#ff00cc", WHITE])
        title2.move_to([0,-4.5,0])
        title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)
