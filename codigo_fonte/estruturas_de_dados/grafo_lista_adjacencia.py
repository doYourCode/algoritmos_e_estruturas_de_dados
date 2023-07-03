"""
Grafos são estruturas de dados não-lineares
Compreendendo um conjunto finito de vértices e arestas.
Essa implementação utiliza um dicionário, em que a chave é um vértice
e o valor é o conjunto de vértices que estão ligado à chave.
Aviso: Implementação de um grafo NÃO ORIENTADO
"""
__author__ = 'Franck ALlyson da Silva Rocha'
__date__ = '10/11/2022'
__credits__ = ''
__license__ = 'GPL'
__email__ = 'fasr@aluno.ifnmg.edu.br'

from codigo_fonte.utilidades.utilidades import *


class GrafoListaAdjacencia:
    """Representa o Grafo"""
    def __init__(self):
        self.lista_adjacencias = dict()

    def verifica_vertice(self):
        """
        Verifica se há vértices no grafo

        :returns: True: Há || False: Não há
        """
        if len(self.lista_adjacencias) <= 0:
            print(f'{WARNING}Não há vertices!{ENDC}')
            return False
        print(f'{OKBLUE}Há vertices!{ENDC}')
        return True

    def verifica_arestas(self):
        """
        Verifica se há arestas no grafo

        :return: True: Há || False: Não há
        """
        for lista in self.lista_adjacencias.values():
            if len(lista) > 0:
                print(f'{OKBLUE}Há arestas!{ENDC}')
                return True
        print(f'{WARNING}Não há arestas!{ENDC}')
        return False

    def inserir_vertice(self, valor):
        """
        Insere um vértice no grafo

        :param valor: Valor do vértice á ser inserido
        :return: True: Valor foi inserido || False: Valor não foi inserido
        """
        if valor is None:
            print(f'{FAIL}ERRO! Vértice não foi inserido!{ENDC}')
            return False
        self.lista_adjacencias.update({valor: list()})
        print(f'{OKGREEN}Vértice {valor} inserido!{ENDC}')
        return True

    def remover_vertice(self, valor):
        """
        Remove um vértice pertencente ao Grafo

        :param valor: Valor do vértice a ser removido
        :return: True: Vértice removido || False: Vértice não removido
        """
        vertice = self.le_vertice(valor)
        if not vertice:
            print(f'{FAIL}Vértice indicado não existe!{ENDC}')
            return False

        for k, v in self.lista_adjacencias.items():
            if vertice[0] in v:
                v.remove(vertice[0])
            for adjacencia in vertice[1]:
                if k == adjacencia:
                    vertice[1].remove(k)

        self.lista_adjacencias.pop(vertice[0])
        print(f'{OKGREEN}Vértice [{vertice[0]}] removido!{ENDC}')
        return True

    def inserir_aresta(self, valor_vertice1, valor_vertice2):
        """
        Insere uma aresta no grafo

        :param valor_vertice1: Valor do vértice inicial da aresta
        :param valor_vertice2: Valor do vértice final da aresta
        :return: True: Aresta inserida || False: Aresta não inserida
        """
        vertice1 = self.le_vertice(valor_vertice1)
        vertice2 = self.le_vertice(valor_vertice2)
        if not vertice1 or not vertice2:
            print(f'{FAIL}Um dos vertices indicados não existe!{ENDC}')
            return False
        vertice1[1].append(valor_vertice2)
        vertice2[1].append(valor_vertice1)
        print(f'{OKGREEN}Aresta {vertice1[0], vertice2[0]} inserida!{ENDC}')
        return True

    def remover_aresta(self, valor_vertice1, valor_vertice2):
        """
        Remove uma aresta pertencente ao grafo

        :param valor_vertice1: Valor do vértice inicial da aresta
        :param valor_vertice2: Valor do vértice final da aresta
        :return: True: Aresta removida || False: Aresta não removida
        """
        vertice1 = self.le_vertice(valor_vertice1)
        vertice2 = self.le_vertice(valor_vertice2)

        if vertice1[0] not in vertice2[1] or vertice2[0] not in vertice1[1]:
            print(f'{FAIL}Aresta indicada não existe!{ENDC}')
            return False

        vertice1[1].remove(vertice2[0])
        vertice2[1].remove(vertice1[0])

        print(f'{OKGREEN}Aresta ({vertice1[0], vertice2[0]}) Removida!{ENDC}')
        return True

    def unir_vertices(self, valor_vertice1, valor_vertice2):
        """
        Une dois vértices, caso existam.

        :param valor_vertice1: Valor do primeiro vértice
        :param valor_vertice2: Valor do segunda vértice
        :return: True: União ocorreu || False: União não ocorreu
        """
        vertice1 = self.le_vertice(valor_vertice1)
        vertice2 = self.le_vertice(valor_vertice2)
        if not vertice1 or not vertice2:
            print(f'{FAIL}Algum dos vértices fornecidos não existe!{ENDC}')
            return False

        self.lista_adjacencias.pop(vertice2[0])
        for vertice, adjacencias in self.lista_adjacencias.items():
            # print(vertice)
            # print(adjacencias)

            if vertice == vertice1[0]:
                for valor in vertice2[1]:
                    if valor not in vertice1[1]:
                        vertice1[1].append(valor)
            if vertice2[0] in adjacencias:
                adjacencias.remove(vertice2[0])
                if vertice1[0] not in adjacencias:
                    adjacencias.append(vertice1[0])

        print(f'{OKGREEN}Vértices {valor_vertice1} e {valor_vertice2} foram unidos!{ENDC}')

    def dividir_vertices(self, valor_vertice1, valor_vertice2):
        """
        Divide dois vértices pertencentes ao grafo, caso haja aresta entre eles.

        :param valor_vertice1: Valor do primeiro vértice
        :param valor_vertice2: Valor do segundo vértice
        :return: True: Divisão ocorreu || False: Divisão não ocorreu
        """
        vertice1 = self.le_vertice(valor_vertice1)
        vertice2 = self.le_vertice(valor_vertice2)
        if vertice1[0] not in vertice2[1] or vertice2[0] not in vertice1[1]:
            print(f'{FAIL}Aresta não existe, não há como dividir!{ENDC}')
            return False

        vertice1[1].remove(vertice2[0])
        vertice2[1].remove(vertice1[0])
        print(f'{OKGREEN}Vertices divididos.{ENDC}')
        return True

    def le_vertice(self, valor):
        """
        Lê o valor de um vértice pertencente ao grafo

        :param valor: Valor do vértice
        :return: Conjunto (valor, lista_adjacencias) || None
        """
        chave_valor = (valor, self.lista_adjacencias.get(valor))
        if chave_valor[1] is None:
            print(f'{FAIL}Vértice solicitado não existe!{ENDC}')
            return None

        return chave_valor

    def __str__(self):
        """
        Forma como o grafo será mostrado ao usar o comando print na instância

        :return: String da lista de adjacências
        """
        return str(self.lista_adjacencias)

    def __len__(self):
        """
        O que será mostrado ao usar o comando len na instância da classe

        :return: Quantidade de vértices do grafo
        """
        return len(self.lista_adjacencias)
