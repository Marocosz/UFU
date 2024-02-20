"""
## Listas Encadeadas

A ideia de uma Lista Encadeada é que os elementos dela estejam alocados em espaços quaisquer da memória, e só serão
alocados quando precisar de um novo elemento

E para conseguirmos acessar esses elementos, por não estarem um do lado do outro, precisamos criar uma estrutura chamada
"Nó"

## Nó

O Nó é como um envelope que tem um espaço para o dado e um espaço com o endereço de outro nó, e sabemos que é o último
elemento da lista visto que não há o endereço do próximo

Mas é importante salientar que não há o endereço do nó anterior.
"""


# Classe "Node" que representa o conceito de "Nó"
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""
## Construindo uma Lista Encadeada
"""


class LinkedList:
    def __init__(self):
        self.head = None  # De acordo com os nós, precisamos ter conhecimento do primeiro elemento da lista
        self._size = 0  # "_" para entender que não é para usar o atributo diretamente

    def append(self, elem):
        """
        Função que irá percorrer toda lista até chegar no último elemento e então adicionar um novo, caso não exista
        elemento algum, adicionará no ".head"
        """
        if self.head:
            pointer = self.head  # Variável auxiliar com o endereço do "head"
            # OBS: Sempre usamos uma variável auxiliar para andar pela lista para não perdermos o valor do primeiro ítem
            while pointer.next:  # Código para ir passando elemento por elemento, para chegarmos ao final da lista
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            self.head = Node(elem)

        self._size += 1
    # Complexidade: O(N)

    def __len__(self):  # Método especial: Dando novo "sentido" para função Len já embutida no python
                        # (sobrecarga de operador)
        """Retorna o tamanho da lista"""
        return self._size
    # Complexidade: O(1)

    def _getnode(self, index):
        """
        Função para pegar o valor que está no index escolhido
        """
        """
        De acordo com o "index", o código irá andando na lista usando o "pointer", e então retornará o node desejado
        """
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError(f'List index out of range')
        return pointer

    def get(self, index):
        pass

    def set(self, index, elem):
        pass

    def __getitem__(self, index):
        # Será uma função da class LinkedList como se fosse uma lista embutida do python
        pointer = self._getnode(index)  # Pegando o "node" do index desejado

        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")
    # Complexidade: O(N)

    def __setitem__(self, index, elem):
        # Será uma função da class LinkedList como se fosse uma lista embutida do python
        pointer = self._getnode(index)  # Pegando o "node" do index desejado

        if pointer:
            pointer.data = elem
        else:
            raise IndexError("List index out of range")
    # Complexidade: O(N)

    def index(self, elem):
        """
        Função para buscar determinado valor "elem" na lista e retornar seu index
        """
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elem:
                return i
            else:
                pointer = pointer.next
                i += 1
        raise ValueError(f"{elem} is not in list")
    # Complexidade: O(N)

    def insert(self, index, elem):
        """
        Função para inserção de elementos em um index específico
        """
        node = Node(elem)
        if index == 0:
            # Quando o usuário querer que seja o primeiro ítem da lista
            node.next = self.head
            self.head = node
        else:
            pointer = self._getnode(index-1)  # Pegando o "node" do index desejado
            """
            OBS: Não podemos perder o endereço do nó posterior ao index escolhido, pois assim perderemos todo restante
            da lista, dessa forma, fazemos:
            """
            node.next = pointer.next  # Salvando o endereço do nó posterior para então depois fazer a substituição
            pointer.next = node
        self._size += 1  # Aumentando o tamanho da lista (visto que adicionamos um ítem)
    # Complexidade: 0(N)

    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elem:
                      # removendo
                    ancestor.next = pointer.next
                    pointer.next = None
                ancestor = pointer
                pointer = pointer.next
            self._size -= 1
            return True
        raise ValueError(f"{elem} is not in list")
    # Complexidade: O(N)

    def __repr__(self):
        """
        Método Especial de representação do objeto (print)
        """
        r = ''
        pointer = self.head
        while pointer:
            r = r + str(pointer.data) + '->'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


# Testes
if __name__ == '__main__':
    lista = LinkedList()

    lista.append(2)
    lista.append(6)

    print(len(lista))
    print(lista[0])

    print(lista.index(2))

    lista.insert(1, 32)

    print(lista[1])
    print(lista[2])

    lista.remove(6)

    print(lista)

    lista2 = LinkedList()

    lista2.append(8)
    lista2.append(10)
    lista2.append(23)
    lista2.append(1)
    lista2.append(3)

    print(lista2)

    lista2.remove(10)

    print(lista2)

