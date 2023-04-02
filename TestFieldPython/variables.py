nombre = "dalto" #declarar = definir
nombre = "agus"

#Concatenar con +
bienvenida = "hola " + nombre + " que onda ahhh "

#Modificar variable
numero = 10
numero += 1

#F-strings
nombre2 = 5
bienvenida2 = f"Hola {nombre2} como estas?"
print(bienvenida + nombre + str(numero))
del numero
print(bienvenida2)

#operadores de pertenencia
print("ola" in bienvenida)
print("Mario" not in bienvenida)

#camelCase
broHola = "broHola"

#snakeCase (recomendado)
bro_hola = "bro_hola"