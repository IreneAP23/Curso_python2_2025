"""este programa permite calcular grados C a partir 
de grados F
calculadora de F a C """

#autor: Irene Aguilar
#fecha de creación: 08/04/2025
#versión 1.0

#se usa int para convertir la entrada (str) a entero y float a flotante
grados_farenheit=( input("ingrese los grados farenheit a convertir: "))

grados_farenheit=float(grados_farenheit)

resultado_celsius= (grados_farenheit -32) * 5/9 #esto es igual a grados C

print("la cantidad de grados F corresponde a ", resultado_celsius, "grados celcius")

pass