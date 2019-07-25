class Person:
    def __init__(self, name, cash):
        self.name = name
        self.cash = int(cash)


if __name__ == '__main__':
    input_list = input().split(' = ')
    person_list = []

    while not input_list[0] == 'end':
        if input_list[1].isdigit():
            single_person = Person(name=input_list[0], cash=input_list[1])
            if single_person.name not in [person.name for person in person_list]:
                person_list.append(single_person)
            else:
                for person in person_list:
                    if person.name == single_person.name:
                        person.cash = single_person.cash
        else:
            for person in person_list:
                if person.name == input_list[1]:
                    if input_list[0] not in [person.name for person in person_list]:
                        single_person = Person(
                            name=input_list[0], cash=person.cash)
                        person_list.append(single_person)
                    else:
                        for another_person in person_list:
                            if another_person.name == input_list[0]:
                                another_person.cash = person.cash
        input_list = input().split(' = ')

    for person in person_list:
        print(f'{person.name} === {person.cash}')
