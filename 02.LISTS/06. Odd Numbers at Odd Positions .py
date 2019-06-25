if __name__ == '__main__':
    int_list = list(map(int,input().split(" ")))
    for x in range(0,len(int_list)):
        if x % 2 == 1 and int_list[x] % 2 == 1:
            print(f'Index {x} -> {int_list[x]}')