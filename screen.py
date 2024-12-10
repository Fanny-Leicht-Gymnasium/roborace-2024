from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

def smiley(ev3):
    ev3.screen.clear()
    # face circle
    ev3.screen.draw_circle(90, 60, 50)
    # left eye
    ev3.screen.draw_circle(70, 40, 5, fill=True)
    # right eye
    ev3.screen.draw_circle(110, 40, 5, fill=True) 
    # mouth
    ev3.screen.draw_line(70, 80, 110, 80)
    ev3.screen.draw_line(70, 80, 80, 90)
    ev3.screen.draw_line(110, 80, 100, 90)

