from colored import Style, fore


class Board:
    """
    Proposito: Esta clase está destinada a controlar las funciones del tablero de juego
    encargadas de crear, actualizar e imprimir éste mismo, asimismo de dar información
    al usuario del estado del juego.
    """
    def __init__(self, turns: int) -> None:
        self.__turns = turns
        self.__board = []
        self.__feedback_table = []

    # Gracias, Luis. Por ayudarme con las funciones create_board() y change_color()
    def create_board(self) -> None:
        """
        Proposito: Crear el tablero base tomando como referencia la cantidad de turnos.
        """
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
        """
        Proposito: Crear la tabla que será usada para dar retroalimentación al usuario.
        """
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
        """
        Proposito: Dar color al tablero tomando de referencia las combinaciones de colores que el usuario o cpu ingresen.
        """
        for x in range(len(colors)):
            for y in range(len(colors[x])):
                self.__board[x][y][1] = colors[x][y] # Cambia el color de la posición del tablero por el color ingresado.

    def feedback(self, colors: list[list[str]], pattern: list[str]) -> None:
        """
        Proposito: Dar información al usuario de la posición y existencia de los colores del código secreto.
        """
        for x in range(len(colors)):
            for y in range(len(colors[x])):
                if pattern[y] == colors[x][y]: # Si el color ingresado está en la misma posición que en el código, su posición se marcará en verde.
                    self.__feedback_table[x][y][1] = "medium_spring_green"
                elif colors[x][y] in pattern: # Si el color ingresado existe en el código, pero no está en la posición exacta, su posición de marcara en amarillo/anaranjado.
                    self.__feedback_table[x][y][1] = "gold_3b"
                # En caso que el color no exista, su posición tendrá el color por defecto (blanco).

    def print_board(self) -> None:
        """
        Proposito: Imprimir el tablero y la tabla de información (tablero | tabla)
        """
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
