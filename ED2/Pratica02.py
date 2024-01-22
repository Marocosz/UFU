# Função para gerar uma lista com valores aleatórios a partir de uma quantidade desejada

from random import randint
import time
import matplotlib.pyplot as plt
import copy


# Ordenação por Bolha --------------------------------------------------------------------------------------------------


def gerarListaValoresAleatorios(quantidade):
    resposta = []
    for i in range(quantidade):
        resposta.append(randint(0, 1000))  # valor aleatório entre 0 e 1000
    return resposta

# """
# Função para trocar dois elementos de posição numa lista (i e j são as posições para troca)
def troca(lista, i, j):
    temp = lista[i]
    lista[i] = lista[j]
    lista[j] = temp


# Função de ordenação por Bolha
def bubbleSortOtimizado(lista):
    N = len(lista)
    for nropassagem in range(N - 1, 0, -1):  # o número de passagens começa de N-1 (para reduzir o tamanho da varredura), sendo N o tamanho da lista
        trocou = False  # no início da varredura não há troca
        for i in range(nropassagem):
            if lista[i] > lista[i + 1]:
                troca(lista, i, i + 1)
                trocou = True
        if trocou == False:
            break  # ao final da varredura, se nenhuma troca foi feita, deve-se encerrar a ordenação (tudo pronto!)


def bubbleSortNormal(lista):
    N = len(lista)
    for nropassagem in range(N - 1, 0, -1):  # o número de passagens começa de N-1 (para reduzir o tamanho da varredura), sendo N o tamanho da lista
        for i in range(nropassagem):
            if lista[i] > lista[i + 1]:
                troca(lista, i, i + 1)
                trocou = True


# Função principal: cria uma lista com valores aleatórios, ordenam-se os valores e retorna-se o tempo gasto na ordenação.
def ordenaBolha(quant):
    lista = gerarListaValoresAleatorios(quant)
    listacopy = copy.deepcopy(lista)
    listacopy2 = copy.deepcopy(lista)
    print(f"Lista Aleatória: {listacopy}")
    inicio1 = time.time()
    bubbleSortOtimizado(listacopy)
    fim1 = time.time()
    tempo1 = fim1 - inicio1
    print(f"Resultado por Bolha: {listacopy}")

    print(f"Lista Aleatória: {listacopy2}")
    inicio2 = time.time()
    bubbleSortNormal(listacopy2)
    fim2 = time.time()
    tempo2 = fim2 - inicio2
    print(f"Resultado por Bolha: {listacopy}")
    return tempo1, tempo2


quantidades = [1000, 2000, 3000, 4000, 5000]
tempos = []

for i in quantidades:
    tempo = ordenaBolha(i)
    tempos.append(tempo)



print(tempos)

plt.plot(quantidades, tempos)  # quantidades e tempos foram obtidos na execução anterior
plt.title("Crescimento do Tempo - Bolha")
plt.show()

# plt.plot(quantidades, tempos, color='blue', marker='o', markersize=8, linestyle='--', linewidth=2)
# plt.title("Crescimento do Tempo - Bolha")
# plt.show()
# """


"""
# Ordenação por Seleção ------------------------------------------------------------------------------------------------


def selectionSort(V):
    N = len(V)
    for i in range(N-1):
        menor = i
        for j in range(i+1, N):
            if V[j] < V[menor]:
                menor = j

        if i != menor:
            troca = V[i]
            V[i] = V[menor]
            V[menor] = troca
    tempof = time.time()


def ordenaSelect(quant):
    lista = gerarListaValoresAleatorios(quant)
    tempoi = time.time()
    selectionSort(lista)
    tempof = time.time()
    dif = tempof - tempoi
    return dif


quantidades = [100, 500, 1000, 1500, 2000]
tempos = []

for i in quantidades:
    tempo = ordenaSelect(i)
    tempos.append(tempo)

print(tempos)

class Selection():

    def __init__(self, listaValores):
        self.selectionSort(listaValores)
        print(listaValores)

    def selectionSort(self, V):
        N = len(V)
        for i in range(N-1):
            menor = i
            for j in range(i+1,N):
                if V[j] < V[menor]:
                    menor = j

            if i != menor:
                troca = V[i]
                V[i] = V[menor]
                V[menor] = troca
"""
