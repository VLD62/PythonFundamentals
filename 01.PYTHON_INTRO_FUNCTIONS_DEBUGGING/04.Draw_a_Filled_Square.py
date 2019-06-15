def draw_dashes(n):
    for x in range(0,n*2):
        print("-",end="")
    print()


def draw_body(n):
    for y in range(0,n-2):
        for x in range(0,n + 1):
            if x == 0:
                print("-",end="")
            elif x + 1 == n + 1:
                print("-",end="")
            else:
                print("\/",end="")
        print()


if __name__ == '__main__':
    number = int(input())
    draw_dashes(number)
    draw_body(number)
    draw_dashes(number)