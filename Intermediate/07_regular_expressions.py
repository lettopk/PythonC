### REGULAR EXPRESSIONS ###

import re           ##Espresiones regulares: para buscar coincidencias en una cadena de texto

my_string = "Esta es la leccion numero 7: Leccion llamada Expresiones Regulares"
my_other_string = "Esta no es la leccion numero 6: Manejo de Ficheros"

print(re.match("Esta es la leccion", my_string, re.I))      #MATCH - El match debe ser desde el principio de la cadena

match = re.match("Esta es la leccion", my_string, re.I)
print(match)            
start, end = match.span()
print(my_string[start:end])

print(re.match("Esta no es la leccion", my_other_string))      

match = re.match("Esta no es la leccion", my_other_string)
if not(match ==None):
    print(match)            
    start, end = match.span()
    print(my_other_string[start:end])
else:
    print("No hay concidencia")

print(re.match("Expresiones Regulares", my_string))         #NONE 

##search

search =re.search("leccion", my_string, re.I)           #Busca la primera coincidencia en cualquier parte de la cadena
print(search)
start, end = search.span()
print(my_string[start:end])

##Findall

findall= re.findall("leccion", my_string, re.I)         #Busca todas las coincidencias en cualquier parte de la cadena
print(findall)

##split

print(re.split(":", my_string))                         #busca un patron ":" y a partir de ahi divide en elementos

##sub
print(re.sub("leccion |leccion", "LECCION ", my_string))  #Sustituye el valor inicial por el segundario, en la primera coincidencia
print(re.sub("Expresiones Regulares", "RegEx", my_string))

## Patterns
pattern= r"[lL]eccion"                  #Patron para exprecion regular simple 
print(re.findall(pattern, my_string))

pattern= r"[lL]eccion|Expresiones"      #Patron para exprecion regular combinada
print(re.findall(pattern, my_string))

pattern= r"[0-9]"                       #Patron para exprecion regular numero
print(re.findall(pattern, my_string))

pattern= r"\d"   #Patron para exprecion regular solo para caracteres numericos
print(re.findall(pattern, my_string))

pattern= r"\D"   #Patron para exprecion regular solo para caracteres alfabeticos
print(re.findall(pattern, my_string))

pattern= r"[l]."   #Patron para exprecion regular caracter principal y su caracter seguido
print(re.findall(pattern, my_string))

# email autentication 
email = "letto@misena.edu.co"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(re.findall(pattern, email))
