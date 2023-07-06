""" Exemplo de estrutura de pilha, usando encadeamento, e alguns algoritmos relacionados.

Esse tipo de implementação de pilha funcionará como as demais pilhas, porém objetiva facilitar a alocação
dinâmica de novos elementos e "evitar" o transbordamento de pilha, porém requer mais operações de alocação
e também mais memória. É util para quando desconhecemos o tamanho potencial da pilha.
"""
__author__ = ["Franck Allyson da Silva Rocha",
              "Caio Henriques Sica Lamas"]
__date__ = "17/08/2022"
__credits__ = ["https://www.ime.usp.br/~rt/mac57102012/RT555pilhalink555.pdf",
               "https://www.ufsm.br/pet/sistemas-de-informacao/2020/04/01/entendendo-listas-pilhas-e-filas/",
               "https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/"]
__license__ = "GPL"
__email__ = ["fasr@aluno.ifnmg.edu.br",
             "caio.lamas@ifnmg.edu,br"]


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
        self.topo = None
        self._tamanho = 0

    @property
    def valores(self):
        '''
        Conjunto de nós

        :return: lista com o valor que cada nó da pilha
        '''
        return [nodo.dados for nodo in self]

    def adicionar(self, valor):
        '''
        Adiciona um novo nó ao topo da pilha

        :param valor: Informação a ser armazenada
        '''
        novo_nodo_topo = Nodo(valor)
        novo_nodo_topo.anterior = self.topo
        self.topo = novo_nodo_topo
        self._tamanho += 1
      
    def ler_topo(self):
        '''
        Lê o valor do topo da pilha

        :return: Valor do nó do topo da pilha
        '''
        nodo_topo = self.topo
        return nodo_topo.dados

    def remover(self):
        '''
        Remove o elemento do topo da pilha

        :return: Valor do nó removido ou nada, caso não tenha nenhum nó.
        '''
        if self.topo is None:
            print(f"{FAIL}Não há nenhum elemento na pilha!{ENDC}")
            return

        nodo_topo = self.topo
        valor = nodo_topo.dados
        self.topo = nodo_topo.anterior
        self._tamanho -= 1

        return valor

    def __iter__(self):
        '''
        Prototype de iteração

        :return: Cada nó presente na pilha
        '''
        nodo_topo = self.topo
        while nodo_topo:
            yield nodo_topo
            nodo_topo = nodo_topo.anterior

    def __len__(self):
        '''
        Prototype da função len

        :return: Tamanho da pilha
        '''
        return self._tamanho
