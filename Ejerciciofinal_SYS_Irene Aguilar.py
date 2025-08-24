#Ejercicio final: script de mantenimiento de carpetas
#Python2 (L y M)
#Irene Aguilar

import sys
import os
from datetime import datetime

def log(mensaje):
    with open("log.txt", "a") as f:
        f.write(f"[{datetime.now()}] {mensaje}\n")

if len(sys.argv) < 2: 
    print("Uso: python mantenimiento.py <carpeta base>")#ingresar argumento valido
    sys.exit(1) #python lanza una excepción llamada SystemExist

base= sys.argv[1]
subcarpetas= ["entrada", "salida", "temporal"]

#crea la carpeta base si no existe
if not os.path.exists(base):
        os.mkdir(base)
        log(f"Carpeta base {base} creada. ")

#crea las subcarpetas
for sub in subcarpetas:
    ruta=os.path.join(base, sub)
    if not os.path.exists(ruta):
        os.mkdir(ruta)
        log(f"Subcarpeta {sub} creada. ")

#Elimina archivos temporales
ruta_temporal= os.path.join(base, "temporal")

for archivo in os.listdir(ruta_temporal):
    if archivo.endswith(".tmp"):
        ruta= os.path.join(ruta_temporal, archivo)
        os.remove(ruta)
        log(f"Archivo temporal eliminado: {archivo}")

print("mantenimiento completado. Revisa log.txt. ")