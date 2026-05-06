# item1 = {"name": "samosa", "price": 15, "quantity": 0, "bill": 0}
# item2 = {"name": "tea   ", "price": 10, "quantity": 0, "bill": 0}
# item3 = {"name": "burger", "price": 25, "quantity": 0, "bill": 0}
# item4 = {"name": "pizza", "price": 99, "quantity": 0, "bill": 0}

# items = [item1, item2, item3, item4]
total_bill = 0
items = [
    {"name": "samosa", "price": 15, "quantity": 0, "bill": 0},
    {"name": "tea   ", "price": 10, "quantity": 0, "bill": 0},
    {"name": "burger", "price": 25, "quantity": 0, "bill": 0},
    {"name": "pizza", "price": 99, "quantity": 0, "bill": 0}
]

print("======== Welcome to my shop ========")
print("============= Our menu =============")

for i in range(len(items)):
    # print(f"{i}. {type(items[i])} -> {items[i]}")
    item = items[i]
    print(f"{i+1}. {item['name']}\t\t - Rs. {item['price']}")

for i in range(len(items)):
    item = items[i]
    item['quantity'] = int(input(f"Enter {item['name']} quantity: "))
    if(item['quantity']<0):
        item['quantity'] = 0
        
    item['bill'] = item['quantity'] * item['price']
    total_bill = total_bill + item['bill']
    # print(f"******* {item}")

print("Item\tQuantity\tPrice\tBill")
print("-------------------------------------")
for i in range(len(items)):
    item = items[i]
    print(f"{item['name']}\t{item['quantity']}\t\t{item['price']}\t{item['bill']}")

print("-------------------------------------")
print(f"\t\t\t\t\t\tAmount: {total_bill}")