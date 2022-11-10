from codigo_fonte.estruturas_de_dados.arvore_binaria_de_busca import ArvoreBinariaDeBusca
from codigo_fonte.estruturas_de_dados.arvore_avl import ArvoreAvl
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


def arvore_avl():
    arvore_avl_teste = ArvoreAvl()
    print(f'\n{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 10)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 15)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 5)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 13)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 4)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 2)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 17)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 30)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 45)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 60)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 43)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 65)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 70)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 75)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 73)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 50)
    arvore_avl_teste.inserir(arvore_avl_teste.raiz, 55)
    arvore_avl_teste.caminhar()

    print(f'\n{HEADER}Teste Nº 2 (Exclusões): {ENDC}')

    arvore_avl_teste.remover(arvore_avl_teste.raiz, 65)
    arvore_avl_teste.remover(arvore_avl_teste.raiz, 10)
    arvore_avl_teste.remover(arvore_avl_teste.raiz, 30)
    arvore_avl_teste.remover(arvore_avl_teste.raiz, 43)
    arvore_avl_teste.caminhar()

    print(f'\n{HEADER}Teste Nº 3 (Busca): {ENDC}')
    print(arvore_avl_teste.buscar(50).registro)
    print(arvore_avl_teste.buscar(17).registro)

    print(f'\n{HEADER}Teste Nº 4 (Erros): {ENDC}')
    arvore_avl_teste.buscar(33)
    arvore_avl_teste.remover(arvore_avl_teste.raiz, 33)
    arvore_avl_teste = ArvoreAvl()
    arvore_avl_teste.remover(arvore_avl_teste, 10)

