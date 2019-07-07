if __name__ == '__main__':
    input_string = input()
    city_dict = {}
    city_capacity = {}

    while not input_string == 'ready':
        city_list = input_string.split(":")
        transport_list = city_list[1].split(",")
        transport_array = []
        transport_dict = {}
        for transport in transport_list:

            transport_list1 = transport.split("-")
            transport_dict[transport_list1[0]] = transport_list1[1]

        if city_list[0] in city_dict.keys():
            for k,v in city_dict.items():
                for single_transport in v:
                    for key,value in single_transport.items():
                            for keyt, valuet in transport_dict.items():
                                if key == keyt:
                                    single_transport[key] = valuet
            city_dict[city_list[0]] += transport_array
        else:
            transport_array.append(transport_dict)
            city_dict[city_list[0]] = transport_array
        input_string = input()

    input_string = input()
    while not input_string == 'travel time!':
        capacity_list = input_string.split(" ")
        key = capacity_list[0:-1]
        value = capacity_list[-1]
        city_capacity[" ".join(key)] = int("".join(value))
        input_string = input()

    for k_capacity, v_capacity in city_capacity.items():
        for k_transport, v_transport in city_dict.items():
            if k_capacity == k_transport:
                transport_capacity = 0
                for transport in v_transport:
                       for k,v in transport.items():
                           transport_capacity += int(v)
                if int(v_capacity) <= transport_capacity :
                    print(f'{k_capacity} -> all {v_capacity} accommodated')
                else:
                    print(f'{k_capacity} -> all except {v_capacity - transport_capacity} accommodated')
