if __name__ == '__main__':
    string_array = input().split(" ")
    last_element = string_array.pop()
    string_array.insert(0,last_element)
    print(' '.join(string_array))