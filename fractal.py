from manim import *
import colorsys

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16


config.background_color = "#121212"

rainbow = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#9400D3"]


def right_angle_vertex(A, B, side="left"):
    x1, y1, _ = A
    x2, y2, _ = B

    dx = x2 - x1
    dy = y2 - y1

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    if side == "left":
        C = (mx - dy / 2, my + dx / 2, 0)
    elif side == "right":
        C = (mx + dy / 2, my - dx / 2, 0)
    else:
        raise ValueError("side must be 'left' or 'right'")

    return C

def generateMidpoints(points):
    newPoints = []

    for i in range(1, len(points)):
        newPoints.append(points[i-1])
        if i % 2 == 1:
            newPoints.append(right_angle_vertex(points[i-1], points[i], side = "right"))
        else:
            newPoints.append(right_angle_vertex(points[i-1], points[i], side = "left"))

    newPoints.append(points[len(points) - 1])
    return newPoints

def generateLines(points):
    lines = []
    colors = rainbow_hex(len(points))

    for i in range(1, len(points)):
        line = Line(start=points[i-1], end=points[i], stroke_color=["#db17b4", WHITE])
        lines.append(line)

    return lines

def rainbow_hex(n):
    colors = []
    for i in range(n):
        h = i / n
        r, g, b = colorsys.hsv_to_rgb(h, 1.0, 1.0)
        colors.append('#{:02x}{:02x}{:02x}'.format(
            round(r * 255), round(g * 255), round(b * 255)
        ))
    return colors

class Fractal(Scene):
    def construct(self):
        self.add_sound("Fractal2.wav")

        title1 = Text("Fractal + Music I Wrote", font="Corbel", gradient=["#ff00cc", WHITE])
        title1.move_to([0,4.5,0])

        title2 = Text("Enjoy your day :)", font="Corbel", gradient=["#ff00cc", WHITE])
        #title3 = Text("I make these for fun :)", font="Corbel", gradient=["#ff00cc", WHITE])
        title2.move_to([0,-4.5,0])
        #title3.move_to([0,-5.5,0])


        self.add(title1)
        self.add(title2)
        #self.add(title3)
        points = [[1.5, -2, 0], [1.5, 2, 0], [-2.5, 2, 0]]


        lines = generateLines(points)
        group = VGroup(*lines)
        self.add(group)

        storePoints = []
        storePoints.append(points)
        self.wait(0.2)
        for i in range(7):
            points = generateMidpoints(points)
            storePoints.append(points)

            lines = generateLines(points)
            newGroup = VGroup(*lines)
            self.play(Transform(group, newGroup, run_time=1))

        length = len(storePoints)
        for i in range(7):
            lines = generateLines(storePoints[length - i - 2])
            newGroup = VGroup(*lines)
            self.play(Transform(group, newGroup, run_time=1))

        self.wait(1)


