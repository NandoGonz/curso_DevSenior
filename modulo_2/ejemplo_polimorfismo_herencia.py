class Empleado:
    def __init__(self,nombre, apellido, cedula):
        self.nombre = nombre 
        self.apellido = apellido
        self.cedula = cedula
        
    def mostrar_info(self):
        return f"Informacion del empleado: {self.nombre}, {self.apellido}, {self.cedula}"

class MedioTiempo(Empleado):
    def __init__(self, nombre, apellido, cedula, tipoContrato):
        super().__init__(nombre, apellido, cedula) # herencia
        self.tipoContrato = tipoContrato # nuevo atributo

class porHora(Empleado):
    def __init__(self, nombre, apellido, cedula, horaTrabajadas):
        super().__init__(nombre, apellido, cedula)
        self.horaTrabajadas = horaTrabajadas

# polimorfismo sobrescritura (Overrride)
    def mostrar_info(self): 
        return f"Informacion del empleado: {super().mostrar_info()}, {self.horaTrabajadas}"

    '''def mostrar_info(self): # esta forma funciona
        return f"Informacion del empleado: {self.nombre}, {self.apellido}, {self.cedula}, {self.horaTrabajadas}" '''

empleadoPorHoras = porHora("Luis", "Gonzalez", 1065999017, 12)
print(empleadoPorHoras.mostrar_info())