from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.pilha import Pilha
from codigo_fonte.estruturas_de_dados.pilha_encadeada import PilhaEncadeada


def pilha():
    pilha_teste = Pilha(20)  # ............ Define o tamanho da Pilha

    # Testando inserção
    pilha_teste.inserir(1)  # ............ Inserindo 1 na Pilha
    pilha_teste.inserir(2)  # ............ Inserindo 2 na Pilha
    pilha_teste.inserir(3)  # ............ Inserindo 3 na Pilha
    print(f'O elemento do topo da pilha é {pilha_teste.ler_topo()}')
    print(f'O tamanho da pilha é {pilha_teste.tamanho()}')
    print(f'{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Fila: {pilha_teste.tamanho()}{ENDC}\n')

    # Teste de retorno
    print(f'{HEADER}Teste Nº 3 (Peek): {ENDC}')
    pilha_teste.inserir(7)
    pilha_teste.inserir(3)
    pilha_teste.inserir(9)
    print(f'Elemento do topo: {str(pilha_teste.ler_topo())}')
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Pilha: {pilha_teste.tamanho()}{ENDC}\n')

    # Testando remoção
    pilha_teste.remover()  # ............ Removendo o elemento superior (3)
    pilha_teste.remover()  # ............ Removendo o elemento superior (2)
    print(f'{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{str(pilha_teste.valores)} {OKBLUE} Tamanho da Fila: {pilha_teste.tamanho()}{ENDC}\n')

    # Testando Erro
    print(f'{HEADER}Teste Nº 4 (Erro): {ENDC}')
    pilha_teste.remover()
    pilha_teste.remover()
    pilha_teste.remover()
    pilha_teste.remover()
    pilha_teste.remover()
    print(f'{pilha_teste.valores} {OKBLUE} Tamanho da fila: {pilha_teste.tamanho()} {ENDC}')

    # Verificando se a Pilha está vazia ou não
    if pilha_teste.estaVazia():
        print('Essa pilha está vazia!')
    else:
        print('Essa pilha não está vazia!')

    """Verificar se a Pilha está cheia ou não"""
    if pilha_teste.estaVazia():
        print('A fila está vazia!')
    else:
        print('A fila não está vazia!')


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
