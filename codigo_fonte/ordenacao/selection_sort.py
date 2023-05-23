"""
Na ciência da computação, a ordenação por seleção é um algoritmo de ordenação por comparação no local. Ele tem
uma complexidade de tempo O(n²), o que o torna ineficiente em listas grandes. A ordenação por seleção é conhecida por
sua simplicidade e tem vantagens de desempenho em relação a algoritmos mais complicados em certas situações,
particularmente em pequenos conjuntos e quando a memória auxiliar é limitada ou inexistente.
"""

__author__ = ["Tomaz Martins Batista",
              "Jean Pereira Coelho",
              "Caio Henriques Sica Lamas"]
__date__ = "22/05/2023"
__credits__ = ["https://algoritmosempython.com.br/cursos/algoritmos-python/estruturas-dados/listas-encadeadas/",
               "https://algoritmosempython.com.br/cursos/algoritmos-python/pesquisa-ordenacao/selecao/"]
__license__ = "GPL"
__email__ = "tmb5@aluno.ifnmg.edu.br, jpc3@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"


from codigo_fonte.estruturas_de_dados.lista_encadeada import ListaEncadeada


def selection_sort(lista):  # funçao Selection Sort
    # Caso base
    if lista.cabeca is None:
        return None

    # Inicialização de variáveis
    atual = lista.cabeca
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
    return lista.cabeca


minha_lista = ListaEncadeada()
minha_lista.adicionar_final(4)
minha_lista.adicionar_final(2)
minha_lista.adicionar_final(1)
minha_lista.adicionar_final(3)
minha_lista.adicionar_final(5)

print(minha_lista.valores)

lista_ordenada = selection_sort(minha_lista)

print(minha_lista.valores)
