""" Exemplo de estrutura de lista encadeada simples e alguns algoritmos relacionados.
Essa estrutura se trata de uma sequência de nodos ligados, ou encadeadas, uns aos outros por uma referência.
Os nodos de uma lista encadeada são compostas de dois elementos cada. O primeiro elemento é o dado
efetivo a ser armazenado e o segundo se trata de uma referência para o próximo elemento da lista. A lista
encadeada simples só poderá ser transcorrida em um sentido, do início ao fim.
A principal vantagem da utilização de listas encadeadas sobre listas sequenciais é o ganho em desempenho em
termos de velocidade nas inclusões e remoções de elementos. Entretanto para acessar um item da lista é
necessário transcorrê-la em partes, ou no pior caso ,inteira.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "14/08/2022"
__credits__ = ["https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm",
               "https://towardsdatascience.com/python-linked-lists-c3622205da81",
               "https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa um único nó de uma lista """

    def __init__(self, valor=None):
        self.valor = valor
        self.proximo = None


class ListaEncadeada:
    """
    Representa uma lista cujos elementos (nós) estão encadeados por elos.
    A lista encadeada simples só pode ser iterada em um único sentido (para frente).
    """

    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    @property
    def valores(self):
        """ Conjunto dos nós. """
        return [nodo.valor for nodo in self]

    def add_inicio(self, valor):
        """ Adiciona um novo nó no início da lista. """
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        self._tamanho += 1

    def add_final(self, valor):
        """ Adiciona um novo nó ao final da lista. """
        novo_nodo = Nodo(valor)
        if self.cabeca is None:
            self.cabeca = novo_nodo
            self._tamanho += 1
            return
        ultimo = self.cabeca
        while ultimo.proximo:
            ultimo = ultimo.proximo
        ultimo.proximo = novo_nodo
        self._tamanho += 1

    def add_pos(self, pos_nodo, valor):
        """ Adiciona um novo nó em uma posição posterior à outro nó específico. """
        nodo_temp = self.busca(pos_nodo)
        if nodo_temp is None:
            print(FAIL + "ATENÇÃO!" + ENDC + " Nó '" + pos_nodo + "' não foi encontrado! Inserção não ocorreu.")
            return
        novo_nodo = Nodo(valor)
        novo_nodo.proximo = nodo_temp.proximo
        nodo_temp.proximo = novo_nodo
        self._tamanho += 1

    def remove(self, valor):
        """ Remove um nó específico. """
        nodo_temp = self.cabeca
        nodo_anterior = None
        # Se o nó a ser excluído for a cabeça da lista
        if nodo_temp is not None and nodo_temp.valor == valor:
            self.cabeca = nodo_temp.proximo
            self._tamanho -= 1
            return
        else:
            while nodo_temp is not None and nodo_temp.valor != valor:
                nodo_anterior = nodo_temp
                nodo_temp = nodo_temp.proximo
            if nodo_temp is None:
                print(FAIL + "ATENÇÃO!" + ENDC + " Nó '" + str(valor) + "' não foi encontrado! Exclusão não ocorreu.")
                return
            nodo_anterior.proximo = nodo_temp.proximo
            self._tamanho -= 1

    def busca(self, valor):
        """ Busca um nó especificado. """
        for nodo in self:
            if nodo.valor == valor:
                return nodo
        return None

    def __iter__(self):
        nodo_atual = self.cabeca
        while nodo_atual:
            yield nodo_atual
            nodo_atual = nodo_atual.proximo

    def __len__(self):
        return self._tamanho


def lista_encadeada():
    lista = ListaEncadeada()  # ........................Instancia uma nova lista (em branco)
    # Testando inserção
    lista.add_inicio("Segunda")  # .....................Insere um primeiro elemento
    lista.add_final("Terça")  # ........................Insere 2 elementos ao final da lista
    lista.add_final("Sexta")  #
    lista.add_pos("Terça", "Quarta")  # ...Insere 2 elementos após outros 2 elementos específicos (busca)
    lista.add_pos("Quarta", "Quinta")  # ..PS. Seria possível ter inserido a quarta e depois a terça?
    lista.add_final("Sábado")  # .......................Insere elemento ao final da lista
    lista.add_inicio("Domingo")  # .....................Insere elemento no início da lista
    print(HEADER + "Teste nº 1 (Inserções): " + ENDC)
    print(str(lista.valores) + OKBLUE + " Tamanho da lista: " + str(len(lista)) + ENDC)

    # Testando a remoção
    lista.add_inicio("Dia de são nunca")  # ............Insere 3 nós que não deveriam existir
    lista.add_final("Dia de São Luguinho")
    lista.add_pos("Quinta", "Dia do João Gomes")
    print(HEADER + "Teste nº 2 (Inserções equivocadas): " + ENDC)
    print(str(lista.valores) + OKBLUE + " Tamanho da lista: " + str(len(lista)) + ENDC)
    lista.remove("Dia de são nunca")  # ................Remove os 3 nós que não deveriam existir
    lista.remove("Dia de São Luguinho")
    lista.remove("Dia do João Gomes")
    print(HEADER + "Teste nº 3 (Remoções): " + ENDC)
    print(str(lista.valores) + OKBLUE + " Tamanho da lista: " + str(len(lista)) + ENDC)

    # Testando os erros
    print(HEADER + "Teste nº 4 (Erros): " + ENDC)
    lista.remove("Outro dia")  # ............................Tenta remover um nó que não existe
    lista.add_pos("Dia do trabalhador", "Oitavo dia")  # ... Tenta adicionar um nó em local que não existe
    print(str(lista.valores) + OKBLUE + " Tamanho da lista: " + str(len(lista)) + ENDC)
