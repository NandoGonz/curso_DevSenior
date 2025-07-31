class Animal:# Super clase
    # Atributo 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    # metodos 
    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    
# Clase hija(SubClase)
class Perro(Animal): # colocando el nombre de nuestra super clase dentro de los parentesis, ya sabemso que esta es madre de esta neu8va clase
    def __init__(self, nombre, edad, raza): # podemos agregar más atributos
        super().__init__(nombre, edad)# llamada del constructor padre
        self.raza = raza # nuevo atributo 
    # polimorfismo, es nuna sobre escitura de datos  
    
    def mostrar_info(self):
        return f"{super().mostrar_info()}, raza: {self.raza}" 
        
        
# instanciamos nuestra clase
animal_generico = Animal("Ganz", 5,)
print(animal_generico.mostrar_info())
perro_generico = Perro("Cony", 2, "Criollo")
print(perro_generico.mostrar_info())  