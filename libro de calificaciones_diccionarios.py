#libro de calificaciones

libro_calificaciones={
    "Ana": {"Matematicas":85, "Ingles": 90, "Sociales": 70},
    "Erick":{"Matematicas}":85, "Ingles": 90, "Sociales": 70}
}

print(libro_calificaciones)

nombre=input("ingrese el nombre del estudiante: ")
nota_mate=input("ingrese nota matematicas: ")
nota_ingles=input("ingrese nota ingles:  ")
nota_sociales=input("ingrese nota sociales: ")

nota_mate=int(nota_mate)
nota_ingles=int(nota_ingles)
nota_sociales=int(nota_sociales)

libro_calificaciones[nombre] = {
    "Matematicas": nota_mate,
    "Ingles": nota_ingles,
    "Sociales": nota_sociales
}

print(libro_calificaciones)


print("promeSdio de calificaciones")
print()
for nombre_estudiante in libro_calificaciones.keys():
   
    calificaciones= libro_calificaciones[nombre_estudiante]
   
    #suma_calificaciones= calificaciones["Matematicas"] + calificaciones["Ingles"] + calificaciones["Sociales"]
    suma_calificaciones= sum(calificaciones.values)
   
    promedio = suma_calificaciones / len(calificaciones)
   
    print("promedio de ", nombre_estudiante, "es de ",promedio )


