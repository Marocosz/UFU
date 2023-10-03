"""
import random as rd

qt = int(input('Digite a quantidade de números pseudo-aleatórios deseja ordenar: '))
max = int(input('Digite o máximo de número de 0 a: '))

lista_num = rd.sample(range(max), qt)

lista_nova = []

aux = False


def func_tamanho(lista):
    tam_nova = 0
    for x in lista:
        tam_nova += 1

    return tam_nova


for x in range(qt):

    tamanho = func_tamanho(lista_nova)

    n = lista_num[x]

    if tamanho > 0:

        for y in range(tamanho):

            if n <= lista_nova[y]:
                lista_nova.insert(y, n)

                aux = True

                break

    if x == 0 or not aux:

        lista_nova.append(n)

    else:

        aux = False

print(f'Dos números: {lista_num}, ordenado são: {lista_nova}')
"""

import random as rd

A = int(input('Quantos números deseja ordenar?'))
B = int(input('Os números digitados estarão entre 0 e:'))

lista = rd.sample(range(B), A)

lista_save = lista.copy()


def func_tamanho(lista):
    tam_nova = 0
    for x in lista:
        tam_nova += 1

    return tam_nova


temp = 0

for i in range(0, func_tamanho(lista)):
    for j in range(i+1, func_tamanho(lista)):
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp

print(f'Dos números: {lista_save}, ordenado são: {lista}')
