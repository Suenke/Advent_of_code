import csv

def get_intcode():
    with open("inputd2.csv", "r") as f:
        input = csv.reader(f)
        intcode = []
        for list in input:
            for row in list:
                intcode.append(int(row))
    return intcode


def calc_intcode():
    for noun in range(0,99):
        for verb in range(0,99):
            intcode = get_intcode()
            intcode[1] = noun
            intcode[2] = verb
            for op in range(0,(len(intcode)-3),4):
                if intcode[op]== 99:
                    if intcode[0] == 19690720:
                        print("noun = " + str(noun) + ", verb = " + str(verb) + ", result = " + str(100 * noun + verb))
                        print(intcode[0])
                        return 0
                else:
                    inplace1 = intcode[op +1]
                    inplace2 = intcode[op +2]
                    outplace = intcode[op +3]
                    if all(place < (len(intcode)-1) for place in [inplace1, inplace2, outplace]):
                        if intcode[op] == 1:
                            intcode[outplace] = intcode[inplace1] + intcode[inplace2]
                        elif intcode[op] == 2:
                            intcode[outplace] = intcode[inplace1] * intcode[inplace2]
                    else:
                        break

calc_intcode()


