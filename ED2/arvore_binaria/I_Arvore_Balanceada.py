"""
## Árvores Balanceadas

A complexidade de bsuca de uma "árvore binária de busca" seria O(h), a altura dela, porém, nessa árvore não temos como
garantir uma ótima distribuição da altura, quando num caso onde há números em sequência (parecendo uma lista e assim se
tornando uma espécie de lista), assim não sendo a mais
efieciente.

Com a árvore bem distribuida, balanceada dos dois lados e [completa], temos que a complexidade de busca seria O(ln(N))

OBS: É importante salientar que em alguns casos para remover ou inserir um ítem na árvore, poderiamos ter uma
complexidade o(N) quando formos balancear novamente. E para resolver isso, devemos relaxar um pouco as restrições em
questão da árvore ser completa, assim podemos denotar que a árvore seja proporcional a log(N). Ou seja, nem toda árvore
balanceada é uma árvore completa.


"""

"""
## Árvore AVL (Adeslson-Vesky e Landis)

É uma árvore binária de busca, com a propriedade onde a diferença de altura da subárvore da esquerda com a subárvore da
direita seja apenas 1 (fator de balanço)

# Fator de Balanço = Fb = F

Com isso, a Árvore AVL tem uma propriedade de rotação, para balancear a estrutura
"""
from F_Arvores import Node


class AVL:
    def __init__(self):
        self.__raiz = None

    def __altura(self, node):
        if node == None:
            return -1
        else:
            return node.height

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.left) - self.__altura(no.right))

    def __maior(self, x, y):
        if (x > y):
            return x
        else:
            return y

    def __RotacaoLL(self, A):
        print('RotacaoLL: ', A.data);
        B = A.left
        A.left = B.right
        B.right = A
        A.height = self.__maior(self.__altura(A.left), self.__altura(A.right)) + 1
        B.height = self.__maior(self.__altura(B.left), A.height) + 1
        # A = B
        return B

    def __RotacaoRR(self, A):
        print('RotacaoRR: ', A.data);
        B = A.right
        A.right = B.left
        B.left = A
        A.height = self.__maior(self.__altura(A.left), self.__altura(A.right)) + 1
        B.height = self.__maior(self.__altura(B.right), A.height) + 1
        # A = B
        return B

    def __RotacaoLR(self, A):
        A.left = self.__RotacaoRR(A.left)
        A = self.__RotacaoLL(A)
        return A

    def __RotacaoRL(self, A):
        A.right = self.__RotacaoLL(A.right)
        A = self.__RotacaoRR(A)
        return A

    def __insereValor(self, atual, valor):
        if atual == None:  # árvore vazia ou nó folha
            novo = Node(valor)
            return novo
        else:
            if valor < atual.data:
                atual.left = self.__insereValor(atual.left, valor)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor < atual.left.info:
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
            else:
                atual.right = self.__insereValor(atual.right, valor)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor > atual.right.info:
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)

            atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1
            return atual

    def insere(self, valor):
        if self.busca(valor):
            return False  # valor já existe na árvore
        else:
            self.__raiz = self.__insereValor(self.__raiz, valor)
            return True

    def busca(self, valor):
        if self.__raiz == None:
            return False

        atual = self.__raiz
        while atual != None:
            if valor == atual.data:
                return True

            if valor > atual.data:
                atual = atual.right
            else:
                atual = atual.left

        return False

    def __procuraMenor(self, atual):
        no1 = atual
        no2 = atual.left
        while no2 != None:
            no1 = no2
            no2 = no2.left
        return no1

    def __removeValor(self, atual, valor):
        if atual.data == valor:  # achou o nó a ser removido
            if atual.left == None or atual.right is None:  # nó tem 1 filho ou nenhum
                if atual.left != None:
                    atual = atual.left
                else:
                    atual = atual.right

            else:  # nó tem 2 filhos
                temp = self.__procuraMenor(atual.right)
                atual.data = temp.info
                atual.right = self.__removeValor(atual.right, atual.data)
                if self.__fatorBalanceamento(atual) >= 2:
                    if self.__altura(atual.left.dir) <= self.__altura(atual.left.esq):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            if atual != None:
                atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1

        else:  # procura o nó a ser removido
            if valor < atual.data:
                atual.left = self.__removeValor(atual.left, valor)
                if self.__fatorBalanceamento(atual) >= 2:
                    if self.__altura(atual.right.left) <= self.__altura(atual.right.right):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)
            else:
                atual.right = self.__removeValor(atual.right, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__altura(atual.left.dir) <= self.__altura(atual.left.esq)):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1

        return atual

    def remove(self, valor):
        if (self.__raiz == None or not self.busca(valor)):
            return False  # árvore vazia ou valor não existe na árvore
        else:
            self.__raiz = self.__removeValor(self.__raiz, valor)
            return True

    def __preOrdem(self, raiz):
        if (raiz != None):
            print(raiz.data)
            self.__preOrdem(raiz.left)
            self.__preOrdem(raiz.right)

    def preOrdem(self):
        if (self.__raiz != None):
            self.__preOrdem(self.__raiz)

    def __emOrdem(self, raiz):
        if (raiz != None):
            self.__emOrdem(raiz.left)
            print(raiz.data, end=' ')
            self.__emOrdem(raiz.right)

    def emOrdem(self):
        if (self.__raiz != None):
            self.__emOrdem(self.__raiz)

    def __posOrdem(self, raiz):
        if (raiz != None):
            self.__posOrdem(raiz.left)
            self.__posOrdem(raiz.right)
            print(raiz.data)

    def posOrdem(self):
        if (self.__raiz != None):
            self.__posOrdem(self.__raiz)

    def emNivel(self):
        h = self.__altura(self.__raiz)
        for i in range(0, h + 1):
            self.__imprimeNivel(self.__raiz, i)
            print(' - nivel ', i)

    # Imprimir elementos que estão no mesmo nível
    def __imprimeNivel(self, raiz, nivel):
        if raiz is None:
            return
        if nivel == 0:
            print(raiz.data, end=" ")
        elif nivel > 0:
            self.__imprimeNivel(raiz.left, nivel - 1)
            self.__imprimeNivel(raiz.right, nivel - 1)

    def alteraValNo(self):
        if (self.__raiz != None):
            self.__alteraValorNo(self.__raiz)

    def __alteraValorNo(self, raiz):
        if raiz is None:
            return 0
        elif (raiz.esq == None and raiz.dir == None):
            return raiz.info
        else:
            raiz.info = self.__alteraValorNo(raiz.esq) + self.__alteraValorNo(raiz.dir)
            return raiz.info

    def espelho(self):
        if (self.__raiz != None):
            self.__espelho(self.__raiz)

    def __espelho(self, raiz):
        if raiz is None:
            return
        else:
            temp = raiz
            self.__espelho(raiz.left)
            self.__espelho(raiz.right)
            temp = raiz.left
            raiz.left = raiz.right
            raiz.right = temp
