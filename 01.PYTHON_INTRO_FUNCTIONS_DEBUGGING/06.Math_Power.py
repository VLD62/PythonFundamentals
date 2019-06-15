def power_calculator(n,pow):
    return n ** abs(pow)

if __name__ == '__main__':
    number = float(input())
    power = int(input())
    print(power_calculator(number,power))