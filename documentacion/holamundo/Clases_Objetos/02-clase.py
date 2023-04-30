


#El selfparámetro es una referencia a la instancia actual de la clase y 
#se utiliza para acceder a las variables que pertenecen a la clase.

class Escula: 
    def __init__(self, alumno, funcion):
        self.alumno = alumno
        self.funcion = funcion

    def myfunc(self):
        print("Holaa my name is " + self.alumno , " is  here ", self.funcion, "years")


persona = Escula("Pepe", 25)
persona.myfunc()

