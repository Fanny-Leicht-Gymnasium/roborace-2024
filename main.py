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
    us_motor.run_target(speed=100, target_angle=-90*56/24)

if __name__ =="__main__":
    # setup when starting the program
    setup()
    dt = time.time() - last
    last = time.time()
    # drive forward until red line
    # while True:'
    #     None'
    #     driver.drive(-50, 0)
    
    while not color.checkColor(Color.RED):
        seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
    
    driver.stop()
    driver.turn(-15*40/16)
    # when red line: find the direciton in which the house is located
    house_angle = find_house.find_house(us, us_motor)
    print("--"*30)
    print(house_angle)
    # turn the robot in the direction of the house
    driver.turn(-house_angle*40/16)
    ev3.speaker.beep()
    wait(100)
    us_motor.run_target(1000, 0)
    ev3.speaker.beep()
    wait(100)
    # drive forward until house wall reached (= until distance to the house is <= 20mm)
    while not us.distance() <= 200:
        driver.drive(-50, 0)
    
    driver.stop()
    # turn robot 90 degrees to the left
    # driver.turn(90)
    driver.turn(-90*40/16)
    us_motor.run_target(speed=100, target_angle=-90*56/24)
    ev3.speaker.beep()
    wait(100)
    # drive forward until green line
    while not color.checkColor(Color.GREEN):
        print("Aktuell: ",colorSensor.color(),colorSensor.rgb()," Soll: ",Color.GREEN)
        seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
        
    # draw a smiley and stop
    driver.stop()
    us_motor.run_target(speed=100, target_angle=-0*56/24)
    screen.smiley(ev3)
    while True:
        ev3.speaker.beep()
        wait(100)
    
        
        