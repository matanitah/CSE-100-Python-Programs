"""
Burrows Wheeler Transform
"""
def leftrotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

def bwt(input):
    input += "$"
    output = ""
    rotations = []
    for i in range(len(input)):
        rotation = leftrotate(input, i)
        rotations.append(rotation)
    rotations = sorted(rotations)
    for r in rotations:
        output += r[len(r)-1]
    print(output)

def invbwt(input):
    sortedBST = sorted(input)
    last = []
    first = []
    countLast = {}
    countFirst = {}
    for i in range(len(sortedBST)):
        if(input[i] not in countLast.keys()):
            countLast.update({input[i]: 1})
        else:
            countLast.update({input[i]: countLast[input[i]] + 1})
        if(sortedBST[i] not in countFirst.keys()):
            countFirst.update({sortedBST[i]: 1})
        else:
            countFirst.update({sortedBST[i]: countFirst[sortedBST[i]] + 1})
        last.append((input[i], countLast[input[i]]))
        first.append((sortedBST[i], countFirst[sortedBST[i]]))

    firstToLast = []
    for elt in last:
        firstToLast.append(first.index(elt))
    print("First To Last: ", firstToLast)

    output = ""
    elt = ("$", 1)
    for i in range(len(last)):
        index = last.index(elt)
        output += first[index][0]
        elt = first[index]
    print(output)
bwt("CPLUSPLUS")
invbwt("S$PPSCUULL")
