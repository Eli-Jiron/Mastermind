from random import choice

from colored import Style, fore


class Codemaker:
    """
    Proposito: Esta clase está destinada a manejar las funciones que le permiten
    tanto al usuario como al cpu de crear un código secreto.
    """
    def __init__(self, colors: list[str]) -> None:
        self.__colors = colors
        self.__pattern = []

    def player_pattern(self) -> list[str]:
        """
        Proposito: Permite al usuario crear su propio código secreto.
        """
        while True:
            option = input(
                f'Elija un color de la siguiente lista "{", ".join(self.__colors)}": ' # Muestra al usuario los colores disponibles.
            ).lower()
            if option in self.__colors: # Evita que el usuario ingrese cualquier otra cosa que no sea uno de los colores de la lista.
                if option not in self.__pattern: # Impide el ingreso de colores repetido en la secuencia.
                    self.__pattern.append(option)
                else:
                    print(f"{fore(196)}Error:{Style.reset} la secuencia no puede tener colores repetidos")
            else:
                print(f"{fore(196)}Error:{Style.reset} {option} no es un color de la lista")
            # Una vez el código tenga 4 colores le pedirá confirmación al usuario.
            if len(self.__pattern) == 4:
                option = input(
                    f"¿Confirma su secuencia: {", ".join(self.__pattern)}? ({fore(68)}Y{Style.reset}/{fore(160)}N{Style.reset}): "
                ).lower()
                if option == "y":
                    return self.__pattern
                else:
                    self.__pattern = []

    def cpu_pattern(self) -> list[str]:
        """
        Proposito: Crea un código secreto aleatorio.
        """
        while len(self.__pattern) < 4:
            cpu_choice = choice(self.__colors)
            if cpu_choice not in self.__pattern: # Impide el ingreso de colores repetido en la secuencia.
                self.__pattern.append(cpu_choice)
        return self.__pattern # Retorna el código una vez éste tenga 4 colores
