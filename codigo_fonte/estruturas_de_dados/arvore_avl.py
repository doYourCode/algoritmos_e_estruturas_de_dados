"""Árvore AVL é uma árvore binária de busca balanceada[2], ou seja,
uma árvore balanceada (árvore completa) são as árvores que minimizam
o número de comparações efetuadas no pior caso para uma busca com chaves
de probabilidades de ocorrências idênticas."""

__author__ = "Franck Allyson da Silva Rocha"
__date__ = "04/11/2022"
__credits__ = ["https://pt.wikipedia.org/wiki/%C3%81rvore_AVL",
               "https://www.educba.com/types-of-trees-in-data-structure/",
               "https://www.youtube.com/watch?v=I5cl39jdnow&ab_channel=Programa%C3%A7%C3%A3oDescomplicada",
               "https://www.inf.ufsc.br/~aldo.vw/estruturas/simulador/AVL.html"]
__license__ = "GPL"
__email__ = "fasr@aluno.ifnmg.edu.br"

from codigo_fonte.utilidades.utilidades import *


class Nodo:
    """ Representa um único nó da árvore. """

    def __init__(self, registro=None, fator_balanco=0):
        """ Construtor do nó """

        self.registro = registro
        self.fator_balanco = fator_balanco
        self.filho_esquerda = None
        self.filho_direita = None


class ArvoreAvl:
    """ Representa uma árvore binária balanceada e as operações sobre ela """

    def __init__(self):
        """ Construtor para iniciar a árvore """

        self.raiz = None

    def inserir(self, raiz, valor):
        """
        Função Recursiva para inserir o valor desejado.

        :param raiz: Nó atual da recursividade, iniciando sempre da raíz.
        :param valor: Valor a ser adicionado.
        :return: True: Adicionado  | False: Valor já existente.
        """
        nodo = Nodo(valor)

        if self.vazia():
            self.raiz = nodo
            print(f'{OKGREEN}Raiz {valor} Adicionada com sucesso!!{ENDC}\n')
            return True

        nodo_pai = self.no_pai_inserir(nodo)
        nodo_atual = raiz

        if not nodo_atual:
            if nodo.registro < nodo_pai.registro:
                nodo_pai.filho_esquerda = nodo
            else:
                nodo_pai.filho_direita = nodo
            print(f'{OKGREEN}Valor {valor} adicionado com sucesso!{ENDC}\n')
            return True

        if valor < nodo_atual.registro:

            if self.inserir(nodo_atual.filho_esquerda, valor):

                if self.fator_balanceamento(nodo_atual) >= 2:

                    print(f'{WARNING}Árvore Desbalanceada\nExecutando Balanceamento...{ENDC}')
                    if valor < raiz.filho_esquerda.registro:
                        self.rotacao_direita_simples(raiz)
                    else:
                        self.rotacao_direita_dupla(raiz)
                    print(f'{OKBLUE}Balanceamento Finalizado!\n{ENDC}')
        elif valor > nodo_atual.registro:
            if self.inserir(nodo_atual.filho_direita, valor):
                if self.fator_balanceamento(nodo_atual) >= 2:
                    print(f'{WARNING}Árvore Desbalanceada\nExecutando Balanceamento...{ENDC}')
                    if valor > raiz.filho_direita.registro:
                        self.rotacao_esquerda_simples(raiz)
                    else:
                        self.rotacao_esquerda_dupla(raiz)
                    print(f'{OKBLUE}Balanceamento Finalizado!\n{ENDC}')
        else:
            print(f'{FAIL}Valor já existente na árvore!{ENDC}\n')

            return False

        nodo_atual.fator_balanco = self.fator_balanceamento(nodo_atual)

        return True

    def remover(self, raiz, nodo_registro):
        """
        Função recursiva para remover um valor da árvore

        :param raiz: Nó atual da recursividade, iniciando sempre da raíz.
        :param nodo_registro: Registro do nó que será removido
        :return: True: Sucesso na remoção  | False: Não ocorreu a remoção
        """
        if not self.raiz:
            print(f'{WARNING}Não existe raíz!{ENDC}')
            return False
        if not raiz:
            print(f'{FAIL}Valor selecionado para a remoção não existe!{ENDC}')
            return False

        if nodo_registro < raiz.registro:
            if self.remover(raiz.filho_esquerda, nodo_registro):
                if self.fator_balanceamento(raiz) >= 2:
                    print(f'{WARNING}Árvore Desbalanceada\nExecutando Balanceamento...{ENDC}')
                    if self.altura(raiz.filho_direita.filho_esquerda) <= self.altura(raiz.filho_direita.filho_direita):
                        self.rotacao_esquerda_simples(raiz)
                    else:
                        self.rotacao_esquerda_dupla(raiz)
                    print(f'{OKBLUE}Balanceamento Finalizado!\n{ENDC}')
        elif nodo_registro > raiz.registro:
            if self.remover(raiz.filho_direita, nodo_registro):
                if self.fator_balanceamento(raiz) >= 2:
                    print(f'{WARNING}Árvore Desbalanceada\nExecutando Balanceamento...{ENDC}')
                    if self.altura(raiz.filho_esquerda.filho_direita) <= self.altura(raiz.filho_esquerda.filho_esquerda):
                        self.rotacao_direita_simples(raiz)
                    else:
                        self.rotacao_direita_dupla(raiz)
                    print(f'{OKBLUE}Balanceamento Finalizado!\n{ENDC}')
        else:
            no_pai = self.no_pai(raiz)
            if raiz.filho_esquerda is None or raiz.filho_direita is None:
                if raiz.filho_esquerda is not None:
                    if raiz.registro < no_pai.registro:
                        no_pai.filho_esquerda = raiz.filho_esquerda
                    else:
                        no_pai.filho_direita = raiz.filho_esquerda
                else:
                    if raiz.registro < no_pai.registro:
                        no_pai.filho_esquerda = raiz.filho_direita
                    else:
                        no_pai.filho_direita = raiz.filho_direita
            else:
                no_temp = self.procura_antecessor(raiz.filho_esquerda)

                no_pai_temp = self.no_pai(no_temp)
                no_pai_temp.filho_direita = None
                raiz.registro = no_temp.registro

                if self.fator_balanceamento(raiz) >= 2:
                    if self.altura(raiz.filho_esquerda.filho_direita) <= self.altura(raiz.filho_esquerda.filho_esquerda):
                        self.rotacao_direita_simples(raiz)
                    else:
                        self.rotacao_direita_dupla(raiz)

            raiz.fator_balanco = self.fator_balanceamento(raiz)
            print(f'{OKCYAN}Valor {nodo_registro} removido com sucesso!{ENDC}')
            return True

        raiz.fator_balanco = self.fator_balanceamento(raiz)

        return True

    def buscar(self, nodo_registro):
        """
        Função para buscar um valor na árvore

        :param nodo_registro: Registro do nó desejado
        :return: Nó Encontrado | None caso não encontrar
        """
        nodo_atual = self.raiz
        while nodo_atual:
            if nodo_registro < nodo_atual.registro:
                nodo_atual = nodo_atual.filho_esquerda
            elif nodo_registro > nodo_atual.registro:
                nodo_atual = nodo_atual.filho_direita
            else:
                return nodo_atual
        print(f'{FAIL}Nó não existe!{ENDC}')
        return None

    def rotacao_direita_simples(self, raiz):
        """
        Faz o balanço da árvore em uma volta à direita.

        :param raiz: Nó que está sendo balanceado.
        :return:
        """
        nodo = raiz.filho_esquerda
        raiz.filho_esquerda = nodo.filho_direita
        nodo.filho_direita = raiz

        if raiz == self.raiz:
            self.raiz = nodo
        else:

            no_pai = self.no_pai(raiz)

            if nodo.registro < no_pai.registro:
                no_pai.filho_esquerda = nodo
            else:
                no_pai.filho_direita = nodo

    def rotacao_esquerda_simples(self, raiz):
        """
        Faz o balanço da árvore em uma volta à esquerda

        :param raiz: Nó que está sendo balanceado
        :return:
        """
        nodo = raiz.filho_direita
        raiz.filho_direita = nodo.filho_esquerda
        nodo.filho_esquerda = raiz

        if raiz == self.raiz:
            self.raiz = nodo
        else:
            no_pai = self.no_pai(raiz)
            if nodo.registro < no_pai.registro:
                no_pai.filho_esquerda = nodo
            else:
                no_pai.filho_direita = nodo

    def rotacao_direita_dupla(self, raiz):
        """
        Também conhecida como LR ( Left - Right ), faz dois giros, um à esquerda seguido de outro à direita.
        Usada nos casos em que o nó que causou o desbalanceamento não está na mesma direção do filho à esquerda.

        :param raiz: Nó que receberá o balanceamento
        :return:
        """
        raiz_atual = raiz.filho_esquerda
        nodo = raiz_atual.filho_direita
        raiz_atual.filho_direita = nodo.filho_esquerda
        nodo.filho_esquerda = raiz_atual
        raiz.filho_esquerda = nodo.filho_direita
        nodo.filho_direita = raiz

        if raiz == self.raiz:
            self.raiz = nodo
        else:
            nodo_pai = self.no_pai(raiz)
            if nodo.registro < nodo_pai.registro:
                nodo_pai.filho_esquerda = nodo
            else:
                nodo_pai.filho_direita = nodo

    def rotacao_esquerda_dupla(self, raiz):
        """
        Também conhecida como RL ( Right - Left ), faz um giro à direita seguido de outro à esquerda.
        Usada quando o nó que causou o desbalanceamento não está na mesma direção do filho à direita.

        :param raiz:
        :return:
        """
        raiz_atual = raiz.filho_direita
        nodo = raiz_atual.filho_esquerda
        raiz_atual.filho_esquerda = nodo.filho_direita
        nodo.filho_direita = raiz_atual
        raiz.filho_direita = nodo.filho_esquerda
        nodo.filho_esquerda = raiz

        if raiz == self.raiz:
            self.raiz = nodo
        else:
            nodo_pai = self.no_pai(raiz)
            if nodo.registro < nodo_pai.registro:
                nodo_pai.filho_esquerda = nodo
            else:
                nodo_pai.filho_direita = nodo

    def altura(self, nodo):
        """
        Função para retornar a altura de um nó, retornando a altura da árvore caso use a raiz

        :param nodo: Nó pertencente à árvore.
        :return: Altura do nó
        """
        if not nodo:
            return 0

        if nodo is None or nodo.filho_esquerda is None and nodo.filho_direita is None:
            return 1
        else:
            if self.altura(nodo.filho_esquerda) > self.altura(nodo.filho_direita):
                return 1 + self.altura(nodo.filho_esquerda)
            else:
                return 1 + self.altura(nodo.filho_direita)

    def fator_balanceamento(self, nodo):
        """
        Testa o fator de balanceamento de um nó especifico

        :param nodo: Nó a ser testado
        :return: Valor absoluto do fator de balanceamento
        """
        return abs(self.altura(nodo.filho_esquerda) - self.altura(nodo.filho_direita))

    def procura_antecessor(self, nodo):
        """
        Função auxiliar á remoção, busca o antecessor mais proximo do nó

        :param nodo: Nó à esquerda do desejado
        :return: Nó mais a direita da sub-árvore da esquerda.
        """
        nodo_atual = nodo
        while nodo_atual.filho_direita:
            nodo_atual = nodo_atual.filho_direita

        return nodo_atual

    def no_pai_inserir(self, nodo):
        """
        Função no_pai auxiliar para inserir

        :param nodo: Nó a ser inserido
        :return: O Nó que SERÁ o pai do novo nó | None: se o registro já existir
        """
        nodo_atual = self.raiz
        while True:
            if nodo.registro < nodo_atual.registro:
                if not nodo_atual.filho_esquerda:
                    return nodo_atual
                nodo_atual = nodo_atual.filho_esquerda
            elif nodo.registro > nodo_atual.registro:
                if not nodo_atual.filho_direita:
                    return nodo_atual
                nodo_atual = nodo_atual.filho_direita
            else:
                return None

    def no_pai(self, nodo):
        """
        Busca o pai de um nó existente

        :param nodo: Nó desejado
        :return: Pai do nó ou a raiz da árvore | None: Caso não exista pai
        """
        nodo_atual = self.raiz
        if nodo_atual == nodo:
            return nodo_atual

        while True:

            if not nodo_atual:
                return None
            if nodo_atual.filho_esquerda == nodo or nodo_atual.filho_direita == nodo:
                break

            if nodo.registro > nodo_atual.registro:
                nodo_atual = nodo_atual.filho_direita
            elif nodo.registro < nodo_atual.registro:
                nodo_atual = nodo_atual.filho_esquerda

        return nodo_atual

    def ler_no(self, nodo):
        """
        Lê os dados dentro do nó

        :param nodo: Nó a ser lido
        :return: Registro do nó lido
        """
        return nodo.registro

    def vazia(self):
        """
        Testa se a árvore está vazia

        :return: True: Está vazia | False: Não está vazia
        """
        if not self.raiz:
            return True
        return False

    def folhas(self, atual):
        """
        Função para mostrar quantas "folhas" tem na árvore

        :param atual: Nó raiz
        :return: Todas as folhas a partir do nó raiz.
        """
        if atual is None:
            return 0
        if atual.filho_esquerda is None and atual.filho_direita is None:
            return 1
        return self.folhas(atual.filho_esquerda) + self.folhas(atual.filho_direita)

    def contar_nos(self, atual):
        """
        Função para contar quantos nós foram criados

        :param atual: Nó raiz
        :return: Quantidade de nós a partir do nó raiz
        """
        if atual is None:
            return 0
        else:
            return 1 + self.contar_nos(atual.filho_esquerda) + self.contar_nos(atual.filho_direita)

    def caminhar(self):
        """
        Função para ler a árvore

        :return: Altura da árvore, quantidade de subárvores e quantidade de nós
        """
        print(f'{OKBLUE}Registro da Raíz: {self.raiz.registro}')
        print(f'Altura da arvore: {self.altura(self.raiz)}')
        print(f'Quantidade de folhas: {self.folhas(self.raiz)}')
        print(f'Quantidade de Nós: {self.contar_nos(self.raiz)}{ENDC}')
        print(f'--'*20)
