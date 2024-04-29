
#! BLOQUES E IDENTACION.
# BLOQUE = Es un grupo de sentencias de código fuente que contiene una o más sentencias.
# Están delimitados por su inicio y su fin.
# IDENTACIÓN = Significa mover un bloquer de texto hacia la dcha, insertando espacios o tabuladores.


#! CONDICIONALES O SENTENCIAS CONDICIONALES.
#? IF => SI...-----------------------------
# El código se ejecuta unicamente, si se cumple la condición de entrada.
#? ELIF => PERO SI....---------------------
# Permite generar un camino alternativo con una condición de entrada.
#? ELSE => Y SI NO SE CUMPLE...------------
# Se ejecutará siempre que NO se hayan cumplido las anteriores condiciones (if y elif).


num1 = 50
num2 = 50
if num1 > num2:
  print("Has ganado un coche")
elif num1 == num2:
  print("Te lo vuelves a jugar")
else: 
  print("Has perdido el premio")



#? EJEMPLO DE IF + ELIF + ELSE.
num1 = int(input("Escriba un número entre el 1 y el 100: "))
num2 = int(input("Escriba un segundo número comprendido entre 1 y 100: "))
if num1 > num2:
  print("El primer número es mayor que el segundo")

elif num1 == num2:
  print("Los dos números son iguales")
else:
  print("El segundo número es mayor que el primero")



#! EN CADENAS DE TEXTO.
# IN
# STARTSWITH
# ENDSWITH


# IN
cadena_ejemplo = "En un lugar de la mancha de cuyo nombre no quiero..."
if "lugar" in cadena_ejemplo:
  print("¡Lo has encontrado!")
else:
  print("¡No lo has encontrado!")


# STARTSWITH (Se escribe la variable seguida de UN PUNTO y luego la palabra startswith)
cadena_ejemplo = "En un lugar de la mancha de cuyo nombre no quiero..."
if cadena_ejemplo.startswith("L"):
  print("¡Empieza por L!")
else:
  print("¡No empieza por L!")
  


# ENDSWITH (Se escribe la variable seguida de UN PUNTO y luego la palabra endswith)
cadena_ejemplo = "En un lugar de la mancha de cuyo nombre no quiero..."
if cadena_ejemplo.endswith("L"):
  print("¡Termina por L!")
else:
  print("¡No termina por L!")