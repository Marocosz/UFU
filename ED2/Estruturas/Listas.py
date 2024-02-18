"""
## Listas em Alocação Sequêncial

As listas são estruturas que nos permitem acessar dados de forma aleatória, e sua complexidade seria O(1)

Normalmente, dados do mesmo tipos, lista de inteiros, lista de strings, etc...
Sendo assim, por exemplo, se cada dado dessa lista ter um tamanho de 4 bytes, conseguimos acessa-los usando essa info,
por exemplo, [dado1, dado2, dado3]: 4 bytes, 8 bytes, 12 bytes

Em python, como podemos ter vários tipos de dados, ele usa "ponteiros", ponteiros cujo tem a informação do endereço
do dado (Funciona como um intermediário)

"""


# Analisando a lista estranha sequencialmente
def busca(lista, elem):
    """ Retorna o índice do elemento caso ele esteja na lista, caso contrário, retorna None"""
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

    return None


lista_estranha = [8, "5", 32, 0, "Python", True]
elemento = 2

indice = busca(lista_estranha, elemento)
if indice is not None:
    print(f"O índice do elemento {elemento}, é {indice}")
else:
    print(f"O elemento {elemento} não está na lista")

"""
Nesse caso, temos que a complexidade de tempo do algorítmo é: 2N + 1 -> O(N)
Sendo as opreações elementares o For e o If que multiplica o N (lista), sendo "+1" o return
"""




