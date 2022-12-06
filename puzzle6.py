inputString = ""

with open("inputFiles/q6Input.txt") as file:
    inputString = file.readline()

inputLength = len(inputString)


def repeatCheck(inString):
    for i in range(len(inString)):
        for j in range(i+1, len(inString)):
            if inString[i] == inString[j]:
                return 1
    return 0


# part A
def partA():
    for i in range(4, inputLength):
        if repeatCheck(inputString[i-4:i]) == 0:
            return i


def partB():
    for i in range(14, inputLength):
        if repeatCheck(inputString[i-14:i]) == 0:
            return i


print("Day 6 => The answer to part A is: " + partA())
print("Day 6 => The answer to part B is: " + partB())
