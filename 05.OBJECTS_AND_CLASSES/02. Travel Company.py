class City:
    def __init__(self, name, total_capacity=0, vehicle_list=[]):
        self.name = name
        self.total_capacity = int(total_capacity)
        self.vehicle_list = vehicle_list


class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = int(capacity)


if __name__ == '__main__':

    input_list = input().split(":")
    city_list = []

    while not input_list[0] == "ready":
        new_city = City(name=input_list[0], vehicle_list=[])
        for single_vehicle in input_list[1].split(","):
            single_vehicle_splitted = single_vehicle.split("-")
            new_vehicle = Vehicle(
                name=single_vehicle_splitted[0], capacity=single_vehicle_splitted[1])
            # Checks for existing vehicle and replace capacity
            if new_city.name in [existing_city.name for existing_city in city_list]:
                for existing_city in city_list:
                    if existing_city.name == new_city.name:
                        for vehicles in existing_city.vehicle_list:
                            if new_vehicle.name == vehicles.name:
                                vehicles.capacity = new_vehicle.capacity
                        if not new_vehicle.name in [existing_vehicle.name for existing_vehicle in existing_city.vehicle_list]:
                            existing_city.vehicle_list.append(new_vehicle)
            else:
                new_city.vehicle_list.append(new_vehicle)

        if new_city.name in [existing_city.name for existing_city in city_list]:
            for existing_city in city_list:
                if existing_city.name == new_city.name:
                    existing_city.vehicle_list.extend(new_city.vehicle_list)
        else:
            city_list.append(new_city)
        input_list = input().split(":")

    for city in city_list:
        for vehicle in city.vehicle_list:
            city.total_capacity += vehicle.capacity

    travel_list = input().split()

    while not travel_list[0] == 'travel':
       ref_city = travel_list[0]
       ref_capacity = int(travel_list[1])

       for city in city_list:
          if ref_city == city.name:
              if ref_capacity <= city.total_capacity:
                print(f'{ref_city} -> all {ref_capacity} accommodated')
              else:
                print(
                    f'{ref_city} -> all except {ref_capacity - city.total_capacity} accommodated')

       travel_list = input().split()
