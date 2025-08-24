import os
import subprocess

# host="google.com"
# respuesta= os.system(f"ping -c 4 {host}")
# if respuesta ==0:
#     print(f"{host} esta accesible")
# else:
#     print(f"No se pudo encontrar a {host}")
# os.system("ipconfig")#para windows
# os.system("route print")
# os.system("neststart -an")

#resultado =subprocess.run(["ping", "google.com","-n","-2"])

host= "scanne.nmap.org" #hay que instalar un programa
resultado= subprocess.run(["nmap","-p","80,443", host],capture_output=True,text=True)
print(resultado.stdout)