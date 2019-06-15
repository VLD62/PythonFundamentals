def print_header():
    print('CASH RECEIPT')


def print_mid():
    print('Charged to____________________')
    print('Received by___________________')
    

def print_bottom():
    print('© SoftUni')


def print_dashes():
    print('------------------------------')


def print_receipt():
    print_header()
    print_dashes()
    print_mid()
    print_dashes()
    print_bottom()


if __name__ == '__main__':
    print_receipt()