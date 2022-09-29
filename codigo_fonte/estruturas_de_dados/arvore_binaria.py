__author__ = ["Everton Sousa Oliveira",
              "Caio Henriques Sica Lamas"]
__date__ = "13/09/2022"
__credits__ = ["https://gist.github.com/divanibarbosa/a8662693e44ab9ee0d0e8c2d74808929"]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"

from codigo_fonte.utilidades.utilidades import *

class No:
    def __init__(self, key, dir, esq):
        '''Contrutor para iniciar o nó'''
        self.item = key
        self.dir = dir
        self.esq = esq
class Tree:
    def __init__(self):
        '''Construtor para iniciar a árvore'''
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v):
        '''
        Função para criar um novo nó

        :param v: Informação que será armazenada
        '''
        novo = No(v, None, None)
        print(f'Valor {v} adicionado com sucesso!')
        if self.root == None:
            self.root = novo
        else:  # se nao for a raiz
            atual = self.root
            while True:
                anterior = atual
                if v <= atual.item:  # ir para esquerda
                    atual = atual.esq
                    if atual == None:
                        anterior.esq = novo
                        return
                # fim da condição ir a esquerda
                else:  # ir para direita
                    atual = atual.dir
                    if atual == None:
                        anterior.dir = novo
                        return
                # fim da condição ir a direita

    def buscar(self, chave):
        '''
        Função para buscar um nó

        :return: Informação que será buscada
        '''
        if self.root == None:
            print('Árvore vazia!')
            return None
        atual = self.root
        while atual.item != chave:
            if chave < atual.item:
                atual = atual.esq
            else:
                atual = atual.dir
            if atual == None:
                print(f'Valor {chave} nao encontrado!')
                return None
        print(f'Valor {chave} encontrado!')
        return atual

    def nosucessor(self, apaga):
        '''
        O sucessor é o Nó mais a esquerda da subarvore a direita do Nó que foi passado como parametro do método

        :return: Nó mais a esquerda
        '''
        paidosucessor = apaga
        sucessor = apaga
        atual = apaga.dir

        while atual != None:
            paidosucessor = sucessor
            sucessor = atual
            atual = atual.esq
        if sucessor != apaga.dir:
            paidosucessor.esq = sucessor.dir
            sucessor.dir = apaga.dir
        return sucessor

    def remover(self, v):
        '''
        Função para remover um elemento superior da Pilha

        :param v: Informação que será removida
        '''
        if self.root == None:
            print(f'Valor {v} removido com sucesso!')
            return False
        atual = self.root
        pai = self.root
        filho_esq = True
        # Buscando o valor
        while atual.item != v:
            pai = atual
            if v < atual.item:
                atual = atual.esq
                filho_esq = True
            else:
                atual = atual.dir
                filho_esq = False
            if atual == None:
                return False

        if atual.esq == None and atual.dir == None:
            print(f'Valor {v} removido com sucesso!')
            if atual == self.root:
                self.root = None
            else:
                if filho_esq:
                    pai.esq = None
                else:
                    pai.dir = None

        elif atual.dir == None:
            print(f'Valor {v} removido com sucesso!')
            if atual == self.root:
                self.root = atual.esq
            else:
                if filho_esq:
                    pai.esq = atual.esq
                else:
                    pai.dir = atual.esq
        elif atual.esq == None:
            print(f'Valor {v} removido com sucesso!')
            if atual == self.root:
                self.root = atual.dir
            else:
                if filho_esq:
                    pai.esq = atual.dir
                else:
                    pai.dir = atual.dir
        else:
            print(f'Valor {v} removido com sucesso!')
            sucessor = self.nosucessor(atual)
            if atual == self.root:
                self.root = sucessor
            else:
                if filho_esq:
                    pai.esq = sucessor
                else:
                    pai.dir = sucessor
            sucessor.esq = atual.esq
        return True

    def altura(self, atual):
        '''
        Função para retornar a altura da árvore

        :return: Alturo em que a árvore se encontra
        '''
        if atual == None or atual.esq == None and atual.dir == None:
            return 0
        else:
            if self.altura(atual.esq) > self.altura(atual.dir):
                return 1 + self.altura(atual.esq)
            else:
                return 1 + self.altura(atual.dir)

    def folhas(self, atual):
        '''
        Função para mostrar quantas "folhas" tem na árvore

        :return: Quantidade de subárvores
        '''
        if atual == None:
            return 0
        if atual.esq == None and atual.dir == None:
            return 1
        return self.folhas(atual.esq) + self.folhas(atual.dir)

    def contarNos(self, atual):
        '''
        Função para contar quantos nós foram criados

        :return: Quantidade de nós
        '''
        if atual == None:
            return 0
        else:
            return 1 + self.contarNos(atual.esq) + self.contarNos(atual.dir)

    def caminhar(self):
        '''
        Função para ler a árvore

        :return: Altura da árvore, quantidade de subárvores e quantidade de nós
        '''
        print('Altura da arvore: %d' % (self.altura(self.root)))
        print('Quantidade de folhas: %d' % (self.folhas(self.root)))
        print('Quantidade de Nós: %d' % (self.contarNos(self.root)))

if __name__ == '__main__':
    arvore_teste = Tree()

    # Testando inserção
    print(f'\n{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    arvore_teste.inserir(3)
    arvore_teste.inserir(4)
    arvore_teste.inserir(5)
    arvore_teste.inserir(9)
    arvore_teste.inserir(10)
    arvore_teste.inserir(12)
    arvore_teste.inserir(15)
    arvore_teste.inserir(125)
    arvore_teste.caminhar()

    # Teste de remoção
    print(f'\n{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    arvore_teste.remover(3)
    arvore_teste.remover(4)
    arvore_teste.remover(5)
    arvore_teste.remover(9)
    arvore_teste.caminhar()

    # Teste de busca
    print(f'\n{HEADER}Teste Nº 3 (Busca): {ENDC}')
    arvore_teste.buscar(99)
    arvore_teste.buscar(10)