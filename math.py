#25/02/19
while True:
    a = input("(3*3+3)+3+3*3 = ")
    if a[0] != "-" and not a.isnumeric():
        print("Input the numbers, please")
        continue
    a = int(a)
    if a != (3*3+3)+3+3*3:
        print("Incorrect, try again")
    else:
        print("Correct")
        break
