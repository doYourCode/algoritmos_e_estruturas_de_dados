"""
O shell sort é um algoritmo de ordenação que divide a lista em subgrupos usando um espaçamento inicial, e depois
realiza repetidas passagens de classificação por inserção em cada subgrupo para ordenar de forma eficiente os elementos.
O shell sort tem grau de complexidade O(N^2).
"""

__author__ = ["Murilo Santos Gonçalves",
              "João Eduardo Ferreira Souza",
              "Givanildo Barbosa Sousa Filho"]
__date__ = "26/05/2023"
__credits__ = ["https://www.geeksforgeeks.org/shellsort/"]
__license__ = "GPL"
__email__ = "msg2@aluno.ifnmg.edu.br, jefs1@aluno.ifnmg.edu.br, gbsf@aluno.ifnmg.edu.br"


def shell_sort(array):
    """
    Metodo de ordenação shell sort, dividir e conquistar.
    :param array de elementos que serão ordenados
    :return Conjunto de elementos ordenado
    """
    gap = len(array) // 2

    while gap > 0:
        for i in range(gap, len(array)):
            temp = array[i]
            y = i

            while y >= gap and array[y - gap] > temp:
                array[y] = array[y - gap]
                y -= gap

            array[y] = temp
        gap //= 2
    return array
