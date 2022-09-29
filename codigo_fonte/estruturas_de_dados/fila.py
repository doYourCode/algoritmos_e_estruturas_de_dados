_author__ = ["Everton Sousa Oliveira",
              "Caio Henriques Sica Lamas"]
__date__ = "13/09/2022"
__credits__ = ["https://www.techiedelight.com/pt/filaTesteueue-implementation-python/"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"
from codigo_fonte.utilidades.utilidades import *


# Implementação de fila em Python
class Fila:
    """Inicializar fila"""
    def __init__(self, tamanho):
        self.valores = None
        self.fila_teste = [None] * tamanho
        self.capacidade = tamanho
        self.inicio = 0
        self.final = -1
        self.contador = 0

    def remover(self):
        """
        Função para remover o elemento da frente

        :param valor: Informação que será removida
        """
        if self.estaVazia():
            print(f"{FAIL} Não há nenhum elemento na fila, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        x = self.fila_teste[self.inicio]
        print('Removendo elemento...', x)
        self.inicio = (self.inicio + 1) % self.capacidade
        self.contador -= 1
        return x

    def adicionar(self, valores):
        """
        Função para adicionar um elemento à fila

        :param valor: Informação que será armazenada
        """
        if self.estaCheia():
            print(f"{FAIL} A fila está cheia, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        print('Inserindo elemento...', valores)
        self.final = (self.final + 1) % self.capacidade
        self.fila_teste[self.final] = valores
        self.contador += 1

    def peek(self):
        """
        Função para retornar o elemento da frente da fila sem apagar

        :return: Informação do topo da fila
        """
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        return self.fila_teste[self.inicio]

    def tamanho(self):
        """
        Função para retornar o tamanho da fila

        :return: Tamanho da fila
        """
        return self.contador

    def estaVazia(self):
        """Função para verificar se a fila está vazia ou não"""
        return self.tamanho() == 0

    def estaCheia(self):
        """Função para verificar se a fila está cheia ou não"""
        return self.tamanho() == self.capacidade
        