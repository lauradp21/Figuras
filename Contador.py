Crea una clase Contador con los métodos par
a incrementar y decrementar el contador. La clase 
contendrá un constructor por defecto, un constructor con parámetros
y los métodos getters y 
setters.
class Contador():
    def __init__(self):
        self.contador = 5
    
    def __init__(self,contador):
        self.contador = contador 

    def incrementar(self):
        return self.contador + 1

    def decrementar(self):
        return self.contador - 1 

c1 = Contador()
print(c.incrementar())

c2 = Contador(10)
print(c.decrementar())


        
