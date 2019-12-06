import csv

def get_intcode():
    with open("inputd2.csv", "r") as f:
        input = csv.reader(f)
        intcode = []
        for list in input:
            for row in list:
                intcode.append(int(row))
    return intcode


def calc_intcode(intcode):
    intcode[1] = 12
    intcode[2] = 2
    for op in range(0,len(intcode),4):
        if intcode[op]== 99:
            break
        else:
            inplace1 = intcode[op +1]
            inplace2 = intcode[op +2]
            outplace = intcode[op +3]
            if intcode[op] == 1:
                intcode[outplace] = intcode[inplace1] + intcode[inplace2]
            elif intcode[op] == 2:
                intcode[outplace] = intcode[inplace1] * intcode[inplace2]

    print(intcode[0])

intcode = get_intcode()
calc_intcode(intcode)


