class Complejo():
    def __init__(self,x,y,u,v):
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        print("El primer numero complejo tiene la forma:", x, "+", y,"i")
        print("El segundo numero complejo tiene la forma:", u, "+", v,"i")

    def sumar(self):
        parte1 = x + u 
        parte2 = y + v
        return (print("El resultado de sumar estos numeros complejos es:", parte1, "+", parte2,"i"))
 
    def restar(self):
        parte1 = x - u 
        parte2 = y - v
        return (print("El resultado de restar estos numeros complejos es:", parte1, "+", parte2,"i"))

    def multiplicar(self):
        parte_real = (x*u) - (y*v)
        parte_compleja = (x*v) + (y*u)
        return (print("El resultado de multiplicar estos numeros complejos es:", parte_real, "+", parte_imaginaria,"i"))

    def dividir(self):
        parte_real1 = (x*u) + (y*v)
        parte_compleja1 = -(x*v) + (y*u)
        parte_real2 = (u*u) + (v*v)
        parte_compleja2 = -(u*v) + (v*u)
        total = (parte_real1 + parte_compleja1)/(parte_real2 + parte_compleja2)
        return (print("El resultado de dividir estos numeros complejos es:", total))

c = Complejo(3,4,5,6)
print(c.sumar())
print(c.restar())
print(c.multiplicar())
print(c.dividir())



   
