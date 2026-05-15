item_1_name = "Samosa "
item_1_quantity = 0
item_1_price = 15
item_1_total = 0

item_2_name = "Tea   "
item_2_quantity = 0
item_2_price = 10
item_2_total = 0

item_3_name = "Burger"
item_3_quantity = 0
item_3_price = 55
item_3_total = 0

print("======== Welcome to my shop ========")
print("============= Our menu =============")

print()
print(f"1. {item_1_name}\t\t- RS.{item_1_price}")
print(f"2. {item_2_name}\t\t- RS.{item_2_price}")
print(f"3. {item_3_name}\t\t- RS.{item_3_price}")

print()

item_1_quantity = int(input(f"Enter {item_1_name.strip()} quantity: "))
item_2_quantity = int(input(f"Enter {item_2_name.strip()} quantity: "))
item_3_quantity = int(input(f"Enter {item_3_name.strip()} quantity: "))
print()

item_1_total = item_1_quantity * item_1_price
item_2_total = item_2_quantity * item_2_price
item_3_total = item_3_quantity * item_3_price

print(f"Item\tQuantity\tPrice\tTotal")
print("-------------------------------------")
print(f"{item_1_name}\t\t{item_1_quantity}\t{item_1_price}\t{item_1_total}")
print(f"{item_2_name}\t\t{item_2_quantity}\t{item_2_price}\t{item_2_total}")
print(f"{item_3_name}\t\t{item_3_quantity}\t{item_3_price}\t{item_3_total}")
print("-------------------------------------")
total = item_1_total + item_2_total + item_3_total
print()
print("\t\t\tTotal Bill:",total)
print()
