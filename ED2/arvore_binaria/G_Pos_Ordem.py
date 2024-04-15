"""
Percursão Pós-Ordem em Árvore Binária

Sistema de Busca:
Sempre buscar primeiro os filhos da esquerda (primeiramente) e depois da direita, até a raiz

OBS: Cada nó pode ser olhado como uma raiz, é bom ter essa ideia para trabalharmos com recursão
"""

from F_Arvores import BinaryTree, Node

tree = BinaryTree()

n1 = Node('I')
n2 = Node('S')
n3 = Node('C')
n4 = Node('R')
n5 = Node('E')
n6 = Node('V')
n7 = Node('A')
n8 = Node('S')
n9 = Node('5')
n0 = Node('3')

n0.left = n6
n0.right = n9
n6.left = n1
n6.right = n5
n5.left = n2
n5.right = n4
n4.right = n3
n9.left = n8
n8.right = n7

tree.root = n0

tree.postorder()

print()
print(tree.height())