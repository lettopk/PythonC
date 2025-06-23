### CLASSES ###

class MyEmptyPerson:        #Clase vacia
    pass 

print(MyEmptyPerson)
print(MyEmptyPerson())

class Person:               #Clase con constructor
    def __init__(self, name, surname, alias="Sin alias"):
        self.Full_name = f"{name} {surname} ({alias})"
        self.__name = name #Propiedad privada
    
    def get_name (self):
        return self.__name
    
    def walk(self):         #Con el parametro self puedo acceder a los valores del constructor de la clase
        print(f"{self.Full_name} Esta Caminando")
    
my_person = Person("Letto", "pk")
print(f"{my_person.Full_name}")
print(my_person.get_name())     #Llama name privada
my_person.walk()            #Llama la funcion de la clase

my_other_person = Person("letto", "pk", "Lettopk")  #Creando otra persona
print(f"{my_other_person.Full_name}")
my_other_person.walk()

my_other_person.Full_name= "Hector de leon (El loco de los perros)" #Cambiando el valor a la otra persona
print(my_other_person.Full_name)

