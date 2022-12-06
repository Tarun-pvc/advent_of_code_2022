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
for i in range(4, inputLength):
    if repeatCheck(inputString[i-4:i]) == 0:
        print(i)
        break

# part B
for i in range(14, inputLength):
    if repeatCheck(inputString[i-14:i]) == 0:
        print(i)
        break
