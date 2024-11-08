from pybricks.tools import wait
def find_house(us, usm):
    angle = -75-75
    endAngle = 0
    deg_sec= 1000
    degreePerStep = 5 # Drehwinkel

    minAngle = -1
    minDistance = 2000000
    for angle in range(angle, endAngle, degreePerStep):
        usm.run_target(deg_sec, angle*56/24)
        dis1 = us.distance()
        if  dis1 < minDistance:
            minDistance = dis1
            minAngle = angle
        print(angle, dis1)
        wait(100)
    
    return minAngle
