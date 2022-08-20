""" Exemplo de estrutura de pilha, usando encadeamento, e alguns algoritmos relacionados.

Esse tipo de implementação de pilha funcionará como as demais pilhas, porém objetiva facilitar a alocação
dinâmica de novos elementos e "evitar" o transbordamento de pilha, porém requer mais operações de alocação
e também mais memória. É util para quando desconhecemos o tamanho potencial da pilha.
"""
__author__ = ["Caio Henriques Sica Lamas",
              "Franck Allyson da Silva Rocha"]
__date__ = "17/08/2022"
__credits__ = ["https://www.ime.usp.br/~rt/mac57102012/RT555pilhalink555.pdf",
               "https://www.ufsm.br/pet/sistemas-de-informacao/2020/04/01/entendendo-listas-pilhas-e-filas/",
               "https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa um único nó de uma lista """

    def __init__(self, valor=None):
        self.valor = valor
        self.anterior = None


class PilhaEncadeada:
    """
    Representa uma pilha implementada sobre a plataforma de uma lista encadeada.
    """

    def __init__(self):
        self.topo = None
        self._tamanho = 0

    @property
    def valores(self):
        """ Conjunto de nós """
        return [nodo.valor for nodo in self]

    def adicionar(self, valor):
        """ Adiciona um novo nó ao topo da pilha """
        novo_nodo_topo = Nodo(valor)
        novo_nodo_topo.anterior = self.topo
        self.topo = novo_nodo_topo
        self._tamanho += 1
      
    def ler_topo(self):
        """ Retorna (Sem remover) o valor do topo da pilha"""
        nodo_topo = self.topo
        return nodo_topo.valor

    def remover(self):
        """ Remove o elemento do topo da pilha """
        if self.topo is None:
            print(f"{FAIL}Não há nenhum elemento na pilha!{ENDC}")
            return

        nodo_topo = self.topo
        valor = nodo_topo.valor
        self.topo = nodo_topo.anterior
        self._tamanho -= 1

        return valor

    def __iter__(self):
        nodo_topo = self.topo
        while nodo_topo:
            yield nodo_topo
            nodo_topo = nodo_topo.anterior

    def __len__(self):
        return self._tamanho


def pilha_encadeada():
    pilhaTeste = PilhaEncadeada()  # Iniciando a Pilha sem valor algum.

    # Teste de inserção
    pilhaTeste.adicionar(5)
    pilhaTeste.adicionar(7)
    pilhaTeste.adicionar(1)
    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}\n')

    # Teste de Remoção
    print(f'{HEADER} Teste Nº 2 (Remoção): {ENDC}')
    pilhaTeste.remover()
    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}')
    pilhaTeste.remover()
    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}')
    pilhaTeste.remover()  # Os três dados foram removidos, o próximo deve retornar uma mensagem
    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}')
    pilhaTeste.remover()
    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}\n')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Peek): {ENDC}')
    pilhaTeste.adicionar(7)
    pilhaTeste.adicionar(3)
    pilhaTeste.adicionar(9)
    print(f'Elemento do topo: {str(pilhaTeste.ler_topo())}')
    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}\n')

    # Teste de erro -- Sò há um erro que pode ocorrer: Tentar deletar um topo de uma pilha vazia
    print(f'{HEADER} Teste Nº 4 (Erro): {ENDC}')
    pilhaTeste.remover()
    pilhaTeste.remover()
    pilhaTeste.remover()
    pilhaTeste.remover()
    # Removi 4x pois havia criado 3 no teste anterior.

    print(f'{str(pilhaTeste.valores)} {OKBLUE} Tamanho da Pilha: {str(len(pilhaTeste))}{ENDC}')


