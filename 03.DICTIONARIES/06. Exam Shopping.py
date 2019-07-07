if __name__ == "__main__":
    input_string = input()
    inventory = {}
    
    while not input_string == "shopping time": 
      products = input_string.split(" ")
      if products[1] in inventory.keys():
        inventory[products[1]] += int(products[2])
      else:
        inventory[products[1]] = int(products[2])
      input_string = input()

    while not input_string == "exam time":
        products = input_string.split(" ")

        if products[1] in inventory.keys():
            if inventory[products[1]] == 0:
                print(f"{products[1]} out of stock")
            elif inventory[products[1]] > int(products[2]):
                inventory[products[1]] = inventory[products[1]] - int(products[2])
            elif inventory[products[1]] < int(products[2]):
                inventory[products[1]] = 0
            else:
                inventory[products[1]] = int(products[2]) - inventory[products[1]]
        elif products[1] == "time":
            pass
        else:
            print(f"{products[1]} doesn't exist")
        input_string = input()

    for k,v in inventory.items():
        if v > 0:
            print(f'{k} -> {v}')