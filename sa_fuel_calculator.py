print("=====================================")
kilometers = float(input("Enter kilometers to be travelled\n= "))
current_petrol_price = float(input("Enter current petrol price per liter\n= "))
liters_needed = kilometers / 10
print("")
total_cost = liters_needed * current_petrol_price
print(f"total cost: R{round(total_cost, 2)}")
print("=====================================")


