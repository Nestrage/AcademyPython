resultList = []
while True:
    carname = input("Please input a  name of a car, or q to print the result")
    if carname == "q":
        break
    else:
        resultList.append(carname)

print(resultList)