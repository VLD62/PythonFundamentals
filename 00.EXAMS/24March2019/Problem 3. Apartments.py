class Neighborhood:
    def __init__(self,name,blocks):
        self.name = name
        self.blocks = blocks

class Block:
    def __init__(self,number,available_apartments=0,price_per_apt=None):
        self.number = number
        self.available_apartments = available_apartments
        self.price_per_apt = price_per_apt

if __name__ == "__main__":

    neighborhood_input = input().split(' -> ')
    neighborhood_list = []

    while not neighborhood_input[0] == 'collectApartments':

        new_neighborhood = Neighborhood(name=neighborhood_input[0],blocks = [])
        for block in sorted(list(map(int,neighborhood_input[1].split(",")))):
            new_block = Block(number=block)
            if new_block.number not in [existing_block.number for existing_block in new_neighborhood.blocks]:
                new_neighborhood.blocks.append(new_block)

        if not new_neighborhood.name in [existing_neighborhood.name for existing_neighborhood in neighborhood_list]:
            neighborhood_list.append(new_neighborhood)
        else:
            for existing_neighborhood in neighborhood_list:
                if existing_neighborhood.name == new_neighborhood.name:
                    for existing_block in existing_neighborhood.blocks:
                        for new_block in new_neighborhood.blocks:
                            if existing_block.number == new_block.number:
                                    new_neighborhood.blocks.remove(new_block)
                    existing_neighborhood.blocks += new_neighborhood.blocks

        neighborhood_input = input().split(' -> ')

    apartments_data =  input().split(' -> ')

    while not apartments_data[0] == 'report':
        for neighborhood in neighborhood_list:
            if neighborhood.name == apartments_data[0].split('&')[0]:
                for block in neighborhood.blocks:
                    if block.number == int(apartments_data[0].split('&')[1]):
                        block.available_apartments = apartments_data[1].split('|')[0]
                        block.price_per_apt =  apartments_data[1].split('|')[1]
        apartments_data =  input().split(' -> ')

    neighborhood_list_sorted = sorted(neighborhood_list,key=lambda x: x.name)

    for neighborhood in neighborhood_list_sorted:
        print(f'Neighborhood: {neighborhood.name}')
        for block in neighborhood.blocks:
            print(f'* Block number: {block.number} -> {block.available_apartments} apartments for sale. Price for one: {block.price_per_apt}')