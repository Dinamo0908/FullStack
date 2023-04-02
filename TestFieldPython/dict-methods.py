diccionario = {
    "nombre" : "lucas", #Da lo mismo si es 'key' o "key"
    "apellido" : "dalto",
    "subs" : 100
}

print(diccionario.keys()) #Devuelve las keys del dict
print(diccionario.get('nombre')) #Devuelve el valor de la key ingresada. Si no lo encuentra, lanza 'None'
print(diccionario["nombre"]) #Si no lo encuentra, lanza una excepcion
print(diccionario.items()) #Devuelve el diccionario exactamente como está para poder iterarlo
print(diccionario.pop("nombre", "subs")) #Elimina los valores dentro de las keys ingresadas
print(diccionario.clear()) #Elimina todos los elementos del diccionario