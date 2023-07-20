from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *
from exemplos.plotagem.pintor_grafo_adj import Pintor


class BuscaEmLargura:

    def __init__(self, grafo: GrafoListaAdjacenciaAlt, pintor: Pintor, origem: str):
        self.grafo = grafo
        self.pintor = pintor
        self.fila = []
        self.lista_nos_lidos = set()

        self.fila.append(self.grafo.nodos[origem])

        self.contador = 0

    def atualiza(self, tempo):
        if self.fila and self.contador % tempo == 0:
            n = self.fila.pop(0)
            self.lista_nos_lidos.add(n.nome)
            self.pintor.ler_nodo(n.nome)

            for a in n.arestas:
                outro = self.grafo.nodos[a.outro.nome]
                if outro.nome not in self.lista_nos_lidos:
                    self.fila.append(outro)
                    self.pintor.preparar_aresta(a.origem.nome, outro.nome)
                #self.pintor.ler_aresta(n.nome, self.fila[0].nome)
        self.contador += 1
