### LISTAS ### 
my_list = list()
my_other_list = []

print(len(my_list))

my_list =[30,24,62,52,30,17]

print(my_list)
print(len(my_list))

my_other_list = [30, 1.67, "letto", "pk"]
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])


# FUNCIONES CON LISTAS
print(my_other_list.count("letto"))
print(my_list.count(30)) #saber cuantas veces se repite el valor

age, height, name, surname =my_other_list
print (name)

print(my_list + my_other_list)

my_other_list.append("56d") #Agregar un elemento alfinal de la lista
print(my_other_list)

my_other_list.insert(1,"Rojo") #Agregar un valor en el index definido en la lista
print(my_other_list)

my_other_list[1] = "Azul" #Asiganr un nuevo valor a un indice ya existente
print(my_other_list)

my_other_list.remove("Azul") # elimina el primer elemento que coincide con el valor
print(my_other_list)

my_list.pop() #elimina un elemnto de la lista por defecto del indice -1, pero retorna el valor 
print(my_list)
print(my_list.pop())

del my_list[2] #elimina del todo el valor en el indice especificado
print(my_list)

my_new_list = my_list.copy() #copia una lista en una nueva lista


my_list.clear() #borra todos los valores de la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() #Ordena los valores al reves
print(my_new_list)

my_new_list.sort() #Ordena por orden de menor a mayor (por defecto), pero se le puede asignar condiciones de organizacion
print(my_new_list)

print(my_new_list[1:2]) #"sub lista"


my_list = "Hola Python"
print(my_list)
print(type(my_list))