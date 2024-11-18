from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

def smiley(ev3):
    ev3.screen.clear()

    # Draw the face circle
    ev3.screen.draw_circle(90, 60, 50)  # (x, y, radius)

    # Draw the left eye
    ev3.screen.draw_circle(70, 40, 5, fill=True)  # (x, y, radius, fill=True makes it a filled circle)

    # Draw the right eye
    ev3.screen.draw_circle(110, 40, 5, fill=True)  # (x, y, radius, fill=True makes it a filled circle)

    # Draw the smile
    ev3.screen.draw_line(70, 80, 110, 80)  # Top line of the smile
    ev3.screen.draw_line(70, 80, 80, 90)   # Left diagonal line
    ev3.screen.draw_line(110, 80, 100, 90) # Right diagonal line

