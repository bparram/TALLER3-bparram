from abc import ABC, abstractmethod

class Animal(ABC): #esta estructura indica que es abstracta
    
    def __init__(self,nombre: str, edad:int, peso:float) -> None:
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        
    #metodos
    
    @abstractmethod #indica que el metodo es abstracto
    def hacer_sonido():
        pass
            
    #getters y setters
    @property
    def nombre(self) -> str:
        """ Devuelve el valor del atributo privado 'nombre' """
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value:str) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'nombre'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, str):
            self.__nombre = value
        else:
            raise ValueError('Expected type')
    
    @property
    def edad(self) -> int:
        """ Devuelve el valor del atributo privado 'edad' """
        return self.__edad
    
    @edad.setter
    def edad(self, value:int) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'edad'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, int):
            self.__edad = value
        else:
            raise ValueError('Expected type')
        
    @property
    def peso(self) -> float:
        """ Devuelve el valor del atributo privado 'peso' """
        return self.__peso
    
    @peso.setter
    def peso(self, value:float) -> None:
        """ 
        Establece un nuevo valor para el atributo privado 'peso'
    
        Valida que el valor enviado corresponda al tipo de dato del atributo
        """ 
        if isinstance(value, float):
            self.__peso = value
        else:
            raise ValueError('Expected type')
        
        
