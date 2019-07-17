class BankAccount:

   def __init__(self, name, bank, balance):
       self.name = name
       self.bank = bank
       self.balance = balance


if __name__ == "__main__":

    input_line = input()
    accounts_list = []
    while not input_line == 'end':

        single_account_list = input_line.split(" | ")
        account = BankAccount(name=single_account_list[1],bank=single_account_list[0],balance=float(single_account_list[2]))
        accounts_list.append(account)
        input_line = input()

    for account in sorted(accounts_list,key=lambda x: (-x.balance,len(x.bank))):
        print(f'{account.name} -> {account.balance:.2f} ({account.bank})')