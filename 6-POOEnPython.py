class Persona:
    nBrazos= 0
    nPiernas= 0
    cabello= True
    colorCabello= 'Default'
    hambre = 0

    #cosntructor o inicializador
    def __init__(self):# self: a nosotros mismos
        self.nBrazos=2
        self.nPiernas=2

    #definiendo metodos
    # def dormir():#funcion sin definir
       # pass

    def comer(self):#modifica el atributo hambre de mi mismo
        self.hambre = 0

class Automovil:
    pass #permite dejar clase sin definir

class Hombre(Persona): #esta heredando de persona
    nombre='Default'
    sexo="M"

    def cambiarNombre(self, nombre):
        self.nombre = nombre

class Mujer(Persona):
    nombre='Default'
    sexo="F"

jose = Hombre()
jose.comer()
print(jose.hambre)
