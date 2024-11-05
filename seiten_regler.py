from pybricks.ev3devices import UltrasonicSensor

import csv

# PID constants
Kp = 5
Ki = 0#.0025
Kd = 0.000
SETPOINT_DISTANCE = 10  # Target distance from the wall in mm
integral = 0
previous_error = 0
counter = 0
def PID(Kp, Ki, Kd, dt, setpoint, current_value):
    global integral, previous_error
    
    error = setpoint - current_value
    integral += error * dt * Ki
    integral = min(integral,40)
    integral = max(integral,-40)
    derivative = (error - previous_error) / dt
    output = Kp * error + integral + Kd * derivative
    previous_error = error
    print(current_value,"\t",error,"\t",integral,"\t",derivative,"\t",output)
    return output

def seiten_regler(ev3, dt, us, driver) -> str:  # Returns new state
    distance = us.distance()  # Get current distance from the wall
    # print("Distance:", distance)
    distance = min(distance, 1000)
    output = PID(Kp, Ki, Kd, dt, SETPOINT_DISTANCE, distance)
    Motor_Regelung(output, driver)
    return "seitenFollow"

def Motor_Regelung(output, driver):
    # Adjust motors based on PID output
    # Positive output means too far; negative means too close
    driver.drive(40, -output/10)  # Adjust steering; 100 is the speed