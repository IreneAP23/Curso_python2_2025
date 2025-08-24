
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



"""
#4 Función que recibe párametros con restricciones:
#**kwargs: acepta cualquier cantidad de argumentos

def imprimir_info(nombre: str, apellido: str, edad: int, profesion: str, email: str, direccion: str="No indica", telefono: int="No indica"):

    diccionario= {
        "Nombre":nombre,
        "Apellido":apellido,
        "Edad":edad,
        "Profesion":profesion,
        "Email":email,
        "Dirección":direccion,
        "Telefono":telefono
    }
    return diccionario
    
#llamado a la función
x= imprimir_info("Juan", "Salas", 33, "Informático", "correo@ejemplo.com", 88881010)
for clave , valor in x.items():
    print(F"{clave}:{valor}")
 
"""
