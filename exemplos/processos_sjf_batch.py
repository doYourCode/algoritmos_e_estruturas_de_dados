"""
Esse programa busca mostrar de forma didática como
o sistema operacional escalona os processos pelo método
SJF, em sistemas Batchs.
"""

from codigo_fonte.estruturas_de_dados.fila import Fila
from codigo_fonte.utilidades.utilidades import *


class FilaSjf(Fila):

    def adicionar(self, tempo_processo):
        super().adicionar(tempo_processo)


def sjf_sistema_batch():
    processos = {}
    quantidade = int(input('Quantidade de processos que serão usados nesse lote: '))
    lote = FilaSjf(quantidade)
    for c in range(0, quantidade):
        tempo = int(input(f'Digite o tempo em segundos(s) que o processo {c} dura:'))
        lote.adicionar(tempo)
        processos[c] = tempo

    lote.fila_teste.sort()

    input('\nTecle enter para continuar\n')

    for c in range(0, quantidade):
        valor_removido = lote.remover()
        for chave, chave_valor in enumerate(processos.items()):

            if chave_valor[1] == valor_removido:
                print(f'{WARNING}Processo {chave} foi finalizado!{ENDC}')
                break
