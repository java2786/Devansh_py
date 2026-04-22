for num in range(10001):
    original_num = num
    count = 0

    while(num>0):
        # ld = num % 10     
        num = num // 10     
        count = count + 1   

    num = original_num
    add = 0

    while(num>0):
        ld = num % 10 
        add = add + ld**count    
        num = num // 10 

    num = original_num

    if(num == add):
        print(num,"is armstrong number.")
