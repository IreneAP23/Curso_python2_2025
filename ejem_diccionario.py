"ejemplo de diccionarios"
datos_personales = {
    "nombre": "José",
    "apellidos": "jimenez",
    "edad":35
}

#agrega un nuevo elemneto al diccionario
datos_personales["salario"]= 125665.55

#borrar edad
del datos_personales["edad"]

print( datos_personales)

tamanyo=len(datos_personales)
print(tamanyo)

