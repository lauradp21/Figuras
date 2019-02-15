class Producto():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

class Medicamento(Producto):
    def __init__(self, nombre, producto, composicion, porcentaje):
        self.composicion = composicion
        self.porcentaje = porcentaje

    def get_composicion(self):
        return self.composicion

    def get_porcentaje(self):
        return self.porcentaje

lista_productos = []
gasas = Producto("Gasas", 3)
matraz = Producto("Matraz", 7)
lista_productos.append(gasa)
lista_productos.append(matraz)

lista_medicamentos = []
aspirina = Medicamento("aspirina", 4, "sacarina", 0.2)
paracetamol = Medicamento("paracetamol", 1.7, "povidona", 0.05)
lista_medicamentos.append(aspirina)
lista_medicamentos.append(paracetamol)



class Laboratorio():
    def __init__(self, prod1, prod2, med1, med2)
        self.prod1 = prod1
        self.prod2 = prod2
        self.med1 = med1
        self.med2 = med2

    def total(self):
        return self.prod1, self.prod2, self.med1, self.med2

Mi_Labo = Laboratorio(lista_productos[0], lista_productos[1], lista_medicamentos[0], lista_medicamentos[1])
print("En nuestro laboratorio los productos totales incluyendo los medicamentos son:", Mi_Labo.prod1.get_nombre, Mi_Labo.prod2.get_nombre, Mi_Labo.med1.get_nombre, Mi_Labo.med2.get_nombre)
print("Como ejemplo de la informacion que hemos obtenido de uno de los medicamentos es: Nombre:", Mi_Labo.med1.get_nombre, "Precio:", Mi_Labo.med1.get_precio, "Composicion:", Mi_Labo.med1.get_composicion, "Porcentaje:", Mi_Labo.med1.get_porcentaje) 





        
    
