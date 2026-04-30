class Autor:
    def __init__(self, nombre, nacionalidad):
        self.nombre = nombre
        self.nacionalidad = nacionalidad

class Libro:
    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor # AGREGACION: recibe el Autor desde afuera
        self.isbn = isbn
        self.paginas = paginas
def mostrar(self):
    print(f"Titulo: {self.titulo}")
    print(f"Autor: {self.autor.nombre} ({self.autor.nacionalidad})")
    print(f"ISBN: {self.isbn}")
    print(f"{self.paginas} paginas")

# Uso
a = Autor("Borges", "argentino")
l = Libro("Ficciones", a, "978-950-00-0000-0", 224)
l.mostrar()
# Si destruyo 'l', el Autor 'a' sigue existiendo -> agregacion