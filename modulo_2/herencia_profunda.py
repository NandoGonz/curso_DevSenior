class Animal: # Super clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        
    # Metodos
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


class Canino(Animal):
    def __init__(self, nombre, edad, tiempoVida):
        super().__init__(nombre, edad)
        self.tiempoVida = tiempoVida

class Perro(Canino):
    def __init__(self, nombre, edad, tiempoVida, raza):
        super().__init__(nombre, edad, tiempoVida)
        self.raza = raza
        
    def mostrar_info(self):
        return f"Nombre: {super().mostrar_info()}, Tiempo de vida {self.tiempoVida}, Raza: {self.raza}"


# Instanciamos nuestras clases y objetos
perro_1 = Perro("Tobby", 5, 10, "Criolla")
print(perro_1.mostrar_info())