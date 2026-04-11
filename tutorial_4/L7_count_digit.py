# cound digits in a number
num = 2432 
count = 0

while(num>0):
    ld = num % 10
    num = num // 10
    count = count + 1