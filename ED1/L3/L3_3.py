def pascal(i, c):
    if c == 0 or c == i:
        return 1
    else:
        return pascal(i - 1, c - 1) + pascal(i - 1, c)


def gerador_pascal_matriz(n):
    triangulo = []

    for linha_index in range(n):
        valor = []
        for coluna_index in range(linha_index + 1):
            valor.append(pascal(linha_index, coluna_index))
        
        triangulo.append(valor)

    return triangulo


def imprime_triangulo(lista):
    for x in lista:
        for y in x:
            print(y, end=' ')
        
        print()

print("Triangulo: ")
imprime_triangulo(gerador_pascal_matriz(4))

print()

print("Matriz: ")
print(gerador_pascal_matriz(4))