M = []

M.append([])
M.append([])
M.append([])

print(M)

M[0].append(1)  # [[1], [], []]
M[0].remove(1)  # [[], [], []]
M[0].extend([2])  # [[2], [], []]
M[0].pop()  # [[], [], []]
M[0].append([1, 2])  # [[[1, 2]], [], []]
M[0].pop()  # [[], [], []]
M[0].extend([1, 2])  # [[1, 2], [], []]
M[1].extend([10, 11, 12])  # [[1, 2], [10, 11, 12], []]
M[2].extend([20, 11, 22])  # [[1, 2], [10, 11, 12], [20, 11, 22]]
M[2].pop()  # [[1, 2], [10, 11, 12], [20, 11]]
M[2].insert(2, 22)  # [[1, 2], [10, 11, 12], [20, 11, 22]]

print(M)


def breedm2(max):
    Matriz = []
    for i in range(0, max):
        Matriz.append([])
        for j in range(0, max):
            Matriz[i].append(0)
    return Matriz


def printm2(Matriz):
    max = len(Matriz)
    for i in range(0, max+1):
        if i > 0:
            print('i=' + str(i-1) + '\t', end='')
        for j in range(0, max):
            if i > 0:
                print('\t' + str(Matriz[i-1][j]) + '\t', end=' ')
            if i == 0:
                print('\t\tj=' + str(j), end='')
        print('\n\t')


printm2(breedm2(1000))
