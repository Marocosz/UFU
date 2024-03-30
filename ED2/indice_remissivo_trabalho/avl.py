from node import Node


class AVL:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    def __height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def balancingFactor(self, node):
        return abs(self.__height(node.left) - self.__height(node.right))

    def bigger(self, x, y):
        if x > y:
            return x
        else:
            return y

    def rotationLL(self, A):
        B = A.left
        A.left = B.right
        B.dir = A
        A.height = self.bigger(self.__height(A.left), self.__height(A.right)) + 1
        B.height = self.bigger(self.__height(B.left), A.height) + 1

        return B

    def rotationRR(self, A):
        B = A.right
        A.right = B.left
        B.left = A
        A.height = self.bigger(self.__height(A.left), self.__height(A.right)) + 1
        B.height = self.bigger(self.__height(B.left), A.height) + 1

        return B

    def rotationLR(self, A):
        A.left = self.rotationRR(A.left)
        A = self.rotationLL(A)

        return A

    def rotationRL(self, A):
        A.right = self.rotationLL(A.right)
        A = self.rotationRR(A)

        return A

    def search(self, elem):
        # Se não houver nenhum nó na árvore (retornar false)
        if self.root is None:
            return False

        current = self.root
        while current is not None:
            if current.data == elem:
                return True

            if elem > current.data:
                current = current.right
            else:
                current = current.left

        return False

    def searchMin(self, current):
        node1 = current
        node2 = current.left
        while node2 is not None:
            node1 = node2
            node2 = node2.left
        return node1

    def __insert(self, elem, current):
        if current is None:
            new = Node(elem)
            return new
        else:
            if elem < current.data:
                current.left = self.__insert(current.left, elem)
                if self.balancingFactor(current) >= 2:
                    if elem < current.left.data:
                        current = self.rotationLL(current)
                    else:
                        current = self.rotationLR(current)

            else:
                current.right = self.__insert(current.right, elem)
                if self.balancingFactor(current) >= 2:
                    if elem > current.right.data:
                        current = self.rotationRR(current)
                    else:
                        current = self.rotationRL(current)

            current.height = self.bigger(self.__height(current.left), self.__height(current.right)) + 1

            return current

    def insert(self, elem):
        if self.search(elem):
            return False
        else:
            self.root = self.__insert(self.root, elem)
            return True

    def __remove(self, current, valor):

        if current.info == valor: # Achou o nó a se removido
            if current.left is None or current.left is None: # Há apenas um filho
                if current.left is None:
                    current = current.left
                else:
                    current = current.right

            else: # Há dois filhos
                temp = self.searchMin(current.right)
                current.data = temp.data
                current.right = self.__remove(current.right, current.data)

                if self.balancingFactor(current) >= 2:
                    if self.__height(current.left.right) <= self.__height(current.left.right):
                        current = self.rotationLL(current)
                    else:
                        current = self.rotationLR(current)

            if current is not None:
                current.height = self.bigger(self.__height(current.left), self.__height(current.right)) + 1

        else: # Procurará o nó a ser removido
            if valor < current.data:
                current.left = self.__remove(current.left, valor)

                if self.balancingFactor(current) >= 2:
                    if self.__height(current.right.left) <= self.__height(current.right.right):
                        current = self.rotationRR(current)
                    else:
                        current = self.rotationRL(current)

            else:
                current.right = self.__remove(current.right, valor)

                if self.balancingFactor(current) >= 2:
                    if self.__height(current.left.right) <= self.__height(current.left.left):
                        current = self.rotationLL(current)
                    else:
                        current = self.rotationLR(current)

            current.height =

    def remove(self, elem):
        if self.root is None or not self.search(elem):
            # árvore não existe ou item não existe
            return False
        else:
            self.root = self.__remove(self.root, elem)
            return True

    def preOrder(self, root):
        if root is not None:
            print(root.data)
            self.preOrder(root.left)
            self.preOrder(root.right)

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            print(root.data, end='')
            self.inOrder(root.right)

    def postOrder(self, root):
        if root is not None:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root)

    def printLevel(self, root, level):
        if root is None:
            return 0
        if level == 0:
            print(root.data, end=' ')
        elif level > 0:
            self.printLevel(root.left, level-1)
            self.printLevel(root.right, level-1)

    def inLevel(self):
        h = self.__height(self.root)
        for i in range(0, h+1):
            self.printLevel(self.root, i)
            print(f'{i}º Level')

    def __changeValueNode(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.data
        else:
            root.data = self.__changeValueNode(root.left) + self.__changeValueNode(root.right)
            return root.data

    def changeValueNode(self):
        if self.root is not None:
            self.__changeValueNode(self.root)
