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
# COMENTÁRIOS DO PROFESSOR (APAGAR APÓS CORRIGIR)
# PEP 8 E 302 -> 2 linhas em branco entre cabeçalho e docstring da função
# PEP 8 E292 -> é necessário UMA linha em branco ao final do arquivo
# Usamos docstring na linha que sucede o nome da função, para documentar o que a função faz, seus parametros e retorno
# esperado
# Não é necessário comentários dentro da função, apenas a docstring, favor pesquisar sobre como implementar docstring,
# é o comentário com 3 aspas
def selection_sort(nums):
    for i in range(len(nums)):
        # Encontra o índice do menor elemento restante no subarray não ordenado
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        # Troca o elemento atual com o menor elemento encontrado
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums