def uniq_check(array):
    return len(set(array)) == len(array)

if __name__ == "__main__":
    input_list = input().split()

    while not input_list[0] == 'stop':
        input_list = list(map(int,input_list))
        new_list = []
        if (uniq_check(input_list)):
            new_list = [el+2 if el % 2 == 0 else el for el in input_list ]
            new_list.sort()
            print(f'Unique list: {",".join(list(map(str,new_list)))}\nOutput: {sum(new_list)/len(new_list):.2f}')
        else:
            new_list = [el+3 if el % 2 == 1 else el for el in input_list ]
            new_list.sort()
            print(f'Non-unique list: {":".join(list(map(str,new_list)))}\nOutput: {sum(new_list)/len(new_list):.2f}')
        input_list = input().split()
