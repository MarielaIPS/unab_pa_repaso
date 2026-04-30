'''A partir de la clase Animal del ejemplo integrador, agregá Pato y Oveja. Implementá hablar() en
cada una. En el main, creá una lista con al menos un animal de cada tipo y usá un for que llame a
hablar() sobre todos.'''


class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre # encapsulamiento (convención con guion bajo)
        self._edad = edad
    def get_nombre(self): # getter
        return self._nombre
    def get_edad(self):
        return self._edad
    def hablar(self): # abstracción: las hijas la implementan
        raise NotImplementedError("Las subclases deben implementar hablar()")

class Perro(Animal): # herencia
    def hablar(self): # polimorfismo (override)
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

class Vaca(Animal):
    def hablar(self):
        return "Muu!"
    
    
class Pato(Animal):
    def hablar(self):
        return "Cuack-cuack"
    
class Oveja(Animal):
    def hablar(self):
        return "Meeeee"

# Polimorfismo en acción: un mismo mensaje, respuestas distintas
animales = [Perro("Toby", 3), Gato("Michi", 5), Vaca("Lola", 4),Oveja("Juana",2),Pato("Pepe",10)]
for a in animales:
    print(f"{a.get_nombre()} ({a.get_edad()} años) dice: {a.hablar()}")
