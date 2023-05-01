### File Handling ###

import os

# .txt file
# Si el fichero no existe, crea el fichero
txt_file_01 = open("Intermedio/my_file_01.txt", "w+")  #Al poner r+, es posible leer y escribir en el fichero especificado. 
txt_file_01.write("Mi nombre es Manuel\nMi apellido es Castellanos\n38 años\nEl mejor lenguaje es Python\nTambién me gusta Kotlin")

print(txt_file_01.read(10))
print(txt_file_01.readline())
print(txt_file_01.readline())
print(txt_file_01.readlines())

for line in txt_file_01.readlines():
    print(line)

txt_file_01.write("\nTambién me gusta Kotlin")
print(txt_file_01.readline())

txt_file_01.close()

# Para borrar un fichero, se puede hacer con la siguiente línea:
#os.remove("Intermedio/my_file_01.txt")


# .json file
import json

json_file_01 = open("Intermedio/my_file_02.json", "w+")

json_test = {
    "name": "Manuel",
    "surname": "Castellanos",
    "age": 38,
    "languages": ["Python", "Swift", "Kotlin"],
    "website": "https://manuelricardo.com"
}

json.dump(json_test, json_file_01, indent=4)

json_file_01.close()

with open("Intermedio/my_file_02.json") as my_file_json:
    for line in my_file_json.readlines():
        print(line)

json_dict_01 = json.load(open("Intermedio/my_file_02.json"))
print(json_dict_01)
print(type(json_dict_01))
print(json_dict_01["name"])
print(json_dict_01["languages"])



# .csv file
import csv

csv_file_01 = open("Intermedio/my_file_03.csv", "w+")

csv_writer = csv.writer(csv_file_01)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Manuel", "Castellanos", 38, "Python", "https://manuelricardo.com"])
csv_writer.writerow(["Roswell", "", 2, "COBOL", ""])

csv_file_01.close()

with open("Intermedio/my_file_03.csv") as my_file_csv:
    for line in my_file_csv.readlines():
        print(line)




# .xlsx file
# import xlrd # Debe instalarse el módulo



# .xml file
import xml