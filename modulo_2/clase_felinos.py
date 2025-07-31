class Felinos:
    def __init__(self,  nombre, color, tamano, garras, especie):
        self.nombre = nombre
        self.color = color
        self.tamano = tamano
        self.garras = garras
        self.especie = especie
        
    def presentar_felino(self):
        print(f"el nombre del felino es {self.nombre}, su color es {self.color},su tamaño es {self.tamano}, sus garras son {self.garras} y su especie es {self.especie}")    
        
        
gato = Felinos("Sombra", "negro y gris", "pequeño","retractiles", "Felis catus")
gato.presentar_felino()
tigre = Felinos("Tigre","blanco con manchas negras", "grande","retractiles", "Phantera tigris")
tigre.presentar_felino()
pantera = Felinos("Pantera", "felino grande de color negro", "grande","retractiles", "Panthera")
pantera.presentar_felino()
        