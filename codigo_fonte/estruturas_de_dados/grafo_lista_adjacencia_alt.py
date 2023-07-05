

class Nodo:

    def __init__(self, nome: str, valor=None):
        self.nome = nome
        self.valor = valor
        self.arestas = list()

    def __repr__(self):
        return f"nome:{self.nome} valor:{self.valor} arestas:{self.arestas}\n"


class Aresta:

    def __init__(self, outro: Nodo, custo: int):
        self.outro = outro
        self.custo = custo

    def __repr__(self):
        return f"outro:{self.outro.nome} custo:{self.custo}"


class GrafoListaAdjacenciaAlt:

    def __init__(self):
        self.nodos = dict()

    def adicionar_nodo(self, nome: str, valor=None):
        n = Nodo(nome, valor)
        self.nodos.update({nome: n})

    def adicionar_aresta(self, nome: str, outro: str, custo: int, directional: bool = False):

        if not directional:
            self.nodos[outro].arestas.append(Aresta(self.nodos[nome], custo))

        self.nodos[nome].arestas.append(Aresta(self.nodos[outro], custo))

    def imprimir_grafo(self):
        print(self.nodos)
