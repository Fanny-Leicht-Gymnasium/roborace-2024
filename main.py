#Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = None
state = "find"
def mainloop():
    global state
    if state == "find":
        ev3.screen.print("find")
        state = "follow"
    elif state == "follow":
        ev3.screen.print("follow")
        state = "find"
    else:
        ev3.screen.print("error")
        state = "find"

def setup():
    global ev3
    ev3 = EV3Brick()

if __name__ =="__main__":
    setup()
    while True:
        mainloop()
    
