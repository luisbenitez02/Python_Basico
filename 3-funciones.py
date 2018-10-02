'''Veremos los elementos esenciales de las funciones:
- Que reciben variables y regresan valores, con paraemtros por defecto '''

def saludar():
     print('Hola Pythoneros')

def saludoNew(nombre):
     print('Hola, ', nombre)

def sumar(num1,num2):
     suma = num1+num2
     return suma

#parametros por defecto
def elevado(num1=5,num2=2):
     eleva = num1**num2
     return eleva

saludar()
saludoNew('Vivi')
print(sumar(5,2))

print(elevado())

valores = elevado(10, 2)
print(valores)
