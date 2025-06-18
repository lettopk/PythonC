### STRINGS ### 

my_string = "Mi String"
my_other_string = 'Mi Otro String'

print(len(my_string))
print(len(my_other_string))

print(my_string +" "+ my_other_string)

my_new_line_string = "Este es una String \ncon salto de linea "
print (my_new_line_string)

my_tab_string = "\t Este es una String con tabulacion"
print (my_tab_string)

my_scape_string = "\\t Este es una String con \n escapado" #Doble \\ para cancelar el comando
print (my_scape_string)


# FORMATEO
name, surname, age = "Letto" , "pk" , 30
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# DESEMPAQUETADO DE CARACTERES
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)


#Division
language_slice = language[1:3] # 1 y 2 
print(language_slice)

language_slice = language[1:] # 1 en adelante
print(language_slice)

language_slice = language[-2] # final menos la cantidad
print(language_slice)

language_slice = language[0:6:2] # todos los caracteres de 2 en 2 
print(language_slice)

#REVERSE
reverse_language = language[::-1] #Da la vuelta a la cadena de texto
print(reverse_language)

#FUNCIONES
print(language.capitalize()) #pone en mayuscula elprimer caracter
print(language.upper()) #Pone todo en mayuscula
print(language.count("t")) #Cuanta cuantas  t hay en la cadena
print(language.isnumeric()) #identifica si es un numero 
print(language.lower())
print(language.upper().isupper()) #concatenacion de Mayuculas y verificacion de mayuscula
print(language.startswith("py")) #verificacion de caracteres con los que empieza la cadena 