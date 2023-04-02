str1 = "Hola soy Agus 23"
str2 = "Bienvenido rey"
str3 = "hola"

print(dir(str1)) #devuelve lista de atributos, funcion
print(str2.upper()) #metodo que pasa string a mayusc
print(str2.lower()) #metodo que pasa string a minusc
print(str1.capitalize()) #Transforma todo en minusc y luego la primera letra en mayusc
print(str1.find("A")) #Busca las posiciones de cada caracter ingresado y se detiene a la primera vez que lo encuentra
print(str1.find("z")) #Cuando no lo encuentra, devuelve -1
print(str1.index("a")) #Similar a find, pero si no encuentra el caracter, lanza una excepcion
print(str1.isnumeric()) #Devuelve True/False dependiendo de si es un texto unicamente numerico o no
print(str3.isalpha()) #Devuelve True/False dependeinde de si es un texto con caracteres de la a - z
print(str1.count("o")) #Cuenta la cantidad de veces que se repiten los caracteres ingresados
print(len(str3)) #Cuenta la cantidad de caracteres en un string, funcion
print(str1.startswith("H")) #Devuelve True/Flase dependiendo de si el string empieza con el caracter ingresado
print(str1.endswith("3")) #Mismo que la anterior, solo que considera si termina con el caracter ingresado
print(str1.replace("Ho", "Puto")) #Reemplaza un caracter por otro. De no encontrar el caracter en el string, lo mantiene igual.
print(str2.replace("z", "jeje"))
print(str1.split(" ")) #Separa el contenido del string mediando el caracter ingresado como referencia y los añade a una lista