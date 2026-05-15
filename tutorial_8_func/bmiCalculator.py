# BMI is body mass index

# def getBMI():
#     wkg = 70
#     hm = 1.74

#     bmi = wkg / (hm*hm)

#     print("BMI:",bmi)
#     if (bmi < 18):
#         print("Underweight")
#     elif(bmi < 25):
#         print("Normal")
#     elif(bmi<30):
#         print("Overweight")
#     else:
#         print("Obese")

def getBMI(wkg, hcm):
    # wkg = 70
    hm = hcm/100

    bmi = wkg / (hm*hm)

    # print("BMI:",bmi)
    if (bmi < 18):
        return (bmi, "Underweight")
    elif(bmi < 25):
        return (bmi, "Normal")
    elif(bmi<30):
        return (bmi, "Overweight")
    else:
        return (bmi, "Obese")