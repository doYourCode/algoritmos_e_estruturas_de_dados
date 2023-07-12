from threading import Thread

import arcade

from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *
from exemplos.plotagem.pintor_grafo_adj import Pintor
from exemplos.plotagem.busca_em_largura import busca_em_largura


def grafo_simples_main():

    arcade.open_window(1280, 720, "Graph Plot", antialiasing=True)

    arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

    grafo = GrafoListaAdjacenciaAlt()

    grafo.carregar_arquivo("dados/grafo_ex_01.json")

    pintor = Pintor(grafo)

    # COMENTÁRIO
    # Suponho que o erro aqui está em não utilizar uma abordagem Iterativa, como um gameloop, preciso verificar se
    # a lib arcade tem essa funcionalidade e implementá-la, assim será possível interagir com os algoritmos de busca

    #busca_em_largura(grafo, pintor, "A")

    #thread = Thread(target=busca_em_largura, args=(grafo, pintor, "A", 2))

    #thread.start()

    arcade.start_render() # essa parte precisa ir pro metodo onDraw()

    pintor.desenha()

    arcade.finish_render()

    arcade.run()
