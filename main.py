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


usstart=67.5
# functions
def is_color_in_range(measured_color, target_color, tolerance):
    return color.checkColor(Color.GREEN)

def checkColor(target_color):
    measured_rgb = colorSensor.rgb()
    return color.checkColor(Color.RED)#is_color_in_range(measured_rgb, target_color, tolerance)

def setup():
    # while True:
    #     us_motor.run_target(speed=300, target_angle=40)
    #     # wait(1000)
    #     us_motor.run_target(speed=300, target_angle=-12*56/24)
    #     wait(1000)
    # us_motor.run_target(speed=300, target_angle=0)

    us_motor.run_target(speed=300, target_angle=(67.5-usstart)*56/24)
    # driver.drive(-5000, 0)  # Adjust steering; 100 is the speed
    # wait(1000000)
def dropPackage():
    us_motor.run_target(speed=3000, target_angle=40)
    # wait(1000)
    us_motor.run_target(speed=3000, target_angle=-12*56/24)
    # driver.drive(1000, 0)
if __name__ =="__main__":
    # setup when starting the program
    setup()
    dt = time.time() - last
    last = time.time()
    
    # loop the main program until green line
    while not color.checkColor(Color.GREEN):
        while not color.checkColor(Color.RED):
            seiten_regler.seiten_regler(ev3, dt, us, driver, wall_distance)
            # wait(100)

            # print(checkColor(red))
        ''' 
        /////////////////////
        DROP PACKAGE FUNCTION HERE
        idea: 
        1. save current state of us_sensor_motor
        2. turn the motor as far as it needs to for the package to drop
        3. turn the motor back to the saved state
        4. continue
        /////////////////////
        '''
        driver.stop()
        driver.turn((75))
        # dropPackage()

        # when red line: find the direction in which the house is located
        house_angle = find_house.find_house(us, us_motor)
        print("--"*30)
        print(house_angle)
        # turn the robot in the direction of the house
        driver.turn(-house_angle)
        ev3.speaker.beep()
        #wait(100)
        us_motor.run_target(10000, -usstart*56/24)
        ev3.speaker.beep()
        #wait(100)
        # drive forward until house wall reached (= until distance to the house is <= 20mm)
        while not us.distance() <= wall_distance-50:
            driver.drive(-250, 0)
        
        driver.stop()
        # turn robot 90 degrees to the left
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
    
        
        