### CONDITIONALS ###

my_condition = False

if my_condition:
    print("Se ejecuta la condicion del if")
    
my_condition = 5*5

if my_condition == 10:
    print("Se ejecuta la condicion del segundo if")
    
if my_condition > 10 and my_condition < 20:
    print("Es Mayor que 10 y menor que 20")
elif my_condition ==25 :
    print("Es igual 25")
else:
    print("Es Menor o igual que 10 o mayor o igual que 20 o distinto de 25")

print("la condicion continua")

my_string =""

if not my_string:
    print("Mi cadenade texto es vacia")
    
if my_string == "Mi cadena de textooo":
    print("Estas cadenas de texto coinciden")
