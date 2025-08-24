import json
import os

menu = """
----------------------------------------------------------------------
    1) Registrar nota de estudiante
    2) Consultar todas las notas
    3) Calcular el promedio de notas
    4) Guardar registro de notas
    5) Salir
-----------------------------------------------------------------------
"""

print("-----------------------------------------------------------------------")
print("                      REGISTRO DE NOTAS                                ", end="")



# {
#    "Elena Araya" : 85,
#    "Sandra Sánchez" : 92,
#    ...
# }

ruta = "calificaciones.json"

if os.path.exists(ruta) == False:
    with open(ruta, mode="w", encoding="utf-8") as archivo:
        json.dump({}, archivo)


with open(ruta, mode="r", encoding="utf-8") as archivo:
    libro_calificaciones = json.load(archivo)


archivoGuardado = True

while True:

    print(menu)
    if archivoGuardado == False:
        print("El archivo no ha sido guardado! Utilice la opción #4 antes de salir.")
        print()

    opcion = input("Ingrese el número de la opción que desea ejecutar: ")

    os.system("clear")

    if opcion == "1":
       
       nombre_estudiante = input("Indique el nombre del estudiante: ")
       calificacion = input("Indique la calificación del estudiante: ")

       calificacion = float(calificacion)

       libro_calificaciones[nombre_estudiante] = calificacion

       archivoGuardado = False

       print("SE HA AGREGADO EL REGISTRO DEL ESTUDIANTE")
       input("Pulse Enter para continuar!")
       os.system("clear")
       

    elif opcion == "2":
        
        for nombre, calificacion in libro_calificaciones.items():
            print(  f"* {nombre} {calificacion}"  )

        print("SE HA IMPRESO EL LISTADO DE CALIFICACIONES")
        input("Pulse Enter para continuar!")
        os.system("clear")

    elif opcion == "3":
        
        # total_calificaciones = 0
        # for calificacion in libro_calificaciones.values():
        #     total_calificaciones = total_calificaciones + calificacion
        
        # cantidad_calificaciones = len(libro_calificaciones) 

        # promedio = total_calificaciones / cantidad_calificaciones

        if len(libro_calificaciones) == 0:
            promedio = 0
        else:
            total_calificaciones = sum( libro_calificaciones.values() )
            promedio = total_calificaciones / len(libro_calificaciones)

        print("El promedio de calificaciones del grupo es de", promedio)

        print("SE HA IMPRESO EL PROMEDIO DE CALIFICACIONES")
        input("Pulse Enter para continuar!")
        os.system("clear")

    elif opcion == "4":

        with open(ruta, mode="w", encoding="utf-8") as archivo:
            json.dump(libro_calificaciones, archivo, indent=4)

        print("SE HA GUARDADO EL ARCHIVO")
        input("Pulse Enter para continuar!")
        os.system("clear")

    elif opcion == "5":
        break
    else:
        print("La opción seleccionada es incorrecta")
        input("Pulse Enter para continuar!")
        os.system("clear")



print("Adios!")