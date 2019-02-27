#a = input("Inpute the telephone number")
a ="123144f543"
if a.isdigit() and len(a) == 10:
    print("Phone number is correct")
else:
#     if not a.isdigit():
#         print("Number must cntain only digits")
#     if not len(a) == 10:
#         print("Number must have only 10 symbols")
    if not a.isdigit():
        for element in a:
            if not element.isdigit():
               print(f" Element {element} is invalid")

    if not len(a) == 10:
        print("Number must have only 10 symbols")