names = ["Samosa ", "Tea   ", "Burger"]
prices = [15, 10, 55]
quantities = [0, 0, 0]
total = 0

print("======== Welcome to my shop ========")
print("============= Our menu =============")

print()
for i in range(len(names)):
    print(f"{i+1}. {names[i]}\t\t- RS.{prices[i]}")

print()
for i in range(len(names)):
    quantities[i] = int(input(f"Enter {names[i].strip()} quantity: "))
    total = total + (quantities[i] * prices[i])

print()

print(f"Item\tQuantity\tPrice\tTotal")
print("-------------------------------------")
for i in range(len(names)):
    print(f"{names[i]}\t\t{quantities[i]}\t{prices[i]}\t{quantities[i]*prices[i]}")
print("-------------------------------------")

print()
print("\t\t\tTotal Bill:",total)
print()
