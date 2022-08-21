""" O intuito desse arquivo é organizar as multiplas importações e facilitar a leitura e manipulação do arquivo main.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "16/08/2022"
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"


from codigo_fonte.estruturas_de_dados.lista_encadeada import lista_encadeada
from codigo_fonte.estruturas_de_dados.lista_duplamente_encadeada import lista_duplamente_encadeada
from codigo_fonte.estruturas_de_dados.pilha_encadeada import pilha_encadeada
from codigo_fonte.estruturas_de_dados.fila_encadeada import fila_encadeada

def executar(func):
    """ Executa o teste/exemplo inserido na lista de parâmetros.

    :param func: A função de teste/exemplo que será carregada e executada.
    """
    func()
