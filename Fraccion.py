class Fraccion():
    def __init__(self,x,y,u,v):
        self.x = x
        self.y = y
        self.u = u
        self.v = v

    def sumar(self):
        total = (x/y) + (u/v)
        return total
    
    def restar(self):
        total = (x/y) - (u/v)
        return total

    def multiplicar(self):
        total = (x*u)/(y*v)
        return total
 
    def dividir(self):
        total = (x*v)/(y*u)
        return total

f1 = Fraccion(2,5,7,4)
print(f1.restar())
print(f1.multiplicar())

f2 = Fraccion(6,9,8,3)
print(f2.dividir())
print(f2.sumar())
