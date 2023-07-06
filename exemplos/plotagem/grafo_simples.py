import arcade

from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *
from exemplos.plotagem.pintor_grafo_adj import Pintor


def grafo_simples_main():

    arcade.open_window(1280, 720, "Graph Plot", antialiasing=True)

    arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

    grafo = GrafoListaAdjacenciaAlt()

    grafo.adicionar_nodo("A", {"x": 32, "y": 74})
    grafo.adicionar_nodo("B", {"x": 143, "y": 211})
    grafo.adicionar_nodo("C", {"x": 160, "y": 370})
    grafo.adicionar_nodo("D", {"x": 370, "y": 390})
    grafo.adicionar_nodo("E", {"x": 512, "y": 290})
    grafo.adicionar_nodo("F", {"x": 640, "y": 190})
    grafo.adicionar_nodo("G", {"x": 360, "y": 160})

    grafo.adicionar_aresta("A", "B", 32)
    grafo.adicionar_aresta("B", "C", 17)
    grafo.adicionar_aresta("C", "D", 12)
    grafo.adicionar_aresta("B", "D", 11)
    grafo.adicionar_aresta("D", "E", 11)
    grafo.adicionar_aresta("B", "E", 11)
    grafo.adicionar_aresta("B", "G", 11)

    pintor = Pintor(grafo)

    pintor.ler_nodo("A")
    pintor.ler_nodo("B")
    pintor.ler_aresta("A", "B")

    arcade.start_render()

    pintor.desenha()

    arcade.finish_render()

    arcade.run()
