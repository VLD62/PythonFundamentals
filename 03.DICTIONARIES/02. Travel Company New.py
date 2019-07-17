def string_to_dict(s):
    tmp = s.split(',')
    return {i.split('-')[0]: int(i.split('-')[1]) for i in tmp}


def sum_it(s):
    sum = 0
    for vh, co in s.items():
        sum += co
    return int(sum)


city_vhk_d = {}
while True:
    inp = input().split(':')
    if inp[0] == "ready":
        break
    else:
        if inp[0] not in city_vhk_d:
            city_vhk_d[inp[0]] = string_to_dict(inp[1])
        else:
            city_vhk_d[inp[0]].update(string_to_dict(inp[1]))

# print(city_vhk_d)

city_capacity = {}
while True:
    inp = input().split()
    if inp[0] == "travel" and inp[1] == "time!":
        break
    else:
        city_name = ' '.join(inp[:-1])
        city_cap = int(inp[-1:][0])
        if inp[0] not in city_capacity.keys():
            city_capacity[city_name] = city_cap
        else:
            city_capacity[city_name].update(city_cap)

# print(city_capacity)
for city, cap in city_capacity.items():
    if cap <= sum_it(city_vhk_d[city]):
        print(f'{city} -> all {cap} accommodated')
    else:
        print(f'{city} -> all except {abs(cap - sum_it(city_vhk_d[city]))} accommodated')
