'''Creá una clase base Figura con método area() que lance NotImplementedError. Definí las
subclases Cuadrado, Triangulo y Circulo, cada una con su propia implementación de area().
Después, creá una lista mezclada de figuras y recorrela imprimiendo el área de cada una. Identificá
en comentarios qué pilar estás usando en cada paso.'''


'''Se utililiza polimorfirmo:  al establecer que cada metodo area se comporte de manera diferente segun la clase
Herencia en las clases hijas de Figura, abstraccion al establecer cada atributo y metodo '''

import math 

class Figura():
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError("Las clases hijas deben implementar este metodo")

class Cuadrado(Figura):
    '''Hereda  de Figura y utiliza polimorfismo en metodo area'''
    def __init__(self,lado):
        self.lado=lado
        self.nombre='Cuadrado'
        
    def area(self):
        return self.lado**2

class Triangulo(Figura):
    '''Hereda  de Figura y utiliza polimorfismo en metodo area'''
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
        self.nombre='Triangulo'
        
    def area(self):
        return (self.base*self.altura)/2

class Circulo(Figura):
    '''Hereda  de Figura y utiliza polimorfismo en metodo area'''
    def __init__(self,radio):
      self.radio=radio
      self.pi=math.pi
      self.nombre='Circulo'
      
    def area(self):  
      return self.pi*(self.radio**2)
         



circulo=Circulo(5)
triangulo=Triangulo(2,4)
cuadrado=Cuadrado(20)

Lista=[circulo,triangulo,cuadrado]

for i in Lista:
    print("El area del ",i.nombre,'es: ',i.area())