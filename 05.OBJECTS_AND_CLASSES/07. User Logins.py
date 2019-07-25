class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password


if __name__ == '__main__':

    input_info = input().split(" -> ")
    users_list = []
    failed_logins_count = 0

    while not input_info[0] == "login":

        new_user = User(name=input_info[0], password=input_info[1])
        if new_user.name not in [user.name for user in users_list]:
            users_list.append(new_user)
        else:
            for user in users_list:
                if user.name == new_user.name:
                    user.password = new_user.password
        input_info = input().split(" -> ")

    input_info = input().split(" -> ")
    while not input_info[0] == "end":

        ref_user = User(name=input_info[0], password=input_info[1])
        if ref_user.name not in [user.name for user in users_list]:
            failed_logins_count += 1
            print(f'{ref_user.name}: login failed')
        else:
            for user in users_list:
                if user.name == ref_user.name and user.password == ref_user.password:
                    print(f'{ref_user.name}: logged in successfully')
                elif user.name == ref_user.name:
                    failed_logins_count += 1
                    print(f'{ref_user.name}: login failed')
        input_info = input().split(" -> ")

    print(f'unsuccessful login attempts: {failed_logins_count}')
