def item_counter(list_of_string):
    item_count = {}
    for i in range(0,len(list_of_string)):
           if list_of_string[i] in item_count:
               item_count[list_of_string[i]] += 1
           else:
               item_count[list_of_string[i]] = 1
    return item_count


if __name__ == '__main__':
    n = int(input())
    clothes_dict = {}

    for i in range(0,n):
        input_list = input().split(" -> ")
        if input_list[0] in clothes_dict:
            clothes_dict[input_list[0]] += input_list[1].split(",")
        else:
            clothes_dict[input_list[0]] = input_list[1].split(",")

    target_item = input().split(" ")

    for k,v in clothes_dict.items():
        print(f'{k} clothes:')
        for ky,va in item_counter(v).items():
            if target_item[0] == k and target_item[1] == ky:
               print(f'* {ky} - {va} (found!)')
            else:
               print(f'* {ky} - {va}')