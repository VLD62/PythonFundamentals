class BasicMonster:
    def __init__(self, name, _id, strength, ugliness):
        self.name = name
        self._id = _id
        self.strength = strength
        self.ugliness = ugliness


class Hydralisk(BasicMonster):
    def __init__(self, name, _id, strength, ugliness, _range):
        super().__init__(name, _id, strength, ugliness)
        self._range = _range


class Zergling(BasicMonster):
    def __init__(self, name, _id, strength, ugliness, speed):
        super().__init__(name, _id, strength, ugliness)
        self.speed = speed


def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True


if __name__ == "__main__":

    monster_input = input().split("(")
    army = []
    overall_speed = 0
    overall_strength = 0
    hydralisk_count = 0
    zergling_count = 0

    while not monster_input[0] == 'stopAddingArmy':
        kind = monster_input[0]
        parameters = monster_input[1].rstrip(")").split(",")
        if kind == 'Zergling':
            if len(parameters) < 5:
                print("__init__() missing 1 required positional argument: 'speed'")
            elif not is_int(parameters[4]):
                print('Speed must be integer')
            else:
                new_zergling = Zergling(name=parameters[0], _id=parameters[1], strength=int(
                    parameters[2]), ugliness=parameters[3], speed=int(parameters[4]))
                army.append(new_zergling)
        elif kind == 'Hydralisk':
            if len(parameters) < 5:
                print("__init__() missing 1 required positional argument: 'range'")
            elif is_int(parameters[4]):
                print('Range must be string')
            else:
                new_hydralisk = Hydralisk(name=parameters[0], _id=parameters[1], strength=int(
                    parameters[2]), ugliness=parameters[3], _range=parameters[4])
                army.append(new_hydralisk)
        else:
            print(
                "Can't instantiate abstract class BaseMonster with abstract methods __init__")
        monster_input = input().split("(")
    for monster in army:
        overall_strength += monster.strength
        if isinstance(monster, Hydralisk):
            hydralisk_count += 1
        else:
            zergling_count += 1
            overall_speed += monster.speed
    print(
        f'Overall speed of army: {overall_speed}\nOverall stength: {overall_strength}\nHydralisk: {hydralisk_count}; Zergling: {zergling_count}')
