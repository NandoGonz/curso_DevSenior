class Volador:
    def __init__(self, altura):
        self.altura = altura
        
    def volar(self):
        return "puede volar"
    
class Corredor:
    def __init__(self, velocidad):
        self.velocidad = velocidad
        
    def correr(self):
        return "puede caminar"
    
class Nadador():
    def __init__(self, profundidad):
        self.profudidad = profundidad
    
    def nadar(self):
        return "puede nadar"      


# creamos las clases hijas 
class Perro(Corredor):
    pass


class Pato(Volador, Corredor, Nadador):
    pass

# instanciamos 
pato_1 = Pato(56)