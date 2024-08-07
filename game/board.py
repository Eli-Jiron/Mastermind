from colored import Style, fore


class Board:
    def __init__(self, turns: int) -> None:
        self.__turns = turns
        self.__board = []
        self.__feedback_table = []

    # Gracias, Luis. Por ayudarme con las funciones create_board() y change_color()
    def create_board(self) -> None:
        for i in range(self.__turns):
            self.__board.append(
                [
                    ["✪", "white"],
                    ["✪", "white"],
                    ["✪", "white"],
                    ["✪", "white"],
                ]
            )

    def create_feedback_table(self) -> None:
        for i in range(self.__turns):
            self.__feedback_table.append(
                [
                    ["•", "white"],
                    ["•", "white"],
                    ["•", "white"],
                    ["•", "white"],
                ]
            )

    def change_color(self, colors: list[list[str]]) -> None:
        for x in range(len(colors)):
            for y in range(len(colors[x])):
                self.__board[x][y][1] = colors[x][y]

    def feedback(self, colors: list[list[str]], pattern: list[str]):
        for x in range(len(colors)):
            for y in range(len(colors[x])):
                if pattern[y] == colors[x][y]:
                    self.__feedback_table[x][y][1] = "medium_spring_green"
                elif colors[x][y] in pattern:
                    self.__feedback_table[x][y][1] = "gold_3b"

    def print_board(self) -> None:
        print("-------------------------\n")
        for x in range(len(self.__board)):
            for y in range(len(self.__board[x])):
                print(
                    "\a",
                    f"{fore(self.__board[x][y][1])}{self.__board[x][y][0]}{Style.reset}",
                    end="  ",
                )
            for y in range(len(self.__board[x])):
                print(
                    "\a",
                    f"{fore(self.__feedback_table[x][y][1])}{self.__feedback_table[x][y][0]}{Style.reset}",
                    end="",
                )
            print()
        print("\n-------------------------")
