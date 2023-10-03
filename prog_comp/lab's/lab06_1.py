Matriz = [ [0, 1,2], [10, 11, 12], [20,21, 22]]

for i in Matriz:
    for j in i:
        print(j)

for i in range(0, 3):
    for j in range(0, 3):
        print(Matriz[i][i])

for i in range(0, 3):
    for j in range(0, 3):
        print(Matriz[i][j], end=" ")
    print("\n")

for i in range(0, 3):
    for j in range(0, 3):
        print(Matriz[i][j], end=' ')
    print("\n")

for i in range(0, 4):
    if i < 3:
        print('i='+str(i)+'\t', end="")
    for j in range(0, 3):
        if i < 3:
            print('\t' + str(Matriz[i][j]) + '\t', end=" ")
        if i == 3:
            print('\t\tj=' + str(j), end="")
    print("\n\t")

for i in range(0, 4):
    if i > 0:
        print('i='+str(i-1)+'\t', end="")
    for j in range(0, 3):
        if i > 0:
            print('\t' + str(Matriz[i-1][j]) + '\t', end=" ")
        if i == 0:
            print('\t\tj=' + str(j), end="")
    print('\n\t')

max = 5

for i in range(0, max):
    if i > 0:
        print('i='+str(i-1)+'\t', end='')
    for j in range(0, max-1):
        if i > 0:
            print('\t' + str(i-1) + str(j) + '\t', end=' ')
        if i == 0:
            print('\t\tj=' + str(j), end='')
    print('\n\t')

