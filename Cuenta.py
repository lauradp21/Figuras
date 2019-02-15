class Cuenta():
    def __init__(self): #valor por defecto
        self.valor = 10000
   
    def __init__(self, valor):
        self.valor = valor

    def get_ingreso(self,ingreso):
        total = valor + ingreso
        return total
    
    def get_integro (self, integro):
        total = valor + integro
        return total

    def get_transferencia (self, transferencia): #Teniendo en cuenta que soy yo la que hace la tran
        total = valor - transferencia 
        return total


c1 = Cuenta()
print(c1.get_integro(100))

c2= Cuenta(2000)
print(c2.get_transferencia(50))

