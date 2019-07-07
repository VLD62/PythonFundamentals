if __name__ == '__main__':
    user_dict = {}
    command = input().split(' -> ')
    while not command[0] == 'end':
        key = command[0]
        values = command[1]
        if values[0].isdigit():
            if key in user_dict.keys():
                user_dict[key] += ', ' + values
            else:
                user_dict[key] = values
        else:
            if  values in user_dict.keys():
                user_dict[key] = user_dict[values]
        command = input().split(' -> ')
    for k,v in user_dict.items():
        print(f'{k} === {v}')