### DICTIONERIES ###

my_dict = dict()
my_other_dic = {}
print(type(my_dict))
print(type(my_other_dic))

my_other_dic={"nombre": "letto", "apellido":"pk", "edad":30, 1:"Python"}
my_dict  = {
    "nombre": "letto", 
    "apellido":"pk", 
    "edad":30, 
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.67
    }

print(my_dict)
print(my_other_dic)

print(len(my_other_dic))
print(len(my_dict))

print(my_dict["nombre"])

my_dict["nombre"] ="pedro" #Actualizar un campo del diccionario
print(my_dict["nombre"])

print(my_dict[1])

my_dict["calle"] ="Calle letto" #Agregar un elemento al diccionario
print(my_dict)

del my_dict["calle"]  #Eliminar un solo elemento del diccionario
print(my_dict)

print("letto" in my_dict) 
print("nombre" in my_dict) #Buscar clave en el diccionario
print("pk" in my_dict["apellido"]) #Buscar valor en una clave del diccionario

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dic = dict.fromkeys(("nombre", 1,2)) #crea un diccionario nuevo sin valores
print(my_new_dic)

my_new_dic = dict.fromkeys(my_dict) #crea un diccionario nuevo sin valores
print(my_new_dic)

my_new_dic = dict.fromkeys(my_dict,["letto" , "pk"]) #crea un diccionario nuevo sin valores
print(my_new_dic)