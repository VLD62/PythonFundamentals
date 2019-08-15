if __name__ == "__main__":
    destination_star = input()
    star_distance = int(input())
    budget = int(input())
    fuel_cons = float(input()) 
    gas_price = float(input())


    total = (star_distance * (fuel_cons/100 * gas_price))

    if total > budget :
        print(f'Maybe another time, need ${(total - budget):.2f} more')
    else:
        print(f'Off to {destination_star} with ${(budget-total):.2f} for snacks')