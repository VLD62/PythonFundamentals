class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number


if __name__ == '__main__':

    input_list = input().split(' : ')

    person_list = []

    while not input_list[0] == 'Over':
        if input_list[0].isdigit():
            new_person = Person(name=input_list[1], number=input_list[0])
        else:
            new_person = Person(name=input_list[0], number=input_list[1])
        person_list.append(new_person)
        input_list = input().split(' : ')

    new_list = sorted(person_list, key=lambda x: x.name)

    for person in new_list:
        print(f'{person.name} -> {person.number}')
