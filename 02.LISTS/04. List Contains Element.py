if __name__ == "__main__":
    list_int = list(map(int,input().split(" ")))
    n = int(input())

    flag = 'no'
    for number in list_int:
        if number == n:
            flag = 'yes'

    print(flag)