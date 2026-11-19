from manim import *
import numpy as np

def connect_line_to_dots(line: Line, dot1: Dot, dot2: Dot) -> Line:
 
    def updater(mob: Line):
        mob.put_start_and_end_on(dot1.get_center(), dot2.get_center())
        mob.set_opacity(min(dot1.get_stroke_opacity(), dot2.get_stroke_opacity()))
        
 
    line.add_updater(updater)
    return line