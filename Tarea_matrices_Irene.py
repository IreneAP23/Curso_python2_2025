#Curso python2
#Tarea 1
#Creado por: Irene Aguilar Peña.
#Fecha de entrega: 6 de agosto 2025

#Suma de Matrices de cualquier tamaño
#Ambas deben tener las mismas dimenciones(filas -columnas)

import numpy as np

matriz1=([0,1,2],[3,4,5])
matriz2=([0,1,3],[2,2,4])

#verificar que cumple con las dimenciones
def sumar_matrices(matriz_1, matriz_2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        resultado =[]
        for i in range(len(matriz1)):
            fila=[]
            for j in range(len(matriz2)):
                suma=matriz1
                fila.append(matriz1[i][j] + matriz2[i][j])
            resultado.append(fila)
        print("Resultado", resultado)
    else:
        print("las matrices no tienen las mismas dimenciones")

suma= sumar_matrices(matriz1, matriz2)