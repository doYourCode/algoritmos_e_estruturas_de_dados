"""
A fila duplamente encadeada é basicamente como uma fila,
 exceto que você pode adicionar ou remover de qualquer lado.
"""
__author__ = ["Franck Allyson da Silva Rocha"]
__date__ = "20/08/2022"
__credits__ = ["https://the-algorithms.com/algorithm/linked-deque",
               "https://1library.org/article/filas-duplas-encadeadas-estruturas-de-dados-nodrm-pdf.y93p5kly"]
__license__ = "GPL"
__email__ = ["fasr@aluno.ifnmg.edu.br"]


from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """Representa um único nó de uma lista"""
    def __init__(self, valor):
        """
        Construtor

        :param valor: Representa o valor que será armazenado no nó
        """
        self.valor = valor
        self.proximo = None
        self.anterior = None


class FilaDuplaEncadeada:
    """Representa a estrutura da fila dupla encadeada e as operações que podem ser feitas sobre ela"""

    def __init__(self):
        """Construtor da estrutura de dados"""
        self._inicio = None
        self._final = None
        self._tamanho = 0

    def valores(self, reverso=False):
        """
        Mostra os valores contidos na fila

        :param reverso: True: Do Fim para o Início  | False: Do Início para o Fim
        :return: Lista com o valores de cada nó da fila
        """
        if reverso:
            return [nodo.valor for nodo in reversed(self)]
        else:
            return [nodo.valor for nodo in self]

    def enfileirar(self, valor):
        """
        Função que adiciona um valor no fim da fila

        :param valor: Valor a ser adicionado
        :return:
        """
        novo_nodo = Nodo(valor)

        if self.vazia():
            self._inicio = novo_nodo
            self._final = novo_nodo
            self._tamanho += 1
            return

        novo_nodo.anterior = self._final
        self._final.proximo = novo_nodo
        self._final = novo_nodo
        self._tamanho += 1

    def enfileirar_inicio(self, valor):
        """
        Adiciona um valor no inicio da fila ( Dupla Encadeada )

        :param valor: Valor a ser adicionado
        :return:
        """
        novo_nodo = Nodo(valor)

        if self.vazia():
            self._inicio = novo_nodo
            self._final = novo_nodo
            self._tamanho += 1
            return

        novo_nodo.proximo = self._inicio
        self._inicio.anterior = novo_nodo
        self._inicio = novo_nodo
        self._tamanho += 1

    def desenfileirar(self):
        """
        Remove um valor do início da fila

        :return: Valor do nó que foi removido
        """
        if self.vazia():
            print(FAIL + "ATENÇÃO!" + ENDC + " Fila Vazia! Exclusão não ocorreu.")
            return

        valor_removido = self._inicio.valor
        self._inicio.anterior = None
        self._inicio = self._inicio.proximo
        self._tamanho -= 1
        return valor_removido

    def desenfileirar_final(self):
        """
        Remove um valor do final da fila ( Dupla Encadeada )

        :return: Valor do nó que foi removido
        """
        if self.vazia():
            print(FAIL + "ATENÇÃO!" + ENDC + " Fila Vazia! Exclusão não ocorreu.")
            return

        valor_removido = self._final.valor
        self._final = self._final.anterior
        self._final.proximo = None
        self._tamanho -= 1
        return valor_removido

    def ler_inicio(self):
        """
        Verifica o elemento do início da fila sem remover

        :return: Valor do nó do início da fila
        """
        return self._inicio.valor

    def ler_final(self):
        """
        Verifica o elemetnod o final da fila sem remover

        :return: Valor do nó do final da fila
        """
        return self._final.valor

    def vazia(self):
        """
        Verifica se a fila está vazia ou não

        :return: True: Está Vazia | False: Não está vazia
        """
        if len(self) == 0:
            return True
        return False

    def __len__(self):
        """
        Função len usada sobre a estrutura de dados

        :return: Tamanho da fila
        """
        return self._tamanho

    def __reversed__(self):
        """
        Função que define a forma de iterar a estrutura de trás para frente

        :return: Cada nó iterado
        """
        nodo_final = self._final
        while nodo_final:
            yield nodo_final
            nodo_final = nodo_final.anterior

    def __iter__(self):
        """
        Função que define como a estrutura de dados será iterada

        :return: Cada nó iterado
        """
        nodo_inicio = self._inicio
        while nodo_inicio:
            yield nodo_inicio
            nodo_inicio = nodo_inicio.proximo
