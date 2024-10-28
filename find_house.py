def find_house(us, usm):
    angle = 0
    deg_sec = 40 # Winkelgeschwindigkeit
    degree = 20 # Drehwinkel
    
    usm.run_angle(deg_sec, 0)
    dis1 = us.distance()
    usm.run_angle(deg_sec, degree)
    angle += degree
    dis2 = us.distance()

    winkel = []
    distance = []
    while angle < 140:
        print(angle)
        if dis1 or dis2 < 150:
            while dis1 > dis2:
                dis1 = dis2
                angle += degree
                usm.run_angle(deg_sec, degree)
                dis2 = us.distance()
            winkel.append(angle)
            while dis1 < dis2:
                dis1 = dis2
                angle += degree
                usm.run_angle(deg_sec, degree)
                dis2 = us.distance()
                print("l2")
            print("if")
        else:
            dis1 = dis2
            angle += degree
            usm.run_angle(deg_sec, degree)
            dis2 = us.distance()
            print("else")
        
    small_dis = min(distance)
    ind_dis = distance.index(small_dis)
    small_winkel = winkel[ind_dis]
    return small_winkel
