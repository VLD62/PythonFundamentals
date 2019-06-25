if __name__ == '__main__':
    array = input()
    count = 0
    for element in array.split(" "):
        if (int(element) % 2 != 0):
            count += 1
    print(count)