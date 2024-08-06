class Board:
    def __init__(self, board: list[list]) -> None:
        self.__board = board

    def print_board(self):
        print("--------------------")
        for row in self.__board:
            for e in row:
                print("\a", e, end="")
            print()
        print("--------------------")
