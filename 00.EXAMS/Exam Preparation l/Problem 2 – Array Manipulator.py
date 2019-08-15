def max_element_index(array):
    even_odd_index = {'even': 0, 'odd': 0}
    try:
        max_element_even = max([el for el in array if el % 2 == 0])
        even_odd_index['even'] = max(
            [idx for idx, el in enumerate(array) if el == max_element_even])
    except:
        even_odd_index['even'] = 'q'

    try:
        max_element_odd = max([el for el in array if el % 2 == 1])
        even_odd_index['odd'] = max(
            [idx for idx, el in enumerate(array) if el == max_element_odd])
    except:
        even_odd_index['odd'] = 'q'

    return even_odd_index


def min_element_index(array):
    even_odd_index = {'even': 0, 'odd': 0}
    try:
        min_element_even = min([el for el in array if el % 2 == 0])
        even_odd_index['even'] = max(
            [idx for idx, el in enumerate(array) if el == min_element_even])
    except:
        even_odd_index['even'] = 'q'
    try:
        min_element_odd = min([el for el in array if el % 2 == 1])
        even_odd_index['odd'] = max(
            [idx for idx, el in enumerate(array) if el == min_element_odd])
    except:
        even_odd_index['odd'] = 'q'
    return even_odd_index


if __name__ == "__main__":
    input_array = list(map(int, input().split()))
    input_cmd = input().split()

    while not input_cmd[0] == 'end':
        if input_cmd[0] == 'exchange':
            index = int(input_cmd[1])
            if index > len(input_array) - 1 or index < 0:
                print('Invalid index')
            else:
                part_one = input_array[:index+1]
                part_two = input_array[index+1:]
                input_array = part_two + part_one
        if input_cmd[0] == 'max':
            if input_cmd[1] == 'odd':
                odd_list = [el for el in input_array if el % 2 == 1]
                if len(odd_list) == 0:
                    print('No matches')
                else:
                    print(max_element_index(input_array)['odd'])
            else:
                even_list = [el for el in input_array if el % 2 == 0]
                if len(even_list) == 0:
                    print('No matches')
                else:
                    print(max_element_index(input_array)['even'])
        if input_cmd[0] == 'min':
            if input_cmd[1] == 'odd':
                odd_list = [el for el in input_array if el % 2 == 1]
                if len(odd_list) == 0:
                    print('No matches')
                else:
                    print(min_element_index(input_array)['odd'])
            else:
                even_list = [el for el in input_array if el % 2 == 0]
                if len(even_list) == 0:
                    print('No matches')
                else:
                    print(min_element_index(input_array)['even'])

        if input_cmd[0] == 'first':
            count = int(input_cmd[1])
            if count > len(input_array):
                print('Invalid count')
            else:
                if input_cmd[2] == 'odd':
                    odd_list = [el for el in input_array if el % 2 == 1]
                    print(odd_list[0:count])
                else:
                    even_list = [el for el in input_array if el % 2 == 0]
                    print(even_list[0:count])

        if input_cmd[0] == 'last':
            count = int(input_cmd[1])
            if count > len(input_array):
                print('Invalid count')
            else:
                if input_cmd[2] == 'odd':
                    odd_list = [el for el in input_array if el % 2 == 1]
                    print(odd_list[-count:])
                else:
                    even_list = [el for el in input_array if el % 2 == 0]
                    print(even_list[-count:])
        input_cmd = input().split()
    print(input_array)
