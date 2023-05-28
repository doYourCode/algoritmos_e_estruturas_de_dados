"""
A busca binária é um método eficiente para buscar elementos em listas ordenadas, reduzindo o tempo de busca em relação à busca linear.
A busca binária possui uma complexidade de tempo de O(log n), sendo mais efetiva que a busca linear que possui complexidade O(n).
Na busca binária, a cada iteração, o espaço de busca é reduzido pela metade. 
Dessa forma, o número de comparações necessárias para encontrar o elemento desejado cresce de forma muito mais lenta à medida que o tamanho do array aumenta.

__author__ = ["Filipe Santos Lima",
              "Gabriel Antunes Cunha",
              "Míriam Souza Leal"]
__date__ = "28/05/2023"
__credits__ = ["https://www.alura.com.br/artigos/busca-binaria-aprenda-implementar-python"]
__license__ = "GPL"
__email__ = "fsl1@aluno.ifnmg.edu.br, gac9@aluno.ifnmg.edu.br, msl10@aluno.ifnmg.edu.br"
"""


# É interessante utilizar uma lista ja ordenada, ou inserir um método de ordenação no seu código.

def busca_binaria(array, elemento):
    inicio = 0
    fim = len(array) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        if array[meio] == elemento: 
            return meio
        elif array[meio] < elemento:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1
