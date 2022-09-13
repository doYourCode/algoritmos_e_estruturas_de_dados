from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.fila_encadeada import FilaEncadeada


def fila_encadeada():
    fila_teste = FilaEncadeada()  # Iniciando a Fila sem valor algum.

    # Teste de inserção
    fila_teste.adicionar("Franck")
    fila_teste.adicionar("Allyson")
    fila_teste.adicionar("Ronaldinho")
    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')

    # Teste de remoção
    fila_teste.remover()
    fila_teste.remover()  # Queremos verificar se o PEPS(Primeiro a Entrar, Primeiro a sair) está sendo cumprido.
    print(f'{HEADER} Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Leitura): {ENDC}')
    fila_teste.adicionar("Franck")
    fila_teste.adicionar("Caio")
    fila_teste.adicionar("Lamas")
    print(f'Elemento do inicio: {str(fila_teste.ler_inicio())}')
    print(f'Elemento do final: {str(fila_teste.ler_final())}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')

    # Teste de Erro
    print(f'{HEADER} Teste Nº 4 (Erro): {ENDC}')
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')
