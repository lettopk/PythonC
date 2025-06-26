### TUPLES ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.67, "letto", "pk" , "letto")
my_other_tuple =(30, 60, 35)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("letto")) #Cuenta cuantos valores coinciden con el valor que le damos
print(my_tuple.index("pk"))# Retorna el index del valor que le demos

# my_tuple[1]= 1.80 no se puede cambiar el valor, es inmutable

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])

my_tuple = list(my_tuple) #se puede tranformar en lista para poder modificar
print(type(my_tuple))

my_tuple[4] = "56d"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

del my_tuple # ya no esta definida
# print(my_tuple) error, no existe