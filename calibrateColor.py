#!/usr/bin/env pybricks-micropython
# Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
import time


# System vars
ev3 = EV3Brick()
colorSensor = ColorSensor(Port.S1)

# Main loop
while True:
    color_value = colorSensor.color()
    ev3.screen.clear()
    ev3.screen.draw_text(0, 50, "Color Sensor Value: {}".format(color_value))
    time.sleep(5)
