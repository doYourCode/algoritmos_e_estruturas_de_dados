""" O intuito desse arquivo é organizar as multiplas importações e facilitar a leitura e manipulação do arquivo main.
"""
__author__ = "Caio Henriques Sica Lamas"
__date__ = "16/08/2022"
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu,br"

from codigo_fonte.estruturas_de_dados.testes.testes_listas import *
from codigo_fonte.estruturas_de_dados.testes.testes_filas import *
from codigo_fonte.estruturas_de_dados.testes.testes_pilhas import *
from codigo_fonte.estruturas_de_dados.testes.testes_hash import *
from codigo_fonte.estruturas_de_dados.testes.testes_grafos import *
from codigo_fonte.estruturas_de_dados.testes.testes_arvores import *

from codigo_fonte.ordenacao.testes import *

from exemplos.escalonamento.processos_fifo_batch import *
from exemplos.escalonamento.processos_sjf_batch import *


def executar(func):
    """ Executa o teste/exemplo inserido na lista de parâmetros.

    :param func: A função de teste/exemplo que será carregada e executada.
    """
    func()


def executar_p(func, param):
    """ Executa o teste/exemplo inserido na lista de parâmetros.

    :param func: A função de teste/exemplo que será carregada e executada.
    :param param: O parâmetro que será passado para a função.
    """
    func(param)
