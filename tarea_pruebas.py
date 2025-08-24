#Ejercicios optativos
#6.
#Dos funciones que calculen el factorial de cualquier número entre 0 y menor que 25
# Pienso que se puede verificar los valores desde el inicio para ir depurando errores.

try:
    num=input("Ingrese un número, del cual desee conocer el factorial!: ")
    num=int(num)
    if num >25:
        print("¡Error!: el número no puede ser mayor a 25.")
    if num <0:
        print("¡Error! el número no puede ser menor a 0.")
except ValueError:
    print("¡Error!: ingrese un número valido")

def factorial_recursiva(num: int):
    """
    Esta función calcula el factorial de un numero de forma recursiva
    @num: es el valor que se va revisar, si es igual a 0 devuelve 1; 
    si es menor a 0 da error y si es mayor, 
    3! = 3*2*1=6
    @return guarda la formula de multiplicar
    el num por num-1
    """
    
    if num < 0:
        raise ValueError("¡Error!: el número no puede ser negativo")
    if num > 25:
        raise ValueError("¡Error!: el número no puede ser mayor a 25")
    if num ==0: #valor base que detiene la llamada recursiva
        return 1
    return num * factorial_recursiva(num-1)

#llamo la función
resultado= factorial_recursiva(num)
print(f"El factorial del número es: {resultado}")


#factorial iterativa

def factorial_iterativa(num: int):
    """
    Esta funcón calcula el factorial de un número de forma iterativa
    @num: es el valor que se va revisar, si es igual a 0 devuelve 1; 
    si es menor a 0 da error y si es mayor a 25 da error.
    @return: devuelve el resultado del ciclo for
    3! = 3*2*1=6
    @return :
    """
    if num < 0:
        raise ValueError("¡Error!: el número no puede ser negativo")
    elif num == 0:
        return 1
    if num > 25:
        raise ValueError("¡Error!: el número no puede ser mayor a 25")
    resultado=1
    for i in range(1, num+1):
        resultado *=i
    return resultado
    
#llamo la función
resultado= factorial_iterativa(num)
print(f"El factorial del número es: {resultado}")


#7 juego piedra, papel o tijera 

#1. piedra mata tijera
#2. papel envuelve piedra
#3. tijera mata papel

import random

def juego():
    """
    Esta función es el juego de piedra, papel o tijera
    se crea una lista que contenga los valores
    @compu recibe los valores de forma aleatorea con ramdon
    @jugador ingresa el valor con el que desea jugar
    """
    lista= ["piedra", "papel", "tijera"]

    while True:
        compu = random.choice(lista)
        jugador = None

        while jugador not in lista:
            jugador = input(" piedra papel o tijera: ").lower()
        if jugador == compu:
            print(f"compu", {compu})
            print(f"jugador", {jugador})
            print("¡Empate!")
        elif jugador == "piedra":
            if compu == "papel":
                print(f"compu", {compu})
                print(f"jugador", {jugador})
                print("¡Perdiste!")
            if compu == "tijera":
                print(f"compu", {compu})
                print("jugador", {jugador})
                print(f"¡Ganaste!")
        elif jugador == "papel":
            if compu == "tijera":
                print(f"compu", {compu})
                print(f"jugador", {jugador})
                print("¡Perdiste!")
            if compu == "piedra":
                print(f"compu", {compu})
                print(f"jugador", {jugador})
                print("¡Ganaste!")
        elif jugador == "tijera":
            if compu == "piedra":
                print(f"compu", {compu})
                print(f"jugador", {jugador})
                print("¡Perdiste!")
            if compu == "papel":
                print(f"compu", {compu})
                print(f"jugador", {jugador})
                print("¡Ganaste!")
        jugar_otra_vez= input("Desea continuar jugando (si/no): ").lower()
    
        if jugar_otra_vez != "si":
            break
    print( "\nFin del juego")

juego()




