from codigo_fonte.estruturas_de_dados.lista_encadeada import ListaEncadeada
from codigo_fonte.estruturas_de_dados.lista_duplamente_encadeada import ListaDuplamenteEncadeada
from codigo_fonte.utilidades.utilidades import *


def lista_encadeada():
    lista = ListaEncadeada()  # ........................Instancia uma nova lista (em branco)
    # Testando inserção
    lista.adicionar_inicio("Segunda")  # .....................Insere um primeiro elemento
    lista.adicionar_final("Terça")  # ........................Insere 2 elementos ao final da lista
    lista.adicionar_final("Sexta")  #
    lista.adicionar_pos("Terça", "Quarta")  # ...Insere 2 elementos após outros 2 elementos específicos (busca)
    lista.adicionar_pos("Quarta", "Quinta")  # ..PS. Seria possível ter inserido a quarta e depois a terça?
    lista.adicionar_final("Sábado")  # .......................Insere elemento ao final da lista
    lista.adicionar_inicio("Domingo")  # .....................Insere elemento no início da lista
    print(f"{HEADER} Teste nº 1 (Inserções):  {ENDC}")
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    # Testando a remoção
    lista.adicionar_inicio("Dia de são nunca")  # ............Insere 3 nós que não deveriam existir
    lista.adicionar_final("Dia de São Luguinho")
    lista.adicionar_pos("Quinta", "Dia do João Gomes")
    print(f"{HEADER} Teste nº 2 (Inserções equivocadas):  {ENDC}")
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")
    lista.remover("Dia de são nunca")  # ................Remove os 3 nós que não deveriam existir
    lista.remover("Dia de São Luguinho")
    lista.remover("Dia do João Gomes")
    print(f"{HEADER} Teste nº 3 (Remoções):  {ENDC}")
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    # Testando os erros
    print(f"{HEADER} Teste nº 4 (Erros):  {ENDC}")
    lista.remover("Outro dia")  # ............................Tenta remover um nó que não existe
    lista.adicionar_pos("Dia do trabalhador", "Oitavo dia")  # ... Tenta adicionar um nó em local que não existe
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    # Testando a vericação de estar vazia
    print(f"{HEADER} Teste nº 5 (lista vazia):  {ENDC}")
    lista = ListaEncadeada()
    print(lista.esta_vazia())
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")


def lista_duplamente_encadeada():
    lista = ListaDuplamenteEncadeada()  # ........................Instancia uma nova lista (em branco)
    # Testando inserção
    lista.adicionar_inicio("Segunda")  # .....................Insere um primeiro elemento
    lista.adicionar_final("Quarta")  # ........................Insere 2 elementos ao final da lista
    lista.adicionar_final("Sexta")
    lista.adicionar_pos("Segunda", "Terça")
    lista.adicionar_pos("Quarta", "Quinta")
    print(f"{HEADER} Teste nº 1 (Inserções):  {ENDC}")
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    lista.adicionar_inicio("Dia de são nunca")  # ............Insere 3 nós que não deveriam existir
    lista.adicionar_final("Dia de São Luguinho")
    lista.adicionar_pos("Quinta", "Dia do João Gomes")
    lista.remover("Dia de são nunca")  # ................Remove os 3 nós que não deveriam existir
    lista.remover("Dia de São Luguinho")
    lista.remover("Dia do João Gomes")
    print(f"{HEADER} Teste nº 2 (Remoções):  {ENDC}")
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    print(f"{HEADER} Teste nº 3 (Busca):  {ENDC}")
    print(lista.buscar("Quarta").dados)
    print(lista.buscar("Sexta").dados)
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    print(f"{HEADER} Teste nº 4 (Erros):  {ENDC}")
    lista.remover("Dia de São Luguinho")
    print(lista.buscar("Dia de São Luguinho"))
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")

    print(f"{HEADER} Teste nº 5 (Esta Vazia):  {ENDC}")
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")
    print(lista.esta_vazia())
    lista = ListaEncadeada()
    print(f"{str(lista.valores)} {OKBLUE} +  Tamanho da lista: {str(len(lista))} {ENDC}")
    print(lista.esta_vazia())
