try:
    file = open("demo.txt", "r")
    for line in file.readlines():
        print(line,end="")
    file.close()
except FileNotFoundError:
    print("File does not exist")