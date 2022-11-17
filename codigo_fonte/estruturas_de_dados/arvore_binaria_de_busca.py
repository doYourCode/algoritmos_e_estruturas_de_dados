__author__ = ["Everton Sousa Oliveira",
              "Caio Henriques Sica Lamas",
              "Franck Allyson da Silva Rocha"]
__date__ = "13/09/2022"
__credits__ = ["https://gist.github.com/divanibarbosa/a8662693e44ab9ee0d0e8c2d74808929",
               "https://www.onlinegdb.com/4ee0CIOLH"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br, fasr@aluno.ifnmg.edu.br"

from codigo_fonte.utilidades.utilidades import *


class No:
    def __init__(self, chave=None):
        """Contrutor para iniciar o nó"""
        self.item = chave
        self.dir = None
        self.esq = None


class ArvoreBinariaDeBusca:
    def __init__(self):
        """Construtor para iniciar a árvore"""

        self.raiz = None

    """ @property
    def valores(self):
        return [nodo.item for nodo in self]"""

    def inserir(self, v):
        """
        Função para criar um novo nó

        :param v: Informação que será armazenada
        """
        novo = No(v)

        if self.raiz is None:
            self.raiz = novo
            print(f'{OKGREEN}Raíz {v} inserida com sucesso!{ENDC}')
        else:  # se nao for a raiz
            atual = self.raiz
            while True:
                anterior = atual
                if v <= atual.item:  # ir para esquerda
                    atual = atual.esq
                    if atual is None:
                        anterior.esq = novo
                        print(f'{OKGREEN}Valor {v} adicionado com sucesso!{ENDC}')
                        return
                # fim da condição ir a esquerda
                else:  # ir para direita
                    atual = atual.dir
                    if atual is None:
                        anterior.dir = novo
                        print(f'{OKGREEN}Valor {v} adicionado com sucesso!{ENDC}')
                        return
                # fim da condição ir a direita

    def buscar(self, chave):
        """
        Função para buscar um nó através de sua chave

        :return: Informação encontrada | None caso não encontrar
        """

        if self.raiz is None:
            print(f'{FAIL}Árvore vazia!{ENDC}')
            return None
        atual = self.raiz
        while atual.item != chave:
            if chave < atual.item:
                atual = atual.esq
            else:
                atual = atual.dir

            if atual is None:
                print(f'{FAIL}Valor {chave} nao encontrado!{ENDC}')
                return None
        print(f'{OKBLUE}Valor {chave} encontrado{ENDC}!')
        return atual

    def nosucessor(self, no):
        """
        O sucessor é o Nó mais a esquerda da subarvore a direita do Nó que foi passado como parametro do método

        :param no: Nó pertencente a arvore
        :return: Sucessor mais próximo do nó recebido
        """

        sucessor = no.dir

        while sucessor.esq is not None:
            sucessor = sucessor.esq
        return sucessor

    def busca_no_pai(self, no):
        atual = self.raiz
        pai = None
        while atual != no:
            pai = atual
            if no.item < atual.item:
                atual = atual.esq
            else:
                atual = atual.dir
            if atual is None:
                return False
        return pai

    def remover(self, v):
        """
        Função para remover um elemento da Árvore

        :param v: Informação que será removida
        """

        if self.raiz is None:
            print(f'{WARNING}Árvore Vazia!{ENDC}')
            return False

        atual = self.buscar(v)

        if atual is None:
            return False

        no_pai = self.busca_no_pai(atual)

        if atual.esq is None and atual.dir is None:

            if atual == self.raiz:
                self.raiz = None
            else:
                if no_pai.esq == atual:
                    no_pai.esq = None
                if no_pai.dir == atual:
                    no_pai.dir = None
                print(f'{WARNING}Valor {v} removido com sucesso!{ENDC}')

        elif atual.dir is None:
            if atual == self.raiz:
                self.raiz = atual.esq
            else:
                if no_pai.esq == atual:
                    no_pai.esq = atual.esq
                if no_pai.dir == atual:
                    no_pai.dir = atual.esq
                print(f'{WARNING}Valor {v} removido com sucesso!{ENDC}')
        elif atual.esq is None:
            if atual == self.raiz:
                self.raiz = atual.dir
            else:
                if no_pai.esq == atual:
                    no_pai.esq = atual.dir
                if no_pai.dir == atual:
                    no_pai.dir = atual.dir
            print(f'{WARNING}Valor {v} removido com sucesso!{ENDC}')
        else:
            sucessor = self.nosucessor(atual)

            pai_do_sucessor = self.busca_no_pai(sucessor)

            if pai_do_sucessor != atual:
                pai_do_sucessor.esq = sucessor.dir
                sucessor.dir = atual.dir

            sucessor.esq = atual.esq

            if atual == self.raiz:
                self.raiz = sucessor
            else:

                if no_pai.esq == atual:
                    no_pai.esq = sucessor
                if no_pai.dir == atual:
                    no_pai.dir = sucessor

            print(f'{WARNING}Valor {v} removido com sucesso!{ENDC}')
        return True

    def altura(self, atual):
        """
        Função para retornar a altura de um nó, retornando a altura da árvore caso use a raiz

        :param atual: Nó pertencente à árvore.
        :return: Altura do nó
        """
        if atual is None or atual.esq is None and atual.dir is None:
            return 1
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return 1 + self.altura(atual.esq)
            else:
                return 1 + self.altura(atual.dir)

    def folhas(self, atual):
        """
        Função para mostrar quantas "folhas" tem na árvore

        :param atual: Nó raiz
        :return: Todas as folhas a partir do nó raiz.
        """
        if atual is None:
            return 0
        if atual.esq is None and atual.dir is None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)

    def contar_nos(self, atual):
        """
        Função para contar quantos nós foram criados

        :param atual: Nó raiz
        :return: Quantidade de nós a partir do nó raiz
        """
        if atual is None:
            return 0
        else:
            return 1 + self.contar_nos(atual.esq) + self.contar_nos(atual.dir)

    def caminhar(self):
        """
        Função para ler a árvore

        :return: Altura da árvore, quantidade de subárvores e quantidade de nós
        """
        print('Altura da arvore: %d' % (self.altura(self.raiz)))
        print('Quantidade de folhas: %d' % (self.folhas(self.raiz)))
        print('Quantidade de Nós: %d' % (self.contar_nos(self.raiz)))

    """def _percorre_arvore(self, nodo):
        if not nodo:
            return

        self._percorre_arvore(nodo.esq).item
        yield
        self._percorre_arvore(nodo.dir)

    def __iter__(self):
        for nodo in self._percorre_arvore(self.raiz):
            yield nodo"""
