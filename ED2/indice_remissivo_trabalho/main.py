arq = open('cosmos_de_carl_sagan.txt', mode='r', encoding='utf-8')

line = arq.readline()

while line != '':
    for i in line:
        if i == "O":
            print(i)
    line = arq.readline()