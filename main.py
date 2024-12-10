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
wheel_diameter = 66.6*5
axle_track = 200
wall_distance = 256 # min distance to walls in mm


# system vars
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.B)
us_motor = Motor(Port.C) 
driver = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)
colorSensor = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
last = time.time()-10
usstart=67.5


# functions
def is_color_in_range(measured_color, target_color, tolerance):
    return color.checkColor(Color.GREEN)

def checkColor(target_color):
    measured_rgb = colorSensor.rgb()
    return color.checkColor(Color.RED)

def setup():
    us_motor.run_target(speed=300, target_angle=(67.5-usstart)*56/24)

def dropPackage():
    us_motor.run_target(speed=3000, target_angle=40)
    us_motor.run_target(speed=3000, target_angle=-12*56/24)

if __name__ =="__main__":
    setup()
    dt = time.time() - last
    last = time.time()
    
    # loop the main program until green line
    while not color.checkColor(Color.GREEN):
        while not color.checkColor(Color.RED):
            seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
        
        driver.stop()
        driver.turn((75))

        # when red line: find the direction in which the house is located
        house_angle = find_house.find_house(us, us_motor)
        print("--"*30)
        print(house_angle)
        
        # turn the robot in the direction of the house
        driver.turn(-house_angle)
        ev3.speaker.beep()
        us_motor.run_target(10000, -usstart*56/24)
        ev3.speaker.beep()

        # drive forward until house wall reached (= until distance to the house is <= 20mm)
        while not us.distance() <= wall_distance-50:
            driver.drive(-250, 0)
        
        driver.stop()
        driver.turn(90)
        us_motor.run_target(speed=100, target_angle=(67.5-usstart)*56/24)
        ev3.speaker.beep()
        
            
    # draw a smiley and stop
    driver.stop()
    us_motor.run_target(speed=100, target_angle=-0*56/24)
    screen.smiley(ev3)
    while True:
        ev3.speaker.beep()
        wait(100)
    
        
        