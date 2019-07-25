class RealNumber:
    def __init__(self, value, count):
        self.value = value
        self.count = count


if __name__ == "__main__":
    list_of_nums = input().split()
    list_of_RealNumber = []

    for num in list_of_nums:
        Real_Num = RealNumber(value=num, count=0)
        if num not in [x.value for x in list_of_RealNumber]:
            list_of_RealNumber.append(Real_Num)

    for real_num in list_of_RealNumber:
        for num in list_of_nums:
            if real_num.value == num:
                real_num.count += 1

    new_list = sorted(list_of_RealNumber,key=lambda x: float(x.value))

    for real_num in new_list:
        print(f'{float(real_num.value)} -> {real_num.count} times')
