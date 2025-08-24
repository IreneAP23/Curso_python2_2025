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