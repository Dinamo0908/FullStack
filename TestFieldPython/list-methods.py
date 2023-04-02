lista = list(["hola", "dalto", 34]) #Crea una lista
print(len(lista)) #Devuelve cantidad de elementos de la lista
print(lista.append(2)) #Añade un elemento al final de la lista
print(lista)
lista.insert(1, "HOPLAAAAA") #Añade un elemento en el index especificado
print(lista)
lista.extend([2030, 2120]) #Añade elementos de otra lista dentro de la lista
print(lista)
lista.pop(0) #Elimina elementos de la lista segun el index seleccionado
print(lista)
lista.pop(-1) #Elimina el ultimo elemento de la lista
print(lista)
lista.remove(2) #Elimina el elemento en base a su valor
print(lista)
lista.clear() #Elimina todos los elementos de la lista
print(lista)

lista2 = [False, True, 32, 2.3]
lista2.sort() #Ordena los elementos de menor a mayor
print(lista2)
lista2.sort(reverse=True) #Ordena los elementos de menor a mayor y luego de mayor a menor
print(lista2)
lista2.reverse() #Invierte el orden de los elementos
print(lista2)
el_enc = lista2.index(32)
print(el_enc)


print(dir(set["hola", "chau"])) #metodos aplicables a set
print(dir(tuple["hola", "chau"])) #metodos aplicables a tuple
