"""
Esse programa busca mostrar de forma didática como
o sistema operacional escalona os processos pelo método
FIFO, em sistemas Batchs.
"""

from codigo_fonte.estruturas_de_dados.fila import Fila
from codigo_fonte.utilidades.utilidades import *


def FIFO_sistema_batch():
    quantidade = int(input('Quantidade de processos que serão usados nesse lote: '))

    lote = Fila(quantidade)
    for c in range(0, quantidade):
        lote.adicionar(c)
        print(f'{OKGREEN}Processo {c} Adicionado no Lote!{ENDC}')

    while True:
        print('Pressione Enter para continuar')
        input()
        break

    for c in range(0, quantidade):
        lote.remover()

        print(f'{WARNING}Processo {c} foi finalizado!{ENDC}')
