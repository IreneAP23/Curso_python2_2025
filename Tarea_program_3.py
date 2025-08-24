
#Tarea programada 3
#Creado por: Irene Aguilar Peña.

#1.
#entrada: 3 parámetros obligatorios
#definir la variable y hacer el input (entrada de datos).

#se crea la función que va a recibir los 3 parámetros

def funcion(operacion, numero1, numero2):
    """
    Esta función es un tipo de calculadora
    @parámetro 1: es la operación: suma, resta , multiplicación o modulo
    @parámetro 2: y 3 son los valores a los que se le va a aplicar la operación
    @return: se usa en modulo para deterner la función si hay un error
    """

    if operacion == "suma":
        resultado= numero1 + numero2 #suma los valores dados
    elif operacion == "resta":
        resultado= numero1 - numero2 #resta los valores dados
        #mejor incluí las palabras con tilde porque el usuario las podría escribir de las dos formas.
    elif operacion == "multiplicacion" or operacion== "multiplicación":
        resultado= numero1 * numero2 #multiplica los valores dados
    elif operacion == "modulo" or operacion == "módulo":
        if numero2 == 0 : 
            print("¡Error!. La variable numero2 debe ser mayor a 0.")#si el numero es menor a 2 da error.
            return #salir si hay error
        resultado= numero1 % numero2 #saca el modulo de los valores dados
    print(f"El resultado de la operación {operacion} es: {resultado}")

#se hace un try -except porque hay que garantizar que se ingrese un valor en número.
try:
    operacion=input("ingrese la operación a utilizar: ")
    numero1= input("ingrese el primer numero: ")
    numero2= input ("ingrese el segundo numero: ")
#modulo solo funciona con numeros enteros
    numero1=int(numero1)
    numero2=int(numero2)
except ValueError:
    print("¡Error!. Ingrese el valor de las variables llamadas número como un valor.")
    print()
    exit()

funcion( operacion, numero1, numero2)
print()


#2. crear una lista de numeros, ordenarla menor a mayor y obtener su mediana
#pedir al usuario una lista de numeros
lista=[]

while True:
    num= input("¡Bienvenido!, ingrese un número para crear una lista, escriba (S) para terminar: ")
    if num == "S" or num == "s":
        break
    try:
        num=float(num)
        lista.append(num)
    except ValueError:
        print("¡Error!. Solo debe ingresar números.")
    #ordenar la lista, sort la ordena de menor a mayor
    lista.sort()
    
print ("\nLos números ordenados de la lista son : ", lista)

#defino la función

def funcion_m(lista:list):
    """
    Esta función calcula la mediana de una lista dada
    @indice_i: me da la mitad de la lista -1, 
    @indice_s:me da la mitad de la lista
    @centro=me da la mitad de la lista en listas pares
    """
    #medir el tamaño de la lista
    tamanyo=len(lista)
#sacar la mediana
#si la lista es par se promedian los valores centrales
    if tamanyo % 2 == 0:
        indice_i=tamanyo // 2 - 1
        indice_s= tamanyo //2
        mediana= (lista[indice_i]+ lista[indice_s])/2
    else: #si a lista es impar se toma el valor del centro
        centro=tamanyo//2
        mediana= lista[centro]
    print("\nLa mediana de la lista es: ", mediana )

#llamo la función
funcion_m(lista)
print()

#3. funcion que concatene lo que reciba

def concatena(*args):
    """
    Esta función une los argumentos que le dan e ingresa un espacio entre ellos
    @concatenar: es la que va a recibir los elementos que se van a unir
    @elemento: es la variable que uso en el for para ver cada elemento
    @return: devuelve lo que se concatena
    """
    concatenar=""
    for elemento in args:
        concatenar += str(elemento) + " "
    return concatenar

#llamar la funcion
resultado= concatena("Este es el mes", 4, "=", "True" )
print(resultado)
print()

#4 Función que recibe párametros con restricciones:
def imprimir_info(**kwargs):
    """
    Esta función devuelve pares clave-valor de información suministrada
    @clave: es la llave del diccionario, va a recibir el valor
    @valor: es el valor que se le asigno a la llave
    """
    for clave, valor in kwargs.items():
        if valor == None: #se hace para asignar el "no indica" si el valor no se asigna.
            valor = "No indica"
        print(clave + ": " + str(valor))

# si el valor no exite debe imprimir no indica
imprimir_info(Nombre="Juan", Apellido="Salas", Direccion= None, Edad="33", Profesion="Informático", Email="correo@ejemplo.com", Telefono=22107085)
print()

#5 Función con dos valores, sumar y si no se puede, indicar el error

#voy a ingresara dos valores
val1= input("Ingrese un primer valor: ")
val2= input("Ingrese un segundo valor: ")


def suma(val1: int, val2: int):
    """
    Esta función debe sumar dos valores, 
    si alguno no es valido debe mostrar el mensaje de error
    @val1:es el primer valor ingresado
    @val2: es el segundo valor ingresado
    @return si todo esta bien devuelve la suma, si no en la exepción indica que 
    no puede aplicar los datos al operador enviado.
    """
    try:
        val1= int(val1)
        val2= int(val2)
        return val1 +val2
    except ValueError:
        return ("No se puede aplicar este operador a los datos enviados") 

#se llama la función
resultado=suma(val1, val2)
print(resultado)
print()
print("Final del código")






