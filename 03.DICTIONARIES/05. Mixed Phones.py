def isInt(astring):
    """ Is the given string an integer? """
    try: int(astring)
    except ValueError: return False
    else: return True

if __name__ == "__main__":
    input_string = input()
    phonebook = {}
    while not input_string == "Over":
        list_of_string = input_string.split(" : ")
        if isInt(list_of_string[0]):
            phonebook[list_of_string[1]] = list_of_string[0]
        else:
            phonebook[list_of_string[0]] = list_of_string[1]
        input_string = input()
    for k,v in sorted(phonebook.items()):
           print(f"{k} -> {v}")    
