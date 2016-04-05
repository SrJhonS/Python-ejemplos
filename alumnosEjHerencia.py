class Persona():

    def __init__(self, nombre, apellido, edad):#El constructor
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre+" "+self.apellido+", "+str(self.edad) 

    @property#Ponemos property para que al llamar a mayor_de_edad, este llamando a un atributo
    def mayor_de_edad(self):
        return self.edad > 17


class Alumno(Persona):
    def __init__(self, nombre, apellidos, edad, asignatura):
        super().__init__(nombre, apellidos, edad)
        self.asignatura=asignatura

    def __str__(self):
        return super().__str__()+" Asignatura: "+self.asignatura   


def agregar(numero, bbdd=[]):

    for i in range(numero):
        nombre = str(input("Introduce un nombre: "))
        apellido = str(input("Introduce un apellido: "))
        edad = int(input("Introduce el numero de edad: "))
        asignatura = int(input("Introduce la asignatura: "))

        bbdd.append(Alumno(nombre, apellido, edad, asignatura))

    return bbdd

def mostrar(bbdd):
    for i in bbdd:
        print(i)#Con esto muestra toda la informacion
        #print(i.nombre)#Con esto solo muestra los nombres

def mostrar_adultos(bbdd):
    for i in bbdd:
        if i.mayor_de_edad:
            print(i)

bbdd=[
        Alumno('Jose Luis', 'Rodriguez', 26, 'Matematicas'), 
        Alumno('Gabriel', 'Sanchez', 17, 'Filosofia'), 
        Alumno('Laura', 'de la Torres', 12, 'Educacion Fisica'), 
        Alumno('Virginia', 'Sanz', 25, 'Biologia'),
        Persona('Sara', 'Garrido', 18)
]

numero = int(input("Introduce el numero de alumnos que va a anadir: "))
bbdd = agregar(numero, bbdd)
mostrar(bbdd)
#mostrar_adultos(bbdd)