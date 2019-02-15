class Alumno():
    def __init__(self, nombre, n_matricula, nota1, nota2, nota3):
        return
    
    def dame_info(self):
        print(n_matricula)
        print(nombre)
        nota_final = (nota1 + nota2 + nota3)/3
        print(nota_final)
        if nota_final >= 4.8:
            print("Has aprobado el examen")
        else:
            print("Has suspendido el examen")

a = Alumno(Pepe, 672, 7, 4, 6)
print(a.dame_info())
