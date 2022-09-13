"""
Grafos são estruturas de dados não-lineares
Compreendendo um conjunto finiito de vértices e arestas.
Os vértices são os elementos, e as arestas são os pares
ordenados das conexões entre os vértices.
"""

__author__ = ["Caio Henriques Sica Lamas",
              "Franck Allyson da Silva Rocha"]
__date__ = "29/08/2022"
__credits__ = ["https://www.geeksforgeeks.org/introduction-to-graphs/?ref=lbp",
               "https://www.educba.com/graph-in-data-structure/?source=leftnav",
               "https://www.educba.com/types-of-graph-in-data-structure/"]
__license__ = "GPL"
__email__ = ["caio.lamas@ifnmg.edu.br",
             "fasr@aluno.ifnmg.edu.br"]

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
    def __init__(self, vertice_a, vertice_b, informacao=None, peso=None):
        self.aresta = (vertice_a, vertice_b)
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
        """Função para mostrar as etiquetas de vértices/arestas"""
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
        """Inserir um vértice caso ele ainda não exista."""
        try:
            self.busca_vertice(etiqueta)
        except ValueError:
            novo_vertice = Vertice(etiqueta, valor)
            self.vertices.append(novo_vertice)
        else:
            print(f'{FAIL}Já existe um vértice com a etiqueta dada.{ENDC}')

    def inserir_aresta(self, etiqueta_vertice1, etiqueta_vertice2):
        """Inserir uma aresta se os vértices existem e se a aresta ainda não existe."""
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
        """Remove o vértice e todas as referências de arestas nele presente."""
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
        """Remove as arestas, caso existam."""
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
        """ Une vértices, atribuindo as arestas do segundo ao primeiro."""
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
        """Busca um vértice ou retorna um ValueError caso não exista."""
        for vertice in self.vertices:
            if vertice.etiqueta == etiqueta_vertice:
                return vertice
        raise ValueError

    def busca_aresta(self, vertice1, vertice2):
        """Busca um vértice ou retorna um ValueError caso não exista."""
        for aresta in self.arestas:
            if (vertice1, vertice2) == aresta.aresta:
                return aresta
        raise ValueError
