from models.programa import Programa
from models.estudiante import Estudiante
from models.matricula import Matricula

class ControllerMatricula:
    def __init__(self):
        self.matriculas = []

    def agregarMatricula(self, matricula: Matricula):
        for matriculas in self.matriculas:
            if matriculas.id == matricula.id:
                return False
        self.matriculas.append(matricula)
        return True
    
    def mostrarMatriculas(self):
        for matricula in self.matriculas:
            return matricula