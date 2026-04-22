# store 5 subjects

import array
# n = int(input("Enter total subjects count: "))
n = 5
marks = array.array("i")

for i in range(n):
    marks.append(int(input(f"Enter subject #{i+1} marks: ")))

print(marks)