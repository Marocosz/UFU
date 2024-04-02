from node import NO


class AVL:
    def __init__(self):
        self.__raiz = None
        self.rotacoes_ll_rr = 0
        self.rotacoes_lr_rl = 0
        self.arqtxt = []


    def __altura(self, no):
        if (no == None):
            return -1
        else:
            return no.altura

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.esq) - self.__altura(no.dir))

    def __maior(self, x, y):
        if (x > y):
            return x
        else:
            return y

    def __RotacaoLL(self, A):
        B = A.esq
        A.esq = B.dir
        B.dir = A
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.esq), A.altura) + 1
        self.rotacoes_ll_rr += 1
        # A = B
        return B

    def __RotacaoRR(self, A):
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir), A.altura) + 1
        self.rotacoes_ll_rr += 1
        # A = B
        return B

    def __RotacaoLR(self, A):
        A.esq = self.__RotacaoRR(A.esq)
        A = self.__RotacaoLL(A)
        self.rotacoes_lr_rl += 1
        self.rotacoes_ll_rr -= 1
        return A

    def __RotacaoRL(self, A):
        A.dir = self.__RotacaoLL(A.dir)
        A = self.__RotacaoRR(A)
        self.rotacoes_lr_rl += 1
        self.rotacoes_ll_rr -= 1
        return A

    def __insereValor(self, atual, valor, valorlista):
        if (atual == None):  # árvore vazia ou nó folha
            novo = NO(valor)
            novo.lista_linha.append(valorlista)
            return novo
        else:
            if (valor < atual.info):
                atual.esq = self.__insereValor(atual.esq, valor, valorlista)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (valor < atual.esq.info):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)
            else:
                atual.dir = self.__insereValor(atual.dir, valor, valorlista)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (valor > atual.dir.info):
                        atual = self.__RotacaoRR(atual)
                    else:
                        atual = self.__RotacaoRL(atual)

            atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1
            return atual

    def num_elementos(self, no):
      if no is None:
          return 0
      return 1 + self.num_elementos(no.esq) + self.num_elementos(no.dir)

    def buscaME(self, valor):
        if(self.__raiz == None):
            return False

        atual = self.__raiz
        while atual != None:
            if(valor == atual.info):
              ME = self.num_elementos(atual.esq) - self.num_elementos(atual.dir)
              if ME == 0:
                return 0
              elif ME != 0:
                print('O valor de ME é:', ME)
                return 1

            if(valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq

        return -1

    def insere(self, valor, valorlista):
        if (self.busca(valor)):
            return False  # valor já existe na árvore
        else:
            self.__raiz = self.__insereValor(self.__raiz, valor, valorlista)
            return True

    def insere_lista_linha(self, valor, valorlista):
        atual = self.__raiz
        while (atual != None):
            if (valor == atual.info):
                atual.lista_linha.append(valorlista)

            if (valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq

    def busca(self, valor):
        if (self.__raiz == None):
            return False

        atual = self.__raiz
        while (atual != None):
            if (valor == atual.info):
                return True

            if (valor > atual.info):
                atual = atual.dir
            else:
                atual = atual.esq

        return False

    def __procuraMenor(self, atual):
        no1 = atual
        no2 = atual.esq
        while (no2 != None):
            no1 = no2
            no2 = no2.esq
        return no1

    def __removeValor(self, atual, valor):
        if (atual.info == valor):  # achou o nó a ser removido
            if (atual.esq == None or atual.dir == None):  # nó tem 1 filho ou nenhum
                if (atual.esq != None):
                    atual = atual.esq
                else:
                    atual = atual.dir

            else:  # nó tem 2 filhos
                temp = self.__procuraMenor(atual.dir)
                atual.info = temp.info
                atual.dir = self.__removeValor(atual.dir, atual.info)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__altura(atual.esq.dir) <= self.__altura(atual.esq.esq)):
                        atual = self.__RotacaoLL(atual)
                    else:
                        atual = self.__RotacaoLR(atual)

            if (atual != None):
                atual.altura = self.__maior(self.__altura(atual.esq), self.__altura(atual.dir)) + 1

        else:  # procura o nó a ser removido
            if (valor < atual.info):
                atual.esq = self.__removeValor(atual.esq, valor)
                if (self.__fatorBalanceamento(atual) >= 2):
                    if (self.__altura(atual.dir.esq) <= self.__altura(atual.dir.dir)):
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
            self.arqtxt.append(raiz.info + " " + ', '.join(raiz.lista_linha))
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
