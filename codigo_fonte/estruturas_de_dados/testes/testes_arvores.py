from codigo_fonte.estruturas_de_dados.arvore_binaria_de_busca import ArvoreBinariaDeBusca
from codigo_fonte.utilidades.utilidades import *


def arvore_binaria_de_busca():
    arvore_teste = ArvoreBinariaDeBusca()

    # Testando inserção
    print(f'\n{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    arvore_teste.inserir(10)
    arvore_teste.inserir(15)
    arvore_teste.inserir(5)
    arvore_teste.inserir(3)
    arvore_teste.inserir(7)
    arvore_teste.inserir(12)
    arvore_teste.inserir(17)
    arvore_teste.inserir(125)
    arvore_teste.caminhar()

    # Teste de remoção
    print(f'\n{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    arvore_teste.remover(125)
    arvore_teste.remover(4)
    arvore_teste.remover(5)
    arvore_teste.remover(9)
    arvore_teste.caminhar()

    # Teste de busca
    print(f'\n{HEADER}Teste Nº 3 (Busca): {ENDC}')
    arvore_teste.buscar(99)
    arvore_teste.buscar(10)
