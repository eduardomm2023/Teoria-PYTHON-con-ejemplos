
#! CADENAS DE TEXTO (BASICO).

cadena_ejemplo = "Hola a todos desde Time of Software"
print(cadena_ejemplo)

# Uso de \n para un salto de linea
cadena_ejemplo = "Hola a todos desde Time of Software\nEsto es una cadena multilinea\nque permite dividir una oración\nen diferentes líneas independientes"
print(cadena_ejemplo)


#! CADENAS DE TEXTO (AVANZADO).

"""
Capitalize---------------------Convertir la primera letra en mayúscula.
UPPER--------------------------Todo en MAYUSCULAS.
lower--------------------------Todo en minúsculas.
LEN----------------------------Permite saber el nº de caracteres de una cadena de texto.
isalnum------------------------Comprueba si todos los caracteres son alfanuméricos o no.
isalpha------------------------Comprueba si todos los caracteres son caracteres alfabéticos (SOLO LAS LETRAS).Los nº,   los puntos y los espacios en blanco no son caracteres alfabéticos.
isdigit------------------------Comprueba si todos los caracteres son numéricos.
islower------------------------Comprueba si todos los caracteres están en minúscula.
isupper------------------------Comprueba si todos los caracteres están en mayúscula.
lstrip,------------------------Eliminar (AL COMIENZO) los espacios en blanco de la cadena.
rstrip,------------------------Eliminar (AL FINAL) los espacios en blanco de la cadena.
strip--------------------------Eliminar AMBOS A LA VEZ.
max y min----------------------Conocer el caracter alfabético mayor y menor de la cadena de texto.
REPLACE------------------------REEMPLAZAR CARACTERES POR OTROS.
swapcase-----------------------INVERTIR  de mayúsculas a minúsculas y viceversa.
SPLIT--------------------------CONVERTIR una cadena de texto EN UNA LISTA DE ELEMENTOS que se encuentran separados por espacios en la cadena de texto original.
"""

cadena_ejemplo = "en un lugar de la mancha de cuyo nombre no quiero acordarme..."
cadena_ejemplo1 ="an bvrjeiogjfdshb24732857438957"
cadena_ejemplo2 ="uEFBVOONBEEGfegfjrhjytjrhguhu8765587891398 "
cadena_ejemplo3 ="   57436754389081903271   "
print(cadena_ejemplo.capitalize())
print(cadena_ejemplo.upper())
print(cadena_ejemplo.lower())
print(len(cadena_ejemplo))
print(cadena_ejemplo1.isalnum())
print(cadena_ejemplo2.isalpha())
print(cadena_ejemplo3.isdigit())
print(cadena_ejemplo2.islower())
print(cadena_ejemplo2.isupper())
print(cadena_ejemplo2.lstrip())
print(cadena_ejemplo2.rstrip())
print(cadena_ejemplo3.strip())
print(max(cadena_ejemplo2))
print(min(cadena_ejemplo2))
print(cadena_ejemplo2.replace("E","UUUUUH"))
print(cadena_ejemplo2.swapcase())
print(cadena_ejemplo.split())