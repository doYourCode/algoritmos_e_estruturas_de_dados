""" Exemplo de estrutura de pilha, usando encadeamento, e alguns algoritmos relacionados.

Esse tipo de implementação de pilha funcionará como as demais pilhas, porém objetiva facilitar a alocação
dinâmica de novos elementos e "evitar" o transbordamento de pilha, porém requer mais operações de alocação
e também mais memória. É util para quando desconhecemos o tamanho potencial da pilha.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "17/08/2022"
__credits__ = ["https://www.ime.usp.br/~rt/mac57102012/RT555pilhalink555.pdf",
               "https://www.ufsm.br/pet/sistemas-de-informacao/2020/04/01/entendendo-listas-pilhas-e-filas/",
               "https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/"]
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

    def add_topo(self, valor):
        pass  # TODO
      
    def peek(self):
        pass

    def remove(self):
        pass  # TODO

    def __iter__(self):
        pass  # TODO

    def __len__(self):
        pass  # TODO


def pilha_encadeada():
    pass  # TODO -> implementar os testes das operações
