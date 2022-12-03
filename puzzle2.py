# Q1 : assuming that X,Y,Z = A,B,C =  ROCK,PAPER,SCISSORS.

wins = {'Y': 'A', 'Z': 'B', 'X': 'C'}
scores = {'X': 1, 'Y': 2, 'Z': 3}
difference = ord('A')-ord('X')


def partA():
    total = 0
    with open("inputFiles/q2Input.txt") as file:
        while True:
            line = file.readline()

            if not line:
                break

            total += scores[line[2]]

            if ord(line[0])-ord(line[2]) == difference:
                total += 3
            elif line[0] == wins[line[2]]:
                total += 6

    return total

# Q2: X = lose, Y = draw, Z = win


points = {'X': 0, 'Y': 3, 'Z': 6}

winningPoints = {'A': 2, 'B': 3, 'C': 1}
losingPoints = {'A': 3, 'B': 1, 'C': 2}
tiePoints = {'A': 1, 'B': 2, 'C': 3}


def partB():
    total = 0
    with open("inputFiles/q2Input.txt") as file:
        while True:
            line = file.readline()
            if not line:
                break
            total += points[line[2]]
            if points[line[2]] == 6:
                total += winningPoints[line[0]]
            elif points[line[2]] == 3:
                total += tiePoints[line[0]]
            else:
                total += losingPoints[line[0]]

        return total


print("Day 2=> Answer to part 1: " + str(partA()))
print("Day 2=> Answer to part 2: " + str(partB()))
