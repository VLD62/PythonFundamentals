if __name__ == '__main__':
    int_list = list(map(int,input().split(' ')))
    new_list = [n for n in int_list if n > 0]
    if len(new_list) > 0:
        new_list.reverse()
        print(" ".join(map(str,new_list)))
    else:
        print("empty")