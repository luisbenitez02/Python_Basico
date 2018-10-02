'''La tupla permite guardar elementos combinados o de diferente tipo
La tupla NO puede cambiar'''

#esto sera una tupla
vivi_data = (21,1.70,'cafes','A+','Viviana','Bonilla',True)

print(vivi_data[4])#imprimo 4 elemento de la tupla (desde 0)
#recorre la tupla

indice =0
while indice < len(vivi_data):
     print(vivi_data[indice])
     indice+=1

#con la sentencia FOR
print('Con el FOR')
for dato in vivi_data:
     print(dato)

'''Porciones de la tupla: tomar pedazos para trabajar con ellos'''

vivi_basic = vivi_data[0:2] # edad, estatura, color ojos

'''Manejo de cadenas'''
nombre = 'Luis Hernando'
print(nombre[0:4])

'''Las listas: estas si se pueden cambiar, tanto su valor como su tamanio'''
luis_data = ['Luis', 'Benitez', 23, '1.73', 'O+', True]

print(len(luis_data))

for dato in luis_data:
     print(dato)

#vamos a agregar una lista 
daticos_extra = ['Ing de sistemas', 'Palmira', 'Colombia', 2705896]

total = luis_data + daticos_extra
print(total)

#operaciones con listas
if 23 in luis_data:
     print('Valor encontrado')

print(daticos_extra[1:2])

#valores negativos para acceder
print('Ultimo valor (-1),', total[-1]) #imprime solo uno, no todo el acumulado

'''Los diccionarios'''
beniLarouse = {'Luis':23,'Viviana':21,'Hot Dog': 6500, 'Halo':'Papus'}

print(beniLarouse['Luis'])

