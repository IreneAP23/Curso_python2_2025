"Elegibilidad para beca"
#autor: Irene Aguilar 
#año de creación 2025

"Datos del usuario"
prom_calificaciones= float(input("Ingrese el promedio de las calificaciones, en escala de 0 a 10: "))

prueba_estandar= float(input("Ingrese la puntuación de la prueba estandarizada en una escala de 0 a 100: "))

"Elegibilidad"
if prom_calificaciones >=8 and prueba_estandar >=80:
    print("!Felicidades! Usted es elegible para la beca.")
else:
    print ("No califica para la beca.")

pass