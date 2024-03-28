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


