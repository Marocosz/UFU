"""
## Fila

Funciona como uma fila mesmo, quero remover do começo, e inserir no final
"""
from No_Alocação_Encadeada import Node


class Queue:
    def __init__(self):
        # Temos que ter o endereço do ínicio e final da fila, visto seu comportamento
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elem):
        """
        Função para inserir um elemento no final da fila
        """
        node = Node(elem)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node

        self._size += 1

    def pop(self):
        """
        Função para remoção do ínicio da fila
        """
        if self._size > 0:
            elem = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elem

        raise IndexError('The Queue is empty')

    def peek(self):
        """
        Função para retornar o início da fila
        """
        if self._size > 0:
            elem = self.first.data
            return elem

        raise IndexError('The Queue is empty')

    def __len__(self):  # Método especial: Dando novo "sentido" para função Len já embutida no python
                        # (sobrecarga de operador)
        """Retorna o tamanho da Pilha"""
        return self._size

    def __repr__(self):
        """
        Método Especial de representação do objeto (print)
        """
        if self._size > 0:
            r = ""
            pointer = self.first
            while pointer:
                r = r + str(pointer.data) + " "
                pointer = pointer.next
            return r
        return "Empty Queue"

    def __str__(self):
        return self.__repr__()


fila = Queue()

print(fila)

fila.push(9)
fila.push('Aaa')
fila.push(2.3)
print(fila)
fila.pop()
print(fila)