'''Este tipo de patrones se utiliza mayormente en programas que tengan manejo de solicitud o un orden jerarquico'''

class Manejador:
    def __init__(self, siguiente = None):
        self.siguiente = siguiente


    def manejo(self, solicitud):
        # Crearmos un if para comprobar si hay una siguiente cadena o esta en este metodo 
        if self.siguiente:
            return self.siguiente.manejo(solicitud)
        return "Solicitud no atendida"

# Creamos una case soporte 

class SoporteBasico(Manejador):
    
    def manejo(self, solicitud):
        if solicitud == "Preguntas generales":
            return "Soporte basico respondido"
        return super().manejo(solicitud)

class SoporteTecnico(Manejador):
    
    def manejo(self, solicitud):
        if solicitud == "Preguntas tecnicas":
            return "Soporte tecnico respondido"
        return super().manejo(solicitud)


class SoporteEspecializado(Manejador):
    
    def manejo(self, solicitud):
        if solicitud == "Error critico":
            return "Soporte especializado respondido"
        return super().manejo(solicitud)


cadena = SoporteBasico(SoporteTecnico(SoporteEspecializado()))
print(cadena.manejo("preguntas generalez"))
print(cadena.manejo("preguntas tecnicas"))
print(cadena.manejo("error critico"))
print(cadena.manejo("pregunta rara"))