
unit_cost = 100

quantity = int(input("Units purchased: "))

total_cost = unit_cost * quantity

if total_cost > 1000:
    discount = total_cost * (10/100)
    total_cost -= discount
    print(f"The total cost after discount: {total_cost}")
else:
    print(f"The total cost is :{total_cost}")

