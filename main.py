#!/usr/bin/env pybricks-micropython
#Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import seiten_regler
import time
# Create your objects here.
# Initialize the EV3 brick, motors, and sensors
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
us_motor = Motor(Port.C)  # For panning if needed
driver = DriveBase(left_motor, right_motor, wheel_diameter=66.8, axle_track=145)
colorSensor = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
last = time.time()-10
state = "seitenFollow"
def mainloop():
    global state, last
    dt = time.time() - last
    last = time.time()
    match state:
        case "find":
            ev3.screen.print("find")
            state = "follow"
        case "seitenFollow":
            seiten_regler.seiten_regler(ev3, dt, us, driver)
            ev3.screen.print("seitenFollow")
        case _:
            ev3.screen.print("error")
            state = "find"
    wait(1)
def setup():
    None

if __name__ =="__main__":
    setup()
    while True:
        mainloop()
    
