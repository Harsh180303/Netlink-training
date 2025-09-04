# Formatting Output

item_name = input("Enter item name ")
quantity = int(input('Enter Quantity' ))
price_per_unit = float(input("Enter per unit price" ))

total_cost = quantity * price_per_unit

print(f"{quantity} unit of {item_name} at {price_per_unit} rs. per_unit is {total_cost}")