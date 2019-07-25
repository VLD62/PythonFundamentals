class Char:
    def __init__(self, character, count):
        self.character = character
        self.count = count


if __name__ == '__main__':
    list_of_chars = [char for char in input()]
    chars_count = []

    for char in list_of_chars:
        single_char = Char(character=char, count=1)
        if single_char.character not in [chr.character for chr in chars_count]:
            chars_count.append(single_char)
        else:
            for chr in chars_count:
                if chr.character == single_char.character:
                    chr.count += 1

    for char in chars_count:
        print(f'{char.character} -> {char.count}')
