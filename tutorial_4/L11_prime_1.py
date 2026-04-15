# num = 25
num = 169
divisible = False

for i in range(2, num):
    print("Divisible by ",i,"=>",num%i==0)
    if(num%i==0):
        divisible = True
        break

if(divisible==True):
    print(num,"is Not Prime")
else:
    print(num,"is Prime")