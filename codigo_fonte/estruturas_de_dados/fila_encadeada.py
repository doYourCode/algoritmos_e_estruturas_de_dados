""" Exemplo de estrutura de FILA, usando encadeamento, e alguns algoritmos relacionados.

Esse tipo de implementação de Fila funcionará como as demais filas, porém objetiva facilitar a alocação
dinâmica de novos elementos, porém requer mais operações de alocação e também mais memória. É util para
quando desconhecemos o tamanho potencial da fila.
"""
__author__ = ["Caio Henriques Sica Lamas",
              "Franck Allyson da Silva Rocha"]
__date__ = "20/08/2022"
__credits__ = [""]  # TODO
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"

from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa o único No de uma Lista """

    def __init__(self, valor):
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
        """ Conjunto de nós """
        return [nodo.valor for nodo in self]

    def adicionar(self, valor):
        """ Adiciona um novo nó ao fim da fila """
        novo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = novo_nodo
        else:
            self.final.proximo = novo_nodo
        self.final = novo_nodo
        self._tamanho += 1

    def ler_inicio(self):
        """ Retorna o valor do inicio da fila """
        nodo_inicio = self.inicio
        return nodo_inicio.valor

    def ler_final(self):
        """ Retorna o valor do final da fila """
        nodo_final = self.final
        return nodo_final.valor

    def remover(self):
        """ Remove o elemento do inicio da Fila """
        if self.inicio is None:
            print(f"{FAIL} Não há nenhum elemento na fila, nenhuma operação foi realizada!{ENDC}")
            return

        nodo_inicio = self.inicio
        valor = nodo_inicio.valor
        self.inicio = nodo_inicio.proximo
        self._tamanho -= 1
        return valor

    def __iter__(self):
        nodo_inicio = self.inicio
        while nodo_inicio:
            yield nodo_inicio
            nodo_inicio = nodo_inicio.proximo

    def __len__(self):
        return self._tamanho


def fila_encadeada():
    filaTeste = FilaEncadeada()  # Iniciando a Fila sem valor algum.

    # Teste de inserção
    filaTeste.adicionar("Franck")
    filaTeste.adicionar("Allyson")
    filaTeste.adicionar("Ronaldinho")
    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(filaTeste.valores)} {OKBLUE} Tamanho da Fila: {str(len(filaTeste))}{ENDC}\n')

    # Teste de remoção
    filaTeste.remover()
    filaTeste.remover()  # Queremos verificar se o PEPS(Primeiro a Entrar, Primeiro a sair) está sendo cumprido.
    print(f'{HEADER} Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{str(filaTeste.valores)} {OKBLUE} Tamanho da Fila: {str(len(filaTeste))}{ENDC}\n')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Leitura): {ENDC}')
    filaTeste.adicionar("Franck")
    filaTeste.adicionar("Caio")
    filaTeste.adicionar("Lamas")
    print(f'Elemento do inicio: {str(filaTeste.ler_inicio())}')
    print(f'Elemento do final: {str(filaTeste.ler_final())}')
    print(f'{str(filaTeste.valores)} {OKBLUE} Tamanho da Fila: {str(len(filaTeste))}{ENDC}\n')

    # Teste de Erro
    print(f'{HEADER} Teste Nº 4 (Erro): {ENDC}')
    filaTeste.remover()
    filaTeste.remover()
    filaTeste.remover()
    filaTeste.remover()
    filaTeste.remover()
    print(f'{str(filaTeste.valores)} {OKBLUE} Tamanho da Fila: {str(len(filaTeste))}{ENDC}\n')

