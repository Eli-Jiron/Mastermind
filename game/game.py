from time import sleep

from codebreaker import Codebreaker
from codemaker import Codemaker


class Game(Codebreaker, Codemaker):
    def __init__(self, colors: list[str]) -> None:
        Codemaker.__init__(self, colors=colors)
        Codebreaker.__init__(self, colors=colors)

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
        turns = 12
        pattern = self.cpu_pattern()
        for play in self.guess_player():
            if play == pattern:
                break
            turns -= 1
            print(f"\nTurnos restantes: {turns}\n")
            if self.no_turns_left(turns=turns):
                break
        if turns != 0:
            print("Felidades. Haz adivinado el codigo secreto.")
        else:
            print("Se han agotado los turnos. Fin del juego")

    def plays_cpu(self):
        turns = 12
        pattern = self.player_pattern()
        for play in self.guess_cpu():
            if play == pattern:
                break
            turns -= 1
            print(f"\nTurnos restantes: {turns}\n")
            if self.no_turns_left(turns=turns):
                break
            sleep(3)
        if turns != 0:
            print("La computadora descifró el codigo")
        else:
            print(
                "Se han agotado los turnos. La computadora no logró descifrar el codigo"
            )

    def no_turns_left(self, turns: int) -> bool:
        if turns == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    new_game = Game(["red", "blue", "green", "black", "pink", "white"])
    new_game.play()
