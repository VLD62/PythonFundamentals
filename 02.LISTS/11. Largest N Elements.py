def array_sorter(unsorted_list):
    for i in range(1,len(unsorted_list)):
      key = unsorted_list[i]
      j = i - 1
      while j >=0 and key > unsorted_list[j]:
          unsorted_list[j+1] = unsorted_list[j]
          j -= 1
      unsorted_list[j+1] = key
    return unsorted_list


if __name__ == '__main__':
    int_list = list(map(int,input().split(' ')))
    n = int(input())
    print(" ".join(map(str,array_sorter(int_list)[:n]))) 