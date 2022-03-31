class Node:
    def __init__(self, character, frequency):
        self.c0 = None
        self.c1 = None
        self.parent = None
        self.character = character
        self.frequency = frequency

    def __lt__(self, other):
        if (self.frequency != other.frequency):
            return self.frequency < other.frequency
        if (self.character != other.character):
            return self.character < other.character
        return 0

class Tree:
    def __init__(self):
        self.root = None
        self.leaves = []
        self.numNodes = 0

    def display(self):
        bits = []

        for leaf in self.leaves:
            currentNode = leaf
            encoding = ""
            while (currentNode.parent != self.root and currentNode.parent != None):
                nextNode = currentNode.parent
                if (nextNode.c0 == currentNode):
                    encoding += "0"
                elif(nextNode.c1 == currentNode):
                    encoding += "1"
                currentNode = nextNode
            bits.append(encoding[::-1])
            print(leaf.character, encoding)
        print(bits)
        print("Number of Nodes: ", self.numNodes)


    def build(self, freqs):
        pq = []
        for i in range(len(freqs)):
            if (freqs[i] == 0):
                continue
            newNode = Node(chr(i), freqs[i])
            self.leaves.append(newNode)
            self.numNodes += 1
            pq.append((freqs[i], newNode))


        pq.sort(key=lambda x:x[0], reverse=True)
        while(len(pq) > 1):
            lowest = pq.pop()[1]
            secondLowest = pq.pop()[1]
            parentNode = Node(chr(0), lowest.frequency + secondLowest.frequency)
            self.numNodes += 1
            lowest.parent = parentNode
            secondLowest.parent = parentNode
            parentNode.c0 = lowest
            parentNode.c1 = secondLowest
            pq.append((parentNode.frequency, parentNode))
        self.root = pq.pop()

# frequency list input
freqs = [0] * 256

# string input
def genInputString(tuples):
    output = ""
    for tuple in tuples:
        for i in range(tuple[1]):
            output += tuple[0]

    return output

frequencies = [("A", 7),
("C", 1),
("E", 5),
("G", 8),
("R", 6),
("T", 2)]
inputString = genInputString(frequencies)
print("Input String: ", inputString)
for char in inputString:
    freqs[ord(char)]+=1

t = Tree()
t.build(freqs)
t.display()
