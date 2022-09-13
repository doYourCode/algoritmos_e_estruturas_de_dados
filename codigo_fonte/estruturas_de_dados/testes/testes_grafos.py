from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.grafo import Grafo


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
