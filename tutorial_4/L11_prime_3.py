for num in range(2, 101):
    divisible = False

    for i in range(2, (num//2)+1):
        if(num%i==0):
            divisible = True
            break

    if(divisible==True):
        # print(num,"is Not Prime")
        pass 
    else:
        print(num,"is Prime")