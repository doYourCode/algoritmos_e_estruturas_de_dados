"""
Tabela hash na estrutura de dados, Tabela Hash é a tabela que armazena
todos os valores do código hash usado ao armazenar as chaves e valores de
dados do elemento usando o mecanismo de hashing. A tabela hash armazena
códigos hash que são gerados usando a função hash. Hashing é o mecanismo
que ajuda a identificar todos os objetos exclusivamente dentro do conjunto de grupos de objetos.
"""

__author__ = ["Caio Henriques Sica Lamas",
              "Franck Allyson da Silva Rocha"]
__date__ = "24/08/2022"
__credits__ = ["https://www.educba.com/hash-table-in-data-structure/?source=leftnav",
               "https://www.programiz.com/dsa/hash-table",
               "https://www2.unifap.br/furtado/files/2016/11/Aula7.pdf"]
__license__ = "GPL"
__email__ = ["caio.lamas@ifnmg.edu,br",
             "fasr@aluno.ifnmg.edu.br"]


class TabelaHash:

    def __init__(self, tamanho):
        self._capacidade = self.obter_primo(tamanho)
        self._tabela = [[], ] * self._capacidade

    def checar_primo(self, valor):
        """ Função que valida se o número é realmente primo """
        if valor == 1 or valor == 0:
            return 0

        for i in range(2, valor//2):
            if valor % i == 0:
                return 0
        return 1

    def obter_primo(self, numero):
        """ Função obtém o primeiro primo superior mais próximo 11"""
        if numero % 2 == 0:
            numero += 1

        while not self.checar_primo(numero):
            numero += 2

        return numero

    def gerar_codigo_hash(self, chave):
        """ Função para gerar o código Hash """
        return chave % self._capacidade

    def inserir_dado(self, chave, valor):
        indice = self.gerar_codigo_hash(chave)
        self._tabela[indice] = [chave, valor]

    def deletar_dado(self, chave):
        indice = self.gerar_codigo_hash(chave)
        self._tabela[indice] = []

    def __str__(self):
        return str(self._tabela)

    def __len__(self):
        return self._capacidade
