r'LISTS:'
'Remove duplicated elements, keeps order of the array:'
    filtered_colors = sorted(set(colors), key=lambda x: colors.index(x))

'Sort list of objects:'
    new_list = sorted(list_of_RealNumber,key=lambda x: float(x.value))

'sort by 2 keys:'
    boxes.sort(key=lambda x: (x.fruit_val, - x.weigth))

'sort by 2 keys asc desc:'
    apartment_list_sorted = sorted(apartment_list,key=lambda x: (float(x.price), -float(x.square_meters)))
    taken_apartments = sorted(sorted(taken_apartments, key=lambda xa: xa.square_meters, reverse=True), key=lambda xa: xa.price)
    items.sort(key = lambda obj: (obj.firstname, [(-ord(c) for c in obj.lastname)]))
    apartment_list.sort(key = lambda obj: (obj.price, [(-ord(c) for c in obj.square_meters)]))
    apartment_list.sort(key = lambda obj: (obj.firstname, [(-ord(c) for c in obj.lastname)]))
    boxes.sort(key=lambda x: (x.fruit_val, - x.weigth))

'sort by 2 keys if one is string:'

    sorted_players = sorted(players,key=lambda x: (-x.score, x.name), reverse=True)


'uniq array keep order:'
def uniq(array):
    if len(array) == 0:
        return []
    else:
        return [array[0]] + uniq([x for x in array if x != array[0]])

'Check if list elements are uniq:'

def _set(array):
    return len(set(array)) == len(array)

'Check if object is in the list of objects:'
    if new_book.title not in [book.title for book in book_store]:
        book_store.append(new_book)

r'STR checks'
'check if str is int:
'
def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True

r'Objects':
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