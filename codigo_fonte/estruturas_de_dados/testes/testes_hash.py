from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.tabela_hash import TabelaHash
from codigo_fonte.estruturas_de_dados.tabela_hash_encadeada import TabelaHashEncadeada


def tabela_hash():

    tabela_teste = TabelaHash(10)  # Iniciando tabela com o tamanho desejado

    # Teste de Inserção
    tabela_teste.inserir_dado(123, "maçã")
    tabela_teste.inserir_dado(432, "manga")
    tabela_teste.inserir_dado(213, "banana")
    tabela_teste.inserir_dado(654, "abacaxi")

    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(tabela_teste)} {OKBLUE} \nTamanho da Tabela: {str(len(tabela_teste))}{ENDC}\n')

    # Teste de exclusão
    tabela_teste.deletar_dado(123)
    tabela_teste.deletar_dado(213)

    print(f'{HEADER} Teste Nº 2 (Remoção): {ENDC}')
    print(f'{str(tabela_teste)} {OKBLUE} \nTamanho da Tabela: {str(len(tabela_teste))}{ENDC}\n')

    # Teste de erro
    # Aqui temos o erro de colisão que pode ocorrer
    tabela_teste.inserir_dado(433, "romã")
    tabela_teste.inserir_dado(434, "pera")
    print(f'{HEADER} Teste Nº 3 (Colisão): {ENDC}')
    print(f'{str(tabela_teste)} {OKBLUE} \nTamanho da Tabela: {str(len(tabela_teste))}{ENDC}\n')
    # Esse teste prova que mesmo com um número primo na capacidade
    # ainda dará problemas de colisão [654, 'abacaxi'] foi colidido pela última inserção
    # O método que resolve esse problema, é fazendo a tabela hash encadeada.


def tabela_hash_encadeada():

    tabela_teste = TabelaHashEncadeada(10) # Iniciando tabela com o tamanho desejado

    # Teste de Inserção
    tabela_teste.inserir_dados(123, "maçã")
    tabela_teste.inserir_dados(432, "manga")
    tabela_teste.inserir_dados(213, "banana")
    tabela_teste.inserir_dados(654, "abacaxi")
    tabela_teste.inserir_dados(655, 'kiwi')
    tabela_teste.inserir_dados(233, 'mamão') # Aqui colidiu, e foi solucionado

    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(tabela_teste)} {OKBLUE} \nTamanho da Tabela: {str(len(tabela_teste))}{ENDC}\n')

    # Teste de exclusão
    tabela_teste.deletar_dados(123)
    tabela_teste.deletar_dados(213)

    print(f'{HEADER} Teste Nº 2 (Remoção): {ENDC}')
    print(f'{str(tabela_teste)} {OKBLUE} \nTamanho da Tabela: {str(len(tabela_teste))}{ENDC}\n')

    # Teste de busca
    print(tabela_teste.buscar_pela_chave(655))
    print(tabela_teste.bucar_pelo_valor('abacaxi'))

    print(f'{HEADER} Teste Nº 3 (Busca): {ENDC}')
    print(f'{str(tabela_teste)} {OKBLUE} \nTamanho da Tabela: {str(len(tabela_teste))}{ENDC}\n')

    # Teste de erro
    # Solucionamos o 'erro'(colisão) do hashing através do encadeamento.


