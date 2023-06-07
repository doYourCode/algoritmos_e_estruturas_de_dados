"""
Bogosort (também conhecido como StupidSort), é um algoritmo de ordenação extremamente ineficiente. É baseado na
reordenação aleatória dos elementos. Não é utilizado na prática, mas pode ser usado no ensino de algoritmos mais
eficientes. Seu nome veio do engraçado termo quantum bogodynamics.
"""

__author__ = ["Caio Henriques Sica Lamas"]
__date__ = "25/05/2023"
__credits__ = ["https://www.geeksforgeeks.org/bogosort-permutation-sort/"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu.br"

import random


def bogo_sort(lista):
    """
    Um dos algoritmos de ordenação mais ineficientes comumente demonstrado como exemplo de algoritmo de complexidade
    que cresce de forma exponencial. Com menos de uma dezena de valores a ordenar seu tempo de execução pode ser
    indeterminado.
    :param lista O conjunto de dados que se pretende ordenar (pretende-se mesmo?
    :return O conjunto ordenado, ou executa por tempo indeterminado
    """
    def is_sorted(lista):
        if len(lista) < 2:
            return True
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                return False
        return True

    while not is_sorted(lista):
        random.shuffle(lista)
    return lista
