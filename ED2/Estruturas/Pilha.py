"""
## Pilhas

Pilha é uma estrutura de dados onde a política de acesso (regras de inserir ou remover dados) obriga que o último
elemento inserido seja o primeiro a ser removido

Pilha: LIFO (Last in first out) (última a entrar, primeiro a sair)

Podemos usar o ctrl+z como um exemplo
"""
# Implementação
from No_Alocação_Encadeada import Node


class Stack:
    def __init__(self):
        self.top = None  # De acordo com os nós, precisamos ter conhecimento do último elemento da Pilha
        self._size = 0  # "_" para entender que não é para usar o atributo diretamente

    def push(self, elem):
        """
        Função para inserir um elemento na pilha
        """
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        """
        Função para remoção do topo da pilha
        """
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size -= 1
            return node.data
        raise IndexError("The stack is empty")


    def peek(self):
        """
        Função para retornar o topo da pilha
        """
        if self._size > 0:
            return self.top.data
        raise IndexError("The stack is empty")

    def __len__(self):  # Método especial: Dando novo "sentido" para função Len já embutida no python
                        # (sobrecarga de operador)
        """Retorna o tamanho da Pilha"""
        return self._size
    # Complexidade: O(1)

    def __repr__(self):
        """
        Método Especial de representação do objeto (print)
        """
        r = ''
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + " "
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


# Testes
pilha1 = Stack()

print(len(pilha1))
pilha1.push(3)
pilha1.push(10)
pilha1.push('Python')
pilha1.push(True)
pilha1.push(1.2)
print(pilha1)
print(len(pilha1))
print(pilha1.peek())
print(pilha1.pop())
print(pilha1)