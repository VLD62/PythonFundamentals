def area_calculator(b,h):
    return (b * h)/ 2


if __name__ == '__main__':
    x = float(input())
    y = float(input())
    area = area_calculator(x,y)

    if area.is_integer():
        print(int(area))
    else:
        print(f"{round(area,12)}")   
