def check_sign(number):
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"

if __name__ == '__main__':
    n = int(input())
    print(f"The number {n} is {check_sign(n)}.")