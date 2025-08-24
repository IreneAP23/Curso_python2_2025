"ejemplo de diccionarios"

datos_personales = {
    "nombre": "José",
    "apellidos": "jimenez",
    "edad":35,
    "salario":125634,
    "Dirección":"Cartago",
    "Hobbies": ["futbol" , "leer", "correr", "nadar"]
}

print(datos_personales["Hobbies"][2])


#lista anidada
grupos_mundial=[
    ["Suiza", "Alemania", "Costa Rica", "Uruguay"], #0 indice
    ["Guatemala", "Brasil", "Camerún", "Japón"],  #1
    ["Argentina", "Mexico", "España", "Tunez"] #2
]

print(grupos_mundial[0][0]) #suiza
print(grupos_mundial[1][0]) #Guatemala


LETRAS_GRUPO= ("A", "B", "C","D", "E", "F", "G")

#ciclo for anidado
#\t agrega una tabulación o sangria.
for indice, grupo in enumerate(grupos_mundial, 0):
    print("GRUPO", LETRAS_GRUPO[indice])
    for pais in grupo:
        print("\t", pais) #tabula