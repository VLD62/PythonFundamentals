if __name__ == "__main__":
    user_string = input()
    inventory = {}
    failed = 0
    while not user_string == "login": 
      users_password = user_string.split(" ")
      inventory[users_password[0]] = users_password[2]
      user_string = input()

    input_string = input()
    while not input_string == "end": 
      users_password = input_string.split(" ")
      if users_password[0] in inventory.keys():
         if inventory[users_password[0]] == users_password[2]:
             print(f'{users_password[0]}: logged in successfully')
         else:
             failed += 1
             print(f'{users_password[0]}: login failed')
      else:
        failed += 1
        print(f'{users_password[0]}: login failed')
      input_string = input()

    print(f'unsuccessful login attempts: {failed}')