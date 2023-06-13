"""
O método de ordenação Insertion Sort funciona: 
Fazendo comparações em que o menor número sempre vá para a esquerda.
Possui a complexidade de:
    O(n) no melhor caso.
    O(n²) no caso médio e pior caso.
"""

__author__ = ["Caio César Oliveira Silva",
              "José Rodrigues Costa Júnior",
              "Jhonatan Rotta Santana",
              "Anthony Henrique de Souza Guimarães"]
__date__ = "26/05/2023"
__credits__ = ["https://youtu.be/S5no2qT8_xg"]
__license__ = "GPL"
__email__ = "ccos1@aluno.ifnmg.edu.br", "jrcj@aluno.ifnmg.edu.br", "jrs7@aluno.ifnmg.edu.br", "ahdsg@aluno.ifnmg.edu.br"


def insertion_sort(lista):
    """
    Método de ordenação que compara cada elemento, a partir da segunda posição, com os outros na esquerda dele. Se for
    encontrado um elemento maior que ele, move ele para a esquerda deste elemento. Se não for encontrado, ele continua
    na sua posição.
    :param lista Conjunto de elementos que serão ordenados
    :return Conjunto de elementos ordenado
    """
    quantidade_elementos = len(lista)
    for i in range(1, quantidade_elementos):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:  
            lista[j + 1] = lista[j] 
            j = j - 1

        lista[j + 1] = atual

    return lista
