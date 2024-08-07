from random import choice


class Codemaker:
    def __init__(self, colors: list[str]) -> None:
        self.__colors = colors
        self.__pattern = []

    def player_pattern(self) -> list[str]:
        while True:
            option = input(
                f"Elija un color de la siguiente lista '{", ".join(self.__colors)}': "
            ).lower()
            if option in self.__colors:
                if option not in self.__pattern:
                    self.__pattern.append(option)
                else:
                    print("Error: la secuencia no puede tener colores repetidos")
            else:
                print(f"Error: {option} no es un color de la lista")
            if len(self.__pattern) == 4:
                option = input(
                    f"¿Confirma su secuencia: {", ".join(self.__pattern)}? (Y/N): "
                ).lower()
                if option == "y":
                    return self.__pattern
                else:
                    self.__pattern = []

    def cpu_pattern(self) -> list[str]:
        while len(self.__pattern) < 4:
            cpu_choice = choice(self.__colors)
            if cpu_choice not in self.__pattern:
                self.__pattern.append(cpu_choice)
        return self.__pattern
