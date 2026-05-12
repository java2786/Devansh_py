import re

email = "arun.kumar.123@gmail.in"
reg = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

if re.match(reg, email):
    print("Valid email")
else:
    print("Invalid email")