import arcade

from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *


def grafo_simples_main():

    arcade.open_window(720, 480, "Graph Plot")

    arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

    grafo = GrafoListaAdjacenciaAlt()

    grafo.adicionar_nodo("A", [32, 74])
    grafo.adicionar_nodo("B", [143, 211])
    grafo.adicionar_nodo("C", [160, 370])
    grafo.adicionar_nodo("D", [370, 390])

    grafo.adicionar_aresta("A", "B", 32)
    grafo.adicionar_aresta("B", "C", 17)
    grafo.adicionar_aresta("C", "D", 12)
    grafo.adicionar_aresta("B", "D", 11)

    arcade.start_render()

    for chave, valor in grafo.nodos.items():

        for aresta in valor.arestas:
            arcade.draw_line(valor.valor[0], valor.valor[1], aresta.outro.valor[0], aresta.outro.valor[1], (255, 255, 255, 255), 1)

        arcade.draw_circle_filled(valor.valor[0], valor.valor[1], 16, arcade.color.YELLOW)
        arcade.draw_text(valor.nome, valor.valor[0], valor.valor[1], arcade.color.BLACK, 16, font_name="Arial", anchor_x="center", anchor_y="center", bold=True)

    arcade.finish_render()

    arcade.run()
