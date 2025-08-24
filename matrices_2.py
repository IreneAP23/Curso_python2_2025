
import numpy as np

matriz_a= np.array([1,2],[3,4])
matriz_b= np.array([5,6],[7,8])

matriz_c= ([1,2],[3,4])
matriz_d= ([5,6],[7,8])
#puedo realizar operaciones matematicas entre ellas

# print("suma:\n", matriz_c+matriz_d)

# def suma_matrices_cuadradas(m1,m2):
#     n=len(m1)
#     resultado=[]
#     for i in range(n):
#         fila=[]
#         for j in range(n):
#             fila.append(m1[i][j] + m2[i][j])
#         resultado.append(fila)
#     return resultado

# suma_matrix=suma_matrices_cuadradas(matriz_c,matriz_d)
# print(len(matriz_c))
# print(suma_matrix)

#tarea: Hacer una funcion que sume matrices de cualquier tamaño

# print("resta \n", matriz_a-matriz_b)
# print("resta \n", matriz_a*matriz_b)

#Funciones de agregación
#matriz_e= np.array([[1,2],[3,4],[5,6]])
#De matriz_a

# print("suma total de los elementos: \n", matriz_a.sum())
# print("promedio de los elementos: \n", matriz_a.mean())
# print("valor maximo de la martriz: \n", matriz_a.max())
# print("valor minimos de la matriz: \n", matriz_a.min())

# print( "suma por columna: \n" , matriz_e.sum(axis=0))
# print("promedio por fila: \n", matriz_a.mean(axis=1))


arreglo= np.arange(12)
print("Arreglo original \n", arreglo)

matriz_3x4=arreglo.reshape(3,4)
print("nueva matriz 3x4: \n", matriz_3x4)

matriz_6x2=arreglo.reshape(6,2)
print("nueva matriz 3x4: \n", matriz_6x2)


