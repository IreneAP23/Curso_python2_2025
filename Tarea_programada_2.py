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
#para trabajar archivos csv
import csv

#1. Reporte general: todos los productos con sus datos completos

ruta="productos.json"
#verificar que el archivo json existe
#lee la cadena json directamente desde un archivo y muestra los datos en memoria y convierte en diccionario
if os.path.exists(ruta):
    with open(ruta, "r", encoding="utf-8") as archivo:
        datos= json.load(archivo)
        pprint.pprint(datos)
else:
    print("Error!, el archivo JSON no existe.")
print()

#ruta relativa, permiste que el código funcione en cualquier entorno
ruta1= "reporte_general.csv"
#crear y escribir el archivo csv según las indicaciones dadas
with open (ruta1, mode="w", newline="", encoding="utf-8") as archivo_csv:
    #extraer llaves para los encabezados
    campos=datos[0].keys()
    #escribir csv basado en diccionarios
    general=csv.DictWriter(archivo_csv, fieldnames=campos)
    #escribir los encabezados
    general.writeheader()
    #escribir filas
    general.writerows(datos)
    
print("Archivo reporte_general.csv fue creado, buscar el archivo en la carpeta.")
print()

#2. Reporte de inventario, solo incluye id, nombre, stock, valor_total

#datos es una lista de diccionarios, hay que extraer los campos que me pide

#multiplicar precio * stock para crear valor_total
for articulo in datos:
    articulo["valor_total"]= articulo["precio"] * articulo["stock"]

#extraigo las llaves y valor que necesito. Y creo una nueva variable con esa información. 
new_datos=[]
for producto in datos:
    new_datos.append({
        "id":producto["id"],
        "nombre": producto["nombre"],
        "stock": producto["stock"],
        "valor_total":producto["valor_total"]
        })

#ruta relativa, permiste que el código funcione en cualquier entorno
ruta_csv="reporte_inventario.csv"

#modo w porque el archivo no existe, lo creo según instrucción dada
with open (ruta_csv, mode="w", newline="", encoding="utf-8") as archivo:
    #definir las columnas solicitadas
    field=["id", "nombre", "stock", "valor_total"] 
    #escribir csv basado en diccionarios
    inventario=csv.DictWriter(archivo, fieldnames=field)
    #escribir los encabezados
    inventario.writeheader()
    #escribir las filas
    inventario.writerows(new_datos)
   
print("Archivo reporte_inventario.csv fue creado, buscar el archivo en la carpeta.")
print()

#3. Reporte por categoría ingresada por el usuario

#Solicitar al ususario que ingrese una categoría 

#cuales categorías hay?
llave= "categoría"
valor_existe=[]  #va a ser mi lista de categorías para verificar existe el valor ingresado por el usuario.
for diccionario in datos:
    valor=diccionario.get(llave) #sacamos el valor de la llave
    valor_existe.append(valor)   #lo hacemos lista
#print( valor_existe) #si se imprime puede ayudar a ver las categorias que existen

#uso un ciclo while para verificar que el valor ingresado por el usuario existe
#si no existe le va a pedir que vuelva a ingresar un valor
ingreso_usuario= input("Ingrese una categoría: ")
while ingreso_usuario not in valor_existe:
    print("Error! vuelva a ingresar un valor: ")
    ingreso_usuario= input("Ingrese una categoría: ")
solo_categoria=[]
for articulo in datos:
    if articulo["categoría"]== ingreso_usuario:
#si existe tiene que jalar todos los articulos de esa categoría
        solo_categoria.append(articulo["nombre"])
#print(solo_categoria) #si se imprime se puede ver lo que va a estar escrito en el csv según la categoría seleccionada
print()
#ruta relativa, permiste que el código funcione en cualquier entorno
ruta3="reporte_categoria.csv"

# #crear y escribir el archivo
#exportar los productos de la categoría que ingreso el usuario
with open (ruta3, mode="w", newline="", encoding="utf-8") as archivo_cat:
    #escribir csv 
    escritor=csv.writer(archivo_cat)
    #escribir filas
    escritor.writerow([solo_categoria])
print("Archivo reporte_categoria.csv fue creado, buscar el archivo en la carpeta.")
print()

