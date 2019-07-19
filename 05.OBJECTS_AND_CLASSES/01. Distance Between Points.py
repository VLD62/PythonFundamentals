import math


class Point:

    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)

def Calc_Distance(p1: Point,p2: Point):
    a = abs(p1.x - p2.x)
    b = abs(p1.y - p2.y)
    return round(math.sqrt(a*a + b*b),3)


if __name__ == "__main__":

    points = input().split()
    pointA = Point(int(points[0]),int(points[1]))
    points = input().split()
    pointB = Point(int(points[0]),int(points[1]))

    print("%.3f" % Calc_Distance(pointA,pointB))