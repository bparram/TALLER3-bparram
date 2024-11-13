from models.boa_constrictor import Boa_Constrictor
from models.huron import Huron
from models.animal import Animal
from models.animal_exotico import Animal_Exotico


boa_carlos = Boa_Constrictor("Carlos",1,15.2,"Amazonas",135.2,0)
huron_1= Huron("Kiplin",2,5.6,"USA",125.9)
#contar_raton1 = 0

print(huron_1.hacer_sonido())

print(boa_carlos.hacer_sonido())

print(huron_1.__dict__)

print(boa_carlos.__dict__)

boa_carlos.agregar_raton()

print(boa_carlos.contar_ratones)

boa_carlos.agregar_raton()

print(boa_carlos.contar_ratones)

print(boa_carlos.calcular_flete())



