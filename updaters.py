from manim import *
import numpy as np

def connect_line_to_dots(line: Line, dot1: Dot, dot2: Dot) -> Line:

    def updater(mob: Line):
        mob.set_points_as_corners([dot1.get_center(), dot2.get_center()])

    line.add_updater(updater)
    return line