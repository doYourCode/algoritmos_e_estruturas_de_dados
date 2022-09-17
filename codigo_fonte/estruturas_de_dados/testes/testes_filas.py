from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.fila_encadeada import FilaEncadeada
from codigo_fonte.estruturas_de_dados.fila import Fila

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

if __name__ == '__main__':

    fila_teste = Fila(20)  # ............ Define o tamanho da fila

    # Testando inserção
    fila_teste.adicionar(1)  # ............ Insere o primeiro elemento
    fila_teste.adicionar(2)  # ............ Insere o segundo elemento
    fila_teste.adicionar(3)  # ............ Insere o terceiro elemento
    print(f'{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    print(f'O tamanho da fila é: {fila_teste.tamanho()}')
    print(f'O elemento da frente é: {fila_teste.peek()}')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Leitura): {ENDC}')
    fila_teste.adicionar(7)
    fila_teste.adicionar(75)
    fila_teste.adicionar(9)
    print(f'O elemento da frente é: {fila_teste.peek()}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {fila_teste.tamanho()}{ENDC}')

    # Testando a Exclusões
    fila_teste.remover()  # ............ Remove o elemento da frente da fila
    print(f'{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    print(f'O elemento da frente é: {fila_teste.peek()}')
    fila_teste.remover()  # ............ Remove o elemento da frente da fila
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {fila_teste.tamanho()}{ENDC}')

    # Testando Erro
    print(f'{HEADER}Teste Nº 4 (Erro): {ENDC}')
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    print(f'{fila_teste.valores} {OKBLUE} Tamanho da fila: {fila_teste.tamanho()} {ENDC}')

    # Verificando se a fila está vazia ou não
    if fila_teste.estaVazia():
        print('A fila está vazia!')
    else:
        print('A fila não está vazia!')
