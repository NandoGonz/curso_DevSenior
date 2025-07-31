from abc import ABC, abstractmethod 

class Forma(ABC):
    
    @abstractmethod # los metodos abstractos no pueden ser usados directamente 
    def calcular_area(self):
        return "No deberias estar aqui"


'''para acceder a un metodo protegido con abstractmethod debemos sobrescribirla al momento de crear un hijo'''
class Rectacgunlo(Forma):
    
    def calcular_area(self):
        return "Estoy calculando el area "



rec_1 = Rectacgunlo()
print(rec_1.calcular_area())