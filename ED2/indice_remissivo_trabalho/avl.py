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
            return no.height

    def __fatorBalanceamento(self, no):
        return abs(self.__altura(no.left) - self.__altura(no.right))

    def __maior(self, x, y):
        if x > y:
            return x
        else:
            return y

    def __RotacaoLL(self, A):
        B = A.left
        A.left = B.right
        B.right = A
        A.height = self.__maior(self.__altura(A.left), self.__altura(A.right)) + 1
        B.height = self.__maior(self.__altura(B.left), A.height) + 1
        self.rotacoes_ll_rr += 1
        return B

    def __RotacaoRR(self, A):
        B = A.right
        A.right = B.left
        B.left = A
        A.height = self.__maior(self.__altura(A.left), self.__altura(A.right)) + 1
        B.height = self.__maior(self.__altura(B.right), A.height) + 1
        self.rotacoes_ll_rr += 1
        return B

    def __RotacaoLR(self, A):
        A.left = self.__RotacaoRR(A.left)
        A = self.__RotacaoLL(A)
        self.rotacoes_lr_rl += 1
        self.rotacoes_ll_rr -= 1
        return A

    def __RotacaoRL(self, A):
        A.right = self.__RotacaoLL(A.right)
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
            if valor < atual.data:
                atual.left = self.__insereValor(atual.left, valor, valorlista)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor < atual.left.info:
                        atual = self.__RotacaoLL(atual)

                    else:
                        atual = self.__RotacaoLR(atual)

            else:
                atual.right = self.__insereValor(atual.right, valor, valorlista)
                if self.__fatorBalanceamento(atual) >= 2:
                    if valor > atual.right.info:
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
            if valor == atual.data:
                ME = self.num_elementos(atual.left) - self.num_elementos(atual.right)

                if ME == 0:
                    return self.ME_(0, ME)

                elif ME != 0:

                    return self.ME_(1,ME)

            if valor > atual.data:
                atual = atual.right

            else:
                atual = atual.left

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
            if valor == atual.data:
                if valorlista not in atual.lista_linha:
                    atual.lista_linha.append(valorlista)

            if valor > atual.data:
                atual = atual.right

            else:
                atual = atual.left

    def busca(self, valor):
        if self.__raiz is None:
            return False

        atual = self.__raiz
        while atual is not None:
            if valor == atual.data:
                return True

            if valor > atual.data:
                atual = atual.right
            else:
                atual = atual.left

        return False

    def __cria_indice(self, raiz):
        if raiz is not None:
            self.__cria_indice(raiz.left)
            self.arqtxt.append(raiz.data + " " + ', '.join(raiz.lista_linha))
            self.__cria_indice(raiz.right)

    def indice(self):
        if self.__raiz is not None:
            self.__cria_indice(self.__raiz)

    def __palavra_mais_vista_em_linhas_diferentes(self, no, no_maior):
        if no is not None:
            self.__palavra_mais_vista_em_linhas_diferentes(no.left, no_maior)
            if len(no.lista_linha) > len(no_maior.lista_linha):
                no_maior.lista_linha = no.lista_linha
                self.mais_aparece = no.data
            self.__palavra_mais_vista_em_linhas_diferentes(no.right, no_maior)

    def palavra_mais_vista_em_linhas_diferentes(self):
        if self.__raiz is not None:
            no_maior = NO(0)
            self.__palavra_mais_vista_em_linhas_diferentes(self.__raiz, no_maior)
