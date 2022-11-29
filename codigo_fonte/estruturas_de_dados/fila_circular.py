_author__ = ["Everton Sousa Oliveira",
              "Caio Henriques Sica Lamas"]
__date__ = "13/09/2022"
__credits__ = ["https://acervolima.com/circular-queue-conjunto-1-introducao-e-implementacao-de-array/"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"
from codigo_fonte.utilidades.utilidades import *


# Implementação de fila circular em Python
class filaCircular():

    def __init__(self, tamanho):
        self.tamanho = tamanho

        self.fila = [None for i in range(tamanho)]
        self.frente = self.final = -1

    def enfileirar(self, data):

        if ((self.final + 1) % self.tamanho == self.frente):
            print("Fila está cheia\n")

        elif (self.frente == -1):
            self.frente = 0
            self.final = 0
            self.fila[self.final] = data

        else:
            self.final = (self.final + 1) % self.tamanho
            self.fila[self.final] = data

    def desinfileirar(self):
        if (self.frente == -1):  # condition for empty queue
            print("Fila está vazia\n")

        # condition for only one element
        elif (self.frente == self.final):
            temp = self.fila[self.frente]
            self.frente = -1
            self.final = -1
            return temp

        else:
            temp = self.fila[self.frente]
            self.frente = (self.frente + 1) % self.tamanho
            return temp

    def display(self):

        if (self.frente == -1):
            print("Fila está vazia")

        elif (self.final >= self.frente):
            print("Os elementos da fila circular são:",
                  end=" ")
            for i in range(self.frente, self.final + 1):
                print(self.fila[i], end=" ")
            print()

        else:
            print("Os elementos da fila circular são:",
                  end=" ")
            for i in range(self.frente, self.tamanho):
                print(self.fila[i], end=" ")
            for i in range(0, self.final + 1):
                print(self.fila[i], end=" ")
            print()

        if ((self.final + 1) % self.tamanho == self.frente):
            print("Fila está cheia")

# Driver Code
teste = filaCircular(5)
teste.enfileirar(14)
teste.enfileirar(22)
teste.enfileirar(13)
teste.enfileirar(-6)
teste.display()
print("Desinfileirando valor = ", teste.desinfileirar())
print("Desinfileirando valor = ", teste.desinfileirar())
teste.display()
teste.enfileirar(9)
teste.enfileirar(20)
teste.enfileirar(5)
teste.display()
