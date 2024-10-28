def find_house():
    deg_sec = 10 # Winkelgeschwindigkeit
    degree = 5 # Drehwinkel
    
    dis1 = UltrasonicSensor.distance_centimeters()
    run_angle(deg_sec, degree, Stop.HOLD, True)
    angle += degree
    dis2 = UltrasonicSensor.distance_centimeters()

    winkel = []
    distance = []
    while angle < 140:
        if dis1 or dis2 < 150:
            while dis1 > dis2:
                dis1 = dis2
                run_angle(deg_sec, degree, Stop.HOLD, True)
                angle += degree
                dis2 = UltrasonicSensor.distance_centimeters()
            winkel.append(winkelauslesen)
            abstand.append(dis1)
            while dis1 < dis2:
                dis1 = dis2
                run_angle(deg_sec, degree, Stop.HOLD, True)
                angle += degree
                dis2 = UltrasonicSensor.distance_centimeters()
        else:
            dis1 = dis2
            run_angle(deg_sec, degree, Stop.HOLD, True)
            angle += degree
            dis2 = UltrasonicSensor.distance_centimeters()
    small_dis = min(distance)
    ind_dis = distance.index(small_dis)
    small_winkel = winkel[ind_dis]
    return small_winkel
