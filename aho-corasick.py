class Node:
  def __init__(self):
    self.children = {}
    self.suffix = ""
    self.endOfString = False
    self.failureLink = None
    self.dictionaryLink = None

class AhoCorasickAutomaton:
    def __init__(self):
      self.root = Node()

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return self.root
            currentNode = node

        if currentNode.endOfString == True:
            return currentNode
        else:
            return self.root

    def insertString(self, word):
        current = self.root
        for i in range(len(word)):
            ch = word[i]
            node = current.children.get(ch)
            if node == None:
                node = Node()
                current.children.update({ch:node})
            node.suffix = word[i:]
            current = node
        current.endOfString = True

    def deleteString(root, word, index):
        ch = word[index]
        currentNode = root.children.get(ch)
        canNodeBeDeleted = False

        if len(currentNode.children) > 1:
            deleteString(currentNode, word, index+1)
            return False

            if index == len(word) - 1:
                if len(currentNode.children) >= 1:
                    currentNode.endOfString = False
                    return False
                else:
                    root.children.pop(ch)
                    return True

                    if currentNode.endOfString == True:
                        deleteString(currentNode, word, index+1)
                        return False

                        canNodeBeDeleted = deleteString(currentNode, word, index+1)
                        if canNodeBeDeleted == True:
                            root.children.pop(ch)
                            return True
                        else:
                            return False

def traverse(root):
    if (root == None):
        return []
    nodes = [root]
    for child in root.children.values():
        nodes.extend(traverse(child))

        # childNodes = traverse(child)
        # for node in childNodes:
        #     nodes.append(node)
    return nodes

# def traverse(root):
#     answer = []
#     traverseUtil(root, answer)
#     return answer
#
# def traverseUtil(root, answer):
#     if (root == None):
#         return
#     for child in root.children:
#         answer.append(traverseUtil(child, answer))
#     answer.append(root)
#     return


def ahoCorasick(database):
    trie = AhoCorasickAutomaton()

    for entry in database:
        trie.insertString(entry)
        nodeList = traverse(trie.root)
    nodeList = traverse(trie.root)

    # failure link logic
        # for each node in the trie
        # get a list of all its proper suffixes
        # make the failure link of the node the longest suffix in the trie

    for node in nodeList:
        suffixes = []
        for i in range(len(node.suffix)):
            suffixes.append(node.suffix[i:])
        print(suffixes)
        longestSuffix = ""
        max = 0
        for suffix in suffixes:
            if(trie.searchString(suffix) != False):
                if(len(suffix) > max):
                    max = len(suffix)
                    longestSuffix = suffix
        node.failureLink = trie.searchString(longestSuffix)

    for node in nodeList:
        current = node
        while(current != trie.root and not current.failureLink.endOfString):
            current = current.failureLink
        if(current.failureLink.endOfString):
            node.dictionaryLink = current.failureLink

        # traverse failure links until reach word node or root

        # if end up at root, no dictionary link

        # else, dictionary link of original equals first word node found

    print("Number of Nodes: ", len(nodeList))

    numFailureLinks = 0
    numDictionaryLinks = 0
    for node in nodeList:
        if (node.failureLink):
            numFailureLinks += 1
        if (node.dictionaryLink):
            numDictionaryLinks += 1

    print("Number of Failure Links: ", numFailureLinks)
    print("Number of Dictionary Links: ", numDictionaryLinks)

    for node in nodeList:
        print("IsWordNode: ", node.endOfString)
        print("Suffix: ", node.suffix)
        print("Failure Link: ", node.failureLink)
        print("Dictionary Link: ", node.dictionaryLink)
    # output: list of nodes, number of nodes
    #         failure links, number of failure links
    #         dictionary links, number of dictionary links

ahoCorasick(["MovieTheatre","Movie","Pop","Popcorn","Move","SodaPop","Mover"])
