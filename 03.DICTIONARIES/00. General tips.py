if __name__ == '__main__':
    #key = input()
    #value = input()
    #N = int(input())
    
    student = {
        'username': 'Ines',
        'pass': 'adasdas46@',
        'courses': ['PB', 'Python']
    }
    #show vaues
    for item in student.items():
        print(item[1])

    for key,value in student.items():
        print(key)
        print(value)
    
    #check if key exists
    print(student.get('Pass','kon')) #check if key exists

    if 'Pass' in student.keys():
        print('here')
    else:
        print('not here')
    #append lists
    second_part_student = {
        'age': 25,
        'grade': 5
    }

    student.update(second_part_student)