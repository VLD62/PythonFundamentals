if __name__ == '__main__':
    int_list = list(map(int,input().split(" ")))
    int_list.sort()
    print(" <= ".join(map(str,int_list)))