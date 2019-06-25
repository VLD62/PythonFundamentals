def swap(array,x,y):
  array[x],array[y]=array[y],array[x] 
if __name__ == '__main__':
    int_list = list(map(int,input().split(' ')))
    sorted_list = []
    sorted_list.append(int_list[0])
    for i in range(1,len(int_list)):
        j = len(sorted_list)
        sorted_list.append(int_list[i])
        while j > 0:
            if sorted_list[j] < sorted_list[j-1]:
                swap(sorted_list,j,j-1)
            j -= 1
    print(" ".join(map(str,sorted_list))) 