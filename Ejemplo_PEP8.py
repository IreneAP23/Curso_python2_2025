def calcular_suma(a, b):
    """Esta funcion calcula la suma de dos numeros."""
    resultado = a + b
    return resultado

class ClaseEjemplo:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_saludo(self):
        print(f"Hola, {self.nombre}!")

#Llama a la función
resultado = calcular_suma(3,5)
print(resultado)

#creación de una instancia de la clase y llamada a un método
objeto_ejemplo = ClaseEjemplo("usuario")
objeto_ejemplo.mostrar_saludo()