'''Ejercicio 6.2 — Por hacer: dos decoradores a la vez
Combiná los decoradores saludar y con_fecha_hora sobre la misma función. Probá cambiar el
orden y explicá con comentarios cómo afecta el resultado. ¿En qué orden se ejecutan?'''


def saludar(function):
    def wrapper():
        print("Hola")
        function()
        print("Chau")
    return wrapper


from datetime import datetime
def con_fecha_hora(function):
    def wrapper(*args, **kwargs):
        ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{ahora}] Ejecutando {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@saludar
@con_fecha_hora
def mi_funcion():
    print("Ver que  hace ")
    
if __name__ == "__main__":
    mi_funcion()