from csv import writer
import random
import networkx as nx
import csv
import matplotlib.pyplot as plt
import pandas as pd

"""
Questão 1: As redes sociais vêm ganhando cada vez mais relevância na comunicação
entre pessoas e organizações afins para a articulação de eventos políticos, eleições e
outras formas de ativismo. Explique como os grafos podem representar redes sociais.

Resposta:
Grafos representam redes sociais atribuindo nós a usuários e arestas a conexões entre 
eles, como amizades, seguidores ou interesses comuns.
"""

"""
Questão 2: Explique como funcionam os percursos em largura e em profundidade num grafo.
Numa rede social, qual seria a utilidade de um percurso em profundidade?

Resposta:
Em largura: Começa visitando o nó inicial e depois explora todos os vizinhos desse nó antes
de continuar para os vizinhos dos vizinhos. Ele explora o grafo em camadas, visitando 
os nós mais próximos antes de se mover para os mais distantes.

Em profundida:
Começa visitando o nó inicial e depois continua a se aprofundar em um ramo específico do 
grafo até atingir um nó sem filhos não visitados, momento em que retorna e explora 
outros ramos. Ele se aprofunda o máximo possível em um ramo antes de retroceder.

Numa rede social, ele pode user útil para descobrir conexoes indiretas entre usuários,
revelar comunidades ou grupos de usuários que estão fotemente conectados entre si, mesmo que
não estejam diretamente ligados ao usuário inicial, pode ser usado também para rastrear
a propagação de uma postagem ou tendência, seguindo as conexões de compartilhamento
"""

# Questão 3 ===================================================================================

with open('simulacao_redes.csv', 'w', encoding='utf-8', newline='') as arq:
    escritor_csv = writer(arq)
    escritor_csv.writerow(['Nomes', 'Amigo', 'Interações'])
    for i in range(0, 20):
        nomes = ["Alice", "Joao", "Carlos", "Denise", "Eva", "Marcos", "Flávia", "Artur",
                 "Simão", "Pedro", "Ana", "Murilo", "Julia", "Vinicius", "Clara", "Marcelo"]
        nome = nomes[random.randint(0, len(nomes)-1)]
        nomes.remove(nome)
        amigo = nomes[random.randint(0, len(nomes)-1)]
        interacao = random.randint(0, 100)
        escritor_csv.writerow([nome, amigo, interacao])

# Questão 4 ===================================================================================

with open('simulacao_redes.csv', 'r', encoding='utf-8') as arq:
    csv_reader = csv.reader(arq)
    lista_simulacao = list(csv_reader)

del lista_simulacao[0]

G = nx.DiGraph()

for x in lista_simulacao:
    G.add_node(x[0])
    G.add_edge(x[0], x[1], weight=x[2])


mapa_de_cores = []
for no_pessoa in G.nodes():
    if G.degree(no_pessoa) >= 6:
        mapa_de_cores.append("red")
    elif G.degree(no_pessoa) >= 3:
        mapa_de_cores.append("orange")
    else:
        mapa_de_cores.append("yellow")

cg = nx.circular_layout(G)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos=cg, node_color=mapa_de_cores, with_labels=True, node_size=1500)
nx.draw_networkx_edge_labels(G, pos=cg, edge_labels=edge_labels)
plt.show()

ch = nx.spiral_layout(G)
nx.draw(G, pos=ch, node_color=mapa_de_cores, with_labels=True, node_size=1500)
nx.draw_networkx_edge_labels(G, pos=ch, edge_labels=edge_labels)
plt.show()

# Questão 5 ===================================================================================


def pares(lista_grafo):
    lista_pares = []
    for i in range(len(lista_grafo)):
        for dados in lista_grafo:
            if lista_grafo[i] != dados:
                if lista_grafo[i][2] == dados[2]:
                    if [f'{lista_grafo[i][0]} -> {lista_grafo[i][1]} = {lista_grafo[i][2]}'] not in lista_pares:
                        lista_pares.append([f'{lista_grafo[i][0]} -> {lista_grafo[i][1]} = {lista_grafo[i][2]}'])

    return lista_pares


print(pares(lista_simulacao))

# Questão 6 ===================================================================================


def maior_inte(lista_grafo):
    aux = lista_grafo[1]
    maior_conteudo = []
    maior = lista_grafo[0][2]
    maior_conteudo.append(lista_grafo[0])
    for dados in lista_grafo:
        if dados != aux:
            if dados[2] > maior:
                maior = dados[2]
                maior_conteudo = [dados]
            elif dados[2] == maior:
                maior_conteudo.append(dados)

    return maior_conteudo


print(maior_inte(lista_simulacao))

# Questão 7 ===================================================================================


def maior_grau(lista_grafo):
    lista_nomes = []
    lista_graus = []
    contador = 0
    for dados in lista_grafo:
        if dados[0] not in lista_nomes:
            lista_nomes.append(dados[0])
            for i in range(len(lista_grafo)):
                if dados != lista_grafo[i]:
                    if lista_grafo[i][0] == dados[0]:
                        contador += 1
                    if lista_grafo[i][1] == dados[0]:
                        contador += 1

            lista_graus.append([f'{dados[0]}', contador+1])
            contador = 0

    lista_graus = sorted(lista_graus, key=lambda x: x[1], reverse=True)

    return lista_graus[0]


print(maior_grau(lista_simulacao))

"""
Questão 8: Como podemos compreender uma rede social em que os graus dos vértices são valores bem próximos,
ou seja, por exemplo, todos os nós tem grau com diferença de no máximo 1? O que isso significa?

Resposta:
Uma rede social onde os graus dos vértices são valores próximos sugere uma distribuição equilibrada 
de conexões entre os membros, indicando uma comunidade coesa sem influenciadores dominantes. Isso 
promove uma propagação orgânica de informações e uma maior resiliência a falhas individuais, 
contribuindo para uma dinâmica mais estável e distribuída na rede.
"""

# Questão 9 ===================================================================================

print(nx.is_strongly_connected(G))

print(nx.number_strongly_connected_components(G))

print(list(nx.strongly_connected_components(G)))

H = nx.condensation(G)

print(H.nodes.data())

"""
Questão 10

A) Esta representação é uma lista de adjacências. Cada nó do grafo é representado por 
uma chave no dicionário, e os valores associados a essas chaves são conjuntos que 
representam os vizinhos (ou nós adjacentes) de cada nó.

B) O grafo é não direcionado. Isso porque os conjuntos de vizinhos para cada nó não fazem 
distinção entre entrada e saída, ou seja, se o nó A está na lista de vizinhos do nó B, 
então o nó B também está na lista de vizinhos do nó A.

C) O grafo é cíclico. Podemos ver isso observando que há pelo menos um caminho que forma um 
ciclo no grafo. Por exemplo, o caminho 0 -> 1 -> 3 -> 4 -> 0 forma um ciclo, onde o nó 0 
é alcançável a partir de si mesmo.

"""


