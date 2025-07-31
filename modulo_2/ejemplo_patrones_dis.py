'''Debemos hacert el uso de una clase sin modificar la anterior y usada, para esto usaremos el patron  adaptativo: me ayuda a adaptar mi código, como este patron existen otros(es un patron de creación)'''

class MotorViejo:
    def encender(self):
        return "Motor encendido"


class MotorNuevo:
    def encendido(self):
        return "Motor nuevo encendido"

# una forma de solucionar este problema es creando una clase nueva
class AdaptadorMotor:
    def __init__(self, motor):
        self.motor = motor

    # creamos un nuevo metodo
    def encender(self):
        print(self.motor.encendido())


# instanciamos nuestras clases y metodos
# instaciamos nuestra clase AdaptadorMotor
motor = AdaptadorMotor(MotorNuevo())
motor.encender() # Código viejo