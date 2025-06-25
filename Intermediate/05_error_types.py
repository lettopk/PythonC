### ERROR TYPES ### 


##SynstaxError

#print "hola comunidad"  #Error mostrado por el interprete, Falta algo o esta mal escrita la sintaxis
print ("Hola comunidad!")


##NameError

#print(language)     #Error mostrado por el interprete, variable no definida
language ="Spanish"
print(language)


##IndexError

numbers =[5,10,15,20]
#print(numbers[4])      #Error mostrado por el interprete, indice fuera de rango 
print(numbers[3])


##ModuleNotFoundError

#import maths        #Error mostrado por el interprete, no hay modulo llamado "maths"
import math

##AtributeError

#print(math.PI)      #Error mostrado por el interprete, El modulo "math" no tiene un atributo "PI"
print(math.pi)

##KeyError

my_dict  = {
    "nombre": "letto", 
    "apellido":"pk", 
    "edad":30, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.67
    }

#print(my_dict["nombres"])       #Error mostrado por el interprete, "nombres"
print(my_dict["nombre"])


##TypeError

#print(numbers["0"])          #Error mostrado por el interprete, los indices de la lista deben ser int, no str
print(numbers[2])

##ImportError

#from math import PI         #Error mostrado por el interprete, no se puede importar "PI" de math
from math import pi


##ValueError

#my_int = int("10 años")       #Error mostrado por el interprete,letral invalido para int()
my_int = int (10)
print(my_int)

##ZeroDivisionError

#print(4/0)                       #Error mostrado por el interprete, division por cero
print(4/2)