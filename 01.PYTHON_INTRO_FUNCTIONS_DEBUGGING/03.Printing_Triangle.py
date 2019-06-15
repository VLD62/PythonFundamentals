def print_main_body(n):
    for x in range (1,n+1):
        for y in range (1,x+1):
            print(y, end=" ")
        print()


def print_bottom(n):
    for x in range (1,n):
        for y in range (1,n-x+1):
            print(y, end=" ")
        print()


if __name__ == '__main__':
    number = int(input())
    print_main_body(number)
    print_bottom(number)