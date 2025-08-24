"calculadora de propina"

cuenta= float(input("ingrese el total de la cuenta: "))

porcentaje_propina= float(input("ingrese el porcentaje de propina a dejar: "))

propina= cuenta *(porcentaje_propina/100)

total_pagar=cuenta + propina

print("El total a pagar es: ", total_pagar, "colones")

pass