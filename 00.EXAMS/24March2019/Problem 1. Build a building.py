if __name__ == "__main__":
    budget = float(input())
    m = float(input())
    n = int(input())

    for i in range (0,n):
        current_money = float(input())
        print(f'Investor {i+1} gave us {current_money:.2f}.')
        m += current_money

        if m >= budget:
            print(f'We will manage to build it. Start now! Extra money - {m - budget:.2f}.')
            exit(0)
    
    if m < budget:
        print(f'Project can not start. We need {budget - m:.2f} more.')
