class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre+" "+self.apellido+", "+str(self.edad) 

    def mayor_de_edad(self):
        return self.edad > 17

def agregar(numero):
    lista = []
    for i in range(numero):
        nombre = str(input("Introduce un nombre: "))
        apellido = str(input("Introduce un apellido: "))
        edad = int(input("Introduce el numero de edad: "))
        lista.append(Persona(nombre, apellido, edad))
    return lista

def mostrar(lista):
    for persona in lista:
        print(persona)

numero = int(input("Introduce el numero de alumnos que va a anadir: "))
lista = agregar(numero)
mostrar(lista)