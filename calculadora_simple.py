"calculadora simple"

x= float(input("Ingrese le primer numero: "))

y= float (input("ingrese el segundo numero: "))

operación= input("Ingrese la oparación a realizar: 1 para suma, 2 para resta, 3 para multiplicación: ")



if operación == "1":
    resultado=  x + y 
elif operación == "2":
    resultado= x - y
elif operación == "3":
    resultado= x * y 

print("el resultado es :", resultado)

pass