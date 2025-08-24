"Idoneidad para un puesto"

experiencia= float(input("Ingrese los años que ha laborado: "))

lenguaje= input("Ingrese el programa (java o python) que conoce: ")

if experiencia >=3 or (experiencia == 2 and (lenguaje =="Java" or lenguaje == "Python")):
    print("elegible")
#elif experiencia <3 and lenguaje == True:
 #   print("elegible")
else:
    print("no eres elegible")

pass