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