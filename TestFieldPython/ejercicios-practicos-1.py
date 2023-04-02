#Ejercicio 1
#a)
MIN_CURSOS = 2.5
PROM_CURSOS = 4.0
MAX_CURSOS = 7.0
CURSO_ACTUAL = 1.5

DIF_MAX_ACTUAL = round(100 - ((CURSO_ACTUAL * 100) / MAX_CURSOS))
DIF_MIN_ACTUAL = round(100 - ((CURSO_ACTUAL * 100) / MIN_CURSOS))
DIF_PROM_ACTUAL = round(100 - ((CURSO_ACTUAL * 100) / PROM_CURSOS))
print("La diferencia entre este curso y el maximo de otros cursos es del " + str(DIF_MAX_ACTUAL) + "%.")
print("La diferencia entre este curso y el minimo de otros cursos es del " + str(DIF_MIN_ACTUAL) + "%.")
print("La diferencia entre este curso y el promedio de otros cursos es del " + str(DIF_PROM_ACTUAL) + "%.")

#b)
CRUDO_PROM = 5.0
CRUDO_ACTUAL = 3.5

MAT_INSERVIBLE_PROM = round(100 - ((PROM_CURSOS * 100) / CRUDO_PROM))
MAT_INSERVIBLE_ACTUAL = round(100 - ((CURSO_ACTUAL * 100) / CRUDO_ACTUAL))
print("El material inservible que se reduce en los cursos promedios es del " + str(MAT_INSERVIBLE_PROM) + "%.")
print("El material inservible que se reduce en el curso actual es del " + str(MAT_INSERVIBLE_ACTUAL) + "%.")

#c)
print(f"Ver 10 horas de este curso equivale a ver {round(PROM_CURSOS / CURSO_ACTUAL * 10)} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {round(CURSO_ACTUAL / PROM_CURSOS * 10)} horas de otros cursos")

#Ejercicios 2
#a)
texto = input("Decime algo: ")
texto_separado = texto.split(" ")
cant_palabras = len(texto_separado)
tiempo_texto = cant_palabras / 2
print(f"La cantidad de palabras que dijiste es {cant_palabras} y tardarias {tiempo_texto} en decirlo.")

#b)
if (tiempo_texto > 60):
    print("Che maestro tampoco te pedí un testamento")

#c)
DALTO_TALKS = 2 * 1.3
tiempo_texto_dalto = round(cant_palabras / DALTO_TALKS)
print(f"Dalto diria ese texto en {tiempo_texto_dalto} segundos.")