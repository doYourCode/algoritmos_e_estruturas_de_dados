"""
Na ciência da computação, a ordenação por seleção é um algoritmo de ordenação por comparação no local. Ele tem
uma complexidade de tempo O(n²), o que o torna ineficiente em listas grandes. A ordenação por seleção é conhecida por
sua simplicidade e tem vantagens de desempenho em relação a algoritmos mais complicados em certas situações,
particularmente em pequenos conjuntos e quando a memória auxiliar é limitada ou inexistente.
"""

__author__ = ["Tomaz Martins Batista",
              "Jean Pereira Coelho"]
__date__ = "22/05/2023"
__credits__ = ["https://www.geeksforgeeks.org/selection-sort/"]
__license__ = "GPL"
__email__ = "tmb5@aluno.ifnmg.edu.br, jpc3@aluno.ifnmg.edu.br"


def selection_sort(lista):
    """
    A função selection_sort é uma implementação do algoritmo de ordenação por seleção. Ela recebe como parâmetro uma lista de elementos 
    e retorna a mesma lista ordenada em ordem crescente. O algoritmo funciona da seguinte maneira: para cada elemento da lista, ele procura 
    o menor elemento à sua direita e troca de posição com ele. Isso é feito até que todos os elementos estejam ordenados.
    :param lista O conjunto de elementos a serem ordenados
    :return O conjunto de elementos em ordem crescente
    """
    for i in range(len(lista)):
        min_idx = i
        
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min_idx]:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista
