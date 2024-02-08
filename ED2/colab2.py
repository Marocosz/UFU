class NO:
    def __init__(self, info):
        self.info = info
        self.esq = None
        self.dir = None


def pre_ordem(raiz):
    if not raiz:
        return

    # Visita nodo corrente.
    print(raiz.info, end = " ")

    # Visita filho da esquerda.
    pre_ordem(raiz.esq)

    # Visita filho da direita.
    pre_ordem(raiz.dir)


def em_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    em_ordem(raiz.esq)

    # Visita nodo corrente.
    print(raiz.info, end = " ")

    # Visita filho da direita.
    em_ordem(raiz.dir)


def pos_ordem(raiz):
    if not raiz:
        return

    # Visita filho da esquerda.
    pos_ordem(raiz.esq)

    # Visita filho da direita.
    pos_ordem(raiz.dir)

    # Visita nodo corrente.
    print(raiz.info, end = " ")


# =====================================================================================================================
raiz = NO(10)

raiz.esq = NO(34)
raiz.dir = NO(89)
raiz.esq.esq = NO(45)
raiz.esq.dir = NO(50)
raiz.dir.esq = NO(65)
raiz.dir.dir = NO(44)
raiz.dir.esq.esq = NO(5)

#  ====================================================================================================================
arvd = NO(50)

arvd.dir = NO(43)
arvd.dir.dir = NO(40)
arvd.dir.dir.dir = NO(33)
arvd.dir.dir.dir.dir = NO(30)
arvd.dir.dir.dir.dir.dir = NO(23)
arvd.dir.dir.dir.dir.dir.dir = NO(20)
arvd.dir.dir.dir.dir.dir.dir.dir = NO(13)

# Para fazer uma busca não é tão bom, visto que para achar um elemento irá passar por todos

# =====================================================================================================================

raiz1 = NO(2)

raiz1.esq = NO(7)
raiz1.dir = NO(5)
raiz1.esq.esq = NO(2)
raiz1.esq.dir = NO(6)
raiz1.dir.dir = NO(9)
raiz1.esq.dir.esq = NO(5)
raiz1.esq.dir.dir = NO(11)
raiz1.dir.dir.esq = NO(4)


pre_ordem(raiz1)
print('')
pos_ordem(raiz1)
print('')
em_ordem(raiz1)

# Exercício 08 ========================================================================================================
# Resposta: Sim, todas as árvores são iniciadas pela raiz, passando pela esquerda primeiramente, a diferença entre elas
# é qual item vai ser impresso ou alterado etc