if __name__ == '__main__':
    list_int = list(map(int,input().split(" ")))
    print(" ".join(map(str,[list_int[n] for n in range(len(list_int) - 1,-1,-1)])))