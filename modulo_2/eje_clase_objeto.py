class Persona:
    def __init__(self, nombre: str, edad: int, ciudad: str = "Sicilia"):
        self.nombre = nombre # atributo 
        self.edad = edad      # atributo 
        self.ciudad = ciudad   # atributo con un _ se protege el atributo
        self.password = "1234"  # atributo con dos __ se privatiza el atributo 
        # self es un párametro especial que se refiere a la misma clase, es el primero en colocarse al definir una clase, representa el objeto llamado
        
    def saludo(self): #  las funciiones dentro de las clase se les llamaran metodo
        print(f"Mi nombre es {self.nombre} y tengo {self.edad} años y vivo en {self.ciudad}")
        
        
    def cumplir_anos(self): # metodo
        self.edad += 1
        
        
    def cambiar_ciudad(self, nueva_ciudad: str): 
        self.ciudad = nueva_ciudad   
        print("Se ha cambiado la ciudad")  
        
    # crearemos un metod para instanciar el atributo password, ya que se encuentra privado y no lo podemos instanciar de forma global    
    def get_password(self): # metodo para imprimir un atributo privado, no funciona con los protegidos
        return self.password
        
# instaciamos nuestros objetos y clases (instanciar es el equivalente de llamr una funcion)
persona1 = Persona("Nando", 29)
''' imprimios nuestro metodo para verificar que se ejecute de forma correcta print(persona1.get_password())'''
'''persona1._ciudad no muestra ninguna excepcion, error de valor o tipo '''
persona1.saludo()        
persona1.cumplir_anos()
persona1.saludo()
persona1.cumplir_anos() # de forma basica si instanciamos los metodos podremos utilizarla de nuevo en este caso agregar un año más a l edad 
persona1.cambiar_ciudad("Masnchester")
persona1.saludo()
        
        
    