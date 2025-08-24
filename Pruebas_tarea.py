"pruebas para tarea"


lista=[]
num= True
while num != 0:
    num= input("¡Bienvenido!, ingrese un número para crear una lista, escriba (fin) para terminar: ")
    if num == "fin":
        break
    num=float(num)
    lista.append(num)

print ("Los números ingresados son : ", lista)

print("__________________________________________________")

#2. Suma total de los numeros ingresados
print("Suma de números")
suma = 0
for y in lista:
    suma += y
print(y)

num_menor = lista[0]
num_mayor = lista[0]

for x in lista:
    if x > num_mayor:
        num_mayor = x
    if x < num_menor:
        num_menor=x



divisor= 2
for i in lista:
    if i %divisor == 0:
        print(i, " no es primo")   
    elif i % divisor!=0:
        divisor=divisor+1
    if i==divisor:
       print(i, " es primo")

#version 2 
for i in lista:
    divisor= 2
    primo = True
    while primo and divisor <i:
        if i % divisor == 0:
            primo =False
        print(i, " no es primo")
        else:
            divisor += 1
    if primo:
       print(i, " es primo")
#Sversion 3
for i in lista:
    divisor= 2
    primo = True
    if i % divisor == 0:
        continue
    print(i, " es primo")
else:
    divisor += 1
    if primo:
        print(i, " no es primo")

#mayor= None
#menor=None
#for elemento in lista: 
 """  if mayor==None or menor == None
    mayor=elemento
    menor= elemento
    else:
    if elemento> mayor:
    mayor=elemento
    if elemento<menor:
    menor=elemento"""