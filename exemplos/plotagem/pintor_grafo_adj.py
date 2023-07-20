import arcade

from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *


class Pintor:

    def __init__(self, grafo: GrafoListaAdjacenciaAlt):

        self.grafo = grafo

        self.lista_nnp = list()
        for chave, nodo in grafo.nodos.items():
            self.lista_nnp.append(nodo)

        self.lista_anp = list()
        for chave, nodo in grafo.nodos.items():
            for aresta in nodo.arestas:
                self.lista_anp.append(aresta)

        self.lista_njp = list()

        self.aresta_prep = list()

        self.lista_ajp = list()

    def desenha(self):

        for aresta in self.lista_anp:
            d = aresta.distancia
            fd = "{:.2f}".format(d)
            arcade.draw_text(
                fd,
                (aresta.origem.dados["x"] + aresta.outro.dados["x"]) / 2,
                (aresta.origem.dados["y"] + aresta.outro.dados["y"]) / 2,
                arcade.color.GRAY,
                10,
                font_name="Arial",
                anchor_x="center",
                anchor_y="bottom",
                bold=True)
            arcade.draw_line(
                aresta.origem.dados["x"],
                aresta.origem.dados["y"],
                aresta.outro.dados["x"],
                aresta.outro.dados["y"],
                (255, 255, 255, 255),
                2
            )

        for aresta in self.aresta_prep:
            arcade.draw_line(
                aresta.origem.dados["x"],
                aresta.origem.dados["y"],
                aresta.outro.dados["x"],
                aresta.outro.dados["y"],
                (128, 128, 240, 255),
                2
            )

        for aresta in self.lista_ajp:
            arcade.draw_line(
                aresta.origem.dados["x"],
                aresta.origem.dados["y"],
                aresta.outro.dados["x"],
                aresta.outro.dados["y"],
                (255, 64, 64, 255),
                2
            )

        for nodo in self.lista_nnp:
            arcade.draw_circle_filled(nodo.dados["x"], nodo.dados["y"], 16, arcade.color.YELLOW)
            arcade.draw_text(
                nodo.nome,
                nodo.dados["x"],
                nodo.dados["y"],
                arcade.color.BLACK,
                16,
                font_name="Arial",
                anchor_x="center",
                anchor_y="center",
                bold=True)

        for nodo in self.lista_njp:
            arcade.draw_circle_filled(nodo.dados["x"], nodo.dados["y"], 16, arcade.color.RED_BROWN)
            arcade.draw_text(
                nodo.nome,
                nodo.dados["x"],
                nodo.dados["y"],
                arcade.color.BLACK,
                16,
                font_name="Arial",
                anchor_x="center",
                anchor_y="center",
                bold=True)

    def ler_nodo(self, nodo: str):
        if self.grafo.nodos[nodo] not in self.lista_njp:
            n = self.grafo.nodos[nodo]
            self.lista_nnp.remove(n)
            self.lista_njp.append(n)

    def preparar_aresta(self, nodo1: str, nodo2: str):

        _a = Aresta

        for a in self.grafo.nodos[nodo1].arestas:
            if a.outro.nome == self.grafo.nodos[nodo2].nome:
                _a = a

        if _a not in self.aresta_prep:
            #self.lista_anp.remove(_a)
            self.aresta_prep.append(_a)

    def ler_aresta(self, nodo1: str, nodo2: str):

        _a = Aresta

        for a in self.grafo.nodos[nodo1].arestas:
            if a.outro.nome == self.grafo.nodos[nodo2].nome:
                _a = a

        if _a not in self.lista_ajp:
            self.lista_anp.remove(_a)
            self.lista_ajp.append(_a)
