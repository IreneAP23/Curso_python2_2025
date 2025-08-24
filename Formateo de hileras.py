#Formateo de hileras

#nombre= input("Ingrese un nombre")

#frase_completa= "¡Hola a todos desde python. Les saluda: " 

nombre ="Juan"
apellidos ="Sanchez"
edad= 35
salario=125000

#f string, 2f para poner 2 decimales, con solo , se le pone la coma a los numeros
datos_completos= f"El empleado se llama {nombre} {apellidos} tiene {edad} años y gana {salario:,.2f} colones a la semana"
print(datos_completos)

