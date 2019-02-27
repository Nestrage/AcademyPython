import random

#25.02.19
while True:
    a = input("Please input the number (1-5)")
    if a in "12345":
        b = random.randint(1,5)
        a = int(a)
        if a == b:
            print("Congratulation!")
        else:
            print("lucky next time")
            print(a,b)
        req = input("Do you want try again? (y - yes? something else - no)")
        if req == "y":
            continue
        else:
            print("See you soon")
            break
    else:
        print("Input error. You need to input the number from 1 to 5")