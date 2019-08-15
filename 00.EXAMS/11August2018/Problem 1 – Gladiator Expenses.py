if __name__ == "__main__":

    lost_fights_count = int(input())
    helmet_price = float(input())
    sword_price = float(input())
    shield_price = float(input())
    armor_price = float(input())
    shield_broken = 0
    total_expenses = 0

    for n in range(1, lost_fights_count+1):
        if n % 2 == 0:
            total_expenses += helmet_price
        if n % 3 == 0:
            total_expenses += sword_price
        if n % 2 == 0 and n % 3 == 0:
            total_expenses += shield_price
            shield_broken += 1
        if shield_broken == 2:
            total_expenses += armor_price
            shield_broken = 0

    print(f'Gladiator expenses: {total_expenses:.2f} aureus')