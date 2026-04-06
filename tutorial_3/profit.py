price = 15
pay = int(input("Enter amount to pay:"))

profit = pay - price 

if(profit >= 0):
    print("Profit",profit)
else:
    print("Loss",profit)
    