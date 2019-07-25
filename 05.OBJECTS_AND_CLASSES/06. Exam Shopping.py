class Product:
    def __init__(self, name, qty):
        self.name = name
        self.qty = int(qty)


if __name__ == '__main__':

    command = input().split()
    inventory = []
    while not command[0] == 'shopping':
        new_product = Product(name=command[1], qty=command[2])
        if new_product.name not in [product.name for product in inventory]:
            inventory.append(new_product)
        else:
            for product in inventory:
                if new_product.name == product.name:
                    product.qty += new_product.qty
        command = input().split()
    command = input().split()
    while not command[0] == 'exam':
        buy_product = Product(name=command[1], qty=command[2])
        if buy_product.name not in [product.name for product in inventory]:
            print(f"{buy_product.name} doesn't exist")
        else:
            for product in inventory:
                if buy_product.name == product.name:
                    if product.qty < 1:
                        print(f'{buy_product.name} out of stock')
                    else:
                        product.qty -= buy_product.qty
        command = input().split()
    for product in inventory:
        if product.qty > 0:
            print(f"{product.name} -> {product.qty}")
