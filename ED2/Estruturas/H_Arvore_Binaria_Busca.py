"""
Árvores Binárias de Busca

Propriedades:
Olhando para qualquer "nó" de uma árvore binária de busca temos que seu "filho esquerdo" é menor que o "pai" e seu
"filho direito" é maior que o "pai"
"""
# Implementando
from F_Arvores import Node, BinaryTree
import random

ROOT = "ROOT"


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

    def search(self, elem, node=ROOT):
        if node == ROOT:
            # Se não passarmos o "nó" começar da raiz da árvore
            node = self.root

        if node is None:
            return node

        if node.data == elem:
            return BinarySearchTree(node)

        if elem < node.data:
            return self.search(elem, node.left)

        return self.search(elem, node.right)

    def min(self, node=ROOT):
        if node == ROOT:
            node = self.root

        while node.left:
            node = node.left

        return node.data

    def max(self, node=ROOT):
        if node == ROOT:
            node = self.root

        while node.right:
            node = node.right

        return node.data

    def remove(self, elem, node=ROOT):
        # Se for o valor padrão, executa a partir da raiz
        if node == ROOT:
            node = self.root
        # Se desceu até um ramo nulo, não há nada a fazer
        if node is None:
            return node
        # Se o valor for menor, desce à esquerda
        if elem < node.data:
            node.left = self.remove(elem, node.left)
        # Se o valor for maior, desce à direita
        elif elem > node.data:
            node.right = self.remove(elem, node.right)
        # Se não for nem menor, nem maior, encontramos! Vamos remover...
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Substituto é o sucessor do valor a ser removido
                substitute = self.min(node.right)
                # Ao invés de trocar a posição dos nós, troca o valor
                node.data = substitute
                # Depois, remove o substituto da subárvore à direita
                node.right = self.remove(substitute, node.right)

        return node

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
    values = [30, 5, 45, 11, 23, 51, 37, 2]
    bst = BinarySearchTree()

    for v in values:
        bst.insert(v)

    bst.inorder()
    print()
    bst.preorder()
    print()
    bst.postorder()
    print()
    print(bst.height())