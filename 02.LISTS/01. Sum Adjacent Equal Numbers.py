def list_sumator(array):
    for n in range(0,len(array)):
        if n < len(array) - 1 and array[n] == array[n+1]:
           array[n] = (array[n] + array[n+1])
           array.remove(array[n+1])
    return array


if __name__ == '__main__':
    num_list = list(map(float,input().split(" ")))
    i = 0
    new_array = list_sumator(num_list)
    while  i < len(new_array) - 1:
        new_array = list_sumator(new_array)
        i += 1
    print(" ".join(map(str,new_array)))
