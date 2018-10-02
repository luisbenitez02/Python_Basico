'''Condicional IF Simple'''
edad= 20
if edad>19:
     print('Es correcto')
else:
     print('estamos pailas')
#identar en python es esencial

'''IF Anidados'''
chance = 240
ganador= True

if chance==240:
     if ganador:
          print('Eres un ganador')
     else:
          print('Tu billete es falso loco')
else:
     print('Ese numero no salio')

'''Operadores relacionales'''

if chance!=204:
     print('Casi le atinas')

'''Operadores Logicos'''
#se expresan con palabras y no con letras como en java
if chance==240 and edad>18:
     print('Eres un joven millonario')

if edad==20 or chance==240:
     print('O eres joven o eres millonario, no estan nada mal')

'''Bucle while------------------------------------------------------------------'''
numero = 0
while numero<20:
     print(numero)
     numero+=1