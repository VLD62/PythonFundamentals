class Person:
    def __init__(self, firstName, lastName, cardNum, tickets):
        self.firstName = firstName
        self.lastName = lastName
        self.cardNum = cardNum
        self.tickets = tickets
        self.ident = self.firstName + ' ' + self.lastName
        self.total_sum = self.get_ticket_sum()

    def get_ticket_sum(self):
        total_price = 0
        for ticket in self.tickets:
            total_price += ticket.price
        return total_price


class Ticket:
    def __init__(self, destination, price, discount):
        self.destination = destination
        self.price = price
        self.discount = discount


if __name__ == "__main__":

    N = int(input())
    persons = []

    for num in range(N):
        person_input = input()

        first_name = person_input.split()[0]
        last_name = person_input.split()[1]
        card_num = person_input.split()[2]
        new_person = Person(firstName=first_name, lastName=last_name,
                            cardNum=[], tickets=[])
        new_person.cardNum.append(card_num)
        if new_person.ident not in [existing_person.ident for existing_person in persons]:
            persons.append(new_person)
        else:
            for existing_person in persons:
                if new_person.ident == existing_person.ident:
                    existing_person.cardNum += new_person.cardNum

    input_cmd = input().split()
    while not input_cmd[0] == 'time':

        if input_cmd[0] == 'createTicket':
            firstName = input_cmd[1]
            lastName = input_cmd[2]
            destination = input_cmd[3]
            cardNumber = input_cmd[4]
            ident = firstName + ' ' + lastName
            new_ticket = Ticket(destination=destination,
                                price=sum(ord(ch) for ch in destination) / 100, discount=None)

            new_person = Person(firstName=firstName, lastName=lastName,
                                cardNum=[], tickets=[])

            if new_person.ident not in [existing_person.ident for existing_person in persons]:
                persons.append(new_person)

            for person in persons:
                if new_person.ident == person.ident:
                    if cardNumber in [existing_cardNum for existing_cardNum in person.cardNum]:
                        new_ticket.price = new_ticket.price / 2
                        new_ticket.discount = cardNumber
                    else:
                        if sum(int(num) for num in cardNumber) % 7 == 0:
                            existing = False
                            for person_exist in persons:
                                if not person_exist.ident == ident:
                                    if cardNumber in [existing_cardNum for existing_cardNum in person_exist.cardNum]:
                                        print(
                                            f'card {cardNumber} already exists for another passenger!')
                                        existing = cardNumber
                            if not existing:
                                person.cardNum.append(cardNumber)
                                print(f'issuing card {cardNumber}')
                                new_ticket.price = new_ticket.price / 2
                                new_ticket.discount = cardNumber
                        else:
                            print(f'card {cardNumber} is not valid!')
                    person.tickets.append(new_ticket)
                    person.total_sum = person.get_ticket_sum()

        input_cmd = input().split()
        print_persons = [
            person for person in persons if len(person.tickets) > 0]

    for person in sorted(print_persons, key=lambda x: -x.total_sum):
        print(f'{person.ident}:')
        total_price = 0
        for ticket in sorted(person.tickets, key=lambda x: -x.price):
            if not ticket.discount == None:
                print(
                    f'--{ticket.destination}: {ticket.price:.2f}lv (using card {ticket.discount})')
            else:
                print(f'--{ticket.destination}: {ticket.price:.2f}lv')
        print(f'total: {person.total_sum:.2f}lv')
