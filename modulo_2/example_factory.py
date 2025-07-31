'''Patron de fabrica: este tipo de patron nos indica que no debemos dejar que la clase se instancie directamente (instanciar asignar la clase a una variable)'''
class Perro:
    def hacer_sonido(self):
        return "Guau"


class Gato:
    def hacer_sonido(self):
        return "Miau"


class Pato:
    def hacer_sonido(self):
        return "Cuak"


# para evitar el instanciamento de cada clase y metodo usaremos el patron de fabrica
# creamos una nueva clase que instancie los metodos de cada clase 
class FabricaHacerSonido:
    def crear_sonido(self, objeto):
        return objeto()

FabricaSonido = FabricaHacerSonido()
print(FabricaSonido.crear_sonido(Perro).hacer_sonido())