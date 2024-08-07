from colored import Style, fore


class Board:
    def __init__(self, turns: int) -> None:
        self.__turns = turns
        self.__board = []

    # Gracias, Luis. Por ayudarme con las funciones create_board() y change_color()
    def create_board(self) -> None:
        for i in range(self.__turns):
            self.__board.append(
                [
                    ["O", "white"],
                    ["O", "white"],
                    ["O", "white"],
                    ["O", "white"],
                ]
            )

    def change_color(self, colors: list[list[str]]) -> None:
        for row in colors:
            for color in row:
                self.__board[colors.index(row)][row.index(color)][1] = color

    def print_board(self) -> None:
        print("--------------------")
        for row in self.__board:
            for e in row:
                print("\a", f"{fore(e[1])}{e[0]}{Style.reset}", end="  ")
            print()
        print("--------------------")
