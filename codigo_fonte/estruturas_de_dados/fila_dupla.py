__author__ = ["Everton Sousa Oliveira",
              "Caio Henriques Sica Lamas"]
__date__ = "13/09/2022"
__credits__ = ["https://www.askpython.com/python/examples/double-ended-queue"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"
from codigo_fonte.utilidades.utilidades import *
# Implementação de fila dupla em Python
class Fila_dupla:
    def __init__(self, tamanho):
        self.filaDupla = []
        self.contador = 0
        self.capacidade = tamanho

    def adicionarInicio(self, data):
        """
        Função para adicionar um elemento à fila ao topo da fila
        :param valor: Informação que será armazenada no inicio
        """
        if self.estaCheia():
            print(f"{FAIL} A fila está cheia, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        self.filaDupla.insert(0, data)
        print('Inserindo elemento na frente da fila...', data)
        self.contador += 1
        return

    def adicionarFinal(self, data):
        """
        Função para adicionar um elemento à fila ao final da fila
        :param valor: Informação que será armazenada no final
        """
        if self.estaCheia():
            print(f"{FAIL} A fila está cheia, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        print('Inserindo elemento no final da fila...', data)
        self.filaDupla.append(data)
        self.contador += 1
        return

    def removerInicio(self):
        """
        Função para remover o elemento da frente

        :param valor: Informação que será removida do inicio
        """
        if self.estaVazia():
            print(f"{FAIL} Não há nenhum elemento na fila, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        x = self.filaDupla.pop(0)
        print('Removendo elemento do inicio da fila...', x)
        self.contador -= 1
        return x

    def removerFinal(self):
        """
        Função para remover o elemento do final

        :param valor: Informação que será removida do final
        """
        if self.estaVazia():
            print(f"{FAIL} Não há nenhum elemento na fila, nenhuma operação foi realizada!{ENDC}")
            exit(-1)
        x = self.filaDupla.pop()
        print('Removendo elemento do final da fila...', x)
        self.contador -= 1
        return x

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
