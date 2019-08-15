import math
class Barrel:
    def __init__(self,r,h,v):
        self.r = r
        self.h = h
        self.v = v


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    n = int(input())
    v_truck = a * b * c
    barrels = []

    for idx in range(n):
         radius = float(input())
         heigh = float(input())
         volume = radius * radius * heigh * math.pi
         new_barrel = Barrel(r = radius, h = heigh, v = volume)
         v_truck -= new_barrel.v
         if v_truck > 0:
            barrels.append(new_barrel)
         else:
            print(f'Truck is full. {len(barrels)} on board!')
            exit(0)

    print(f'All barrels on board. Capacity left - {v_truck:.2f}.')