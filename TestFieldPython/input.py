#pide una entrada de datos al usuario
nombre = input("che capo, como te llamas: ") #input() devuelve SIEMPRE un string
print(nombre)
nombre_nuevo = nombre + "1"
print(nombre_nuevo)

#Transforma el input a otro tipo
numero = int(input("Bueno ahora dame un numero: ")) #tambien puede ser float()
suma = numero + 2
print("Bueno mira el numero que me diste es " + str(suma))