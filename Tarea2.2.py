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


#Reporte por categoría

#Solicitar al ususario que ingrese una categoria 

#cuales categorías hay?
llave= "categoría"
tipo_categoria= []

for diccionario in datos:
    tipo_categoria.append(diccionario[llave])
    for elemento in tipo_categoria:
        if elemento not in tipo_categoria:
            tipo_categoria.append(elemento)
print(tipo_categoria )

#uso un ciclo while para verificar que el valor ingresado por el usuario existe.
cat_usuario= input("Ingrese una categoria: ")

while cat_usuario== tipo_categoria:
    if cat_usuario== True:
    #si existe tiene que jalar todos los articulos de esa categoria
        articulo=tipo_categoria.values("nombre")
        break
    else:
        print("Error! vuelva a ingresar un valor: ")
print()


#crear y escribir el archivo
ruta3="reporte_categoria.csv"

#exportar los productos de esa categoria
with open (ruta3, mode="w", newline="", encoding="utf-8") as archivo_cat:
    #extraer llaves para los encabezados ##revisar extraer productos
    campos=["nombre"]
    #escribir csv 
    cat=csv.DictWriter(archivo_cat, fieldnames=campos)
    #escribir los encabezados
    cat.writeheader()
    #escribir filas
    cat.writerows(articulo)

print("Archivo reporte_categoria.csv fue creado, buscar el archivo en la carpeta.")
print()