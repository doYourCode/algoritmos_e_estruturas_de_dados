# Implementação de Pilha em Python
class Pilha:

    # Construtor # para inicializar a Stack
    def __init__(self, tamanho):
        self.arr = [None] * tamanho
        self.capacidade = tamanho
        self.topo = -1

    # Função para adicionar um elemento `valor` à Stack
    def push(self, valor):
        if self.isFull():
            print('Stack Overflow!! Calling exit()…')
            exit(-1)

        print(f'Inserindo {valor} na pilha…')
        self.topo = self.topo + 1
        self.arr[self.topo] = valor

    # Função para remover um elemento superior da Stack
    def pop(self):
        # verifica se há underflow da Stack
        if self.estaVazia():
            print('Stack Underflow!! Calling exit()…')
            exit(-1)

        print(f'Removendo {self.peek()} da pilha')

        # diminui o tamanho da Stack em 1 e (opcionalmente) retorna o elemento estourado
        topo = self.arr[self.topo]
        self.topo = self.topo - 1
        return topo

    # Função para retornar o elemento do topo da Stack
    def peek(self):
        if self.estaVazia():
            exit(-1)
        return self.arr[self.topo]

    # Função para retornar o tamanho da Stack
    def tamanho(self):
        return self.topo + 1

    # Função para verificar se a Stack está vazia ou não
    def estaVazia(self):
        return self.tamanho() == 0

    # Função para verificar se a Stack está cheia ou não
    def isFull(self):
        return self.tamanho() == self.capacidade


if __name__ == '__main__':

    pilha = Pilha(3)

    pilha.push(1)  # Inserindo 1 na Stack
    pilha.push(2)  # Inserindo 2 na Stack

    pilha.pop()  # removendo o elemento superior (2)
    pilha.pop()  # removendo o elemento superior (1)

    pilha.push(3)  # Inserindo 3 na Stack

    print(f'O elemento do topo da pilha é {pilha.peek()}')
    print(f'O tamanho da pilha é {pilha.tamanho()}')

    pilha.pop()  # removendo o elemento superior (3)

    # verifica se a Stack está vazia
    if pilha.estaVazia():
        print('Essa pilha está vazia!')
    else:
        print('Essa pilha não está vazia!')