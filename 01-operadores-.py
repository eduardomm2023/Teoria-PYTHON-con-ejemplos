
#! OPERADORES ARITMETICOS.

# SUMA (INT = NUMEROS)
num1 = int(input("Escriba el primer número de la suma: "))
num2 = int(input("Escriba el segundo número de la suma: "))
print("Resultado de la suma: ", num1 + num2)

# SUMA CON DECIMALES (FLOAT = DECIMALES)
num1 = float(input("Escriba el primer número de la suma con decimales: "))
num2 = float(input("Escriba el segundo número de la suma con decimales: "))
print("Resultado de la suma con decimales: ", num1 + num2)

# RESTA
num1 = int(input("Escriba el primer número de la resta: "))
num2 = int(input("Escriba el segundo número de la resta: "))
print("Resultado de la resta: ", num1 - num2)

# MULTIPLICACION
num1 = int(input("Escriba el primer número de la multiplicación: "))
num2 = int(input("Escriba el segundo número de la multiplicación: "))
print("Resultado de la multiplicación: ", num1 * num2)

# DIVISION
num1 = int(input("Escriba el primer número de la división: "))
num2 = int(input("Escriba el segundo número de la división: "))
print("Resultado de la división: ", num1 / num2)

# DIVISION (ROUND = PARA REDONDEAR EL NJMERO RESULTANTE. 
# Despues del num2 seguido de una coma, se escribe el nº de decimales que quiero que aparezcan: 
# 1= un decimal; 2= dos decimales; 3= tres decimales, etc.)
num1 = float(input("Escriba el primer número de la división: "))
num2 = float(input("Escriba el segundo número de la división: "))
resultado = round(num1 / num2,3)
print("Resultado de la división: ", resultado)


#! OPERADORES LÓGICOS (AND, OR y NOT).
# AND
booleano1 = True
booleano2 = True
print(booleano1 and booleano2)

booleano1 = True
booleano2 = False
print(booleano1 and booleano2)

booleano1 = False
booleano2 = False
print(booleano1 and booleano2)

# OR
booleano1 = True
booleano2 = True
print(booleano1 or booleano2)

booleano1 = True
booleano2 = False
print(booleano1 or booleano2)

# NOT
booleano1 = True
print(not booleano1)

booleano1 = False
print(not booleano1)


#! OPERADORES RELACIONALES ( <, >, <=, >=, ==, !=)
== igualdad
!= distinto
< menor que
> mayor que 
<= menor o igual que
>= mayor o igual que



