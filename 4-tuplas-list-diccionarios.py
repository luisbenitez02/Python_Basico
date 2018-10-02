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