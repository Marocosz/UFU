"""
Questão 01
"""


# Definição da Classe TabelaHash com tamanho pré-definido e listas vazias
class TabelaHash:
    def __init__(self, tam):
        self.tamanho = tam
        self.indice = [None] * self.tamanho  # lista vazia para o armazenamento das chaves (ou índices)
        self.item = [None] * self.tamanho  # lista vazia para o armazenamento dos valores (ou itens)

    def funcao_hash(self, novo_indice, tamanho):
        return novo_indice % tamanho

    def funcao_novo_hash(self, hash_antigo, tamanho):    # nova posição hash usando sondagem linear
        return (hash_antigo+1) % tamanho

    def insere(self, novo_indice, novo_item):
        pos_hash = self.funcao_hash(novo_indice, self.tamanho)

        if self.indice[pos_hash] is None:
            self.indice[pos_hash] = novo_indice
            self.item[pos_hash] = novo_item
        else:                                            # programação da sondagem linear
            nova_pos_hash = self.funcao_novo_hash(pos_hash, self.tamanho)
            while self.indice[nova_pos_hash] is not None:
                 nova_pos_hash = self.funcao_novo_hash(nova_pos_hash, self.tamanho)

            self.indice[nova_pos_hash] = novo_indice
            self.item[nova_pos_hash] = novo_item

    def busca(self, indice_desejado):
        pos_hash = self.funcao_hash(indice_desejado, self.tamanho)

        if self.indice[pos_hash] == indice_desejado:
            return self.item[pos_hash]
        else:
            nova_pos_hash = self.funcao_novo_hash(pos_hash, self.tamanho)
            while nova_pos_hash != pos_hash:
                if self.indice[nova_pos_hash] == indice_desejado:
                    return self.item[nova_pos_hash]
                nova_pos_hash = self.funcao_novo_hash(nova_pos_hash, self.tamanho)
            return None

# Testando as funções 'funcao_hash' e 'funcao_novo_hash'
T = TabelaHash(11)
pos_hash = T.funcao_hash(356,11)
nova_pos = T.funcao_novo_hash(pos_hash,11)
print(pos_hash, nova_pos)

# Testando os três casos de colisão identificados anteriormente.
# Com a sondagem linear, os itens serão armazenados nas próximas posições livres.
T = TabelaHash(11)
T.insere(356, "Maria")
T.insere(785, "Victor")
T.insere(224, "Caio")
print(T.indice, "\n", T.item)

"""
Exercício 02
"""

T = TabelaHash(7)
T.insere(2341, "Marcos1")
T.insere(4234, "Marcos2")
T.insere(2839, "Marcos3")
T.insere(430, "Marcos4")
T.insere(22, "Marcos5")
T.insere(397, "Marcos6")
T.insere(3920, "Marcos7")
print(T.indice, "\n", T.item)

"""
Exercício 03
"""

print(T.busca(2340))
