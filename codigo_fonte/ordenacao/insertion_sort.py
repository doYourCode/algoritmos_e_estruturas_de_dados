"""
O método de ordenação Insertion Sort funciona: 
Comparando cada elemento com cada um dos outros na esquerda dele, até que um elemento menor que ele seja encontrado.
Se for encontrado um elemento maior que ele, move ele para a esquerda deste elemento.
Se não for encontrado, ele continua na sua posição.
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
# COMENTÁRIO DO PROFESSOR (APAGAR APOS CORRIGIR)
# PEP 8 E 302 -> 2 linhas em branco entre cabeçalho e docstring da função
# Usamos docstring na linha que sucede o nome da função, para documentar o que a função faz, seus parametros e retorno
# esperado
def insertion_sort(lista):
    quantidade_elementos = len(lista)
    for i in range(1, quantidade_elementos):
        atual = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > atual:  
            lista[j + 1] = lista[j] 
            j = j - 1 

        lista[j + 1] = atual
