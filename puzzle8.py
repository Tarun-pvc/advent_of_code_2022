treeGrid = []
gridSize = 0


def convertIntoList(instring: str):
    retList = []
    for char in instring:
        retList.append(char)
    return retList


with open("inputFiles/q8Input.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        else:
            treeGrid.append(convertIntoList(line.strip()))
gridSize = len(treeGrid)

# part one:


def checkRow(row, column):
    value = treeGrid[row][column]
    left = 0
    right = 0
    for i in range(gridSize):
        if i < column and treeGrid[row][i] >= value:
            left += 1
        elif i > column and treeGrid[row][i] >= value:
            right += 1
    if left >= 1 and right >= 1:
        return False
    else:
        return True


def checkColumn(row, column):
    value = treeGrid[row][column]
    left = 0
    right = 0
    for i in range(gridSize):
        if i < row and treeGrid[i][column] >= value:
            left += 1
        elif i > row and treeGrid[i][column] >= value:
            right += 1
    if left >= 1 and right >= 1:
        return False
    else:
        return True


total = 0
for i in range(1, gridSize-1):
    for j in range(1, gridSize-1):
        if checkRow(i, j) or checkColumn(i, j):
            total += 1

total += gridSize*2 + (gridSize-2)*2

# print(gridSize)
# print(total)

# End of part one

# part two:


def leftTrees(row, column):
    value = treeGrid[row][column]
    left = 0
    for i in range(column):
        if treeGrid[row][column-i-1] < value:
            left += 1
        else:
            left += 1
            break
    return left


def rightTrees(row, column):
    value = treeGrid[row][column]
    right = 0
    for i in range(column+1, gridSize):
        if treeGrid[row][i] < value:
            right += 1
        else:
            right += 1
            break
    return right


def topTrees(row, column):
    value = treeGrid[row][column]
    top = 0
    for i in range(row):
        if treeGrid[row - i - 1][column] < value:
            top += 1
        else:
            top += 1
            break
    return top


def bottomTrees(row, column):
    value = treeGrid[row][column]
    bottom = 0
    for i in range(row+1, gridSize):
        if treeGrid[i][column] < value:
            bottom += 1
        else:
            bottom += 1
            break
    return bottom


def scenicScore(row, column):
    top = topTrees(row, column)
    bottom = bottomTrees(row, column)
    left = leftTrees(row, column)
    right = rightTrees(row, column)
    return top*bottom*left*right


max = 0
for i in range(gridSize):
    for j in range(gridSize):
        if scenicScore(i, j) > max:
            max = scenicScore(i, j)

print(max)
