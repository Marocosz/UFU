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
            return node.altura

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.esq) - self.__altura(no.dir))

    def __maior(self, x, y):
        if (x > y):
            return x
        else:
            return y

    def __RotacaoLL(self, A):
        print('RotacaoLL: ', A.info);
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), A.altura) + 1
        # A = B
        return B

    def __RotacaoRR(self, A):
        print('RotacaoRR: ', A.info);
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir), A.altura) + 1
        # A = B
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        A = self.__RotacaoLL(A)
        return A

    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        A = self.__RotacaoRR(A)
        return A

    def __insereValor(self, atual, valor):
        if atual == None:  # árvore vazia ou nó folha
            novo = Node(valor)
            return novo
        else:
            if valor < atual.info:
                atual.esq = self.__insereValor(atual.esq, valor)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor < atual.esq.info:
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
            else:
                atual.dir = self.__insereValor(atual.dir, valor)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor > atual.dir.info:
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
            if valor == atual.info:
                return True

            if valor > atual.info:
                atual = atual.dir
            else:
                atual = atual.esq

        return False

    def __procuraMenor(self, atual):
        no1 = atual
        no2 = atual.esq
        while no2 != None:
            no1 = no2
            no2 = no2.esq
        return no1

    def __removeValor(self, atual, valor):
        if atual.info == valor:  # achou o nó a ser removido
            if atual.esq == None or atual.dir is None:  # nó tem 1 filho ou nenhum
                if atual.esq != None:
                    atual = atual.esq
                else:
                    atual = atual.dir

            else:  # nó tem 2 filhos
                temp = self.__procuraMenor(atual.dir)
                atual.info = temp.info
                atual.dir = self.__removeValor(atual.dir, atual.info)
                if self.__fatorBalanceamento(atual) >= 2:
                    if self.__altura(atual.esq.dir) <= self.__altura(atual.esq.esq):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            if atual != None:
                atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1

        else:  # procura o nó a ser removido
            if valor < atual.info:
                atual.esq = self.__removeValor(atual.esq, valor)
                if self.__fatorBalanceamento(atual) >= 2:
                    if self.__altura(atual.dir.esq) <= self.__altura(atual.dir.dir):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)
            else:
                atual.dir = self.__removeValor(atual.dir, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__altura(atual.esq.dir) <= self.__altura(atual.esq.esq)):
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
            print(raiz.info)
            self.__preOrdem(raiz.esq)
            self.__preOrdem(raiz.dir)

    def preOrdem(self):
        if (self.__raiz != None):
            self.__preOrdem(self.__raiz)

    def __emOrdem(self, raiz):
        if (raiz != None):
            self.__emOrdem(raiz.esq)
            print(raiz.info, end=' ')
            self.__emOrdem(raiz.dir)

    def emOrdem(self):
        if (self.__raiz != None):
            self.__emOrdem(self.__raiz)

    def __posOrdem(self, raiz):
        if (raiz != None):
            self.__posOrdem(raiz.esq)
            self.__posOrdem(raiz.dir)
            print(raiz.info)

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
            print(raiz.info, end=" ")
        elif nivel > 0:
            self.__imprimeNivel(raiz.esq, nivel - 1)
            self.__imprimeNivel(raiz.dir, nivel - 1)

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
            self.__espelho(raiz.esq)
            self.__espelho(raiz.dir)
            temp = raiz.esq
            raiz.esq = raiz.dir
            raiz.dir = temp
