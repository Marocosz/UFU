"""
## Arvores

É uma estrutura de dado, muito usada, melhor estrutura para sistema de busca

Raiz: É o primeiro elemento de uma árvore (no topo da árvore)
Folha: São os últimos elementos, quais não tem ligação posterior nenhuma a nenhum outro elemento
(todos são "nós")

Há o conceito de "pai" e "filho" dentro da estrutura
Há o conceito de "ancestral" e "descendente" dentro da estrutura

Caminho: É uma sequência de "Nós" que estão interligados, podemos contar por "Arestas" ou por "Nós"
Altura: É o comprimento do caminho entre a "Raiz" e a "Folha" mais profunda (Lembrando que há subárvores)
Profundidade: A Profundidade de um "Nó" se dá pela distância do caminho desse "Nó" até a "Raíz" da Árvore

## Árvore Binária

Trabalha com que um "pai" tenha no MÁXIMO dois "filhos"
E o conceito de "esquerda" e "direita" é bem usado dentro dessa estrutura

Entendendo

         '+'
        /   \
     'a'     '*'
            /   \
         'b'     '-'
                /   \
              '/'    'e'
             /   \
          'c'     'd'

Temos isso como uma representação de uma árvore, fazendo uma expressão matemática, sendo assim:

Fazendo um percurso em ordem simétrica:
a + (b * ((c / d) - e))
"""
# Implementação


class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self, data=None):
        # Basicamente estamos apenas determinando a raiz da class BinaryTree, e também teremos os métodos de árvore
        if data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Percurso de forma simétrica
    def inorder(self, node=None):
        """
        Função recursiva que ao chegar na raiz, ele pedirá para exibir o filho da esquerda (que também é uma raiz, da
        subárvore) então por isso a recursividade, ao fazer isso com a esquerda, ele irá para a direita, e fará o
        mesmo, caso a raiz da subárvore da direita tenha filho á esquerda, a recursividade irá pega-la
        """
        if node is None:
            # Se o nó for vazio, percorra a partir da raiz
            node = self.root

        if node.left:
            print('(', end='')  # Como precisamos da '(' sempre antes dos elementos 'esquerda', adotamos isso antes
            self.inorder(node.left)
        print(node, end='')

        if node.right:
            self.inorder(node.right)
            print(')', end='')  # Como precisamos da ')' sempre depois dos elementos 'direita', adotamos isso depois

    def postorder(self, node=None):
        """
        Percursão Pós-Ordem em Árvore Binária

        Sistema de Busca:
        Sempre buscar primeiro os filhos da esquerda (primeiramente) e depois da direita, até a raiz

        OBS: Cada nó pode ser olhado como uma raiz, é bom ter essa ideia para trabalharmos com recursão
        """
        if node is None:
            node = self.root

        if node.left:
            self.postorder(node.left)

        if node.right:
            self.postorder(node.right)

        print(node, end=' ')

    def height(self, node=None):
        if node is None:
            node = self.root

        hleft = 0
        hright = 0

        if node.left:
            hleft = self.height(node.left)

        if node.right:
            hright = self.height(node.right)

        if hright > hleft:
            return hright + 1
        else:
            return hleft + 1



if __name__ == "__main__":
    # Dados para implementar o desenho feito (A mão)
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    tree.root = n2

    tree.inorder()
    # Assim, conseguimos salvar uma expressão matemática em uma árvore

    print()
    print(tree.height())