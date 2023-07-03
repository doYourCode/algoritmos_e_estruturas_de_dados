"""
Grafos são estruturas de dados não-lineares, compreendendo um conjunto finito de vértices e arestas.
Essa implementação utiliza um array bidimensional para guardar pesos e relações de vizinhança entre os nós.
Aviso: Implementação de um grafo direcionado.
"""
__author__ = 'Caio Henriques Sica Lamas'
__date__ = '29/06/2023'
__credits__ = ''
__license__ = 'GPL'
__email__ = 'caio.lamas@ifnmg.edu.br'

import json
from codigo_fonte.utilidades.utilidades import *


class GrafoMatrizAdjacencia(object):

    # Initialize the matrix
    def __init__(self, tamanho):
        self.matriz_adjacencia = []
        for i in range(tamanho):
            self.matriz_adjacencia.append([0 for i in range(tamanho)])
        self.tamanho = tamanho

    # Add edges
    def adicionar_aresta(self, v1, v2):
        if v1 == v2:
            print("Os vértices %d e %d não podem ser identicos" % (v1, v2))
        self.matriz_adjacencia[v1][v2] = 1
        self.matriz_adjacencia[v2][v1] = 1

    # Remove edges
    def remover_aresta(self, v1, v2):
        if self.matriz_adjacencia[v1][v2] == 0:
            print("Não há arestas entre os vértices %d e %d" % (v1, v2))
            return
        self.matriz_adjacencia[v1][v2] = 0
        self.matriz_adjacencia[v2][v1] = 0

    def __len__(self):
        return self.tamanho

    # Print the matrix
    def imprimir_matriz(self):
        for row in self.matriz_adjacencia:
            for val in row:
                print('{:4}'.format(val)),
