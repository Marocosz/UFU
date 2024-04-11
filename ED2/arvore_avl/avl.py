from node import NO

"""
Árvore AVL é uma árvore binária com o objetivo de balancear a estrutura de forma "automática"
de acordo com seu fator de balanceamento, ou seja, que a diferença máxima de altura das 
sub-árvores esquerda e direita de cada nó, seja de no máximo UMA unidade, e para isso usamos 
rotações, simples ou duplas, que são executadas a cada inserção ou remoção

Custo máximo de qualquer algoritmo é O(Log N)

O Fato de balanceamento deve ser +1, 0 ou -1
Se Fb > 1 ou < -1, a árvore deve ser balanceada naquele nó

=====================================================================================================================

Rotações são aplicadas no ancestral mais próximo do nó inserido cujo fator de balanceamento passa a ser +2 ou -2


"""

class AVL:
    def __init__(self):
        self.__raiz = None

    # Função para ter acesso a altura do nó qualquer
    def __height(self, no):
        if no is None:
            # Já definimos a altura de um nó não existente como "-1"
            return -1
        else:
            return no.height

    # Função para termos acesso ao fator de balanceamento (altura da esquerdo - altura da direita) de um nó qualquer
    def __fatorBalanceamento(self, no):
        return abs(self.__height(no.left) - self.__height(no.right))

    # Função básica que determina qual maior valor entre 2 valores
    def __maior(self, x, y):
        if x > y:
            return x
        else:
            return y

    """
    Rotação Simples a Direita
    
    Um novo nó é inserido na sub-árvore da esuqerda do filho esquerdo de A
    
    Assim, A é o nó desbalanceado
    Faremos dois movimentos para a esquerda: Left Left
    
    É necessário fazer uma rotação à direita, de modo que  o nó intermediário B ocupe o 
    lugar de A, e A se torne  a sub-árvore direita de B e a subárvore da direita de B vira
    subrárvore da esquerda de A
    """
    def __RotacaoLL(self, A):
        B = A.left
        A.left = B.right
        B.right = A
        A.height = self.__maior(self.__height(A.left), self.__height(A.right)) + 1
        B.height = self.__maior(self.__height(B.left), A.height) + 1
        # A = B
        return B

    """
    Rotação Simples a Esquerda

    Um novo nó é inserido na sub-árvore da direita do filho direito de A
    
    Assim, A é o nó desbalanceado
    Faremos dois movimentos para a esquerda: Right Right

    É necessário fazer uma rotação à esquerda, de modo que  o nó intermediário B ocupe o 
    lugar de A, e A se torne  a sub-árvore esquerda de B e a subárvore da esquerda de B vira
    subrárvore da direita de A
    """

    def __RotacaoRR(self, A):
        B = A.right
        A.right = B.left
        B.left = A
        A.height = self.__maior(self.__height(A.left), self.__height(A.right)) + 1
        B.height = self.__maior(self.__height(B.right), A.height) + 1
        # A = B
        return B

    """
    Rotação Dupla à Direita
    
    Um nó é inserido na sub-árvore da direita do filho esquerdo de A
    
    Assim, A fica desbalanceado
    Faremos um movimento para esquerda e outro para direita
    
    É necessário fazer uma rotação dupla, de modo que o nó C se torne pai dos nós A (filho da direita)
    e B (filho da esquerda)
    
    - Rotação RR em B
    - Rotação LL em A
    """
    def __RotacaoLR(self, A):
        A.left = self.__RotacaoRR(A.left)
        A = self.__RotacaoLL(A)
        return A

    """
    Rotação Dupla à Esquerda

    Um nó é inserido na sub-árvore da esquerda do filho direito de A

    Assim, A fica desbalanceado
    Faremos um movimento para direita e outro para esquerda

    É necessário fazer uma rotação dupla, de modo que o nó C se torne pai dos nós A (filho da esquerda)
    e B (filho da direita)

    - Rotação LL em B
    - Rotação RR em A
    """ 
    def __RotacaoRL(self, A):
        A.right = self.__RotacaoLL(A.right)
        A = self.__RotacaoRR(A)
        return A

    def __insereValor(self, atual, valor):
        if (atual == None):  # árvore vazia ou nó folha
            novo = NO(valor)
            return novo
        else:
            if (valor < atual.data):
                atual.left = self.__insereValor(atual.left, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (valor < atual.left.data):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
            else:
                atual.right = self.__insereValor(atual.right, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (valor > atual.right.data):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)

            atual.altura = self.__maior(self.__height(atual.esq), self.__height(atual.dir)) + 1
            return atual

    def insere(self, valor):
        if (self.busca(valor)):
            return False  # valor já existe na árvore
        else:
            self.__raiz = self.__insereValor(self.__raiz, valor)
            return True

    def busca(self, valor):
        if (self.__raiz == None):
            return False

        atual = self.__raiz
        while (atual != None):
            if (valor == atual.data):
                return True

            if (valor > atual.data):
                atual = atual.right
            else:
                atual = atual.left

        return False

    def __procuraMenor(self, atual):
        no1 = atual
        no2 = atual.left
        while (no2 != None):
            no1 = no2
            no2 = no2.left
        return no1

    def __removeValor(self, atual, valor):
        if (atual.data == valor):  # achou o nó a ser removido
            if (atual.left == None or atual.right == None):  # nó tem 1 filho ou nenhum
                if (atual.left != None):
                    atual = atual.left
                else:
                    atual = atual.right

            else:  # nó tem 2 filhos
                temp = self.__procuraMenor(atual.right)
                atual.data = temp.info
                atual.right = self.__removeValor(atual.right, atual.data)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__height(atual.left.dir) <= self.__height(atual.left.esq)):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            if (atual != None):
                atual.altura = self.__maior(self.__height(atual.esq), self.__height(atual.dir)) + 1

        else:  # procura o nó a ser removido
            if (valor < atual.data):
                atual.left = self.__removeValor(atual.left, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__height(atual.right.left) <= self.__height(atual.right.right)):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)
            else:
                atual.right = self.__removeValor(atual.right, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__height(atual.left.dir) <= self.__height(atual.left.esq)):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            atual.altura = self.__maior(self.__height(atual.esq), self.__height(atual.dir)) + 1

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
        h = self.__height(self.__raiz)
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
        if self.__raiz != None:
            self.__alteraValorNo(self.__raiz)

    def __alteraValorNo(self, raiz):
        if raiz is None:
            return 0
        elif raiz.esq == None and raiz.dir == None:
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
