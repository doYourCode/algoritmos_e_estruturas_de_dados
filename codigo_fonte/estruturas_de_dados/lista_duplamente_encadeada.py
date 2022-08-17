""" Exemplo de estrutura de lista duplamente encadeada e alguns algoritmos relacionados

Uma lista duplamente encadeada se comportará como uma lista, com a exceção de que poderá ser transcorrida
em dois sentidos, pois, em seus nodos, guarda referências para os próximos elementos, assim como os anteriores.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "16/08/2022"
__credits__ = ["https://www.tutorialspoint.com/python_data_structure/python_advanced_linked_list.htm",
               "https://www.geeksforgeeks.org/doubly-linked-list/",
               "https://www.programiz.com/dsa/doubly-linked-list"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa um único nó de uma lista """

    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class ListaEncadeada:
    """
    Representa uma lista cujos elementos (nós) estão encadeados por elos.
    A lista encadeada simples só pode ser iterada em um único sentido (para frente).
    """

    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    @property
    def valores(self):
        """ Conjunto dos nós. """
        return [nodo.valor for nodo in self]

    def add_inicio(self, valor):
        """ Adiciona um novo nó no início da lista. """
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = self.cabeca
        if self.cabeca is not None:
            self.cabeca.anterior = novo_nodo
        self.cabeca = novo_nodo
        self._tamanho += 1

    def add_final(self, valor):
        """ Adiciona um novo nó ao final da lista. """
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = None
        if self.cabeca is None:
            novo_nodo.anterior = None
            self.cabeca = novo_nodo
            self._tamanho += 1
            return
        ultimo = self.cabeca
        while ultimo.proximo is not None:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_nodo
        novo_nodo.anterior = ultimo
        self._tamanho += 1

    def add_pos(self, pos_nodo_n, valor):
        """ Adiciona um novo nó em uma posição posterior à outro nó específico. """
        pos_nodo = self.busca(pos_nodo_n)
        if pos_nodo is None:
            self._tamanho += 1
            return
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = pos_nodo.proximo
        pos_nodo.proximo = novo_nodo
        novo_nodo.anterior = pos_nodo
        if novo_nodo.proximo is not None:
            novo_nodo.proximo.anterior = novo_nodo
        self._tamanho += 1

    def busca(self, valor):
        """ Busca um nó especificado. """
        for nodo in self:
            if nodo.valor == valor:
                return nodo
        return None

    def __iter__(self):
        nodo_atual = self.cabeca
        while nodo_atual:
            yield nodo_atual
            nodo_atual = nodo_atual.proximo

    def __len__(self):
        return self._tamanho


def lista_duplamente_encadeada():
    lista = ListaEncadeada()  # ........................Instancia uma nova lista (em branco)
    # Testando inserção
    lista.add_inicio("Segunda")  # .....................Insere um primeiro elemento
    lista.add_final("Quarta")  # ........................Insere 2 elementos ao final da lista
    lista.add_final("Sexta")
    lista.add_pos("Segunda", "Terça")
    lista.add_pos("Quarta", "Quinta")
    print(HEADER + "Teste nº 1 (Inserções): " + ENDC)
    print(str(lista.valores) + OKBLUE + " Tamanho da lista: " + str(len(lista)) + ENDC)
