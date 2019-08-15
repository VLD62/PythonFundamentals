def uniq(array):
    if len(array) == 0:
        return []
    else:
        return [array[0]] + uniq([x for x in array if x != array[0]])


def _set(array):
    return len(set(array)) == len(array)


def _filter(array, cmd):
    if cmd == 'odd':
        new_list = [el for el in array if el % 2 == 1]
    if cmd == 'even':
        new_list = [el for el in array if el % 2 == 0]
    return new_list


def _multiply(array, n):
    new_list = [el*n for el in array]
    return new_list


def _divide(array, n):
    new_list = [el/n for el in array]
    return new_list


def _slice(array, n, m):
    new_list = array[n:m]
    return new_list


if __name__ == "__main__":

    ref_list = list(map(int, input().split()))
    command = input().split()
    count = 0

    while not command[0] == 'exhausted':
        if command[0] == 'set':
            count += 1
            if _set(ref_list):
                print('It is a set')
            else:
                print(uniq(ref_list))

        if command[0] == 'filter':
            count += 1
            new_list = _filter(ref_list, command[1])
            if len(new_list) > 0:
                print(new_list)

        if command[0] == 'multiply':
            count += 1
            print(_multiply(ref_list, int(command[1])))

        if command[0] == 'divide':
            count += 1
            if int(command[1]) == 0:
                print('ZeroDivisionError caught')
            else:
                print(_divide(ref_list, int(command[1])))

        if command[0] == 'slice':
            count += 1
            n = int(command[1])
            m = int(command[2])


            if n >= len(ref_list) or m >= len(ref_list):
                print('IndexError caught')
            else:
                print(_slice(ref_list, n, (m + 1)))

        if command[0] == 'sort':
            count += 1
            print(sorted(ref_list))

        if command[0] == 'reverse':
            count += 1
            new_list = ref_list[::-1]
            print(new_list)

        command = input().split()

    print(f'I beat It for {count} rounds!')