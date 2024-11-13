from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron


class GuarderiaExotica:
    def __init__(self,nombre:str) -> None:
        self.__nombre = nombre
        self.boas = []
        self.hurones = []

    def ingresar_boa(self, nueva_boa:Boa_Constrictor):
        self.boas.append(nueva_boa)

    def ingresar_huron(self, nuevo_huron:Huron):
        self.hurones.append(nuevo_huron)

    def lista_boas(self):
        return self.boas
    
    def lista_hurones(self):
        return self.hurones
    
    def alimentar_boa(self, boa: Boa_Constrictor):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.agregar_raton()
            return "Éxito"
        except ValueError as texto:
            if str(texto) == "Demasiados Ratones!":
                return "La boa está llena"
    
guarderiaexotic = GuarderiaExotica("El mundo fantastico")

boa1= Boa_Constrictor(nombre="Teo", edad=4, peso=15.5, pais_origen="Brasil", impuestos=5.0, contar_ratones=10)
boa2 = Boa_Constrictor(nombre="Gloria", edad=4, peso=15.5, pais_origen="Brasil", impuestos=5.0, contar_ratones=10)

huron1= Huron(nombre="kipllin", edad= 3, peso= 2.5, pais_origen="USA",impuestos=26.9)
huron2= Huron(nombre="krillin", edad= 4, peso= 4.5, pais_origen="USA",impuestos=26.9)

guarderiaexotic.ingresar_boa(boa1)
guarderiaexotic.ingresar_boa(boa2)
guarderiaexotic.ingresar_huron(huron1)
guarderiaexotic.ingresar_huron(huron2)

print(guarderiaexotic.lista_boas())
print(guarderiaexotic.lista_hurones())


        


