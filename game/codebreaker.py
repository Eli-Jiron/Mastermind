from random import choice


class Codebreaker:
    """
    Proposito: Esta clase está destinada a manejar las funciones encargadas de permitir
    tanto al usuario como al cpu de descrifrar el código secreto.
    """
    def __init__(self, colors: list[str]) -> None:
        self.__colors = colors
        self.__response = []

    def guess_player(self):
        """
        Proposito: Permite al usuario crear una secuencia de colores
        del que crea que puede ser código secreto.
        """
        while True:
            print(f"Colores: {", ".join(self.__colors)}") # Muestra las opciones de color disponibles.
            option = input("Ingrese un color: ").lower()
            if option in self.__colors: # Evita que el usuario ingrese cualquier otra cosa que no sea uno de los colores de la lista.
                if option not in self.__response: # Impide el ingreso de colores repetidos en la secuencia.
                    self.__response.append(option)
                else:
                    print("Error: la secuencia no puede tener colores repetidos")
            else:
                print(f"Error: {option} no es un color de la lista")
            if len(self.__response) == 4: # Retorna la secuencia cuando esta tenga 4 colores.
                yield self.__response
                self.__response = []

    # TODO: cambiar por un mejor algoritmo.
    def guess_cpu(self):
        """
        Proposito: Permite al cpu crear secuencia de color aleatorias para descifrar el código secreto.
        """
        while True:
            cpu_choice = choice(self.__colors)
            if cpu_choice not in self.__response: # Impide el ingreso de colores repetidos en la secuencia.
                self.__response.append(cpu_choice)
            if len(self.__response) == 4: # Retorna la secuencia cuando esta tenga 4 colores.
                yield self.__response
                self.__response = []
