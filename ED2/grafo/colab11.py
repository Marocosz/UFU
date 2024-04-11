import networkx as nx  # biblioteca para a construção de grafo
import matplotlib.pyplot as plt  # biblioteca gráfica
import random  # biblioteca para geração de números aleatórios

G = nx.Graph()  # criação de grafo não direcionado
p = 0.3
pessoas = {"Alice", "Joao", "Carlos", "Denise", "Eva", "Marcos", "Flávia", "Artur",
           "Simão", "Pedro", "Ana", "Murilo", "Julia", "Vinicius", "Clara", "Marcelo"}

mapa_de_cores = []

for p1 in pessoas:
    G.add_node(p1)
    for p2 in pessoas:
        if p1 > p2:
            cara_coroa = random.uniform(0, 1)
            if cara_coroa <= p:
                G.add_edge(p1, p2)

for no_pessoa in G.nodes():
    if G.degree(no_pessoa) >= 6:
        mapa_de_cores.append("red")
    elif G.degree(no_pessoa) >= 3:
        mapa_de_cores.append("orange")
    else:
        mapa_de_cores.append("yellow")

nx.draw(G, node_color=mapa_de_cores, with_labels=True, node_size=1500)
plt.show()

cg = nx.circular_layout(G)
nx.draw(G, pos=cg, node_color=mapa_de_cores, with_labels=True, node_size=1500)
plt.show()

# Tarefa 1 =======================================================================
G.add_edge("Ana", "Joao")
G.remove_edge("Ana", "Joao")

nx.draw(G, node_color=mapa_de_cores, with_labels=True, node_size=1500)
plt.show()

# Tarefa 2 =======================================================================
print(list(G.nodes))

# Tarefa 3 =======================================================================
print(list(G.edges))

# Tarefa 4 =======================================================================
print(list(G.neighbors("Ana")))

# Tarefa 5 =======================================================================
# exemplo de como encontrar o grau de um determinado vértice
G.degree("Alice")
graus = []

for a in list(G.nodes):
    graus.append((G.degree(a), a))

print(sorted(graus, reverse=True))

# Tarefa 6 =======================================================================
list(nx.bfs_edges(G, source="Pedro"))

# Tarefa 7 =======================================================================
list(nx.dfs_edges(G, source="Marcelo"))

# Tarefa 8 =======================================================================
nx.shortest_path(G, "Pedro")
nx.shortest_path_length(G, "Pedro")

# Tarefa 9 =======================================================================
nx.descendants_at_distance(G, "Julia", 3)

# Tarefa 10 =======================================================================
nx.is_connected(G)

nx.number_connected_components(G)

[len(c) for c in sorted(nx.connected_components(G), key=len, reverse=True)]

S = [G.subgraph(c).copy() for c in nx.connected_components(G)]
for a in S:
    print(a)

# Tarefa 11 =======================================================================
CC = nx.clustering(G)
for node in CC:
    print(node, "\t", CC[node])

nx.draw(G, pos=cg, with_labels=True, font_weight='bold')
plt.show()