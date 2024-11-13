from models.animal import Animal
from models.animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self,nombre:str,edad:int,peso:float,pais_origen:str, impuestos:float,contar_ratones:int) -> None:
        super().__init__(nombre,edad,peso,pais_origen,impuestos)
        self.contar_ratones = contar_ratones
        
    #metodos
    def agregar_raton(self) ->int:
        if self.contar_ratones >= 20:
            raise ValueError("Demasiados ratones!")
        self.contar_ratones += 1
        return self.contar_ratones 
        
    def hacer_sonido(self):
        return "¡Tsss!"
        
    #Getters & Setters    
    @property
    def contar_ratones(self) -> int:
        """ Devuelve el valor del atributo privado 'contar_ratones' """
        return self.__contar_ratones
    
    @contar_ratones.setter
    def contar_ratones(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'contar_ratones'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__contar_ratones = value
        else:
            raise ValueError('Expected int')
    