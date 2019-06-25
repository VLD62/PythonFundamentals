if __name__ == '__main__':
    int_list = list(map(int,input().split(" ")))
    int_list.sort(reverse=True)
    sqr_list = [n for n in int_list if abs(n**(1/2)) == int(abs(n**(1/2))) and n > 0]
    print(" ".join(map(str,sqr_list)))