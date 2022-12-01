file = open("inputFiles/q1Input.txt", "r")

puzzleSum = 0
puzzleMax = 0
while True:
    line = file.readline()

    if not line:
        break
    if line != '\n':
        puzzleSum += int(line)
    elif line == '\n':
        if puzzleSum > puzzleMax:
            puzzleMax = puzzleSum
        puzzleSum = 0

print(puzzleMax)

file.close()
