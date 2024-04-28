
#! BUCLE = Consiste en la repetición de la ejecución de un bloque de instrucciones,
#! en la que cada REPETICION se llama ITERACION.

#! FOR.
# (Sintaxis = for + variable (puede ser cualquier nombre pero POR CONVENCIÓN, SE USA "i" y tambien se usa,
# "j", "k", "l", etc) + in + elemento a recorrer: 
# (el elemento a recorrer puede ser por ejemplo: 
# una lista, tupla, diccionario, cadena de texto, un rango, etc). 
# FOR está RECOMENDADO para contextos en los que SI SE SABE EL Nº DE ITERACIONES.

#? for variable in elemento a recorrer:
#            (IDENTACIÓN) bucle o bucles
# Ej: for cadena_de_montaje in coches:
# Ej:
lista = [1,2,3,4,5,6,7,8,9]
for item in lista:
  print(item)

for item in range(5,25):
  print(item)



#! WHILE.
# La condicion que se utiliza para comprobar si se tiene que ejecutar una iteracion, 
# deberá ser TRUE PARA QUE SE EJECUTE.
# Si la condición, en caso contrario, es FALSE, LA EJECUCION del bucle FINALIZARÁ. 
# RECOMENDADO para contextos en los que NO SE SABE EXACTAMENTE EL Nº DE ITERACIONES.
# Las variables que se utilizan en la condición del bucle, se llaman VARIABLES DE CONTROL.
# (SINTAXIS = while + condición (que debe cumplirse para que siga repitiéndose  la ejecución del bucle)
# + bloque instrucciones (que es el conjunto de instrucciones)).
# Ej:
i = 0
while i < 10:
  i = i +1
  print(i)


continuar = True
while continuar:
  valor = int(input("Escribe un número entero superior a 100: "))
  if valor > 100:
    continuar = False
print("Programa acabado")



#! BUCLES ANIDADOS.
# Consiste en la utilizacion de bucles como parte de los bloques de instrucciones de otros bucles.
# Ejs:
for item1 in range(3):
  for item2 in range(5):
    print("item1 = " + str(item1) + ", item2 = " + str(item2))


#? BUCLE WHILE y BUCLE FOR.
item1 = 0
while item1 < 3:
  for item2 in range(5):
    print("item1 = " + str(item1)+ ", item2 = " + str(item2))
    item1= item1 + 1


#? 2 BUCLES WHILE.
item1 = 0
while item1 < 3:
  item2 = 0
  while item2 < 5:
     print("item1 = " + str(item1)+ ", item2 = " + str(item2))
     item2 = item2 + 1
  item1 = item1 + 1