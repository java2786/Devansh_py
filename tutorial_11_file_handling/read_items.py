file = open("demo.txt", "r")
# file.write("\nThis is a demo code")
for line in file.readlines():
    print(line, end="")
file.close()

