from models.animal import Animal
from abc import ABC,abstractmethod

class Animal_Exotico(Animal):
    def __init__(self,nombre:str,edad:int,peso:float,pais_origen:str, impuestos:float) -> None:
        super().__init__(nombre,edad,peso)
        
        self.pais_origen = pais_origen
        self.impuestos = impuestos
        
    #metodos
    def calcular_flete(self) -> float:
         return round(self.impuestos * self.peso,2)    
        
    #getters & setters    
        
    @property
    def pais_origen(self) -> str:
        return self.__pais_origen
    
    @pais_origen.setter
    def pais_origen(self, value:str) -> None:
        if isinstance(value, str):
            self.__pais_origen = value
        else:
            raise ValueError('Expected str')
        
    @property
    def impuestos(self) -> float:
        
        return self.__impuestos
    
    @impuestos.setter
    def impuestos(self, value:float) -> None:
        if isinstance(value, float):
            self.__impuestos = value
        else:
            raise ValueError('Expected float')
        
