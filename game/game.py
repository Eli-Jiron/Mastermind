from time import sleep

from board import Board
from codebreaker import Codebreaker
from codemaker import Codemaker
from colored import Style, fore


class Game(Codebreaker, Codemaker, Board):
    """
    Proposito: Esta clase es la encargada de llevar el control del juego.
    """
    def __init__(self, colors: list[str], turns: int) -> None:
        Codemaker.__init__(self, colors=colors)
        Codebreaker.__init__(self, colors=colors)
        Board.__init__(self, turns=turns)
        self.create_board()
        self.create_feedback_table()
        self.__turns = turns
        self.__board_colors = []
        self.__codemaker_pattern = ""

    def play(self):
        """
        Proposito: Permite al usuario elegir si quiere ser adivinador o creador.
        """
        while True:
            print(f"{fore(85)}Modos:{Style.reset}\n  Adivinador: {fore(68)}1{Style.reset}, Creador: {fore(160)}0{Style.reset}") # Muestra los modos disponibles.
            option = input("Elija un modo: ")
            if option in ["1", "0"]: 
                break
            print(f"{fore(196)}Error:{Style.reset} {option} no es una opción valida")
        if int(option): # Dependiendo del modo que haya elegido el usuario ejecuta una función u otra.
            self.plays_player()
        else:
            self.plays_cpu()

    def plays_player(self):
        """
        Proposito: Permite al usuario jugar como adivinador. Deberá
        descifrar el código secreto creado por el cpu.
        """
        self.__codemaker_pattern = self.cpu_pattern() # Crea el código secreto.
        self.print_board()
        for play in self.guess_player():
            self.show_result(play=play) # Mostrará los resultados de la secuencia ingresada.
            self.__turns -= 1 # Resta un turno.
            if self.__turns == 0 or play == self.__codemaker_pattern: # Detendrá el juego cuando se acaben los turnos o se descifre el codigo.
                break
            print(f"\nTurnos restantes: {fore(220)}{self.__turns}{Style.reset}\n") # Informa de los turnos restantes.

        if play == self.__codemaker_pattern: # Al detenerse el juego, compara si la ultima secuencia coincide con el código.
            print("Felidades. Haz adivinado el codigo secreto.")
        else:
            print("Se han agotado los turnos. Fin del juego")

    def plays_cpu(self):
        """
        Proposito: Permite al usuario crear un código secreto que luego el cpu tendrá que descifrar.
        """
        self.__codemaker_pattern = self.player_pattern() # Pide al usuario crear el código secreto
        self.print_board()
        for play in self.guess_cpu():
            self.show_result(play=play) # Mostrará los resultados de la secuencia generada.
            self.__turns -= 1 # Resta un turno.
            if self.__turns == 0 or play == self.__codemaker_pattern: # Detendrá el juego cuando se acaben los turnos o se descifre el codigo.
                break
            print(f"\nTurnos restantes: {fore(220)}{self.__turns}{Style.reset}\n") # Informa de los turnos restantes.
            sleep(1.5) # Volverá a ejecutarse despues de 1.5 segundos.

        if play == self.__codemaker_pattern: # Al detenerse el juego, compara si la ultima secuencia coincide con el código.
            print("La computadora descifró el codigo")
        else:
            print(
                "Se han agotado los turnos. La computadora no logró descifrar el codigo"
            )

    def show_result(self, play: list[str]):
        """
        Proposito: Función destinada a actualizar el tablero con los datos de la secuencia ingresada.
        """
        self.__board_colors.append(play) # Añade la secuencia a una lista que sirve como registro de cada una secuencia ingresadas.
        self.change_color(colors=self.__board_colors) # Actualiza el tablero.
        self.feedback(colors=self.__board_colors, pattern=self.__codemaker_pattern) # Actualiza la tabla de información. 
        self.print_board() # Imprime el tablero actualizado.


if __name__ == "__main__":
    new_game = Game(
        colors=["red", "blue", "violet", "yellow", "tan", "green", "black", "blue_violet", "white", "navy_blue"], turns=4)
    new_game.play()
