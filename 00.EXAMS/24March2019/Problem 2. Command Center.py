def swap_elements(array,a,b):
    a = int(a)
    b = int(b)
    array[a], array[b] = array[b], array[a] 
    return array

def enumerate_list(array):
    return(list(enumerate(array)))

def max_element(array):
    return max(array)

def min_element(array):
    return min(array)

def divisble_by(array,n):
    n = int(n)
    return [element for element in array if element % n == 0]

if __name__ == "__main__":
    input_list = list(map(int,(input().split())))
    commands = input().split()
    operations = 0
    while not commands[0] == 'end':

        if commands[0] == 'swap':
            if int(commands[1]) < len(input_list) and int(commands[2]) < len(input_list):
                print(swap_elements(input_list,commands[1],commands[2]))
                
            else:
                print(input_list)
            operations += 1

        if commands[0] == 'enumerate_list':
            print(enumerate_list(input_list))
            operations += 1


        if commands[0] == 'max':
            print(max_element(input_list))
            operations += 1


        if commands[0] == 'min':
            operations += 1
            print(min_element(input_list))

        if commands[0] == 'get_divisible':
            operations += 1
            print(divisble_by(input_list,commands[2]))
        commands = input().split()

    print(operations)

