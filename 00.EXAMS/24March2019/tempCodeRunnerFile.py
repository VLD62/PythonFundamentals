class Apartment:
    def __init__(self,id_,rooms,baths,square_meters, price, taken):
        self.id_ = id_.strip('\"')
        self.rooms = rooms
        self.baths = baths
        self.square_meters = square_meters
        self.price = price
        self.taken = taken

class LivingApartment(Apartment):
    def __init__(self,id_,rooms,baths,square_meters, price, taken):
        super().__init__(id_,rooms,baths,square_meters, price, taken)

class OfficeApartment(Apartment):
    def __init__(self,id_,rooms,baths,square_meters, price, taken):
        super().__init__(id_,rooms,baths,square_meters, price, taken)


if __name__ == "__main__":

    command_input = input().split("(")
    apartment_list = []


    while not command_input[0] == 'start_selling':
        apt_type = command_input[0]
        details = command_input[1].rstrip(")").split(",")
        if len(details) < 5:
            print("__init__() missing 1 required positional argument: 'price'")
        else:
            if apt_type == 'LivingApartment':
                new_apartment = LivingApartment(id_= details[0], rooms=details[1], baths = details[2], square_meters = details[3], price = details[4], taken = False)
                apartment_list.append(new_apartment)
            if apt_type == 'OfficeApartment':
                new_apartment = OfficeApartment(id_= details[0], rooms=details[1], baths = details[2], square_meters = details[3], price = details[4], taken = False)
                apartment_list.append(new_apartment)
            if apt_type == 'Apartment':
                print("Can't instantiate abstract class Apartment with abstract methods __str__")
        command_input = input().split("(")

    command_input = input().split()

    if len(command_input) > 1:
        while True:
            action, id_ = command_input[0], command_input[1]
            non_exist = True

            if action == 'buy':
                for apartment in apartment_list:
                    if apartment.id_ == id_:
                        non_exist = False
                        if apartment.taken == True:
                            print(f'Apartment with id - {id_} is already taken!')
                        else:
                            apartment.taken = True

            if action == 'hire':
                for apartment in apartment_list:
                    if apartment.id_ == id_:
                        non_exist = False
                        if apartment.taken == True:
                            print(f'Apartment with id - {id_} is already taken!')
                        else:
                            if isinstance(apartment,OfficeApartment):
                                print(f'Apartment with id - {id} is only for renting!')
                            else:
                                apartment.taken = True

            if action == 'rent':
                for apartment in apartment_list:
                    if apartment.id_ == id_:
                        non_exist = False
                        if apartment.taken == True:
                            print(f'Apartment with id - {id_} is already taken!')
                        else:
                            if isinstance(apartment, LivingApartment):
                                print(f'Apartment with id - {id_} is only for selling!')
                            else:
                                apartment.taken = True

            if non_exist == True:
                print(f'Apartment with id - {id_} does not exist!')
            command_input = input().split()
            if command_input[0] == 'free' or command_input[0] == 'taken':
                break

    have_info = False

    apartment_list_sorted = sorted(apartment_list,key=lambda x: (float(x.price), -float(x.square_meters)))

    if command_input[0] == 'taken':
        for apartment in apartment_list_sorted:
            if apartment.taken == True:
                print(f'{apartment.rooms.strip(" ")} rooms place with {apartment.baths.strip(" ")} bathroom/s.\n{float(apartment.square_meters)} sq. meters for {float(apartment.price)} lv.')
                have_info = True

    if command_input[0] == 'free':
        for apartment in apartment_list_sorted:
            if apartment.taken == False:
                print(f'{apartment.rooms.strip(" ")} rooms place with {apartment.baths.strip(" ")} bathroom/s.\n{float(apartment.square_meters)} sq. meters for {float(apartment.price)} lv.')
                have_info = True

    if have_info == False:
        print('No information for this query')
