file = open("inputFiles/q1Input.txt", "r")

puzzleList = []

puzzleSum = 0
while True:
    line = file.readline()

    if not line:
        break
    if line != '\n':
        puzzleSum += int(line)
    elif line == '\n':
        puzzleList.append(puzzleSum)
        puzzleSum = 0

puzzleList.sort()

top3 = (puzzleList[-1], puzzleList[-2], puzzleList[-3])
print(sum(top3))

file.close()
