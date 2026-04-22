num = 4001
original_num = num
result = 0

while(num>0):
    ld = num % 10
    result = (result*10) + ld 
    num = num // 10

print(f"Reverse of {original_num} is {result}.")

