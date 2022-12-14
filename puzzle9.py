HPos = (0, 0)
TPos = (0, 0)
SPos = (0, 0)

visited = {}


def check(T, H):
    c0 = T == H
    c1 = (abs(H[1]-T[1]) == 1 and abs(H[0]-T[0]) == 1)
    c2 = (abs(H[1]-T[1]) == 1) and (H[0] == T[0])
    c3 = H[1] == T[1] and abs(H[0]-T[0]) == 1
    return c0 or c1 or c2 or c3


def TPos(T, H):
    # vertical
    if H[1]-T[1] == 2 and H[0] == T[0]:
        T[1] += 1
    elif T[1]-H[1] == 2 and H[0] == T[0]:
        T[1] -= 1
    # horizontal
    elif H[0]-T[0] == 2 and H[1] == T[1]:
        T[0] += 1
    elif T[0]-H[0] == 2 and H[1] == T[1]:
        T[0] -= 1
    # diagonal
    elif H[1]-T[1] == 2 and H[0]-T[0] == 1:
        T[1] += 1
        T[0] += 1
    elif H[1]-T[1] == 2 and T[0]-H[0] == 1:
        T[1] += 1
        T[0] -= 1
    elif H[0]-T[0] == 2 and H[1]-T[1] == 1:
        T[1] += 1
        T[0] += 1
    elif H[0]-T[0] == 2 and T[1]-H[1] == 1:
        T[1] += 1
        T[0] += 1


with open("inputFiles/testing.txt", 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        else:
            dirn = line.strip().split(' ')
