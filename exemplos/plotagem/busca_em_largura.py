import asyncio

from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *
from exemplos.plotagem.pintor_grafo_adj import Pintor


def busca_em_largura(grafo: GrafoListaAdjacenciaAlt, pintor: Pintor, origem: str, tempo: float = 0.0):

    queue = []
    read = set()

    queue.append(grafo.nodos[origem])

    while queue:

        n = queue.pop(0)
        read.add(n.nome)
        pintor.ler_nodo(n.nome)

        for a in n.arestas:
            outro = grafo.nodos[a.outro.nome]
            if outro.nome not in read:
                queue.append(outro)
                pintor.ler_aresta(a.origem.nome, outro.nome)
                #await asyncio.sleep(tempo)