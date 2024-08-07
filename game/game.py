from time import sleep

from board import Board
from codebreaker import Codebreaker
from codemaker import Codemaker


class Game(Codebreaker, Codemaker, Board):
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
        while True:
            print("Modos:\n  Adivinador: 1, Creador: 0")
            option = input("Elija un modo: ")
            if option in ["1", "0"]:
                break
            print(f"Error: {option} no es una opción valida")
        if int(option):
            self.plays_player()
        else:
            self.plays_cpu()

    def plays_player(self):
        self.__codemaker_pattern = self.cpu_pattern()
        self.print_board()
        for play in self.guess_player():
            self.show_result(play=play)
            self.__turns -= 1
            if self.__turns == 0 or play == self.__codemaker_pattern:
                break
            print(f"\nTurnos restantes: {self.__turns}\n")

        if self.__turns != 0:
            print("Felidades. Haz adivinado el codigo secreto.")
        else:
            print("Se han agotado los turnos. Fin del juego")

    def plays_cpu(self):
        self.__codemaker_pattern = self.player_pattern()
        self.print_board()
        for play in self.guess_cpu():
            self.show_result(play=play)
            self.__turns -= 1
            if self.__turns == 0 or play == self.__codemaker_pattern:
                break
            print(f"\nTurnos restantes: {self.__turns}\n")
            sleep(1.5)

        if self.__turns != 0:
            print("La computadora descifró el codigo")
        else:
            print(
                "Se han agotado los turnos. La computadora no logró descifrar el codigo"
            )

    def show_result(self, play: list[str]):
        self.__board_colors.append(play)
        self.change_color(colors=self.__board_colors)
        self.feedback(colors=self.__board_colors, pattern=self.__codemaker_pattern)
        self.print_board()


if __name__ == "__main__":
    new_game = Game(
        colors=["red", "violet", "green", "black", "yellow", "cyan"], turns=12
    )
    new_game.play()
