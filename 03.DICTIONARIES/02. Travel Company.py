def filtrator(dict_list):
    dictionary = {}
    for item in dict_list:
        for k,v in item.items():
            dictionary[k] = v
    return dictionary


if __name__ == '__main__':
    input_string = input()
    transport_dict = {}
    city_capacity = {}
    while not input_string == 'ready':
        city_list = input_string.split(":")
        el_arr = []
        for element in city_list[1].split(","):
            el = element.split("-")
            el_dict = {}
            el_dict[el[0]] = el[1]
            el_arr.append(el_dict)
        if city_list[0] in transport_dict:
            transport_dict[city_list[0]] += el_arr
        else:
            transport_dict[city_list[0]] = el_arr
        input_string = input()
    for k, v in transport_dict.items():
         transport_dict[k] = (filtrator(v))

    input_string = input()
    while not input_string == 'travel time!':
        capacity_list = input_string.split(" ")
        key = capacity_list[0:-1]
        value = capacity_list[-1]
        city_capacity[" ".join(key)] = int("".join(value))
        input_string = input()

        tobe_printed = ""

        for k_capacity,v_capacity in city_capacity.items():
           for k_transport, v_transport in transport_dict.items():
               if k_capacity == k_transport:
                   transport_capacity = 0
                   for k,v in v_transport.items():
                       transport_capacity += int(v)
                   if int(v_capacity) <= transport_capacity :
                       tobe_printed = (f'{k_capacity} -> all {v_capacity} accommodated')
                   else:
                       tobe_printed = (f'{k_capacity} -> all except {v_capacity - transport_capacity} accommodated')

        print(tobe_printed)