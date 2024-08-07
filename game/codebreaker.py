class Codebreaker:
    def __init__(self, colors: list[str]) -> None:
        self.__colors = colors
        self.__response = []

    def guess_player(self):
        while True:
            print(f"Colores: {", ".join(self.__colors)}")
            option = input("Ingrese un color: ").lower()
            if option in self.__colors:
                if option not in self.__response:
                    self.__response.append(option)
                else:
                    print("Error: la secuencia no puede tener colores repetidos")
            else:
                print(f"Error: {option} no es un color de la lista")
            if len(self.__response) == 4:
                yield self.__response
                self.__response = []

    def guess_cpu(self):
        pass
