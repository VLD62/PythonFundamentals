import math


if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    n = int(input())
    v_truck = a * b * c
    barrels_loaded = 0

    for idx in range(n):
         radius = float(input())
         heigh = float(input())
         b_volume = radius * radius * heigh * math.pi
         v_truck -= b_volume
         if v_truck > 0:
            barrels_loaded += 1
         else:
            print(f'Truck is full. {barrels_loaded} on board!')
            exit(0)

    print(f'All barrels on board. Capacity left - {v_truck:.2f}.')