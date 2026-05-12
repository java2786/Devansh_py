email = "arun123@gmail.com"

# must contain '@'
# '@' must not be first
# last chars must be @gmail.com 

if '@' not in email:
    print("Invalid: does not contain '@'")
if email.count('@')>1:
    print("Invalid: Multiple '@' not valid")
elif '.' not in email:
    print("Invalid: does not contain '.'")
elif email[0]=='@':
    print("Invalid: @ could not be first char")
elif not email.endswith('@gmail.com'):
    print("Invalid: ending is not correct")
else:
    print("valid")