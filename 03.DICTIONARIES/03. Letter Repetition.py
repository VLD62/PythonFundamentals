if __name__ == "__main__":
    list_of_string = input()
    char_count = {}
    for i in range(0,len(list_of_string)):
           if list_of_string[i] in char_count:
               char_count[list_of_string[i]] += 1
           else:
               char_count[list_of_string[i]] = 1
    for k,v in char_count.items():
        print(f'{k} -> {v}')