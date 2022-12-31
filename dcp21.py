"""
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def min_rooms(interval_list):
    rooms = []

    rooms.append(interval_list[0])
    for i in range(1,len(interval_list)):
        for j in range(0,len(rooms)):
            collide = 0
            print(interval_list[i],rooms[j])
            if collide_lectures(interval_list[i],rooms[j]):
                collide = collide + 1
        if collide == len(rooms):
            rooms.append(interval_list[i])
            print("collision:  "+ "True")
            print("collision count: " +str(collide))
        else:
            pass
    return rooms

def collide_lectures(lec1,lec2):
    rlow,rhigh = lec1
    tlow,thigh = lec2
    if ((rlow <= tlow <= rhigh) or (rlow <= thigh <= rhigh) or \
            (tlow <= rlow <= thigh) or (tlow <= rhigh <= thigh)):
        return True
    else:
        return False


if __name__  == "__main__":
    #givenList = [(30, 75), (0, 50), (60, 150)]
    #print(min_rooms(givenList))
    givenList2 = [(0, 50), (30, 75), (60, 150), (10,87), (100,120), (40,80), (150,200)]
    print(min_rooms(givenList2))
