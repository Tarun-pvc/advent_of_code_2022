import re


def partA():
    total = 0
    with open("inputFiles/q4Input.txt") as file:
        while True:
            line = file.readline()
            if not line:
                break
            pairs = re.split(',|-', line)
            for i in range(len(pairs)):
                pairs[i] = int(pairs[i])
            if pairs[3] <= pairs[1] and pairs[2] >= pairs[0]:
                total += 1
            elif pairs[3] >= pairs[1] and pairs[2] <= pairs[0]:
                total += 1

    return (total)


def partB():
    total = 0
    with open("inputFiles/q4Input.txt") as file:
        while True:
            line = file.readline()
            if not line:
                break
            pairs = re.split(',|-', line)
            for i in range(len(pairs)):
                pairs[i] = int(pairs[i])
            if pairs[3] <= pairs[1] and pairs[2] >= pairs[0]:
                total += 1
            elif pairs[3] >= pairs[1] and pairs[2] <= pairs[0]:
                total += 1
            elif pairs[1] >= pairs[2] and pairs[0] <= pairs[2]:
                total += 1
            elif pairs[3] >= pairs[0] and pairs[3] <= pairs[1]:
                total += 1

    return (total)


print("Day 4 => The answer to the first part is: " + str(partA()))
print("Day 4 => The answer to the second part is: " + str(partB()))
