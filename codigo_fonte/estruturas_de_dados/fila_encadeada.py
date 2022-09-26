""" Exemplo de estrutura de FILA, usando encadeamento, e alguns algoritmos relacionados.

Esse tipo de implementação de Fila funcionará como as demais filas, porém objetiva facilitar a alocação
dinâmica de novos elementos, porém requer mais operações de alocação e também mais memória. É util para
quando desconhecemos o tamanho potencial da fila.
"""
__author__ = ["Franck Allyson da Silva Rocha",
              "Caio Henriques Sica Lamas"]
__date__ = "20/08/2022"
__credits__ = ["http://www.ic.uff.br/~cbraga/ed/apostila/ed12-filas.pdf",
               "https://www.geeksforgeeks.org/queue-data-structure/"]
__license__ = "GPL"
__email__ = ["fasr@aluno.ifnmg.edu.br",
             "caio.lamas@ifnmg.edu,br"]

from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa o único No de uma Lista """

    def __init__(self, valor):
        '''
        Construtor

        :param valor: Dado a ser armazenado
        '''
        self.valor = valor
        self.proximo = None


class FilaEncadeada:
    """ Representa uma Fila implementada sobre a plataforma de uma lista encadeada """

    def __init__(self):
        self.inicio = None
        self.final = None
        self._tamanho = 0

    @property
    def valores(self):
        '''
        Conjunto de nós

        :return: Lista com o valor de cada nó
        '''
        return [nodo.valor for nodo in self]

    def adicionar(self, valor):
        '''
        Adiciona um novo nó ao fim da lista

        :param valor: Informação que será armazenada
        '''
        novo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            self.final.proximo = novo_nodo
        self.final = novo_nodo
        self._tamanho += 1

    def ler_inicio(self):
        '''
        Retorna o valor do inicio da fila

        :return:Valor do nó que está no inicio da fila
        '''
        nodo_inicio = self.inicio
        return nodo_inicio.valor

    def ler_final(self):
        '''
        Retorna o valor do final da fila

        :return: Valor do nó que está no fim da fila
        '''
        nodo_final = self.final
        return nodo_final.valor

    def remover(self):
        '''
        Remove o elemento do inicio da Fila

        :return: Valor que foi removido
        '''
        if self.inicio is None:
            print(f"{FAIL} Não há nenhum elemento na fila, nenhuma operação foi realizada!{ENDC}")
            return

        nodo_inicio = self.inicio
        valor = nodo_inicio.valor
        self.inicio = nodo_inicio.proximo
        self._tamanho -= 1
        return valor

    def __iter__(self):
        '''
        Prototype de iteração, definimos o que será percorrido na iteração sobre a classe

        :return: Cada nó que está sendo iterado
        '''
        nodo_inicio = self.inicio
        while nodo_inicio:
            yield nodo_inicio
            nodo_inicio = nodo_inicio.proximo

    def __len__(self):
        '''
        Prototype da função len, aqui definimos o que será mostrado ao pedirmos o tamanho da estrturua

        :return: Tamanho da fila
        '''
        return self._tamanho
