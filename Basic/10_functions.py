### FUNCTIONS ###

def my_function ():
    print("Esto es una funcion")

my_function()

def sum_two_values(first_value, second_value):
    print(first_value + second_value)
    
sum_two_values(5 , 7)
sum_two_values("5", "7")

def sum_two_values_with_return (first_value, second_value): #retorno de valor
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname): #Asignando valores a el parametro textual
    print(f"{name} {surname}")
    
print_name(surname="pk", name="letto")

def print_name_with_default (name, surname, alias="Sin alias"): #Valor por defecto
    print(f"{name} {surname} {alias}")
    
print_name_with_default ("letto", "pk", "lettopk")
print_name_with_default("letto", "pk")

def print_upper_texts(*texts): #Multiples Parametros dinamico
    for text in texts:
      print(text.upper())
    
print_upper_texts("hola", "python", "lettopk")
print_upper_texts("hola")