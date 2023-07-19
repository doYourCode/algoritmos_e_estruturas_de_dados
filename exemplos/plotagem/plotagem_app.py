import arcade
from arcade import Window

from codigo_fonte.estruturas_de_dados.grafo_lista_adjacencia_alt import *
from exemplos.plotagem.pintor_grafo_adj import Pintor
from exemplos.plotagem.busca_em_largura import BuscaEmLargura


class App(Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_IMPERIAL_BLUE)

        self.grafo = GrafoListaAdjacenciaAlt()

        self.grafo.carregar_arquivo("D:/Repos/Python/algoritmos_e_estruturas_de_dados/dados/grafo_ex_01.json")

        self.pintor = Pintor(self.grafo)

        self.bfs = BuscaEmLargura(self.grafo, self.pintor, "A")

        # If you have sprite lists, you should create them here,
        # and set them to None

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below
        arcade.start_render()  # essa parte precisa ir pro metodo onDraw()

        self.pintor.desenha()

        arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        self.bfs.atualiza()

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():
    """ Main function """
    game = App(1280, 720, "Plotagem de grafo")

    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()
