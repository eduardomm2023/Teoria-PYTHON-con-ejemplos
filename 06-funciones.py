
#! FUNCION = Es un bloque de código fuente que contiene un conjunto de instrucciones y que 
#! puede ser utilizada desde el código fuente que escribes tantas veces como necesites.
#! Puede RECIBIR DATOS DE ENTRADA O NO (ES OPCIONAL).
#! Puede DEVOLVER O RETORNAR DATOS O NO (ES OPCIONAL).
#! USA la palabra reservada DEF.
# SINTAXIS = defNombreFuncion(parámetros):  -----(Los parámetros son opcionales)------
#             BloqueInstrucciones
#             returnValorRetorno(datos que se retornan)   -----(return, es opcional)--------

#! Para poder UTILIZAR (también llamado INVOCACIÓN) FUNCIONES hay que hacerlo de la siguiente manera:
# Variable = NombreFuncion(parámetros)------------
# Ej:
def EsMayorQueCero(param):
  if param > 0:
    print(param, "es mayor que cero")
  else:
    print(param, "no es mayor que cero")
numero = int(input("Escriba un número: "))
EsMayorQueCero(numero)

def Sumar(*valores):#(si quiero poner X valores o parametros tengo que escribir: *valores)
  resultado = 0
  for item in valores:
    resultado = resultado + item
  return resultado

resultado = Sumar(34,85,103,10545,2)
print("El resultado de la suma es: ", + resultado)


def Sumar(sum1, sum2):#(si quiero poner X valores o parametros tengo que escribir: *valores)
  return sum1 + sum2
sum1 = int(input("Escriba el primer número a sumar: "))
sum2 = int(input("Escriba el segundo número a sumar: "))
resultado = Sumar(sum1, sum2)
print("El resultado de la suma es: ", sum1 + sum2)



def Restar(rest1, rest2):
  return rest1 + rest2
rest1 = int(input("Escriba el primer número a restar: "))
rest2 = int(input("Escriba el segundo número a restar: "))
resultado = Restar(rest1, rest2)
print("El resultado de la resta es: ", rest1 + rest2)



def Multiplicar(mult1, mult2):
  return mult1 + mult2
mult1 = int(input("Escriba el primer número a multiplicar: "))
mult2 = int(input("Escriba el segundo número a multiplicar: "))
resultado = Multiplicar(mult1, mult2)
print("El resultado de la multiplicación es: ", mult1 + mult2)



def Dividir(divis1, divis2):
  return divis1 + divis2
divis1 = int(input("Escriba el primer número a dividir: "))
divis2 = int(input("Escriba el segundo número a dividir: "))
resultado = Dividir(divis1, divis2)
print("El resultado de la división es: ", divis1 + divis2)