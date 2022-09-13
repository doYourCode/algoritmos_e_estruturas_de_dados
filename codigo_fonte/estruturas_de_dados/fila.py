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
        self.valor = None
        self.filaTeste = [None] * tamanho
        self.capacidade = tamanho
        self.frente = 0
        self.final = -1
        self.contador = 0

    """Função para remover o elemento da frente"""
    def remover(self):
        """ Verifica se a fila está vazia"""
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        x = self.filaTeste[self.frente]
        print('Removendo elemento...', x)
        self.frente = (self.frente + 1) % self.capacidade
        self.contador = self.contador - 1
        return x

    """Função para adicionar um elemento à fila"""
    def enfileirar(self, valor):
        """verifica se há estouro de fila"""
        if self.estaCheia():
            print('Fila Cheia! Encerrando processo...')
            exit(-1)
        print('Inserindo elemento...', valor)
        self.final = (self.final + 1) % self.capacidade
        self.filaTeste[self.final] = valor
        self.contador = self.contador + 1

    """Função para retornar o elemento da frente da fila sem apagar"""
    def peek(self):
        if self.estaVazia():
            print('Fila Vazia! Encerrando processo...')
            exit(-1)
        return self.filaTeste[self.frente]

    """Função para retornar o tamanho da fila"""
    def tamanho(self):
        return self.contador

    """Função para verificar se a fila está vazia ou não"""
    def estaVazia(self):
        return self.tamanho() == 0

    """Função para verificar se a fila está cheia ou não"""
    def estaCheia(self):
        return self.tamanho() == self.capacidade


if __name__ == '__main__':

    filaTeste = Fila(5)  # ............ Define o tamanho da fila
    # Testando inserção
    filaTeste.enfileirar(1)  # ............ Insere o primeiro elemento
    filaTeste.enfileirar(2)  # ............ Insere o segundo elemento
    filaTeste.enfileirar(3)  # ............ Insere o terceiro elemento
    print(f'{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    print(f'O tamanho da fila é: {filaTeste.tamanho()}')
    print(f'O elemento da frente é: {filaTeste.peek()}')

    # Testando a remoção
    filaTeste.remover()  # ............ Remove o elemento da frente da fila
    print(f'O elemento da frente é: {filaTeste.peek()}')
    filaTeste.remover()  # ............ Remove o elemento da frente da fila
    print(f'{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{str(filaTeste.valor)} {OKBLUE} Tamanho da Fila: {filaTeste.tamanho()}{ENDC}\n')

    # Testando Erro
    print(f'{HEADER}Teste Nº 4 (Erro): {ENDC}')
    filaTeste.remover()
    filaTeste.remover()
    filaTeste.remover()
    filaTeste.remover()
    filaTeste.remover()
    print(f'{filaTeste.valor} {OKBLUE} Tamanho da fila: {filaTeste.tamanho()} {ENDC}')

    # Verificando se a fila está vazia ou não
    if filaTeste.estaVazia():
        print('A fila está vazia!')
    else:
        print('A fila não está vazia!')
        