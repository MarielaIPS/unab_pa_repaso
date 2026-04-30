'''Modelá una clase Computadora que esté compuesta por un Procesador y una Memoria (ambas
clases creadas por vos, con sus atributos). La Computadora debe crear sus componentes dentro de
su propio constructor. Agregá un método ficha_tecnica() que imprima la info completa. Justificá por
qué es composición y no agregación.'''

'''Es composicion por que si la computadora desaparece tambien lo hacen sus partes'''

class Computadora():
    def __init__(self,modelo,capacidad):
        # COMPOSICIÓN: La computadora crea sus propias partes al nacer.
        self.procesador=Procesador(modelo)
        self.memoria=Memoria(capacidad)

    def ficha_tecnica(self):
        print(f"El modelo del procesador es: {self.procesador} y su memoria tiene una capacidad de: {self.memoria} GB")

class Procesador():
    def __init__(self,modelo):
        self.modelo=modelo
        
    def __str__(self):
        return self.modelo

class Memoria():
    def __init__(self,capacidad):
        self.capacidad=capacidad
    def __str__(self):
        return str(self.capacidad)
        
computadora=Computadora("MR123",78)
computadora.ficha_tecnica()