if __name__ == '__main__':
    num_list = list(map(int,input().split(" ")))
    counter_list = [0 for n in range(0,max(num_list) + 1)]
    for num in num_list:
        for c in range(0,len(counter_list)):
            if num == c  :
                counter_list[c] += 1

    for e in range(0,len(counter_list)):
        if counter_list[e] > 0:
            print(str(e) + " -> " + str(counter_list[e]))
