"""
Grafos são estruturas de dados não-lineares
Compreendendo um conjunto finiito de vértices e arestas.
Os vértices são os elementos, e as arestas são os pares
ordenados das conexões entre os vértices.
"""

from codigo_fonte.utilidades.utilidades import *


class Vertice:
    """ Representa um vértice do grafo """
    def __init__(self, etiqueta, informacao=None):
        self.etiqueta = etiqueta
        self.informacao = informacao
        self._grau = 0
        self.arestas_pertencentes = []

    def __str__(self):
        return f'{self.etiqueta}'


class Aresta:
    """ Representa uma aresta do grafo """
    def __init__(self, verticeA, verticeB, informacao=None, peso=None):
        self.aresta = (verticeA, verticeB)
        self.informacao = informacao
        self.peso = peso

    def __str__(self):
        return f'({self.aresta[0].etiqueta},{self.aresta[1].etiqueta})'


class Grafo:
    """ Representa o grafo e as operações que recaem sobre ele """
    def __init__(self):
        self.vertices = []
        self.arestas = []

    def etiquetas(self, lista):
        return [str(valor) for valor in lista]

    def checar_vertices(self):
        if len(self.vertices) > 0:
            return True
        return False

    def checar_arestas(self):
        if len(self.arestas) > 0:
            return True
        return False

    def inserir_vertice(self, etiqueta, valor):
        try:
            self.busca_vertice(etiqueta)
        except ValueError:
            novo_vertice = Vertice(etiqueta, valor)
            self.vertices.append(novo_vertice)
        else:
            print(f'{FAIL}Já existe um vértice com a etiqueta dada.{ENDC}')

    def inserir_aresta(self, etiqueta_vertice1, etiqueta_vertice2):
        try:
            vertice1 = self.busca_vertice(etiqueta_vertice1)
            vertice2 = self.busca_vertice(etiqueta_vertice2)
        except ValueError:
            print(f'{FAIL}O Grafo não possui um ou ambos os vértices com a etiqueta dada.{ENDC}')
        else:
            try:
                self.busca_aresta(vertice1, vertice2)
            except ValueError:
                nova_aresta = Aresta(vertice1, vertice2)
                vertice1.arestas_pertencentes.append(nova_aresta)
                vertice2.arestas_pertencentes.append(nova_aresta)

                self.arestas.append(nova_aresta)
            else:
                print(f'{FAIL}Já existe uma aresta com os vértices dados.{ENDC}')

    def remover_vertice(self, etiqueta_vertice):
        try:
            vertice_encontrado = self.busca_vertice(etiqueta_vertice)
            self.vertices.remove(vertice_encontrado)
        except ValueError:
            print('\noi\n')
            print(f'{FAIL}O Grafo não possui o vértice \'{etiqueta_vertice}\'{ENDC}')
        else:
            for aresta in vertice_encontrado.arestas_pertencentes:

                if vertice_encontrado == aresta.aresta[0]:
                    aresta.aresta[1].arestas_pertencentes.remove(aresta)
                else:
                    aresta.aresta[0].arestas_pertencentes.remove(aresta)

                self.arestas.remove(aresta)
                print(f'{WARNING}O vértice deletado estava na aresta {aresta}. Logo, ela foi excluída!{ENDC}')
            vertice_encontrado.arestas_pertencentes.clear()

    def remover_aresta(self, etiqueta_vertice1, etiqueta_vertice2):
        try:
            vertice1 = self.busca_vertice(etiqueta_vertice1)
            vertice2 = self.busca_vertice(etiqueta_vertice2)
        except ValueError:
            print(f'{FAIL}O Grafo não possui um ou ambos os vértices com a etiqueta dada.{ENDC}')
        else:
            try:
                aresta_encontrada = self.busca_aresta(vertice1, vertice2)
            except ValueError:
                print(f'{FAIL}O Grafo não possui a aresta fornecida.{ENDC}')
            else:
                self.arestas.remove(aresta_encontrada)
                vertice1.arestas_pertencentes.remove(aresta_encontrada)
                vertice2.arestas_pertencentes.remove(aresta_encontrada)

    def unir_vertices(self, etiqueta_vertice1, etiqueta_vertice2):
        try:
            vertice1 = self.busca_vertice(etiqueta_vertice1)
            vertice2 = self.busca_vertice(etiqueta_vertice2)
        except ValueError:
            print(f'{FAIL}O Grafo não possui um ou ambos os vértices com a etiqueta dada.{ENDC}')
        else:
            for aresta in vertice2.arestas_pertencentes:

                self.arestas.remove(aresta)

                aresta.aresta = (vertice1, aresta.aresta[1])

                if aresta not in vertice1.arestas_pertencentes:
                    vertice1.arestas_pertencentes.append(aresta)
                    self.arestas.append(aresta)

            vertice2.arestas_pertencentes.clear()
            self.vertices.remove(vertice2)

    def ler_vertice(self, etiqueta_vertice):
        try:
            return self.busca_vertice(etiqueta_vertice).informacao
        except ValueError:
            print(f'{FAIL}O Grafo não possui o vértice \'{etiqueta_vertice}\'{ENDC}')

    def ler_aresta(self, etiqueta_vertice1, etiqueta_vertice2):
        try:
            return self.busca_aresta(etiqueta_vertice1, etiqueta_vertice2).informacao
        except ValueError:
            print(f'{FAIL}O grafo não possui a aresta com os vertices fornecidos!{ENDC}')

    def busca_vertice(self, etiqueta_vertice):
        for vertice in self.vertices:
            if vertice.etiqueta == etiqueta_vertice:
                return vertice
        raise ValueError

    def busca_aresta(self, vertice1, vertice2):
        for aresta in self.arestas:
            if (vertice1, vertice2) == aresta.aresta:
                return aresta
        raise ValueError


def grafo():
    grafo_teste = Grafo()

    # Teste de inserção de vértices

    grafo_teste.inserir_vertice('a', 2)
    grafo_teste.inserir_vertice('b', 7)
    grafo_teste.inserir_vertice('c', 3)
    grafo_teste.inserir_vertice('d', 10)

    print(f'{HEADER} Teste Nº 1 (Inserções vértices): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: {str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: {str(len(grafo_teste.arestas))}{ENDC}\n')
    # Teste de inserção de arestas
    grafo_teste.inserir_aresta('a', 'c')
    grafo_teste.inserir_aresta('a', 'd')
    grafo_teste.inserir_aresta('b', 'd')

    print(f'{HEADER} Teste Nº 2 (Inserções arestas): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: {str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: {str(len(grafo_teste.arestas))}{ENDC}\n')

    # Teste de exclusão de vértices
    print(f'{HEADER} Teste Nº 3 (Remoções vértices): {ENDC}')
    grafo_teste.remover_vertice('a')
    grafo_teste.remover_vertice('b')

    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: {str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: {str(len(grafo_teste.arestas))}{ENDC}\n')

    # Teste de exclusão de arestas
    # Inserindo todos os dados novamente para executar as exclusões:
    grafo_teste.inserir_vertice('a', 2)
    grafo_teste.inserir_vertice('b', 7)
    grafo_teste.inserir_aresta('a', 'c')
    grafo_teste.inserir_aresta('a', 'd')
    grafo_teste.inserir_aresta('b', 'd')

    # Exclusões:
    grafo_teste.remover_aresta('a', 'd')
    grafo_teste.remover_aresta('b', 'd')

    print(f'{HEADER} Teste Nº 4 (Remoções arestas): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: {str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: {str(len(grafo_teste.arestas))}{ENDC}\n')

    # Teste de União de Vértices
    grafo_teste.inserir_aresta('c', 'd')
    grafo_teste.inserir_aresta('a', 'b')

    grafo_teste.unir_vertices('a', 'c')
    print(f'{HEADER} Teste Nº 5 (União vertice): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: {str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: {str(len(grafo_teste.arestas))}{ENDC}\n')

# https://www.educba.com/graph-in-data-structure/?source=leftnav
# https://www.educba.com/types-of-graph-in-data-structure/
