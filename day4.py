

def truestart(intstart):
    start = [i for i in str(intstart)]
    for z in range(1,6):
        if start[z] < start[z-1]:
            start[z] = start[z-1]
    startstr = ''.join(start)
    return startstr

def trueend(intend):
    end = [i for i in str(intend)]
    for z in range(1,6):
        if end[z] < end[z-1]:
            end[z-1] = str(int(end[z-1])-1)
            for j in range (z, 6):
                end[j] = '9'
            endstr = ''.join(end)
            return endstr
    else:
        endstr = ''.join(end)
        return endstr

def adjpair(input):
    for i in range(1,6):
        if input[i] == input[i-1]:
            return True

def increase(candi):
    for num in range (1,6):
        if candi[num] < candi[num-1]:
            return False
    else:
        return True

def cand_iter(anfang, ende):
    worknum = int(anfang)
    for worknum in range(int(anfang), int(ende)+1):
        if increase(str(worknum)) is True and adjpair(str(worknum)) is True:
            yield worknum


def getpw(start, end): #schon listen bzw strings
    candid = [num for num in cand_iter(start, end)]
    return len(candid)

def main(in1, in2):
    start = truestart(in1)
    end = trueend(in2)
    print(start)
    print(end)
    print(getpw(start, end))

if __name__ == '__main__': main(264360, 746325)