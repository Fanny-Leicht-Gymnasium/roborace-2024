#!/usr/bin/env pybricks-micropython
#Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import seiten_regler
import find_house
import color
import time


# Create your objects here.
# Initialize the EV3 brick, motors, and sensors
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.B)
us_motor = Motor(Port.C)  # For panning if needed
driver = DriveBase(left_motor, right_motor, wheel_diameter=66.8, axle_track=145)
colorSensor = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
last = time.time()-10


def mainloop():
    global last
    dt = time.time() - last
    last = time.time()
    #seiten_regler.seiten_regler(ev3, dt, us, driver)
    if color.checkColor(Color.RED):
        print("Color is close to RED!")
    
def setup():
    None

if __name__ =="__main__":
    setup()
    while True:
        mainloop()