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
        self.valor = None
        self.arr = [None] * tamanho
        self.capacidade = tamanho
        self.topo = -1

    """Função para adicionar um elemento valor à Pilha"""
    def inserir(self, valor):
        if self.estaCheio():
            print('Pilha cheia! Encerrando processo...')
            exit(-1)

        print(f'Inserindo {valor} na pilha...')
        self.topo = self.topo + 1
        self.arr[self.topo] = valor

    """Função para remover um elemento superior da Pilha"""
    def remover(self):
        # verifica se a pilha está vazia
        if self.estaVazia():
            print('Pilha vazia! Encerrando processo...')
            exit(-1)

        print(f'Removendo {self.peek()} da pilha')

        """Diminui o tamanho da Pilha em 1 e (opcionalmente) retorna o elemento estourado"""
        topo = self.arr[self.topo]
        self.topo = self.topo - 1
        return topo

    """Função para retornar o elemento do topo da Pilha"""
    def peek(self):
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


if __name__ == '__main__':

    pilha = Pilha(3)  # ............ Define o tamanho da Pilha
    #Testando inserção
    pilha.inserir(1)  # ............ Inserindo 1 na Pilha
    pilha.inserir(2)  # ............ Inserindo 2 na Pilha
    pilha.inserir(3)  # ............ Inserindo 3 na Pilha
    print(f'O elemento do topo da pilha é {pilha.peek()}')
    print(f'O tamanho da pilha é {pilha.tamanho()}')
    print(f'{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(pilha.valor)} {OKBLUE} Tamanho da Fila: {pilha.tamanho()}{ENDC}\n')

    #Testando remoção
    pilha.remover()  # ............ Removendo o elemento superior (3)
    pilha.remover()  # ............ Removendo o elemento superior (2)
    print(f'{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{str(pilha.valor)} {OKBLUE} Tamanho da Fila: {pilha.tamanho()}{ENDC}\n')

    # Testando Erro
    print(f'{HEADER}Teste Nº 4 (Erro): {ENDC}')
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    pilha.remover()
    print(f'{pilha.valor} {OKBLUE} Tamanho da fila: {pilha.tamanho()} {ENDC}')

    # Verificando se a Pilha está vazia ou não
    if pilha.estaVazia():
        print('Essa pilha está vazia!')
    else:
        print('Essa pilha não está vazia!')
