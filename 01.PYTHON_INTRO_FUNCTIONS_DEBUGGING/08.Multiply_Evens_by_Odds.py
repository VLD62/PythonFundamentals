def digits_sumator(n):
    even_sum = 0
    odd_sum = 0
    for x in n:
        if x != "-":
            if int(x) % 2 == 0:
                even_sum +=int(x)
            else:
                odd_sum +=int(x)
    return odd_sum * even_sum


if __name__ == '__main__':
    number = str(input())
    print(digits_sumator(number))