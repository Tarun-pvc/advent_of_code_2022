
stack1 = ['H', 'R', 'B', "D", 'Z', 'F', 'L', 'S']
stack2 = ['T', 'B', 'M', 'Z', 'R']
stack3 = ['Z', 'L', 'C', 'H', 'N', 'S']
stack4 = ['S', 'C', 'F', 'J']
stack5 = ['P', 'G', 'H', 'W', 'R', 'Z', 'B']
stack6 = ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T']
stack7 = ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q']
stack8 = ['R', 'Z', 'M']
stack9 = ['M', 'C', 'L', 'G', 'V', 'R', 'T']

stacks = [stack1, stack2, stack3, stack4,
          stack5, stack6, stack7, stack8, stack9]


def partA():
    with open("inputFiles/q5Input.txt") as file:
        while True:
            line = file.readline()
            if not line:
                break
            strings = line.split(' ')
            iterations = int(strings[1])
            source = int(strings[3])
            destination = int(strings[5])

            for i in range(iterations):
                stacks[destination-1].append(stacks[source-1].pop())

    stringout = ""
    for stack in stacks:
        stringout += stack[-1]

    print(stringout)


def partB():
    with open("inputFiles/q5Input.txt") as file:
        while True:
            line = file.readline()
            if not line:
                break
            strings = line.split(' ')
            iterations = int(strings[1])
            source = int(strings[3])
            destination = int(strings[5])
            tomove = []

            for i in range(iterations):
                tomove.append(stacks[source-1].pop())

            for i in range(iterations):
                stacks[destination-1].append(tomove.pop())

    stringout = ""
    for stack in stacks:
        stringout += stack[-1]

    print(stringout)
