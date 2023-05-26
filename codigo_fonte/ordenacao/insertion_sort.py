"""
O método de ordenção Insertion Sort funciona: 
Fazendo comparações em que o menor número sempre vá para a esquerda.
Não se inicia da primeira posição, pois a lista pode ter apenas um único elemento, então ela já está ordenada.
Possui a complexidade de:
    O(n) no melhor caso.
    O(n²) no caso médio e pior caso.
Sendo assim um método de ordenação estável.
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
    quantidade_elementos = len(lista)
    for i in range(1, quantidade_elementos):
        atual = lista[i] # Pega a posição do elemento atual.
        j = i - 1

        # Compara o atual com cada elemento na esquerda dele, até que um elemento menor que ele seja encontrado.
        # Se for encontrado um elemento maior que o atual, move o atual para a esquerda deste elemento.
        # Se não for encontrado, continua na sua posição.
        while j >= 0 and lista[j] > atual:  
            lista[j + 1] = lista[j] 
            j = j - 1 
        lista[j + 1] = atual