"""
## Grafos (Estrutura não linear) ================================================================================

Vértices = Nós (Que seu significado dependerá da natureza do problema)
Arestas = São oque conectam os nós entre si, usando um critério predefindo

# Grafo G(V,A)

Conjunto V (vértices)
Conjunto A (Arestas)

Exemplo: V = {1, 2, 3, 4}    A = {{1,2}, {1,4}, {2,3}, {2,4}}

* Uma aresta pode ter ou não uma direção

Em um DIGRAFO, se uma aresta tem sentido A -> B, isso significa que podemos ir de A até B, mas no o contrário

* Grau

Grau indica o número de arestas que conectam um vértice do grafo a outros vértices, que chegam ou partem dele

No digrafo, existe o Grau de Entrada (nº de arestas que chegam ao vértice)
e o Grau de Saída (nº de arestas que partem do vértice)

* Laço

Uma aresta é chamada de laço se seu vértice de partida é o mesmo que o de chegada

* Caminho

Um caminho entre dois vértices é uma sequência de vértices onde cada
vértice está conectado ao vértice seguiente por meio de uma aresta

e o comprimento do caminho, é o número de vértices que precisamos percorrer de um vértice até outro

* Ciclo

Caminho onde o vértice incial e o final são o mesmo vértice.
(OBS: Não há vértices repetidos

## Tipos de Grafos ============================================================================

Trivial:
Possui um único vértice e nenhuma arsta

Simples:
Grafo não direcionado, sem laços e sem arstas paralelas

Completo:
Grafo simples onde cada vértice se conecta a todos os outros vértices do grafo

Regular:
Grafo onde todos os seus vértices possuem o mesmo grau
Todo grafo completo é também regular

Entre outros

## Tipos de representação =========================================================================

- Matriz de adjacência
    Utiliza uma matriz N x N para armazenar o grafo, onde N = nº de vértices

- Listade adjacência
    Uma aresta é representada por uma marca na posição (i, j) aresta liga o vértice i ao j

    Utiliza uma lista vértices para descrever as relações entre os vértices

    Um grafo contendo N vértices utiliza um array de ponteiros de tamanho N
    Para cada vértice é cirada uma lista de arestas, onde cada posição da lista,
    armazena o índice do vértice a qual aquele vértice se conecta

## Quando usar qual:

Lista de adjacência é mais indicada para um grafo
que possui muitos vértices mas poucas arestas ligando
esses vértices.

A medida que o número de arestas cresce e não
havendo nenhuma outra informação associada a aresta
(por exemplo, seu peso), o uso de uma matriz de
adjacência se torna mais eficiente

## Busca em grafos ===============================================================================

Consiste em explorar o grafo de uma maneira bem específica

* O ponto de partida é um aspecto bastante importante da própria busca

## Busca em largura

- Funcionamento

    Partindo de um vértice inicial, a busca explora todos os vizinhos de vértice. Em seguida, para
    cada vértice vizinho, ela repete, esse processo, visitando os vértices ainda inexplorados

    Em outras palavas, ela se inicia em um vértice e então visita todos os seu visinhos antes de se
    aprofundar na bsuca, esse processo continua até que:
        - o alvo da busca seja encontrado
        - não existam mais vértices inexplorados

    * Esse algoritmo faz uso do conceito de fila

    O grafo é percorrido de maneira sistemática, primeiro marcando como "visitado" todos os vizinhos
    de um vértice, e em seguida começa a visitar os vizinnhos de cada vértice na ordem em que eles
    forem marcados

    * Para realizar essa tarefa, uma fila é utilizada para administrar a visitação dos vértices
    * Ou seja, o primeiro vértice marcado, ou marcado a mais tempo, é o primeiro a ser visitado

    # Implementação

    def buscaLargura(self, ini):
        cont = 1
        IF = 0
        FF = 0
        visitado = [0 for i in range(self.__nro_vertices)]
        fila = [0 for i in range(self.__nro_vertices)]

        FF = FF + 1
        fila[FF] = ini
        visitado[ini] = cont

        while IF != FF:
            IF = (IF + 1) % self.__nro_vertices
            vert = fila[FF]
            cont = cont + 1
            grau = len(self.__arestas[vert])
            for i in range(grau):
                if visitado[gr.__arestas[vert][i]] == 0:
                    FF = (FF + 1) % self.__nro_vertices
                    fila[FF] = gr.__arestas[vert][i]
                    visitado[gr.__arestas[vert][i]] = cont

        return visitado

    # Complexidade
    Em um grafo G(V,A), o pior caso é:
        - Custo de inserção e remoção = constante
        - custo de enfileirar e remover todos os vértice uma vez 0(|V|)
        - Custo de utilizar todas as arestas |A|
        - Complexidade da busca no pior caso = O(|V| + |A|)

    # Aplicações
        - Achar todos vértices conectados a apenas um componente
        - Achar o menor caminho entre dois vértices
        - Testar se um grafo é bipartido
        - roteamento: encontrar o número minimo de hops(vértices intermediários no
         caminho correspondente à conexao) em uma rede
         - Encontrar o número mínimo de intermediários entre 2 pessoas


"""


class Grafo:
    def __init__(self):
        self.__arestas = {}

    def arestas(self):
        return self.__arestas

    def insereVertice(self, vertice):
        self.__arestas[vertice] = []

    def insereAresta(self, origem, destino):
        if origem not in self.__arestas:
            self.__arestas[origem] = [destino]
        else:
            if destino in self.__arestas[origem]:
                return False
            else:
                self.__arestas[origem].append(destino)
        return True

    def imprime(self):
        print("{")
        for (a, b) in self.__arestas.items():
            print(a, ":", b, end='\n')
        print("}")

    def __buscaProfundidade_Rec(self, ini, visitados):
        visitados.append(ini)
        vizinhos = self.__arestas[ini]
        for vi in vizinhos:
            if (vi not in visitados):
                self.__buscaProfundidade_Rec(vi, visitados)

    def buscaProfundidade(self, ini):
        visitados = []
        self.__buscaProfundidade_Rec(ini, visitados)
        return visitados