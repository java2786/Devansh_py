# Sum of factorials of each num

num = 132
result = 0
while(num>0):
    ld = num % 10
    fact = 1
    for i in range(1, ld+1):
        fact = fact * i 
    result = result + fact 
    num = num // 10

print(result)
