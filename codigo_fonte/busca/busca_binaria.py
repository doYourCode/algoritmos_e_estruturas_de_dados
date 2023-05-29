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
  #define inicio do array
  inicio = 0 
  #define fim do array pelo tamanho do array -1
  fim = len(array) - 1
  #enquanto o inicio for menor ou igual ao fim
  while inicio <= fim:
      #define o meio do array como a soma do inicio e fim dividido por 2
      meio = (inicio + fim) // 2
      #se o elemento for igual ao meio do array, retorna o meio, o indice do elemento
      if array[meio] == elemento: 
          return meio
      #se o elemento for maior que o meio do array, define o inicio como meio + 1
      elif array[meio] < elemento:
          inicio = meio + 1
      #se o elemento for menor que o meio do array, define o fim como meio - 1
      else:
          fim = meio - 1
  #se o elemento nao for encontrado, retorna -1
  return -1

#para usar a funcao de busca binaria recursiva, basta chamar a funcao passando o array e o elemento a ser buscado, o inicio e fim do array 
def busca_Binaria_Recursiva(array, elemento, inicio, fim):
    #se o inicio for maior que o fim, retorna -1
    if inicio > fim:
        return -1
    #define o meio do array como a soma do inicio e fim dividido por 2
    meio = (inicio + fim) // 2
    #se o elemento for igual ao meio do array, retorna o meio, o indice do elemento
    if array[meio] == elemento:
        return meio
    #se o elemento for maior que o meio do array, chama a funcao novamente, definindo o inicio como meio + 1
    elif array[meio] < elemento:
        return busca_Binaria_Recursiva(array, elemento, meio + 1, fim)
    #se o elemento for menor que o meio do array, chama a funcao novamente, definindo o fim como meio - 1
    else:
        return busca_Binaria_Recursiva(array, elemento, inicio, meio - 1)
