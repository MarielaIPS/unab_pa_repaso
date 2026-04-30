'''Definí una clase CuentaBancaria con atributos titular y _saldo (protegido).
Agregá métodos
depositar(monto), extraer(monto) (que no permita dejar saldo negativo) y consultar_saldo(). Justificá
brevemente qué pilar de la POO estás aplicando al usar _saldo.'''

class CuentaBancaria():
    
    def __init__(self,titular,saldo):
        self.titular=titular
        self._saldo=saldo
    
    def depositar(self,monto):
        self._saldo+=monto
        print(f'Su Deposito de $ {monto} se ha realizado con exito')
    
    def extraer(self,monto):
        if self._saldo <= monto:
            raise ValueError("No puede extrar más saldo del que tiene")
        else: self._saldo-=monto
        print(f'La Extraccion de $ {monto} se ha realizado con exito')
    
    def consultar_saldo(self):
        mostrar=print(f"El saldo en su cuenta es de $ {self._saldo}")
        return mostrar
    
juan=CuentaBancaria('juan perez',20)
juan.depositar(10)
juan.consultar_saldo()
juan.extraer(15)
juan.consultar_saldo()
