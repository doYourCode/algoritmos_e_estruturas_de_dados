"""
O Quicksort é um algoritmo eficiente de ordenação por comparação amplamente 
utilizado na ciência da computação. Ele possui uma complexidade de tempo 
média O(n log n), tornando-o ideal para ordenar listas de tamanho médio a 
grande. O Quicksort é conhecido por sua velocidade e pelo fato de ser um 
algoritmo in-place, o que significa que requer pouca memória auxiliar. No 
entanto, em casos extremos, pode ter um desempenho mais lento, como quando 
a lista já está quase ordenada. Em geral, o Quicksort é uma opção popular 
para a maioria das situações de ordenação.
"""

__author__ = ["Gustavo da Silva Dias",
              "Luis Gustavo Barbosa Santiago",
              "Osvaldo Bispo de Andrade Neto",
              "Yan Silveira De Souza",
              "Caio Henriques Sica Lamas"]
__date__ = "26/05/2023"
__credits__ = ["https://drive.google.com/file/d/1GVur92ff65Zf2hiOlVZz2PThRr8nlW6V/view."]
__license__ = "GPL"
__email__ = "gdsd@aluno.ifnmg.edu.br, lgbs@aluno.ifnmg.edu.br, obdan@aluno.ifnmg.edu.br, ysds@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"

def partition(vetor, inicio, fim):
    pivot = vetor[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1

def quickSort1(vetor, inicio, fim):
    if inicio < fim:
        pi = partition(vetor, inicio, fim)
        quickSort1(vetor, inicio, pi - 1)
        quickSort1(vetor, pi + 1, fim)

vetor = [4, 2, 1, 6, 8, 5, 7, 75, 64, 32, 100, 3, 22, 9]

print('Vetor antes de ordenar: ', vetor)
quickSort1(vetor, 0, len(vetor) - 1)
print('Vetor depois de ordenar: ', vetor)