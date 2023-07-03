from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.grafo import Grafo
from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia import GrafoListaAdjacencia
from codigo_fonte.estruturas_de_dados.grafo_matriz_adjacencia import GrafoMatrizAdjacencia

import os


def grafo():
    grafo_teste = Grafo()

    # Teste de inserção de vértices

    grafo_teste.inserir_vertice('a', 2)
    grafo_teste.inserir_vertice('b', 7)
    grafo_teste.inserir_vertice('c', 3)
    grafo_teste.inserir_vertice('d', 10)

    print(f'{HEADER} Teste Nº 1 (Inserções vértices): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: '
          f'{str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: '
          f'{str(len(grafo_teste.arestas))}{ENDC}\n')
    # Teste de inserção de arestas
    grafo_teste.inserir_aresta('a', 'c')
    grafo_teste.inserir_aresta('a', 'd')
    grafo_teste.inserir_aresta('b', 'd')

    print(f'{HEADER} Teste Nº 2 (Inserções arestas): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: '
          f'{str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: '
          f'{str(len(grafo_teste.arestas))}{ENDC}\n')

    # Teste de exclusão de vértices
    print(f'{HEADER} Teste Nº 3 (Remoções vértices): {ENDC}')
    grafo_teste.remover_vertice('a')
    grafo_teste.remover_vertice('b')

    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: '
          f'{str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: '
          f'{str(len(grafo_teste.arestas))}{ENDC}\n')

    # Teste de exclusão de arestas
    # Inserindo todos os dados novamente para executar as exclusões:
    grafo_teste.inserir_vertice('a', 2)
    grafo_teste.inserir_vertice('b', 7)
    grafo_teste.inserir_aresta('a', 'c')
    grafo_teste.inserir_aresta('a', 'd')
    grafo_teste.inserir_aresta('b', 'd')

    # Exclusões:
    grafo_teste.remover_aresta('a', 'd')
    grafo_teste.remover_aresta('b', 'd')

    print(f'{HEADER} Teste Nº 4 (Remoções arestas): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: '
          f'{str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: '
          f'{str(len(grafo_teste.arestas))}{ENDC}\n')

    # Teste de União de Vértices
    grafo_teste.inserir_aresta('c', 'd')
    grafo_teste.inserir_aresta('a', 'b')

    grafo_teste.unir_vertices('a', 'c')
    print(f'{HEADER} Teste Nº 5 (União vertice): {ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.vertices))} {OKBLUE} Quantidade de Vértices: '
          f'{str(len(grafo_teste.vertices))}{ENDC}')
    print(f'{str(grafo_teste.etiquetas(grafo_teste.arestas))} {OKBLUE} Quantidade de arestas: '
          f'{str(len(grafo_teste.arestas))}{ENDC}\n')


def grafo_lista_adjacencia():
    grafo_teste = GrafoListaAdjacencia()

    # Inserção
    grafo_teste.inserir_vertice(4)
    grafo_teste.inserir_vertice(5)
    grafo_teste.inserir_vertice(6)
    grafo_teste.inserir_vertice(7)
    grafo_teste.inserir_vertice(8)
    grafo_teste.inserir_vertice(9)
    grafo_teste.inserir_vertice(10)
    print(f'{HEADER}Teste Nº 1 (Inserções vértices): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')

    grafo_teste.inserir_aresta(4, 5)
    grafo_teste.inserir_aresta(4, 6)
    grafo_teste.inserir_aresta(5, 7)
    grafo_teste.inserir_aresta(7, 8)
    grafo_teste.inserir_aresta(7, 10)
    grafo_teste.inserir_aresta(10, 4)
    print(f'{HEADER}Teste Nº 2 (Inserções Arestas): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')

    grafo_teste.dividir_vertices(6, 4)
    print(f'{HEADER}Teste Nº 3 (Divisão Vértices): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')

    grafo_teste.unir_vertices(4, 7)
    print(f'{HEADER}Teste Nº 4 (União Vértices): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')

    grafo_teste.remover_vertice(9)
    grafo_teste.remover_vertice(8)
    print(f'{HEADER}Teste Nº 5 (Remoção Vértices): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')

    grafo_teste.remover_aresta(4, 10)
    grafo_teste.remover_aresta(5, 4)
    print(f'{HEADER}Teste Nº 6 (Remoção Vértices): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')

    grafo_teste.inserir_vertice(None)
    grafo_teste.inserir_aresta(8, 9)
    grafo_teste.remover_vertice(11)
    grafo_teste.remover_aresta(4, 5)
    grafo_teste.unir_vertices(11, 12)
    grafo_teste.dividir_vertices(4, 5)
    print(f'{HEADER}Teste Nº 7 (Erros): {ENDC}')
    print(f'{OKBLUE}{grafo_teste} \nQuantidade de vértices: {len(grafo_teste)}\n\n{ENDC}')


def grafo_matriz_adjacencia():
    g = Grafo(5)
    g.adicionar_aresta(0, 1)
    g.adicionar_aresta(0, 2)
    g.adicionar_aresta(1, 2)
    g.adicionar_aresta(2, 0)
    g.adicionar_aresta(2, 3)

    g.imprimir_matriz()