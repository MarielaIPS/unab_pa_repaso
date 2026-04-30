'''Rehacé al menos 3 clases que ya hayas programado antes (por ejemplo Punto, Linea, Cancion)
usando el constructor type() en lugar de class. Verificá que los objetos creados funcionan igual.'''

def __init__Animal(self,nombre,edad):
    self.nombre=nombre
    self.edad=edad
    
def sonido(self,so):
    self.so=so
    print(f"{so}")
    
Animal=type('Animal',(),{'__init__':__init__Animal,'sonido':sonido})

perro1=Animal("perro",5)
perro1.sonido("GUAUUUU")
print(perro1.nombre)

gato=Animal("gato",10)
gato.sonido("Miau-miau")
print("Nombre:" , gato.nombre, "Edad: ", gato.edad)

'''---------------------------------------------------'''

def __init_cancion(self,nombre,autor):
    self.nombre=nombre
    self.autor=autor

def mostrar(self):
    return f"La cancion es: {self.nombre}, Su autor es: {self.autor}"

Cancion=type("Cancion",(),{"__init__":__init_cancion, "mostrar":mostrar})

cancion1=Cancion("La vida loca","Ricky Martin")
print(cancion1.mostrar())

'''---------------------'''
