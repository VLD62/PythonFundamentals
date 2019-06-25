if __name__ == '__main__':
    array = input()
    p = int(input())
    result = [int(i) * p for i in array.split(" ")]

    print(' '.join(list(map(str,result))))