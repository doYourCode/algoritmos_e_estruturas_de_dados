"""
Esse programa busca mostrar de forma didática como
o sistema operacional escalona os processos pelo método
SJF, em sistemas Batchs.
"""

from codigo_fonte.estruturas_de_dados.fila import Fila
from codigo_fonte.utilidades.utilidades import *


class FilaSJF(Fila):

    def adicionar(self, tempo_processo):
        super().adicionar(tempo_processo)


def SJF_sistema_batch():
    processos = {}
    quantidade = int(input('Quantidade de processos que serão usados nesse lote: '))
    lote = FilaSJF(quantidade)
    for c in range(0, quantidade):
        tempo = int(input(f'Digite o tempo em segundos(s) que o processo {c} dura:'))
        lote.adicionar(tempo)
        processos[c] = tempo


    lote.fila_teste.sort()

    for c in range(0, quantidade):
        valor_removido = lote.remover()
        for chave, chave_valor in enumerate(processos.items()):

            if chave_valor[1] == valor_removido:
                print(f'Processo {chave} foi finalizado!')
                break
