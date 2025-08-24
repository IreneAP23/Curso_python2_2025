
import numpy as np
#matriz_uno= [[1,2,3], [4,5,6]]

#print(matriz_uno)
#print(matriz_uno [0][1])

# matriz_2= np.array([[1,2,3],[3,4,5]])
# print(matriz_2)
# print(type(matriz_2))

# ceros= np.zeros((3,4))
# print("Matriz de ceros:\n",ceros)

# #hacer una matriz 1 de dimenciones 2x2

# unos= np.ones((2,2))
# print("matriz de unos:\n",unos)

# #hacer una matriz  de identidad

# identidad= np.eye(5) 
# print(identidad)
# print()
# #hacer un arreglo en un rango
# rango= np.arange(10)
# print(rango)
# print()
# #hacer una matriz consecutiva del 0 al 8 en una matriz de tamaño 3x3
# matriz_consecutiva= np.arange(9).reshape(3,3)
# print(matriz_consecutiva)
# print()

#Hacer matriz de numeros aleatorios
# aleatorios= np.random.rand(2,3)
# print(aleatorios)
# print()
# aleatorios_normal= np.random.randn(2,3)
# print(aleatorios_normal)
# print("--------------------------------------------------")
#Atributos de una matriz en Numpy

# print("Dimenciones: ", matriz_2.shape)
# print("Numero de dimensiones: ", matriz_2.ndim)
# print("Tipo de datos que contiene la matriz: ", matriz_2.dtype)
# print("Cantidad de elementos: ", matriz_2.size)

#Operaciones con matrices
matriz_3= np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Accediendo al segundo elmento de la segunda fila: ", matriz_3[1,1])
print("Accediendo al ultimo elmento de la matriz: ", matriz_3[2,2])
print("Accediendo al ultimo elmento de la matriz: ", matriz_3[-1,-1])

print("Accediendo a todos los elementos de una fila: ", matriz_3[0, :])
print("Accediendo a todos los elementos de una fila: ", matriz_3[1, :])
print("Accediendo a todos los elementos de una fila: ", matriz_3[2])

print("Accediendo a una columna completa de una matriz: ", matriz_3[:,0])

sub_matriz= matriz_3[0:2,1:3]
print(sub_matriz)

data= np.array([[10,20,30],[40,50,60],[70,80,90]])
mask= data > 50
print("imprimiendo solo valores mayores a 50")
print(data[mask])