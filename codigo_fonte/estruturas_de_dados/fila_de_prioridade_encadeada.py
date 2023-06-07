__author__ = 'Jônatas Pereira da Rocha'
__date__ = '05/06/2023'
__credits__ = ''
__license__ = 'GPL'
__email__ = 'jpr@aluno.ifnmg.edu.br'


from codigo_fonte.utilidades.utilidades import *

# COMENTÁRIO DO PROFESSOR: Fico feliz em ver que a qualidade da documentação do seu código cresceu fortemente.
# como já disse, vou verificar o procedimento das filas de prioridade e entro em contato.
class No:
    """ Representa um único nó de uma fila """
    def __init__(self, valor, prioridade):
        self.valor = valor
        self.prioridade = prioridade
        self.proximo = None


class FilaPrioridade:
    """
    Representa uma lista cujos elementos (nós) estão encadeados por elos.
    A lista encadeada simples só pode ser iterada em um único sentido (para frente).
    """
    def __init__(self):
        self.cabeca = None
        self._tamanho = 0

    @property
    def valores(self):
        """ Conjunto contendo todos os nós. """
        return [no.valor for no in self]

    def esta_vazia(self):
        """ Verifica se a fila está vazia. """
        return self.cabeca is None

    def enfileirar(self, valor, prioridade):
        """
        Insere um novo nó na fila com base em sua prioridade.
        :param valor: Os dados que comporão o nó a ser criado.
        :param prioridade: Define a prioridade que o nó terá ao entrar na fila.
        """
        novo_no = No(valor, prioridade)
        if self.esta_vazia() or prioridade > self.cabeca.prioridade:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
            self._tamanho += 1
        else:
            no_atual = self.cabeca
            while no_atual.proximo and prioridade <= no_atual.proximo.prioridade:
                no_atual = no_atual.proximo
            novo_no.proximo = no_atual.proximo
            no_atual.proximo = novo_no
            self._tamanho += 1

    def desenfileirar(self):
        """
        Remove nó na cabeça da fila.
        :return: Conteúdo em valor de nó removido
        """
        if self.esta_vazia():
            print(FAIL + "ATENÇÃO!" + ENDC + " Fila Vazia! Exclusão não ocorreu.")
            return
        valor = self.cabeca.valor
        self.cabeca = self.cabeca.proximo
        self._tamanho -= 1
        return valor

    def __iter__(self):
        """ Define o algoritmo que percorre toda a lista que compõe a fila. """
        no_atual = self.cabeca
        while no_atual:
            yield no_atual
            no_atual = no_atual.proximo

    def __len__(self):
        """
        Retorna o tamanho.
        :return: O tamanho da lista (nº de nós / elementos).
        """
        return self._tamanho
