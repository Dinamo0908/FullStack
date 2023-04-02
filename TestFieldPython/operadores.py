#operadores aritmeticos

#suma y resta
suma = 12 + 5
print(suma)
resta = 12 - 5
print(resta)

#multiplicacion y division
mult = 12 * 5
print(mult)
div = 12 / 5 #devuelve un dato float
print(div)
print(type(div)) #Devuelve el tipo de dato

#division de enteros
div = 12 // 5 #devuelve un int
print(div)
print(type(div))

#resto/modulo
div = 12 % 5
print(div)

#exponente
expo = 5**2
print(expo)

#operadores de comparación
es_igual_que = 5 == 6
print(es_igual_que)
es_distinto_que = 5 != 6
print(es_distinto_que)
es_mayor_que = 5 > 6
print(es_mayor_que)
es_mayor_igual_que = 5 >= 6
print(es_mayor_igual_que)
es_menor_que = 5 < 6
print(es_menor_que)
es_menor_igual_que = 5 <= 6
print(es_menor_igual_que)

a = 50
b = 10
c = 20
comparacion = a +  b < c
print(comparacion)

contrasenia_guardada = "Dalto"
contrasenia_escrita = 'Dalto'
print(contrasenia_escrita == contrasenia_escrita) #Ignora los "" y los '', son lo mismo

#Condicionales
if (a > 49):
    print("podes pasar") #esta es la opcion que se cumplira, por ser la condicion principal
    if (c == 19):
        print("Que capo")
    elif (c + a == 70):
        print("Que caposaurio")
elif (b == 10):
    print("Quizas puedas pasar")
else:
    print("No podes pasar")
    
#Operadores Logicos
resultado_and = True & False #False
print(resultado_and)
resultado_or = False | False #False
print(resultado_or)
resultado_not = not True #False
print(resultado_not)