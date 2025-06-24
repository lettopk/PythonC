#Variables 

my_string_variable = "My string Variable"
print(my_string_variable)

my_int_variable= 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenacion de variables en un print 
print(my_string_variable, my_int_variable, my_bool_variable)
print('Este es el valor de:', my_bool_variable)

#Algunas funciones del sistema

print(len(my_string_variable)) #contador de caracteres

#variables en una sola linea
name,surname, alias, age = "Marlon", "Tarazona", "Letto", 29
print("Min nombre es", name, surname, "tengo" , age, "y mi alias es:", alias)

address:str = "Mi direccion"
address = 32
print(address)