"Tarea programada 20%"
#Creado por: Irene Aguilar Peña

#Escribir un programa en Python que permita al usuario
#  ingresar una serie de números hasta que el usuario decida
#  no seguir cargando más. Los números ingresados deben
#  guardarse en una lista como flotante. 

lista=[]
num= True
while num != 0:
    num= input("¡Bienvenido!, ingrese un número para crear una lista, escriba (fin) para terminar: ")
    if num == "fin":
        break
    num=float(num)
    lista.append(num)
print()
print ("Los números ingresados son : ", lista)

print("__________________________________________________")

#1. Obtener número menor y mayor de la lista.
print("Números mayor y menor")
print()
tamanyo_lista= len(lista)
num_menor = None
num_mayor = None

if tamanyo_lista > 0:
    num_menor = lista[0]
    num_mayor = lista[0]

for x in lista:
    if x > num_mayor:
        num_mayor = x
    if x < num_menor:
        num_menor=x

print("El numero menor de la lista es: ", num_menor)

print("El número mayor de la lista es: ", num_mayor)

print("__________________________________________________")

#2. Suma total de los numeros ingresados
print("Suma de números")
print()
suma = 0
for elemento in lista:
    suma = suma + elemento

print("La suma total de los numeros ingresados es: ", suma)

print("__________________________________________________")

#3. media o promedio
print("Promedio")
print()
cuenta =0
for elemento in lista:
    cuenta= cuenta+1

total = suma/cuenta

print ("El promedio es: ", total )

print("__________________________________________________")
#4. Lista adicional de numeros pares
print("Números pares")
print()
par = []
for z in lista:
    if z %2==0:
        par.append(z)
print ("Los números pares ingresados son : ", par)

print("__________________________________________________")
#5. Numeros Primos o no. entero, >=1, divisible por si mismo
print("Números primos")
print()
for i in lista:
    divisor= 2
    primo = True
    if i % divisor == 0:
        print(i, ": no es primo")
    else:
        divisor += 1
        if primo:
            print(i, ": es primo")

print("__________________________________________________")

#6 Opcional: ordenar la lista de menor a mayor

print("Lista ordenada de menor a mayor")
print()
#Usando método burbuja

band=False
while band ==False:
    band=True
    for valor in range (len(lista)-1):
        if lista[valor] > lista[valor +1]:
            aux=lista[valor]
            lista[valor] = lista[valor+1]
            lista[valor + 1] = aux
            band= False
print("La lista ordenada es: ", lista)
print()
print("_________________fin del programa_________________")
print()