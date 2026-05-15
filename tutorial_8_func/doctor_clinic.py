from bmiCalculator import getBMI

print("find bmi for ramesh")
rw = 82
rhcm = 179
bmiTuple = getBMI(rw, rhcm)
print(f"Ramesh: BMI #{bmiTuple[0]} and {bmiTuple[1]}")

print("find bmi for dinesh")
bmiTuple= getBMI(65, 172)
print(f"Dinesh: BMI #{bmiTuple[0]} and {bmiTuple[1]}")

