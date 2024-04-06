class NO:
    # Construtor de um nó (esquerda e direita são sempre nulos)
    def __init__(self, info):
        self.info = info
        self.esquerda = None
        self.direita = None

    # Representação de um nó - função para exibir na tela
    def __repr__(self):
        return f'{self.esquerda and self.esquerda.data} <- {self.info} -> {self.direita and self.direita.data}'


    def buscaRec(self, valor):
        if self == None:
            return False
        else:
            if valor == self.info:
                return True
            elif valor > self.info:
                return self.direita.buscaRec(valor)
            else:
                return self.esquerda.buscaRec(valor)
        return False


    def insRec(self, valor):
        if self is None:
            return NO(valor)
        else:
            if valor > self.info:
                if self.direita:
                   self.direita = self.direita.insRec(valor)
                else:
                   self.direita = NO(valor)
            else:
                if self.esquerda:
                   self.esquerda = self.esquerda.insRec(valor)
                else:
                   self.esquerda = NO(valor)
            return self



class ArvBinBusca:
    def __init__(self):
        self.__raiz = None

    def raizElem(self):
        return self.__raiz

    def insere(self, valor):
        novo = NO(valor)

        if self.__raiz == None:
            self.__raiz = novo
        else:
            atual = self.__raiz
            ant = None
            while atual != None:
                ant = atual
                if valor > atual.info:
                    atual = atual.direita
                elif valor < atual.info:
                    atual = atual.esquerda
                else:
                    return False
            if valor > ant.info:
                ant.direita = novo
            else:
                ant.esquerda = novo
        return True

    def insereRec(self, valor):
        self.__raiz = self.__insereRec(self.__raiz, valor)

    def __insereRec(self, raiz, valor):
        if raiz == None:
            novo = NO(valor)
            raiz = novo
            return raiz
        else:
            if (valor > raiz.data):
                raiz.direita = self.__insereRec(raiz.direita, valor)
            else:
                raiz.esquerda = self.__insereRec(raiz.esquerda, valor)
            return raiz

    def emOrdem(self):
        if self.__raiz != None:
            self.__emOrdem(self.__raiz)
        return

    def __emOrdem(self, raiz):
        if raiz != None:
            # Visita filho da esquerda.
            self.__emOrdem(raiz.esquerda)
            print(raiz.data, end=" ")
            # Visita filho da direita.
            self.__emOrdem(raiz.direita)

    def busca(self, valor):
        if self.__raiz == None:
            return False

        atual = self.__raiz
        while atual != None:
            if valor == atual.data:
                return True
            if valor > atual.data:
                atual = atual.direita
            else:
                atual = atual.esquerda

        return False

    def somaValores(self):
        if self.__raiz != None:
            soma = self.__somaValores(self.__raiz)
        return soma

    def __somaValores(self, raiz):
        if raiz == None:
            return 0
        else:
            return self.__somaValores(raiz.esquerda) + raiz.data + self.__somaValores(raiz.direita)

    def menor(self):
        if self.__raiz != None:
            min = self.__menor(self.__raiz)
        return min

    def __menor(self, raiz):
        if raiz.esquerda == None:
            return raiz.data
        else:
            return self.__menor(raiz.esquerda)


arv2 = ArvBinBusca()

arv2.insereRec(30)
arv2.insereRec(15)
arv2.insereRec(45)
arv2.insereRec(10)
arv2.insereRec(20)
arv2.insereRec(40)
arv2.insereRec(50)

arv2.emOrdem()
s = arv2.somaValores()
print('\nResultado Soma = ',s)

r = arv2.busca(5)
print('\nResultado Busca 5 = ',r)

# Obter o nó raiz da árvore, para aplicar a função de busca recursiva
no_raiz = arv2.raizElem()
r = no_raiz.buscaRec(10)
print('\nResultado Busca 10 = ',r)

s = arv2.menor()
print('\nResultado menor = ',s)
