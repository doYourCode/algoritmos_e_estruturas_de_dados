__author__ = ["Caio Henriques Sica Lamas",
              "Everton Sousa Oliveira"]
__date__ = "13/09/2022"
__credits__ = ["https://www.askpython.com/python/examples/double-ended-queue"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"

# Implementação de fila dupla em Python
class Fila_dupla:
    def __init__(self, tamanho):
        self.filaDupla = []
        self.contador = 0
        self.capacidade = tamanho

    def adicionarInicio(self, data):
        if self.estaCheia():
            print('Fila Cheia! Encerrando processo...')
            exit(-1)
        self.filaDupla.insert(0, data)
        print('Inserindo elemento na frente da fila...', data)
        self.contador += 1
        return

    def adicionarFinal(self, data):
        if self.estaCheia():
            print('Fila Cheia! Encerrando processo...')
            exit(-1)
        print('Inserindo elemento no final da fila...', data)
        self.filaDupla.append(data)
        self.contador += 1
        return

    def removerInicio(self):
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        x = self.filaDupla.pop(0)
        print('Removendo elemento do inicio da fila...', x)
        self.contador -= 1
        return x

    def removerFinal(self):
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        x = self.filaDupla.pop()
        print('Removendo elemento do final da fila...', x)
        self.contador -= 1
        return x

    def tamanho(self):
        return self.contador

    def estaVazia(self):
        return self.tamanho() == 0

    """Função para verificar se a fila está cheia ou não"""

    def estaCheia(self):
        return self.tamanho() == self.capacidade
