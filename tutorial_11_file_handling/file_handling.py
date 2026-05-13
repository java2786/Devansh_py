file = open("items.txt", "r")
# file.write("\nThis is a demo code")
for line in file.readlines():
    # print(type(line))
    # print(line, end="")
    list = line.split(",")
    name = list[0]
    price = int(list[1])
    quantity = int(list[2])
    bill = int(list[3])

    print(f"Name: {name}, Price: {price}, Quantity: {quantity}, Bill: {bill}")
file.close()

