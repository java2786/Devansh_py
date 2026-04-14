"""
153
    total digits = 3
    1 + 125 + 27 = 153

7
    total digits = 1
    7 = 7

135
    total digits = 3
    1 + 27 + 125 = 153

Tasks to do:
    find digits - count
    power on each digit -> add all
    compare with original number
"""

num = 743
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
else:
    print(num,"is not armstrong number.")