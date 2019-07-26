class Person:
    def __init__ (self, name, values=[]):
        self.name = name
        self.values = values

if __name__ == '__main__':
    input_list = input().split(' -> ')
    person_list = []

    while not input_list[0] == 'end':
        if input_list[1][0].isdigit():
            new_person = Person(name=input_list[0],values=input_list[1].split(', '))
            if new_person.name not in [existing_person.name for existing_person in person_list]:
                person_list.append(new_person)
            else:
                for existing_person in person_list:
                    if existing_person.name == new_person.name:
                        existing_person.values.extend(new_person.values)
        else:
            if input_list[1] in [existing_person.name for existing_person in person_list]:
                for existing_person in person_list:
                    if existing_person.name == input_list[1]:
                        new_person=Person(name=input_list[0],values=existing_person.values)
                        person_list.append(new_person)


        input_list = input().split(' -> ')

    for person in person_list:
        print(f'{person.name} === {", ".join(person.values)}')
