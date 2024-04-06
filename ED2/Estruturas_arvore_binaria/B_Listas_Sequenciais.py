"""
## Listas em Alocação Sequêncial

As listas são estruturas que nos permitem acessar dados de forma aleatória, e sua complexidade seria O(1)
Os elementos dessa lista estão alocados na memória um do lado do outro

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

"""
## Inserçãoe e Remoção em Listas Sequenciais

Para inserir um ítem ao final da lista, por podermos acessar via índice, nessa lista é bem fácil e sua complexidade
seria apenas O(1)

Agora, para inserir um ítem ao meio da lista, teremos que "mexer" com todos os ítens da lista de acordo com a posição
que você queira, no seu pior caso, quando queremos inserir o ítem no primeiro índice da lista, a complexidade será
O(N)

OBS: Quando criamos uma lista sequencial, a memória alocada pra ela é unicamente feita para os elementos da lista, 
sendo assim, não temos um acesso "livre" do endereço de memória que vem antes do primeiro elemento da lista ou depois 
do último, visto que esse endereço de memória pode ser utilizado para qualquer outra coisa dentro do código.
Para inserir, por baixo dos panos, a memoria iria cirar outra lista, copiar os elementos da primeira lista só que agora 
com maior espaço de memória para inserir um elemento.

Para remoção esses comportamentos são similares
"""



