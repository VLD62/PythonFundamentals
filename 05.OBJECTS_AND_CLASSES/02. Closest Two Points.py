import math
import sys


def Calc_Distance(p1,p2):

    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    return round(math.sqrt(a*a + b*b),3)


def Calc_Lowest(points):

    low_p1 = ()
    low_p2 = ()
    lowest_distance = sys.maxsize

    for i in range(0,len(points)):
        for j in range(0,len(points)):
            if not i == j:
                p1 = Point(points[i][0], points[i][1])
                p2 = Point(points[j][0], points[j][1])
                if Calc_Distance(p1, p2) < lowest_distance:
                    lowest_distance = Calc_Distance(p1, p2)
                    low_p1 = p1
                    low_p2 = p2

    print("%.3f" % round(lowest_distance,3))
    print(f"({low_p1.x}, {low_p1.y})")
    print(f"({low_p2.x}, {low_p2.y})")


class Point:

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)


if __name__ == "__main__":

    n = int(input())
    points = []
    result  = []

    for i in range(0,n):
        single_point = input().split()
        points.append((single_point[0],single_point[1]))

    Calc_Lowest(points)