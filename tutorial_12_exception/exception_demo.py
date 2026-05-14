num1 = 5
num2 = 0

try:
    print(num1/num2)
except ZeroDivisionError:
    print("you can not divide",num1,"by zero")


print("After division: ")

score = "seventy two"

try:
    print(int(score))
except ValueError:
    print(f"you can not convert {type(score)} into number")
print("end")

item = ("samosa", 15)

try:
    item[1] = 20
except TypeError:
    print("tuple values can not be updated")
print("Name:",item[0])
print("Price:",item[1])