#__init__(), que siempre se ejecuta cuando se inicia la clase

class Personas: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Personas("Jordan", 24) 
print(p1.name)
print(p1.age)       
#nota: 
# La __init__()función se llama automáticamente cada vez que la clase se usa para crear un nuevo objeto.



print("-_-")
#__str__() controla lo que se debe devolver cuando el objeto de clase se representa como una cadena.
#__str__() no está configurada, se devuelve la representación de cadena del objeto:

#representacion de una cadena de un objeto

class Car: 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"{self.marca} y el modelo {self.modelo}"

auto = Car("Toyota", 2030)

print(auto)
        
print("-_-")

#los objetos tambien pueden tener metodos
#los metodos son funciones que pertenecen a un objeto


class Escula: 
    def __init__(self, alumno, funcion):
        self.alumno = alumno
        self.funcion = funcion

    def myfunc(self):
        print("Holaa my name is " + self.alumno , " y here ", self.funcion)


persona = Escula("Pepe", 12)
print(persona)
