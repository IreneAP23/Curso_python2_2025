#Ejercicio 1, 2, 
#Python2 (L y M)
#Irene Aguilar

import os
base= "proyecto_demo"
subcarpetas= ["entrada", "salida", "temporal"]

if not os.path.exists(base):
    os.mkdir(base)
    print(f"Carpeta {base} creada. ")

for sub in subcarpetas:
    ruta=os.path.join(base, sub)
    if not os.path.exists(ruta):
        os.mkdir(ruta)
        print(f"Subcarpeta {sub} creada. ")

#crear archivos temporales
for i in range(3):
    ruta_archivo=os.path.join(base, "temporal", f"archivo{i}.tmp")
    with open(ruta_archivo,"w") as f:
        f.write("Este es un archivo temporal.\n")

#Ejercicio 2

ruta_temporal= os.path.join("proyecto_demo", "temporal")

for archivo in os.listdir(ruta_temporal):
    if archivo.endswith(".tmp"):
        ruta= os.path.join(ruta_temporal, archivo)
        os.remove(ruta)
        print(f"Eliminado: {archivo}")
#archivos tmp desaparecieron

