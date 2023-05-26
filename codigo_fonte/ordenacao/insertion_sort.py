"""
O método Insertion Sort lida com a ordenação: 
Fazendo comparações que o menor número sempre vá para a esquerda.
Não se inicia da primeira posição, pois a lista pode ter apenas um único elemento, então nesse caso a lista se inicia com 0.
Possui a complexidade de:
    O(n) no melhor caso.
    O(n²) no caso médio e pior caso.
Sendo assim um método de ordenação estável.
"""

__author__ = ["Caio César Oliveira Silva",
              "José Rorigues Costa Júnior",
              "Jhonatan Rotta Santana",
              "Anthony Henrique de Souza Guimarães"]
__date__ = "26/05/2023"
__credits__ = ["https://youtu.be/S5no2qT8_xg"]
__license__ = "GPL"
__email__ = "ccos1@aluno.ifnmg.edu.br", "jrcj@aluno.ifnmg.edu.br", "jrs7@aluno.ifnmg.edu.br", "ahdsg@aluno.ifnmg.edu.br"

def insertion_sort(lista):
    quantidade_elementos = len(lista)
    for i in range(1, quantidade_elementos):
        atual = lista[i] # Pega a posição do elemento e começa do segundo item que compara com o anterior.
        j = i - 1
        while j >= 0 and lista[j] > atual:  # Se for menor que o anterior ele vai para trás.
                                            # Se o anterior for maior ele, ele vai para frente.  
                                            # Se for igual não fará nada.
            lista[j + 1] = lista[j] 
            j = j - 1  
        lista[j + 1] = atual