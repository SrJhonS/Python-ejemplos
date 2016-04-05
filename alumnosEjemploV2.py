class Persona():

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre+" "+self.apellido+", "+str(self.edad) 

    @property#Ponemos property para que al llamar a mayor_de_edad, este llamando a un atributo
    def mayor_de_edad(self):
        return self.edad > 17

def agregar(numero, bbdd=[]):

    for i in range(numero):
        nombre = str(input("Introduce un nombre: "))
        apellido = str(input("Introduce un apellido: "))
        edad = int(input("Introduce el numero de edad: "))

        bbdd.append(Persona(nombre, apellido, edad))

    return bbdd

def mostrar(bbdd):
    for persona in bbdd:
        print(persona)#Con esto muestra toda la informacion
        #print(persona.nombre)#Con esto solo muestra los nombres

def mostrar_adultos(bbdd):
    for persona in bbdd:
        if persona.mayor_de_edad:
            print(persona)

bbdd=[
        Persona('Jose Luis', 'Rodriguez', 26), 
        Persona('Gabriel', 'Sanchez', 17), 
        Persona('Laura', 'de la Torres', 12), 
        Persona('Virginia', 'Sanz', 25)
]

numero = int(input("Introduce el numero de alumnos que va a anadir: "))
bbdd = agregar(numero, bbdd)
#mostrar(bbdd)
mostrar_adultos(bbdd)