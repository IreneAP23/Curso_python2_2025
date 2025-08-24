"""Tarea 10% Suma de números Impares y conteo de Números pares hasta N"""
#Autor: Irene Aguilar Peña

numero= input("Ingrese un número entero positivo: ")
numero= int(numero)

if numero <= 0:
    print("Error: debe ingresar un numero entero positivo")

for i in range(1, numero):
   print(i)


print("-----------------------")  
suma=0
contador =0
for x in range(1, numero):   
    if x %2==0:
        contador +=1
        #print( contador)
    else:
        suma += x
        #print(suma)

print("La cantidad total de números pares encontrados es: ", contador)
print("La suma total de los números impares es: ", suma)

print("fin del programa")