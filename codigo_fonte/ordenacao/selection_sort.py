"""
Ordenação por seleção (SELECTION SORT).
Um problema bem clássico dentro da área de algoritmo e a ordenação
O objetivo do Selection Sort e colocar em ordem crescente um conjunto de dados que geralmente vem em forma de lista. 
O algoritmo percorre uma lista de dados desordenada comparando os elementos entre si, para determinar qual é o elemento de menor valor.
Encontrado o elemento de menor valor esse elemento será trocado com o elemento que estiver na primeira posição da lista.
O elemento que estava na primeira posição sera posicionado no lugar em que o elemento definido como menor estava inicialmente.
Apos encontrado o primeiro elemento, continua-se o processo buscando o elemento de segundo menor valor.
Depois de encontrado ele será trocado com o elemento que estivar na segunda posição da lista.
Esse processo será realizado com (n-1) elementos da lista.
No final do processo vai se obter uma lista ordenada.
"""
__author__ = ["Tomaz Martins Batista",
              "Jean Pereira Coelho",
              "Caio Henriques Sica Lamas"]
__date__ = "22/05/2023"
__credits__ = ["https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/listas-encadeadas/",
               "https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/selecao/"]
__license__ = "GPL"
__email__ = "tmb5@aluno.ifnmg.edu.br, jpc3@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br" 

class Nodo:
    def __init__(self, valor): # # Construtor para inicializar o objeto nó
        self.valor = valor
        self.proximo = None
        
class ListaEncadeada: # classe da lista encadeada 
    def __init__(self):
        self.cabeca = None
        
    def adicionar(self, novo_valor):  
        novo_nodo = Nodo(novo_valor) # cria um novo nó
        novo_nodo.proximo = self.cabeca # o novo nó passa a ser a cabeça da lista.
        self.cabeca = novo_nodo # cabeça da lista recebe novo nó
        
    def selection_sort(self): # funçao Selection Sort
        # Caso base
        if self.cabeca is None:
            return None
        
        # Inicialização de variáveis
        atual = self.cabeca
        while atual.proximo:
            nodo_minimo = atual
            nodo_proximo = atual.proximo
            while nodo_proximo:
                if nodo_proximo.valor < nodo_minimo.valor:
                    nodo_minimo = nodo_proximo
                nodo_proximo = nodo_proximo.proximo
                
            # Trocar os nós correspondentes
            atual.valor, nodo_minimo.valor = nodo_minimo.valor, atual.valor
            atual = atual.proximo
        
        return self.cabeca

    def esta_vazia(self):
        # Verifica se a lista está vazia.
        return self.cabeca is None

lista_encadeada = ListaEncadeada()
lista_encadeada.adicionar(4)
lista_encadeada.adicionar(2)
lista_encadeada.adicionar(1)
lista_encadeada.adicionar(3)
lista_encadeada.adicionar(5)

# Testando se a lista está vazia.
print(lista_encadeada.esta_vazia()) 
# False = não está vazia 
# True = está vazia

lista_ordenada = lista_encadeada.selection_sort()
while lista_ordenada:
    print(lista_ordenada.valor)
    lista_ordenada = lista_ordenada.proximo



