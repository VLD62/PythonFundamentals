class Employee:
    def __init__(self, name, age=None, salary=None, position=None,
    age_input_counter=0, salary_input_counter=0, position_input_counter=0):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position
        self.age_input_counter = int(age_input_counter)
        self.salary_input_counter = int(salary_input_counter)
        self.position_input_counter = int(position_input_counter)



def string_checker(input_value):
    reference = None
    try:
       reference = int(input_value)
       input_value = reference
    except:
        try:
           reference = float(input_value)
           if int(reference) == float(reference):
                reference = int(reference)
           input_value = reference
        except:
           pass
    return input_value


if __name__ == "__main__":

    input_list = input().split(' -> ')
    employee_list = []
    age_counter = 0
    salary_counter = 0
    position_counter = 0

    while not input_list[0] == "filter base":
        new_employee = Employee(name=input_list[0])
        if isinstance(string_checker(input_list[1]), int):
            new_employee.age = input_list[1]
            age_counter += 1
        elif isinstance(string_checker(input_list[1]), float):
            new_employee.salary = input_list[1]
            salary_counter +=1
        else:
            new_employee.position = input_list[1]
            position_counter += 1
            new_employee.position_input_counter += position_counter
        if not new_employee.name in [some_employee.name for some_employee in employee_list]:
            employee_list.append(new_employee)
        else:
            for one_employee in employee_list:
                if one_employee.name == new_employee.name:
                    if new_employee.age is not None:
                        one_employee.age = new_employee.age
                        one_employee.age_input_counter = age_counter
                    if new_employee.salary is not None:
                        one_employee.salary = new_employee.salary
                        one_employee.salary_input_counter = salary_counter
                    if new_employee.position is not None:
                        one_employee.position = new_employee.position
                        one_employee.position_input_counter = position_counter
        input_list = input().split(' -> ')

    cmd = input()
    if cmd == 'Position':
        sorted_list = sorted(employee_list, key=lambda x: x.position_input_counter)
        for existing_employee in sorted_list:
            if existing_employee.position is not None:
                print(f'Name: {existing_employee.name}')
                print(f'Position: {existing_employee.position}')
                print('====================')
    elif cmd == 'Salary':
        sorted_list = sorted(employee_list, key=lambda x: x.salary_input_counter)
        for existing_employee in sorted_list:
            if existing_employee.salary is not None:
                print(f'Name: {existing_employee.name}')
                print(f'Salary: {existing_employee.salary}')
                print('====================')
    else:
        sorted_list = sorted(employee_list, key=lambda x: x.age_input_counter)
        for existing_employee in sorted_list:
            if existing_employee.age is not None:
                print(f'Name: {existing_employee.name}')
                print(f'Age: {existing_employee.age}')
                print('====================')
