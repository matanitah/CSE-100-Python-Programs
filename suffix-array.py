"""
Suffix Array
"""

def suffixArr(input):
    suffixes = []
    for i in range(len(input)):
        suffixes.append((input[i :], i))
    suffixes = sorted(suffixes)
    output = []
    for suffix in suffixes:
        output.append(suffix[1])
    print(output)

suffixArr("HUFFMANCODE")
