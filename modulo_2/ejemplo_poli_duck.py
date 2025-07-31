class Pato:
    def nadar(self):
        return "El pato nada en el agua"


class Barco:
    def nadar(self):
        return "El barco nada en el agua"


class Pez:
    def nadar(self):
        return "El pez nada en el agua"


def precesar_objeto_acuatico(objeto):
    return objeto.nadar()

pato_1 = Pato()
barco_1 = Barco()
pez_1 = Pez()
print(precesar_objeto_acuatico(pez_1))
print(precesar_objeto_acuatico(barco_1))
print(precesar_objeto_acuatico(pez_1))