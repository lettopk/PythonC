### FILE HANDLING ###
import os

#.txt File

txt_file = open("Intermediate/my_file.txt", "w+") #Escribir y leer w+

#txt_file.write("mi nombre es Letto\nMi apellido es PK\n30 anios\nmi lenguaje favorito es PYTHON")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())
#print(txt_file.readlines())
for line in txt_file.readlines(): #Leer varias lineas
    print(line)
    
txt_file.write("\nAunque tambien me gusta java")    #Escribir
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt") as my_other_file:
    for line in my_other_file.readlines(): #Leer varias lineas
        print(line)


#os.remove("Intermediate/my_file.txt")

#.JSON file
import json

json_file = open("Intermediate/my_file.json", "w+") #Abrir el archivo

json_test = {
    "nombre": "letto",
    "apellido":"pk",
    "edad":30,
    "language": ["Python", "swift","kotlin"],
    "website": "https://letto.dev"}

json.dump(json_test, json_file, indent= 2)     #Escritura

json_file.close()

with open("Intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines(): #Leer varias lineas
        print(line)


json_dict = json.load(open("Intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["nombre"])

# .csv file
import csv

csv_file = open("Intermediate/my_file.csv", "w+")

json_test = {
    "nombre": "letto",
    "apellido":"pk",
    "edad":30,
    "language": ["Python", "swift","kotlin"],
    "website": "https://letto.dev"}

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name","surname", "age","language","webside"]) #Escribe fila a fila
csv_writer.writerow(["letto","pk", "35","python","https://letto.dev"])
csv_writer.writerow(["Roswell","", "2","cobol",""])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines(): #Leer varias lineas
        print(line)

#.xlsx file
#import xlrd #debe instalarse el modulo 

# .xml file
import xml

