class Cloth:
    def __init__(self, type, color, count):
        self.type = type
        self.color = color
        self.count = int(count)


if __name__ == "__main__":
    n = int(input())
    wardrobe = []
    input_list = input().split(' -> ')
    colors = []
    for item in input_list[1].split(","):
        new_cloth = Cloth(type=item, color=input_list[0], count=1)
        for existing_cloth in wardrobe:
            if existing_cloth.type == new_cloth.type and existing_cloth.color == new_cloth.color:
                existing_cloth.count += 1
                new_cloth.count += 1
        if new_cloth.count == 1:
            wardrobe.append(new_cloth)
            colors.append(new_cloth.color)
    for i in range(1, n):
        input_list = input().split(' -> ')
        for item in input_list[1].split(","):
            new_cloth = Cloth(type=item, color=input_list[0], count=1)
            for existing_cloth in wardrobe:
                if existing_cloth.type == new_cloth.type and existing_cloth.color == new_cloth.color:
                    existing_cloth.count += 1
                    new_cloth.count += 1
            if new_cloth.count == 1:
                wardrobe.append(new_cloth)
                colors.append(new_cloth.color)

    cmd = input().split()
    filtered_colors = sorted(set(colors), key=lambda x: colors.index(x))
    for clr in filtered_colors:
        print(f'{clr} clothes:')
        for item in wardrobe:
            if item.color == clr:
               if item.color == cmd[0] and item.type == cmd[1]:
                   print(f'* {item.type} - {item.count} (found!)')
               else:
                   print(f'* {item.type} - {item.count}')
