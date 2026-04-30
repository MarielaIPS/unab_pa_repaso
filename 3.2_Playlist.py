'''Ejercicio 3.2 — Por hacer: Playlist (agregación)
Modelá una clase Playlist que tenga una lista de objetos Cancion (reutilizá la clase Cancion de la
práctica 3 con titulo y autor). La Playlist debe recibir las canciones desde afuera (agregación).
Agregá métodos agregar_cancion(c), cantidad() y listar().'''

'''Agregacion: Si yo borrara la Playlist las canciones guardadas en la lista seguirian existiendo '''

class Cancion():
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
        
    def __str__(self):
        return f"Autor: {self.autor} - Titulo: {self.titulo}"

class Playlist():
    def __init__(self,lista):
        self.lista=lista
        
    def agregar_cancion(self,c):
        self.lista.append(c) 
    
    def cantidad(self):
        return len(self.lista) 
    
    def listar(self):
        for indice,i in enumerate(self.lista,start=1):
            print(indice, i.autor,i.titulo)
    
    
    

lista=[Cancion("Cartonero","Ataque 77"),Cancion("Vivire","Cadena Perpetua")]

playlist1=Playlist(lista)
playlist1.agregar_cancion(Cancion("Tres pajaros","Ataque 77"))
print("Cantidad: ",playlist1.cantidad())
playlist1.listar()
print('\n')
playlist1.agregar_cancion(Cancion("Amigo","Ataque 77"))
playlist1.agregar_cancion(Cancion("El jorobadito","Ataque 77"))
playlist1.agregar_cancion(Cancion("El carro de la vida","Sincope"))
playlist1.listar()

print("Cantidad: ",playlist1.cantidad())