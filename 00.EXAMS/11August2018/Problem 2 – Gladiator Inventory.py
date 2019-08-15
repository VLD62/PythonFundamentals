if __name__ == "__main__":

    input_inventory = input().split()

    cmd_input = input().split()

    while not cmd_input[0] == 'Fight!':

        if (cmd_input[1] in [el for el in input_inventory] or cmd_input[1].split("-")[0] in [el for el in input_inventory]):
            for index, item in enumerate(input_inventory):
                if cmd_input[0] == 'Trash' and item == cmd_input[1]:
                    input_inventory.remove(cmd_input[1])
                if cmd_input[0] == 'Repair' and item == cmd_input[1]:
                    input_inventory.remove(cmd_input[1])
                    input_inventory.append(cmd_input[1])
                if cmd_input[0] == 'Upgrade' and item == cmd_input[1].split("-")[0]:
                    input_inventory.insert(
                        index+1, ":".join(cmd_input[1].split("-")))
        else:
            if cmd_input[0] == 'Buy':
                input_inventory.append(cmd_input[1])

        cmd_input = input().split()

    print(" ".join(input_inventory))
