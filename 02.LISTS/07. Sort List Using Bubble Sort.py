def swap(array,x,y):
  array[x],array[y]=array[y],array[x] 

if __name__ == '__main__':
    int_list = list(map(int,input().split(' ')))

    for num in range(0,len(int_list) - 1):
        for num in range(len(int_list) - 1,0,-1):
            if int_list[num] < int_list[num-1]:
                swap(int_list,num,num-1)
    print(" ".join(map(str,int_list)))