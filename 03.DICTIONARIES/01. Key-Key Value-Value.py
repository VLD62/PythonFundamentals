if __name__ == "__main__":
    key = input()
    value = input()
    n = int(input())
    key_key_dict = {}
    for i in range(0,n):
        list_of_string = input().split(' => ')
        key_key_dict[list_of_string[0]] = list_of_string[1].split(";")

    for k,v in key_key_dict.items():
        if key.find(k) != -1:
            print(k)
        if key in k:
            print(f'{k}:')
            for item in v:
                if value in item:
                    print(f'-{item}')