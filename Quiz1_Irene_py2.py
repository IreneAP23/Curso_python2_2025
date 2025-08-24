#Curso python 2
# Quiz/Ejercicio 1
#Fecha:4/08/2025
#Elaborado por: Irene Aguilar Peña

#Matrices
import numpy as np
import matplotlib.pyplot as plt

#Crear una matriz de 4x4 con números aleatorios entre 0 y 100

matriz= np.random.randint(1,101, size=(4, 4 ))
print("Matriz random\n", matriz)
print()
#Extrar las 2 primeras filas y las dos últimas columnas

sub_matriz= matriz[0:2, -2:]
print("Extración 2 primeras filas y las dos últimas columnas\n",sub_matriz)
print()

#gráfico de lineas eje X indices de la primera fila y Y valores de esa fila
datos=matriz[0, :]
print("datos de la primera fila\n", datos)

plt.figure(figsize=(6,6))
plt.plot(datos,datos, label="línea de datos", color="navy", linestyle="-", linewidth=2)
plt.title("Gráfico de línea")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.grid(True)
plt.legend()
plt.show()

#Histograma de todos los elementos de la matriz original
data_hist=matriz.flatten()
plt.figure(figsize=(7,5))
plt.hist(data_hist, bins=50, color="navy", edgecolor="black", alpha=0.6)
plt.title("Histograma de valores de una matriz")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.grid(axis="y", alpha=0.6)
plt.show()





