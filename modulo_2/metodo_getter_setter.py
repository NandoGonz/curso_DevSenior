class Persona:
    def __init__(self, nombre: str, edad: int, ciudad: str = "Sicilia"):
        self._nombre = nombre # atributo 
        self._edad = edad      # atributo 
        self._ciudad = ciudad   # atributo con un _ se protege el atributo
        self._password = "1234"  # atributo con dos __ se privatiza el atributo 
        
        
    def saludo(self): #  las funciiones dentro de las clase se les llamaran metodo
        print(f"Mi nombre es {self._nombre} y tengo {self._edad} años y vivo en {self._ciudad}")
        
            
            
            
persona1 = Persona("luis", 29, "Chivolo")            
persona1._edad = 30
persona1.saludo()
