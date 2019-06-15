def compare_int(v1, v2):
    if abs(v1) > abs(v2):
        print(v1)
    else:
        print(v2)


def compare_char(v1, v2):
    if v1 > v2:
        print((v1).upper())
    else:
        print((v2).upper())


def compare_string(v1, v2):
    v1_sum, v2_sum = 0, 0
    for char in v1:
        v1_sum += ord(char)
    for char in v2:
        v2_sum += ord(char)

    if v1_sum > v2_sum:
        print(v1)
    else:
        print(v2)


if __name__ == "__main__":
    input_type = input()
    value1 = input()
    value2 = input()

    if input_type == "int":
        value1 = int(value1)
        value2 = int(value2)
        compare_int(value1, value2)
    elif input_type == "char":
        value1 = ord(value1)
        value2 = ord(value2)
        compare_char(value1, value2)
    else:
        compare_string(value1, value2)