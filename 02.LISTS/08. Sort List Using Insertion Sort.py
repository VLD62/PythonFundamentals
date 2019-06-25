if __name__ == '__main__':
    int_list = list(map(int,input().split(' ')))

    for i in range(1,len(int_list)):
      key = int_list[i]
      j = i - 1
      while j >=0 and key < int_list[j]:
          int_list[j+1] = int_list[j]
          j -= 1
      int_list[j+1] = key

    print(" ".join(map(str,int_list))) 