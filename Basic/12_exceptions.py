### EXCEPTIONS HANDLING###

number_one = 5
number_two = 1

number_two = "1"

# Try except
try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")   #Se ejecuta si se produce la excepcion
    

# Try except else finally
try:
    print(number_one + number_two)
    print("No se ha producido error")
except:
    print("Se ha producido un error")
else:
    print("La ejecucion continua correctamente")    #Se ejecuta si no se produce la excepcion
finally:
    print("La ejecucion contuna")       #Se ejecuta  Siempre


# Try except captura excepciones por tipo de error
try:
    print(number_one + number_two)
    print("No se ha producido error")
except ValueError:   #Se agrega el tipo de error
    print("Se ha producido un ValueError")
except TypeError:   #Se agrega el tipo de error
    print("Se ha producido un TypeError")
    
    
# Try except captura de la info de la excepciones 
try:
    print(number_one + number_two)
    print("No se ha producido error")
except TypeError as e:  #Captura la info del error para typeError
    print("Se ha producido un TypeError")
    print(e)
except Exception as exception: #Captura la info del error generico que se presento
    print(exception)