from manim import *
import colorsys
import math

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


config.background_color = "#121212"

titleColors = ["#B94EFF", "#D580FF", "#8A2BE2", "#E0B3FF"]


        
def getNewTriangle(points):
    points = []
    for i in range(3):
        i1 = i
        i2 = (i + 1) % 3
        newPoint = midpoint(points[i1], points[i2])
        points.append(newPoint)

    return points

def midpoint(p1, p2):
    if len(p1) != len(p2):
        raise ValueError("Points must have the same number of dimensions")
    return tuple((a + b) / 2 for a, b in zip(p1, p2))

class Run(Scene):
    def construct(self):

        title1 = Text("Mesmerizing Rhythm Loop", font="Corbel", gradient=titleColors)
        title1.move_to([0,4.5,0])

        title2 = Text("Subscribe if you enjoyed :)", font="Corbel", gradient=titleColors)
        title3 = Text("I make these for fun :)", font="Corbel", gradient=["#ff00cc", WHITE])
        title2.move_to([0,-4.5,0])
        title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        self.add(title3)

        p1 = [-3, -2, 0]
        p2 = [3, -2, 0]

        side = math.dist(p1, p2)

        height = (math.sqrt(3) / 2) * side

        p3 = [(p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 + height, 0]

        firstPoints = [p1, p2, p3]

        
