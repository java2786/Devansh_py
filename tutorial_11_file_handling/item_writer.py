file = open("items.txt", "a")
name = input("Enter item name: ")
price = input("Enter item price: ")

file.write(f"{name},{price},0,0\n")
file.close()