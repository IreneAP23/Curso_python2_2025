#mod_sys_os

#import sys
# print("Argumentos recibidos")
# for i, arg in enumerate(sys.argv):
#     print(f"Argumento {i} : {arg}")

# respuesta = input("Desea salir s/n: ")
# if respuesta.lower()=="s":
#     print("saliendo del programa")
#     sys.exit(0)  #funciona como un Kill
# print("continuando...")


# print("Rutas de busqueda")
# for ruta in sys.path:
#     print(ruta)

# print(sys.version)

import os

# directorio_actual= os.getcwd()
# print(f"el directorio actual es: {directorio_actual}")
# directorio_actual= os.getcwd()
# os.chdir("..") # para cambiar directorio
# print(f"el directorio actual es: {directorio_actual}")

# archivos=os.listdir(".")
# print("Archivos en este directorio")
# for archivo in archivos:
#     print(archivo)

usuario=os.environ.get("USER") or os.environ.get("USERNAME")
print(f"usuario actual: {usuario}")

if not os.path.exists("nueva carpeta"):
    os.mkdir("nueva carpeta")
    print("carpeta nueva")
else:
    os.rmdir("nueva carpeta")
    print("carpeta eliminada")
print(os.listdir("."))
