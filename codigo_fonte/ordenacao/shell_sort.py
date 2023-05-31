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

# COMENTÁRIOS DO PROFESSOR (FAVOR APAGAR ISSO APÓS CORREÇÃO)
# a docstring, pra funcionar, tem que vir logo abaixo do nome da função, e objetiva informar o que a função faz, qual
# parâmetro recebe e o que entrega como retorno
# PEP 8 E302 -> esperava 2 linhas em branco entre o cabeçalho e a docstring da função, só há uma linha
def shell_sort(array):
    """gap recebe metade do valor do array""" # Não é necessário comentar interno à função, pode apagar todos
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
    """Retorna o array ordenado""" # Como mencionei, a docstring vem acima do nome da função, nos moldes acima
    # mencionados. Pode apagar esta aqui também.




# PEP 8 292 -> Só é necessária UMA linha em branco ao final do arquivo