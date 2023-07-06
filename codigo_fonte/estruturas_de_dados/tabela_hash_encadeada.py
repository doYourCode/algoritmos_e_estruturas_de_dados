"""
Tabela hash encadeada na estrutura de dados, semelhante a tabela Hash simples.
Ela soluciona o problema de colisões através do encadeamento. Cada posição da
tabela recebe uma lista, que será preenchida dinamicamente de acordo as inserções.
"""

__author__ = ["Franck Allyson da Silva Rocha",
              "Caio Henriques Sica Lamas"]
__date__ = "25/09/2022"
__credits__ = ["https://www.educba.com/hash-table-in-data-structure/?source=leftnav",
               "https://www.programiz.com/dsa/hash-table",
               "https://www2.unifap.br/furtado/files/2016/11/Aula7.pdf",
               "http://www3.decom.ufop.br/toffolo/site_media/uploads/2013-1/bcc202/slides/23-24._hashing.pdf",
               "https://www.ime.usp.br/~pf/algoritmos/aulas/hash.html",
               "DROZDEK, Adam. Estrutura de Dados e Algoritmos em C++. CENGAGE Learning, 2002"]
__license__ = "GPL"
__email__ = ["fasr@aluno.ifnmg.edu.br",
             "caio.lamas@ifnmg.edu,br"]

from codigo_fonte.estruturas_de_dados.lista_encadeada import ListaEncadeada


class TabelaHashEncadeada:

    def __init__(self, tamanho):
        '''
        Construtor

        :param tamanho: Tamanho que a tabela terá
        '''
        self._capacidade = self.obter_primo(tamanho)
        self._tabela = [] * self._capacidade
        for i in range(0, self._capacidade):
            self._tabela.append(ListaEncadeada())

    def checar_primo(self, valor):
        '''
        Função que valida se o número é realmente primo

        :param valor: número que será testado
        :return: 0 -> caso NÃO seja primo | 1 -> caso seja primo
        '''

        if valor == 1 or valor == 0:
            return 0

        for i in range(2, valor//2):
            if valor % i == 0:
                return 0
        return 1

    def obter_primo(self, numero):
        '''
        Busca um número primo superior mais próximo

        :param numero: número que será modificado
        :return: Número primo
        '''
        if numero % 2 == 0:
            numero += 1

        while not self.checar_primo(numero):
            numero += 2

        return numero

    def gerar_codigo_hash(self, chave):
        '''
        Gerador de codigo Hash

        :param chave: Chave para a geração do código
        :return: Código Hash
        '''
        return chave % self._capacidade

    def inserir_dados(self, chave, valor):
        '''
        Insere o par ordenado (chave, valor) na tabela

        :param chave: Chave do dado
        :param valor: Valor do dado
        '''
        indice = self.gerar_codigo_hash(chave)
        self._tabela[indice].adicionar_final((chave, valor))

    def buscar_pela_chave(self, chave):
        '''
        Busca pela chave, complexidade O(n)

        :param chave: chave do dado buscado
        :return: retorna o conjunto (chave, valor) para o dado solicitado
        '''
        indice = self.gerar_codigo_hash(chave)
        lista = self._tabela[indice]
        for nodo in lista:
            if nodo.dados[0] == chave:
                return nodo.dados

    def bucar_pelo_valor(self, valor):
        '''
        Busca pelo valor; complexidade O(n^2) pois é necessário percorrer os indices e depois a lista.

        :param valor: valor do dado buscado
        :return: retorna o conjunto (chave, valor) para o dado solicitado
        '''
        for lista in self._tabela:
            for nodo in lista:
                if nodo.dados[1] == valor:
                    return nodo.dados

    def deletar_dados(self, chave):
        '''
        Exclui o dado solicitado através da chave

        :param chave: Chave do dado
        '''
        indice = self.gerar_codigo_hash(chave)
        dados = self.buscar_pela_chave(chave)
        self._tabela[indice].remover(dados)

    @property
    def valores(self):
        '''
        Gera uma lista de listas contendo os dados da tabela

        :return: Valores organizados contidos na tabela
        '''
        return [lista.valores for lista in self]

    def __iter__(self):
        '''
        Prototype de Iteração, definimos o que será percorrido ao iterarmos sobre a instancia de classe

        :return: retorna cada lista contida na tabela
        '''
        for lista in self._tabela:
            yield lista

    def __str__(self):
        '''
        Prototype de string, definimos o que será mostrado ao printarmos a instancia de classe

        :return: String de valores contidos na tabela
        '''
        return f'{str(self.valores)}'

    def __len__(self):
        '''
        Tamanho da tabela

        :return: Tamanho total da tabela
        '''
        return self._capacidade



