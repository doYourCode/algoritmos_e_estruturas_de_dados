__author__ = ["Caio Henriques Sica Lamas",
              "Everton Sousa Oliveira"]
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

    """Função para remover o elemento da frente"""
    def remover(self):
        """ Verifica se a fila está vazia"""
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        x = self.fila_teste[self.inicio]
        print('Removendo elemento...', x)
        self.inicio = (self.inicio + 1) % self.capacidade
        self.contador -= 1
        return x

    """Função para adicionar um elemento à fila"""
    def adicionar(self, valores):
        """verifica se há estouro de fila"""
        if self.estaCheia():
            print('Fila Cheia! Encerrando processo...')
            exit(-1)
        print('Inserindo elemento...', valores)
        self.final = (self.final + 1) % self.capacidade
        self.fila_teste[self.final] = valores
        self.contador += 1

    """Função para retornar o elemento da frente da fila sem apagar"""
    def peek(self):
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        return self.fila_teste[self.inicio]

    """Função para retornar o tamanho da fila"""
    def tamanho(self):
        return self.contador

    """Função para verificar se a fila está vazia ou não"""
    def estaVazia(self):
        return self.tamanho() == 0

    """Função para verificar se a fila está cheia ou não"""
    def estaCheia(self):
        return self.tamanho() == self.capacidade
        