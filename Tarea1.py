# Primero debemos pedir los datos al usuario
cespanol = input("Ingrese la calificación en Español: ")
cmatematicas = input("Ingrese la calificación en Matemáticas: ")
cciencias = input("Ingrese la calificación en Ciencias: ")
csociales = input("Ingrese la calificación en Sociales: ")

# Al ser strings, se deben convertir a flotante o entero

# Se recicla la variable
cespanol = float(cespanol)
cmatematicas = float(cmatematicas)
cciencias = float(cciencias)
csociales = float(csociales)

# Calculamos el promedio
promedio = (cespanol + cmatematicas + cciencias + csociales) / 4

# Imprimimos la información
print("Calificaciones Ingresadas:")
print("Español:", cespanol)
print("Matemáticas:", cmatematicas)
print("Ciencias:", cciencias)
print("Sociales:", csociales)

print("Promedio Total de Materias:", promedio)