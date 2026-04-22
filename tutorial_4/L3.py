n = 1234
sum = 0

while(n>0):
    ld = n%10
    n = n // 10

    sum = sum + ld

print(sum)