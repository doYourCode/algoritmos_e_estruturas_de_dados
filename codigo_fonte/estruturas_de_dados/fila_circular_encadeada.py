'''Exemplo de de fila circular encadeada
Uma lista circular encadeada é uma série de elementos em que cada elemento
tem ponteiros para seu próximo elemento na série e o último elemento aponta
para o primeiro elemento.
'''

__author__ = "Franck Allyson da Silva Rocha"
__date__ = "24/10/2022"
__credits__ = ["https://pt.wiki-code.net/20517231-circular-linked-list-in-c",
               "https://prepinsta.com/cpp-program/circular-queue-using-linked-list/"]
__license__ = "GPL"
__email__ = "fasr@aluno.ifnmg.edu.br"

from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """Representa um nó de uma fila"""

    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None


class FilaCircularEncadeada:
    """Representa um fila cujos elementos (nós) estão encadeados por elos.
    A Fila circular itera apenas para o próximo elemento e o último elemento
    aponta para o primeiro.
    """

    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self._tamanho = 0

    @property
    def valores(self):
        """
        Valores presentes da fila

        :return: Conjunto de valores presentes em cada nó da fila
        """
        return [nodo.valor for nodo in self]

    def enfileirar(self, valor):
        """Função que adiciona um valor a fila"""
        novo_nodo = Nodo(valor)
        if self.vazia():
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
            self.ultimo.proximo = self.primeiro
            self._tamanho += 1
            return

        self.ultimo.proximo = novo_nodo
        self.ultimo = novo_nodo
        self.ultimo.proximo = self.primeiro
        self._tamanho += 1

    def desenfilerar(self):
        """
        Função que remove o primeiro valor da fila

        :return: Valor do nó removido
        """

        if self.vazia():
            print(FAIL + "ATENÇÃO!" + ENDC + " Fila Vazia! Exclusão não ocorreu.")
            return

        valor = self.primeiro.valor
        self.primeiro = self.primeiro.proximo
        self.ultimo.proximo = self.primeiro
        self._tamanho -= 1
        return valor

    def vazia(self):
        """
        Verifica se a fila está vazia ou não

        :return: True caso esteja vazia | False caso não esteja vazia.
        """
        if len(self) == 0:
            return True
        return False

    def primeiro_elemento(self):
        """
        Verificar primeiro elemento da fila

        :return: Valor do primeiro elemento da fila
        """
        return self.primeiro.valor

    def ultimo_elemento(self):
        """
        Verificar ultimo elemento da fila

        :return: Valor do último elemento da fila
        """
        return self.ultimo.valor

    def __iter__(self):
        """
        Define a forma que a fila será percorrida

        :return: Cada nó da fila
        """

        nodo_atual = self.primeiro
        for c in range(0, self._tamanho):
            yield nodo_atual
            nodo_atual = nodo_atual.proximo

    def __len__(self):
        """
        Função de tamanho da fila

        :return: Tamanho da fila
        """
        return self._tamanho


