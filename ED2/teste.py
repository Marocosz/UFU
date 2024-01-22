from random import randint
import time


def particiona(V, inicio, final):
    esq = inicio
    dir = final
    pivo = V[inicio]
    while esq < dir:
        while esq <= final and V[esq] <= pivo:
            esq = esq + 1

        while dir >= 0 and V[dir] > pivo:
            dir = dir - 1

        if esq < dir:
            aux = V[esq]
            V[esq] = V[dir]
            V[dir] = aux

    V[inicio] = V[dir]
    V[dir] = pivo
    return dir


def quickSort(V, inicio, fim):
    if fim > inicio:
        pivo = particiona(V, inicio, fim)  # particiona a lista em menores que o pivô e maiores
        quickSort(V, inicio, pivo-1)       # recomeça a ordenação para os menores
        quickSort(V, pivo+1, fim)          # recomeça a ordenação para os maiores



# Geradores de Listas --------------------------------------------------------------------------------------------------


def gerarListaValoresAleatorios(quantidade):
   resposta = []
   for i in range(quantidade):
       resposta.append(randint(0,1000))  # valor aleatório entre 0 e 1000
   return resposta


def gerarListaOrdenada(quantidade):
   resposta = []
   inicio = randint(0,1000)
   for i in range(quantidade):
       resposta.append(inicio)
       inicio = inicio + 3
   return resposta


def gerarListaInvertida(quantidade):
   resposta = []
   inicio = randint(0,1000)
   for i in range(quantidade):
       resposta.append(inicio)
       inicio = inicio - 3
   return resposta


def gerarListaPoucasChaves(quantidade, max_chaves):  #max_chaves representa o número de valores distintos
   resposta = []
   for i in range(quantidade):
       resposta.append(randint(1,max_chaves))
   return resposta


"""
listaaleatoria = gerarListaValoresAleatorios(10)
listaordenada = gerarListaOrdenada(10)
print(listaaleatoria)
print(listaordenada)

quickSort(listaaleatoria, 0, 9)
quickSort(listaordenada, 0, 9)
print(listaaleatoria)
print(listaordenada)
"""


# ---------------------------------------------------------------------------------------------------------------------


def ordenaQuickSortDiferentesListas(max):

    l1 = gerarListaValoresAleatorios(max)
    l2 = gerarListaOrdenada(max)
    l3 = gerarListaInvertida(max)
    l4 = gerarListaPoucasChaves(max,8)

    ini1 = time.time()
    quickSort(l1,0,max-1)
    fim1 = time.time()
    taleatorio = fim1-ini1

    ini2 = time.time()
    quickSort(l2,0,max-1)
    fim2 = time.time()
    tordenado = fim2-ini2

    ini3 = time.time()
    quickSort(l3,0,max-1)
    fim3 = time.time()
    tinvertido = fim3-ini3

    ini4 = time.time()
    quickSort(l4,0,max-1)
    fim4 = time.time()
    tpoucaschaves = fim4-ini4

    listatempos = [taleatorio, tordenado, tinvertido, tpoucaschaves]

    print(listatempos)

# ---------------------------------------------------------------------------------------------------------------------


# Listas de tamanhos diferentes
for x in range(10):
    i = randint(0, 1000)
    print(i)
    ordenaQuickSortDiferentesListas(i)
