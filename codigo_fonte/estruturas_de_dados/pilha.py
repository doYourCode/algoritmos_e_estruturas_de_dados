__author__ = ["Everton Sousa Oliveira",
              "Caio Henriques Sica Lamas"]
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

    def inserir(self, valores):
        """
        Função para adicionar um elemento valor à Pilha

        :param valor: Informação que será armazenada
        """
        if self.estaCheio():
            print(f"{FAIL} A fila está cheia, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        print(f'Inserindo {valores} na pilha...')
        self.topo = self.topo + 1
        self.arr[self.topo] = valores

    def remover(self):
        """
        Função para remover um elemento superior da Pilha

        :param valor: Informação que será removida
        """
        if self.estaVazia():
            print(f"{FAIL} Não há nenhum elemento na fila, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        print(f'Removendo {self.ler_topo()} da pilha')
        """Diminui o tamanho da Pilha em 1 e (opcionalmente) retorna o elemento estourado"""
        topo = self.arr[self.topo]
        self.topo = self.topo - 1
        return topo


    def ler_topo(self):
        """
        Função para retornar o elemento da frente da pilha sem apagar

        :return: Informação do topo da fila
        """
        if self.estaVazia():
            exit(-1)
        return self.arr[self.topo]

    def tamanho(self):
        """
        Função para retornar o tamanho da pilha

        :return: Tamanho da pilha
        """
        return self.topo + 1

    def estaVazia(self):
        """Função para verificar se a Pilha está vazia ou não"""
        return self.tamanho() == 0

    def estaCheio(self):
        """Função para verificar se a Pilha está cheia ou não"""
        return self.tamanho() == self.capacidade


