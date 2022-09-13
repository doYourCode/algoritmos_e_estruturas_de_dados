from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.pilha import Pilha
from codigo_fonte.estruturas_de_dados.pilha_encadeada import PilhaEncadeada


def pilha():

    stack = Pilha(3)

    stack.push(1)  # Inserindo 1 na Stack
    stack.push(2)  # Inserindo 2 na Stack

    stack.pop()  # removendo o elemento superior (2)
    stack.pop()  # removendo o elemento superior (1)

    stack.push(3)  # Inserindo 3 na Stack

    print(f'O elemento do topo da pilha é {stack.peek()}')
    print(f'O tamanho da pilha é {stack.size()}')

    stack.pop()  # removendo o elemento superior (3)

    # verifica se a Stack está vazia
    if stack.isEmpty():
        print('Essa pilha está vazia!')
    else:
        print('Essa pilha não está vazia!')


def pilha_encadeada():
    pilha_teste = PilhaEncadeada()  # Iniciando a Pilha sem valor algum.

    # Teste de inserção
    pilha_teste.adicionar(5)
    pilha_teste.adicionar(7)
    pilha_teste.adicionar(1)
    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}\n')

    # Teste de Remoção
    print(f'{HEADER} Teste Nº 2 (Remoção): {ENDC}')
    pilha_teste.remover()
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}')
    pilha_teste.remover()
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}')
    pilha_teste.remover()  # Os três dados foram removidos, o próximo deve retornar uma mensagem
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}')
    pilha_teste.remover()
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}\n')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Peek): {ENDC}')
    pilha_teste.adicionar(7)
    pilha_teste.adicionar(3)
    pilha_teste.adicionar(9)
    print(f'Elemento do topo: {str(pilha_teste.ler_topo())}')
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}\n')

    # Teste de erro -- Sò há um erro que pode ocorrer: Tentar deletar um topo de uma pilha vazia
    print(f'{HEADER} Teste Nº 4 (Erro): {ENDC}')
    pilha_teste.remover()
    pilha_teste.remover()
    pilha_teste.remover()
    pilha_teste.remover()
    # Removi 4x pois havia criado 3 no teste anterior.

    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilha_teste))}{ENDC}')
