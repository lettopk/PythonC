### LIST COMPREHENSION ###

my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

my_range = range(8)     #crea una lista con un rango de 0 a n numero
print(list(my_range))

my_list = [i+1 for i in range(8)] #crea una lista con un rango de 0 a n numero, asignando un valor a cada elemento
print(my_list)

my_list = [i*2 for i in range(8)] 
print(my_list)
my_list = [i*i for i in range(8)] 
print(my_list)

def sum_five(num):
    return num+5

my_list = [sum_five(i) for i in range(8)] #Se modifica el valor, antes de guardarlo en la lista nueva
print(my_list)