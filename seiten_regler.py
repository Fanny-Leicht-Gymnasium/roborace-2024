from pybricks.ev3devices import UltrasonicSensor

import csv

# PID constants
Kp = 0.25
Ki = 0#.0025
Kd = 0.000
Ks=0#.5
slimit=100
integral = 0
previous_error = 0
counter = 0
speed=400
minradus=400
maxrotate=(speed/minradus)*180/3.14
def PID(Kp, Ki, Kd, dt, setpoint, current_value):
    global integral, previous_error
    
    error = setpoint - current_value
    integral += error * dt * Ki
    integral = min(integral,40)
    integral = max(integral,-40)
    derivative = (error - previous_error) / dt
    sqr = error* error * error/abs(error)
    output = Kp * error + integral + Kd * derivative +  max(min(sqr * Ks,slimit),-slimit)
    previous_error = error
    print(current_value,"\t",error,"\t",integral,"\t",derivative,"\t",output, "\t", max(min(output,maxrotate),-maxrotate),maxrotate)
    return max(min(output,maxrotate),-maxrotate)

def seiten_regler(ev3, dt, us, driver, wall_distance) -> str:  # Returns new state
    distance = us.distance()  # Get current distance from the wall
    # print("Distance:", distance)
    output = PID(Kp, Ki, Kd, dt, wall_distance, distance)
    driver.drive(-speed, output)
    return "seitenFollow"
