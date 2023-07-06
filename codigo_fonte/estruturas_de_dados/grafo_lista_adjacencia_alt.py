import math


class Nodo:

    def __init__(self, nome: str, dados: dict = None):
        self.nome = nome
        self.dados = dados
        self.arestas = list()


class Aresta:

    def __init__(self, origem: Nodo, outro: Nodo, custo: int):

        self.origem = origem
        self.outro = outro
        self.custo = custo
        self.distancia = math.sqrt(pow((origem.dados["x"] - outro.dados["x"]), 2) + pow((origem.dados["x"] - outro.dados["x"]), 2))


class GrafoListaAdjacenciaAlt:

    def __init__(self):
        self.nodos = dict()

    def adicionar_nodo(self, nome: str, dados: dict = None):
        n = Nodo(nome, dados)
        self.nodos.update({nome: n})

    def adicionar_aresta(self, nome: str, outro: str, custo: int, directional: bool = False):
        if not directional:
            self.nodos[outro].arestas.append(Aresta(self.nodos[outro], self.nodos[nome], custo))

        self.nodos[nome].arestas.append(Aresta(self.nodos[nome], self.nodos[outro], custo))
