#!/usr/bin/env pybricks-micropython
# Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = None
state = "play"

def mainloop():
    global state
    if state == "find":
        ev3.screen.print("find")
        state = "follow"
    elif state == "play":
        ev3.screen.print(state)
        sound.play(ev3, "audio/imperialMarch.wav") #The file needs to be 1. MONO and 2. have a SAMPLE RATE of 22050 Hz to work on the Brick!
    else:
        ev3.screen.print("error")
        state = "find"

def setup():
    global ev3
    ev3 = EV3Brick()
    ev3.speaker.set_volume(1000) #It is limited somehwre around 256(?), this could however be bypassed

if __name__ == "__main__":
    setup()
    while True:
        mainloop()