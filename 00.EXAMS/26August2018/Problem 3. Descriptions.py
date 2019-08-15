import re

class Person:
    def __init__(self,name,age,birthdate):
        self.name = name
        self.age = age
        self.birthdate = birthdate

if __name__ == "__main__":
    input_string = input()
    person_list = []
    while not input_string == 'make migrations':
        name = re.search(r'name is ([A-Z][\w]+ [A-Z][\w]+)', input_string)
        age  = re.search(r' [\d][\d] years', input_string)
        birthdate = re.search(r'on [\d][\d]-[\d][\d]-[\d][\d][\d][\d]', input_string)

        if name is not None and age is not None and birthdate is not None and int(age.group(0).split()[0]) > 9 and int(age.group(0).split()[0]) < 100:
            new_person = Person(name = name.group(0), age = age.group(0), birthdate = birthdate.group(0))
            person_list.append(new_person)
        input_string = input()

    if len(person_list) < 1:
        print('DB is empty')
    else:
        for person in person_list:
            print(f"Name of the person: {(person.name).lstrip('name is ')}.\nAge of the person: {((person.age).rstrip(' years').strip())}.\nBirthdate of the person: {(person.birthdate).lstrip('on ')}.")