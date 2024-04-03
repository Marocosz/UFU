from node import NO


class AVL:
    def __init__(self):
        self.__raiz = None
        self.rotacoes_ll_rr = 0
        self.rotacoes_lr_rl = 0
        self.arqtxt = []
        self.mais_aparece = None

    def __altura(self, no):
        if no is None:
            return -1
        else:
            return no.altura

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.esq) - self.__altura(no.dir))

    def __maior(self, x, y):
        if x > y:
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
        return B

    def __RotacaoRR(self, A):
        B = A.dir
        A.dir = B.esq
        B.esq = A
        A.altura = self.__maior(self.__altura(A.esq), self.__altura(A.dir)) + 1
        B.altura = self.__maior(self.__altura(B.dir), A.altura) + 1
        self.rotacoes_ll_rr += 1
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
        if atual is None:  # árvore vazia ou nó folha
            novo = NO(valor)
            novo.lista_linha.append(valorlista)
            return novo

        else:
            if valor < atual.info:
                atual.esq = self.__insereValor(atual.esq, valor, valorlista)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor < atual.esq.info:
                        atual = self.__RotacaoLL(atual)

                    else:
                        atual = self.__RotacaoLR(atual)

            else:
                atual.dir = self.__insereValor(atual.dir, valor, valorlista)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor > atual.dir.info:
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
        valor = valor.lower()
        if self.__raiz is None:
            return False

        atual = self.__raiz
        while atual is not None:
            if valor == atual.info:
                ME = self.num_elementos(atual.esq) - self.num_elementos(atual.dir)

                if ME == 0:
                    return self.ME_(0, ME)

                elif ME != 0:

                    return self.ME_(1,ME)

            if valor > atual.info:
                atual = atual.dir

            else:
                atual = atual.esq

        return self.ME_(-1, None)

    def ME_(self, valor, medidor):
      if valor == 0:
        print('O valor de ME é 0')
      if valor == 1 :
        print('O valor de ME é',medidor)
      if valor == -1:
        print('A palavra não foi encontrada')

    def insere(self, valor, valorlista):
        if self.busca(valor):
            return False

        else:
            self.__raiz = self.__insereValor(self.__raiz, valor, valorlista)
            return True

    def insere_lista_linha(self, valor, valorlista):
        atual = self.__raiz
        while atual is not None:
            if valor == atual.info:
                if valorlista not in atual.lista_linha:
                    atual.lista_linha.append(valorlista)

            if valor > atual.info:
                atual = atual.dir

            else:
                atual = atual.esq

    def busca(self, valor):
        if self.__raiz is None:
            return False

        atual = self.__raiz
        while atual is not None:
            if valor == atual.info:
                return True

            if valor > atual.info:
                atual = atual.dir
            else:
                atual = atual.esq

        return False

    def __cria_indice(self, raiz):
        if raiz is not None:
            self.__cria_indice(raiz.esq)
            self.arqtxt.append(raiz.info + " " + ', '.join(raiz.lista_linha))
            self.__cria_indice(raiz.dir)

    def indice(self):
        if self.__raiz is not None:
            self.__cria_indice(self.__raiz)

    def __palavra_mais_vista_em_linhas_diferentes(self, no, no_maior):
        if no is not None:
            self.__palavra_mais_vista_em_linhas_diferentes(no.esq, no_maior)
            if len(no.lista_linha) > len(no_maior.lista_linha):
                no_maior.lista_linha = no.lista_linha
                self.mais_aparece = no.info
            self.__palavra_mais_vista_em_linhas_diferentes(no.dir, no_maior)

    def palavra_mais_vista_em_linhas_diferentes(self):
        if self.__raiz is not None:
            no_maior = NO(0)
            self.__palavra_mais_vista_em_linhas_diferentes(self.__raiz, no_maior)
