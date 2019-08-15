if __name__ == "__main__":
    state_integers = list(map(int,input().split()))
    command_integers = list(map(int,input().split()))
    for cmd in command_integers:

        for index, num in enumerate(state_integers):

            if cmd % 2 == 0:
                if num % 2 == 0:
                    state_integers[index] = num * abs(cmd)
            else:
                if num % 2 == 1:
                    state_integers[index] = num // abs(cmd)
        
        for index, num in enumerate(state_integers):
            if cmd > 0:
                if num > 0:
                    state_integers[index] += cmd
            else:
                if num < 0:
                    state_integers[index] += cmd
    print(state_integers)



