#"Tarea programada #2"
#Creado por: Irene Aguilar Peña
#Generación de reportes CSV a partir de datos JSON

#Programa que lea archivo JSON y cargue los datos en memoria

#Para leer archivo json
import json
#comprobar que el archivo existe
import os

#pretty print: es para ver los datos acomodados de forma más legible
import pprint


#lee la cadena json directamente desde un objeto archivo y muestra los datos en memoria y convierte en diccionario
with open("C:/Users/iagui/Desktop/Python2025/tarea2/productos.json", "r", encoding="utf-8") as archivo:
    datos= json.load(archivo)
    pprint.pprint(datos)

#Reporte general: todos los productos con sus datos completos
print(datos)
import csv
#crear y escribir
with open ("reporte_prueba.csv", mode="w", newline="", encoding="utf-8") as archivo_csv:
    #extraer llaves para los encabezados
    campos=datos[0].keys()
    #escribir csv basado en diccionarios
    general=csv.DictWriter(archivo_csv, fieldnames=campos)
    #escribir los encabezados
    general.writeheader()
    #escribir filas
    general.writerows(datos)
    
print("archivo prueba creado, buscar archivo en la carpeta.")

#Reporte de inventario, solo incluye id, nombre, stock, valor_total

#datos es una lista de diccionarios, hay que extraer los campos que me pide
#multiplicar precio * stock para crear valor_total

for producto in datos:
    for clave, valor in datos.items():
        print({precio} * {stock})

total