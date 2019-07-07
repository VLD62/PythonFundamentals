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


def result_printer(input_string):

    if input_string == "Salary":
        for k,v in salary_dict.items():
            print(f'Name: {k}')
            print(f'Salary: {v}')
            print(delimiter)
    elif input_string == "Position":
        for k,v in position_dict.items():
            print(f'Name: {k}')
            print(f'Position: {v}')
            print(delimiter)
    elif input_string == "Age":
        for k,v in age_dict.items():
            print(f'Name: {k}')
            print(f'Age: {v}')
            print(delimiter)   


if __name__ == "__main__":

    input_string = input()
    age_dict = {}
    salary_dict = {}
    position_dict = {}
    delimiter = '===================='
    
    while not input_string == "filter base": 
        if not input_string == "":
            input_list = input_string.split(" -> ")
            if isinstance(string_checker(input_list[1]),int):
                age_dict[input_list[0]] = input_list[1]
            elif isinstance(string_checker(input_list[1]),float):
                salary_dict[input_list[0]] = input_list[1]
            else:
                position_dict[input_list[0]] = input_list[1]
            input_string = input()
        else:
            break
    
    result_printer(input())
