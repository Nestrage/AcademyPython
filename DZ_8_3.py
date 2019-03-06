import string
from typing import List


def make_operation(oper: string, arguments: List[int]):
    if oper is "+":
        for teh_i in range(1,len(arguments)):
            arguments[0]+= arguments[teh_i]
        print(arguments[0])
    if oper is "-":
        for teh_i in range(1, len(arguments)):
            arguments[0] -= arguments[teh_i]
        print(arguments[0])
    if oper is "*":
        for teh_i in range(1,len(arguments)):
            arguments[0]*= arguments[teh_i]
        print(arguments[0])
    return

make_operation("+", [7,7,2])
make_operation("-", [5,5,-10,-20])
make_operation("*", [7,6])