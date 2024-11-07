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


# system vars
ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.B)
us_motor = Motor(Port.C)  # For panning if needed
driver = DriveBase(left_motor, right_motor, wheel_diameter=wheel_diameter, axle_track=axle_track)
colorSensor = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S4)
last = time.time()-10

def setup():
    us_motor.run_target(speed=100, target_angle=90*56/12)

if __name__ =="__main__":
    # setup when starting the program
    setup()
    dt = time.time() - last
    last = time.time()
    
    # drive forward until red line
    while not color.checkColor(Color.RED):
        seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
    
    # when red line: find the direciton in which the house is located
    house_angle = find_house.find_house(us, us_motor)
    
    # turn the robot in the direction of the house
    driver.turn(house_angle)
    
    # drive forward until house wall reached (= until distance to the house is <= 20mm)
    while not us.distance() <= 20:
        seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
    
    # turn robot 90 degrees to the left
    driver.turn(90)
    
    # drive forward until green line
    while not color.checkColor(Color.GREEN):
        seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
        
    # draw a smiley and stop
    screen.smiley(ev3)
    while True:
        pass 
    
        
        