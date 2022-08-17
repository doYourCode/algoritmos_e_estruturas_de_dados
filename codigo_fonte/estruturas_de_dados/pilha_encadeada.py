""" Exemplo de estrutura de pilha, usando encadeamento, e alguns algoritmos relacionados.

Esse tipo de implementação facilita a alocação dinâmica e "evita" o transbordamento de pilha,
porém requer mais operações de alocação e também mais memória. É util para quando desconhecemos o
tamanho potencial da pilha.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "17/08/2022"
__credits__ = ["https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm",
               "https://towardsdatascience.com/python-linked-lists-c3622205da81",
               "https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa um único nó de uma lista """

    def __init__(self, valor=None):
        self.valor = valor
        self.anterior = None


class PilhaEncadeada:
    """
    Representa uma pilha implementada sobre a plataforma de uma lista encadeada.
    """

    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    @property
    def valores(self):
        pass  # TODO

    def add_inicio(self, valor):
        pass  # TODO

    def add_final(self, valor):
        pass  # TODO

    def add_pos(self, pos_nodo, valor):
        pass  # TODO

    def remove(self, valor):
        pass  # TODO

    def busca(self, valor):
        pass  # TODO

    def __iter__(self):
        pass  # TODO

    def __len__(self):
        pass  # TODO


def pilha_encadeada():
    pass # TODO -> implementar os testes das operações
