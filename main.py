""" Exemplos de estruturas de dados implementadas em Python
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "14/08/2022"
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.utilidades.imports import *


if __name__ == '__main__':

    lista = [72, 13, 26, 109, 40, 1, 9]
    executar_p(teste_selection_sort, lista)
    executar_p(teste_insertion_sort, lista)
    executar_p(teste_bogo_sort, lista)
