#!/usr/bin/env pybricks-micropython
#Import the ev3 libraries
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import seiten_regler
import find_house
import color
import screen

# customization vars
wheel_diameter = 66.8
axle_track = 14
wall_distance = 200 # min distance to walls in mm

# color check (not tested yet!)
# adjust these values as needed
red = (1, 1, 1)
green = (1, 1, 1)
tolerance = 30 

# system vars
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.B)
us_motor = Motor(Port.C)  # For panning if needed
driver = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)
colorSensor = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
last = time.time()-10

# functions
def is_color_in_range(measured_color, target_color, tolerance):
    return all(abs(measured_color[i] - target_color[i]) <= tolerance for i in range(3))

def checkColor(target_color):
    measured_rgb = colorSensor.rgb()
    return is_color_in_range(measured_rgb, target_color, tolerance)

def setup():
    us_motor.run_target(speed=100, target_angle=90*56/24)

if __name__ =="__main__":
    # setup when starting the program
    setup()
    dt = time.time() - last
    last = time.time()
    
    # loop the main program until green line
    while not checkColor(green):
        while not checkColor(red):
            seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
            print(checkColor(red))
        # /////////////////////
        # DROP PACKAGE FUNCTION HERE
        # /////////////////////
        driver.stop()
        driver.turn(15*40/16)
        # when red line: find the direction in which the house is located
        house_angle = find_house.find_house(us, us_motor)
        print("--"*30)
        print(house_angle)
        # turn the robot in the direction of the house
        driver.turn(-house_angle*40/16)
        ev3.speaker.beep()
        #wait(100)
        us_motor.run_target(1000, 0)
        ev3.speaker.beep()
        #wait(100)
        # drive forward until house wall reached (= until distance to the house is <= 20mm)
        while not us.distance() <= 200:
            driver.drive(-50, 0)
        
        driver.stop()
        # turn robot 90 degrees to the left
        driver.turn(90*40/16)
        us_motor.run_target(speed=100, target_angle=90*56/24)
        ev3.speaker.beep()
        wait(100)
            
    # draw a smiley and stop
    driver.stop()
    us_motor.run_target(speed=100, target_angle=-0*56/24)
    screen.smiley(ev3)
    while True:
        ev3.speaker.beep()
        wait(100)
    
        
        