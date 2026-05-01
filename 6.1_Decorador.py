'''Ejercicio 6.1 — Por hacer: evitar división por cero
Programá un decorador evitar_division_cero que se aplique a una función dividir(a, b). Si b es 0,
debe imprimir un mensaje de error y devolver None, sin ejecutar la división. Integralo en un ejemplo.'''

def evitar_division_cero(funcion):
    def envoltura(a,b):
        if b == 0:
            print("Nose puede dividir por Cero")
            return None
        else: 
            return funcion(a,b)
    return envoltura


@evitar_division_cero
def dividir(a,b):
    return a/b

print("Resultado valido: ",dividir(10,5))

print("Resultado Invalido: ",dividir(10,0))