import random as rd

lista = rd.sample(range(1000000000), 1000)

listax = lista.copy()

maior = lista[0]

while lista:

    if lista[0] > maior:
        maior = lista[0]

    lista = lista[1:]

print(f'O maior número é: {maior}')
