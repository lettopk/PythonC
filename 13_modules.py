### MODULES ###

#Importacion de modulo de todo el fichero
import my_module

my_module.sum_value(5, 3, 1)
my_module.print_value("Hola python!")

#Importacion de modulo  directa de la funcion
from my_module import sum_value, print_value

sum_value(5, 3 ,1)
print_value("Hola python!")

#Modulos creados por el sistema
import math

print(math.pi)
print(math.sqrt(25))
print(math.pow(2, 8))

#Renombre elemento especifico del modulo importado

from math import pi as pi_value
print("El numero pi es:" + str(pi_value))