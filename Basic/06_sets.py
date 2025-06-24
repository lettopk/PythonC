### SETS ### 

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Letto", "pk", 30}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("56d") 
print(my_other_set) # No es una estructura ordenada

my_other_set.add("56d") # NO admite repetidos
print(my_other_set)

print("pk" in my_other_set) #consulta si un elemento existedentro del set
print("Moure" in my_other_set) 

my_other_set.remove("pk")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set # Elimina el objeto por completo

my_set = {"Letto", "pk", 30}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set ={"kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set) # Asignacion a un nuevo set, de la union de dos sets
print(my_new_set.union(my_new_set).union(my_set).union({"Java", "C#"})) # se pueden unir cuantos quiera, pero no se van a repetir valores

print(my_new_set.difference(my_set)) #Diferencia entre dos sets