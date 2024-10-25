from pybricks.ev3devices import UltrasonicSensor

def seiten_regler(ev3, dt) -> str: # returns new state
    SETPOINT_DISTANCE = 2 #Sollwert Abstand
    us = UltrasonicSensor()
    distance = us.distance_centimeters_ping()
    print(distance)
    PID( , , , dt, SETPOINT_DISTANCE, distance)
    return "seitenFollow"

def PID(Kp, Ki, Kd, dt, setpoint, current_value):
    error = setpoint - current_value
    integral = integral + Ki * dt * error
    derivative = (current_value - previous_value) / dt
    output = Kp * error + Ki * integral + Kd * derivative
    return output

def Motor_Regelung(output):
    none