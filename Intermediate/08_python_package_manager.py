### PYTHON PACKAGE MANAGER ### 

#PIP 
#instalar "numpy" desde la terminal: pip install numpy 
import numpy

print(numpy.version.version)

numpy_array =numpy.array([35,24,62,52,30,30,17])
print(type(numpy_array))

print(numpy_array *2)

#instalar "pandas" desde la terminal: pip install pandas

import pandas

#Listado de las librerias instalas, desde la terminal: pip list
#desinstalar librerias, desde la terminal: pip uninstall pandas
#detalles del modulo, desde la terminal: pip show numpy

import requests         #Instalas requests, desde la terminal: pip install requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")  #Consumo consulta a api
print(response)
print(response.status_code)
print(response.json())


#Arithmetic package (creado por nosotros)
from my_package import arithmetics

print(arithmetics.sum(5,3))