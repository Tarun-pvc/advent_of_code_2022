# Day 1 of Advent of code!

def A():

    with open("inputFiles/q1Input.txt", "r") as file:
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


def B():
    with open("inputFiles/q1Input.txt", "r") as file:
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


A()
B()
