from pybricks.hubs import EV3Brick
from pybricks.parameters import Color

def smiley(ev3):
    ev3.screen.clear()

    # Draw the face circle
    ev3.screen.draw_circle(90, 60, 50)  # Face outline (x, y, radius)

    # Draw the left eye
    ev3.screen.draw_circle(70, 50, 5, fill=True)  # Slightly higher on the y-axis for a friendlier look

    # Draw the right eye
    ev3.screen.draw_circle(110, 50, 5, fill=True)  # Same adjustment for symmetry

    # Draw a curved smile
    # Use multiple lines to approximate a curved shape (since we can't draw arcs directly in this environment)
    ev3.screen.draw_line(70, 80, 75, 85)  # Left curve
    ev3.screen.draw_line(75, 85, 85, 90)  # Mid-left curve
    ev3.screen.draw_line(85, 90, 95, 90)  # Middle part of the smile
    ev3.screen.draw_line(95, 90, 105, 85) # Mid-right curve
    ev3.screen.draw_line(105, 85, 110, 80) # Right curve

