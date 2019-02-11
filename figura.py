class Figura():
    def __init__(self):
        pass
    
    def dame_area():
        pass
    
    def dame_perimetro():
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado 
    
    def dame_area(self):
        area = self.lado ** 2
        return area
    
    def dame_perimetro(self):
        perimetro = self.lado * 4
        return perimetro
        
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def dame_area(self):
        area = self.base * self.altura
        return area
    
    def dame_perimetro(self):
        perimetro = (self.base * 2) + (self.altura * 2)
        return perimetro
        

c = Cuadrado(3)
print("El area es:" c.dame_area())
print("El perimetro es:" c.dame_perimetro())

r = Rectangulo(4, 5)
print("El area es:" r.dame_area())
print("El perimetro es:" r.dame_perimetro())
    

