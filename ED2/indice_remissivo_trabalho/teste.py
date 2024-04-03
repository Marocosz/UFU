class Node:
    def __init__(self, lista):
        self.lista = lista
        self.left = None
        self.right = None
        self.height = 1

def findNodeWithLargestList(node, max_node):
    if node is not None:
        findNodeWithLargestList(node.left, max_node)
        # Comparar o tamanho da lista do nó atual com o tamanho da lista do nó máximo
        if len(node.lista) > len(max_node.lista):
            # Se a lista do nó atual for maior, atualize o nó máximo
            max_node.lista = node.lista
        findNodeWithLargestList(node.right, max_node)

# Exemplo de utilização:
# Suponha que 'root' é o nó raiz da árvore AVL
root = Node([1, 2, 3])
root.left = Node([4, 5])
root.right = Node([6, 7, 8])
root.left.left = Node([9])
root.left.right = Node([10, 11])
root.right.left = Node([12, 13, 14, 15])
root.right.right = Node([16, 17, 18])

# Criar um nó inicial com uma lista vazia
max_node = Node([])

# Chame a função para encontrar o nó com a maior lista
findNodeWithLargestList(root, max_node)

# O nó com a maior lista agora está armazenado em max_node
print("O nó com a maior lista é:", max_node.lista)
