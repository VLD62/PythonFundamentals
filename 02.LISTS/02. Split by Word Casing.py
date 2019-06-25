import re

def case_checker(word):
    capital_flag = 0
    lower_flag = 0
    for letter in word:
        if letter.isupper():
            capital_flag += 1
        else:
            lower_flag += 1

    if lower_flag == 0 and word.isalpha():
        upper_case.append(word)
    elif capital_flag == 0 and word.isalpha():
        lower_case.append(word)
    else:
        mixed_case.append(word)

if __name__ == '__main__':
    text = re.split(r'[\;\,\:\.\!\(\)\"\'\\\/\[\]\s]',input())
    lower_case = []
    mixed_case = []
    upper_case = []
 
    for word in text:
        case_checker(word)
    

    print('Lower-case: ' + ", ".join(filter(None, lower_case)))
    print('Mixed-case: ' + ", ".join(filter(None, mixed_case)))
    print('Upper-case: ' + ", ".join(filter(None, upper_case)))