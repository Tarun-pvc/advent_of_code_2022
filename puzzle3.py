def value(character):
    if ord(character) >= ord('A') and ord(character) <= ord('Z'):
        return ord(character)-(ord('A')-27)
    if ord(character) >= ord('a') and ord(character) <= ord('z'):
        return ord(character)-(ord('a')-1)


def A():
    total = 0
    with open("inputFiles/q3Input.txt") as file:
        while True:
            line = file.readline()
            if not line:
                break
            lentest = (len(line)//2)
            halves = [line[:lentest], line[lentest:]]

            flag = 1
            for char in halves[0]:
                if flag == 0:
                    break
                if char in halves[1]:
                    total += value(char)
                    flag = 0

    return (total)


def B():
    total = 0
    with open("inputFiles/q3Input.txt") as file:
        inputs = file.readlines()
        length = len(inputs)
        i = 0
        while i < length:
            flag = 0
            for char in inputs[i]:
                if flag == 1:
                    break
                if char in inputs[i+1]:
                    if char in inputs[i+2]:
                        total += value(char)
                        flag = 1

            i += 3
    return (total)


print("The answer to the first part is: " + str(A()))
print("The answer to the second part is: " + str(B()))
