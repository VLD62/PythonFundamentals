import math
class Shell:
    def __init__(self, region, size):
        self.region = region
        self.size = int(size)

def giant_Shell_Checker(array):
    arr_sum = sum(array)
    count = len(array)
    return arr_sum - (arr_sum/count)

if __name__ == "__main__":
    input_list = input().split()
    shells = []
    regions = []
    while not input_list[0] == 'Aggregate':
        new_shell=Shell(region=input_list[0],size=input_list[1])
        shells.append(new_shell)
        regions.append(new_shell.region)
        input_list = input().split()

    filtered_regions = sorted(set(regions), key=lambda x: regions.index(x))

    for filtered_region in filtered_regions:
        shells_sizes = []
        for shell in shells:
            if shell.region == filtered_region:
                shells_sizes.append(shell.size)
        filtered_shells = sorted(set(shells_sizes), key=lambda x: shells_sizes.index(x))
        giant_size_shell = giant_Shell_Checker(filtered_shells)

        print(f'{filtered_region} -> {", ".join(list(map(str,filtered_shells)))} ({math.ceil(giant_size_shell)})')
