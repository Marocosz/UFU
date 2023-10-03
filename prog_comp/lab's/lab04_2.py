lista = [1, 2, 3, 5, 10, 2, 3]

listax = lista

maior = lista[0]  # = 1

while lista:

    if lista[0] > maior:
        maior = lista[0]

    lista = lista[1:]

print(f'Da lista {listax}, o maior número é: {maior}')
