__author__ = ["Caio Henriques Sica Lamas",
              "Everton Sousa Oliveira"]
__date__ = "13/09/2022"
__credits__ = ["https://www.techiedelight.com/pt/stack-implementation-python/"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"

from codigo_fonte.utilidades.utilidades import *

# Implementação de Pilha em Python
class Pilha:

    """Construtor para inicializar a Pilha"""
    def __init__(self, tamanho):
        self.valores = None
        self.arr = [None] * tamanho
        self.capacidade = tamanho
        self.topo = -1

    """Função para adicionar um elemento valor à Pilha"""
    def inserir(self, valores):
        if self.estaCheio():
            print('Pilha cheia! Encerrando processo...')
            exit(-1)

        print(f'Inserindo {valores} na pilha...')
        self.topo = self.topo + 1
        self.arr[self.topo] = valores

    """Função para remover um elemento superior da Pilha"""
    def remover(self):
        # verifica se a pilha está vazia
        if self.estaVazia():
            print('Pilha vazia! Encerrando processo...')
            exit(-1)

        print(f'Removendo {self.ler_topo()} da pilha')

        """Diminui o tamanho da Pilha em 1 e (opcionalmente) retorna o elemento estourado"""
        topo = self.arr[self.topo]
        self.topo = self.topo - 1
        return topo

    """Função para retornar o elemento do topo da Pilha"""
    def ler_topo(self):
        if self.estaVazia():
            exit(-1)
        return self.arr[self.topo]

    """Função para retornar o tamanho da Pilha"""
    def tamanho(self):
        return self.topo + 1

    """Função para verificar se a Pilha está vazia ou não"""
    def estaVazia(self):
        return self.tamanho() == 0

    """Função para verificar se a Pilha está cheia ou não"""
    def estaCheio(self):
        return self.tamanho() == self.capacidade


