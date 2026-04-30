'''Creá una clase Circulo con atributo radio. Agregá métodos area() (usar math.pi), perimetro() y
diametro(). Instanciá dos círculos distintos e imprimí sus valores.'''

import math 

class Circulo():
    
    def __init__(self, radio):
       self.radio=radio   
       self.pi=math.pi 
    
    def area(self):
        print("Area del Circulo:",round(self.pi*(self.radio**2),2) )
        return self

    def perimetro(self):
        print("Perimetro:",round(self.diametro()*self.pi,2))
        return self
    
    def diametro(self):
       return self.radio*2
   
    def ver_diametro(self):
       print("Diametro: " , self.diametro() )
    
circulo1=Circulo(20)
circulo1.area().perimetro().ver_diametro()

circulo2=Circulo(15)
circulo2.area().perimetro().ver_diametro()