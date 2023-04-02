#Datos Simples
"string" #una linea
'string'

""""tus datos son
ola 
ola"""

'''
ola
ola
ola''' #multilinea

int = 4 
float = 4.6

boolean = False #True

#Datos Complejos
#list, modificable
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]
lista[3] = 2.1
print(lista)
print(lista[0])
print(lista[3])
lista = ["jeje"]
print(lista)

#tuple, no modificable sus elementos
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

"""NO SIRVE
tuple[2] = False"""
print(tupla)
tupla = ("Ahora cambie todo")
print(tupla)

#set, modificable sus posiciones pero no sus elementos, igual es iterable
set = {"Lucas", "Soy Dalto", "Lucas"}
print(set)
set = {"Nah mentira"}
print(set)
"""NO SIRVE
print(set[2]) no se puede acceder por index"""

#dict 'key' : value
diccionario = {
    'nombre' : "Agus",
    'canal' : 'Argenzuela Gaming',
    'god' : True,
    'altura' : 1.75
}
print(diccionario['nombre'])

