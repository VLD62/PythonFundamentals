import math
def duplicate_remover(x):
  return list(dict.fromkeys(x))

def average_calculator(array):
    return sum(list(map(int,array))) - sum(list(map(int,array)))/len(array)

if __name__ == '__main__':
    region_dict = {}
    input_string = input()

    while not input_string == 'Aggregate':
        city_list = input_string.split(" ")
        if city_list[0] in region_dict:
            region_dict[city_list[0]] += city_list[1].split(" ")
        else:
            region_dict[city_list[0]] = city_list[1].split(" ")
        input_string = input()

    for k,v in region_dict.items():
        region_dict[k] = duplicate_remover(v)

    for k,v in region_dict.items():
        print(f'{k} -> {", ".join(v)} ({math.ceil(average_calculator(v))})')