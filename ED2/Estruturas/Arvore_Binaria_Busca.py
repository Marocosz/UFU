"""
Árvores Binárias de Busca

Propriedades:
Olhando para qualquer "nó" de uma árvore binária de busca temos que seu "filho esquerdo" é menor que o "pai" e seu
"filho direito" é maior que o "pai"
"""
# Implementando
from Arvores import Node, BinaryTree
import random


# "BinaryTree" no parãmetro para herdar os métodos dela
class BinarySearchTree(BinaryTree):
    def insert(self, elem):
        parent = None
        x = self.root
        while x:
        # Enquanto "x" ter um valor, definir "parent"="x" e verificar se "elem" é menor ou maior, se for menor,
        # daremos para "x" o valor do "x.left" (filho da esquerda), se for maior, daremos para "x" o valor do
        # "x.right" (filho da direita) e então repetirá o algorítmo até "x" não ter valor, assim, a variável
        # "parent", terá o valor do último filho (com um ramo livre) de acordo com o caminho de ABB do elemento dado
            parent = x
            if elem < x.data:
                x = x.left
            else:
                x = x.right

        if not parent:
            # Se não existir nenhum elemento na árvore
            self.root = Node(elem)
        elif elem < parent.data:
            # a partir da folha já selecionada no while acima, criamos um filho a ela, para esquerda ou direita,
            # dependendo do valor do "elem"
            parent.left = Node(elem)
        else:
            parent.right = Node(elem)

    def search(self, elem, node=0):
        if node == 0:
            # Se não passarmos o "nó" começar da raiz da árvore
            node = self.root

        if node is None:
            return node

        if node.data == elem:
            return BinarySearchTree(node)

        if elem < node.data:
            return self.search(elem, node.left)

        return self.search(elem, node.right)


if __name__ == "__main__":
    values = [12, 34, 67, 23, 78, 92, 67, 21, 23, 1000, 1, 35, 90]
    bst = BinarySearchTree()

    for v in values:
        bst.insert(v)

    items = [1, 3, 981, 500, 1000]
    for item in items:
        r = bst.search(item)
        if r is None:
            print(f'{item} não encontrado')
        else:
            print(f'{r.root.data} encontrado')