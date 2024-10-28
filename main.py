#!/usr/bin/env pybricks-micropython
#Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import find_house

# Initialize the motors.
ev3 = EV3Brick()
# left_motor = Motor(Port.A)
# right_motor = Motor(Port.D)
usm = Motor(Port.A)
# driver = DriveBase(left_motor, right_motor, wheel_diameter=66.8, axle_track=145)
# colorSensor = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S1)


#GYRO gyro = GyroSensor(Port.S2)
#tSensor = TouchSensor(Port.S3)

state = "find"
def mainloop():
    global ev3, driver, left_motor, right_motor, usm, colorSensor, us, state
    if state == "find":
        ev3.screen.print("find")
        find_house.find_house(us, usm)
        state = "find"
    elif state == "follow":
        ev3.screen.print("follow")
        state = "find"
    else:
        ev3.screen.print("error")
        state = "find"

def setup():
    global ev3, driver, left_motor, right_motor, usm, colorSensor, us, state

if __name__ =="__main__":
    setup()
    while True:
        mainloop()
    
