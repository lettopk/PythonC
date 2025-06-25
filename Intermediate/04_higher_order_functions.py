### HIGHER ORDER FUNCTIONS ### 

def sum_one (value):
    return value +1 

def sum_five (value):
    return value + 5  

def sum_two_values_and_add_value (first_Value, second_value, f_sum):    #rECIBE UNA FUNCION COMO PARAMETRO
    return f_sum (first_Value + second_value)

print(sum_two_values_and_add_value (5,2, sum_one))
print(sum_two_values_and_add_value (5,2, sum_five))

### CLOSURES ### 

def sum_ten (original_value):       #fUNCIONES ANIDADAS
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))
print(sum_ten(5)(1))  #ejecucion como lambda

### BUILT-IN HIGHER ORDER FUNCTIONS ### 
#Funciones de orden superior en sistema

numbers = [2,5,10,21,3,30,50]
#MAP
def mutiply_two (number):
    return number*2

print(list(map (mutiply_two, numbers))) #itera cada valor en la lista, y lo ejecuta en la funcion
print(list(map (lambda number:number *2 , numbers)))

#FILTER

def filter_greater_than_ten(number):
    if  number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers))) #Recorre toda la lista, y fiiltra con true o false, segun coinsida
print(list(filter(lambda number: number>10, numbers)))


#REDUCE

from functools import reduce

def sum_two_values (first_value,second_value):
    return first_value + second_value

print(reduce(sum_two_values,numbers)) # relaciona cada valor del iterable
print(reduce(lambda first_value, second_value: first_value + second_value ,numbers))