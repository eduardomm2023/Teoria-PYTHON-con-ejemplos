
#!LISTAS (con corchetes []):
#TODO: LISTAS UNIDIMENSIONALES:
#METODOS:
"""
.append() => (añade la final de la lista)
.insert( => (añade en la posicion que le digamos)
.sort() => (ordenar la lista)
.extend() => (añade al final de una lista otra lista = concatenar)
.pop() => (eliminar por el nº o poscion de indice). Si no se le dice la posicion, elimina el ultimo. 
.remove() => (eliminar por el valor)
=> len(tamaño de la lista)
"""

#TODO: LISTAS BIDIMENSIONALES (TABLAS):
#Ej:
print("----------------------------------------------------------------------------")
bi_list = [[1, 2, 3, 4],[5, 6, 7, 8]]
print(bi_list)
print(bi_list[0][3])
print("----------------------------------------------------------------------------")

#TODO: LISTAS TRIDIMENSIONALES (CUBOS):


#!TUPLAS (con paréntesis ()):
#OCUPAN MENOS ESPACIO EN MEMORIA y POR TANTO SON MUCHO MAS RAPIDAS QUE LAS LISTAS.

print("----------------------------------------------------------------------------")
tuple = (1, 2, 3, 48, 6, 9, 0, 12, 1, 5)
print(tuple)
print(tuple[1:4])
print(tuple[3:])
print(tuple[-3])
print("----------------------------------------------------------------------------")

#! DICCIONARIOS (con llaves {}) CLAVE - VALOR:
print("----------------------------------------------------------------------------")
dict_ex = {"Nombre": "Edu", "Edad": 48, "Ciudad": "Madrid", True: 37}
print(dict_ex)

#METODOS:
"""
#?ACCEDER A LAS CLAVES DE UN DICC (usando "get")=> ES MAS SEGURA QUE LA FORMA UTILIZADA EN LISTAS.
#?ES MAS SEGURA XQ NO DEVUELVE UN ERROR SI EL ELEMENTO NO EXISTE (devuelve NONE).
print(dict_ex.get("edad")) => DEVUELVE NONE PERO NO DARÁ ERROR.

dict_ex ["Pais"] = "España". => AÑADIR UN PAR CLAVE-VALOR NUEVO:
print(dict_ex)

print(dict_ex.keys()). => ACCEDER SOLO A LAS CLAVES

print(dict_ex.values(). => ACCEDER SOLO A LOS VALORES

print(dict_ex.items()). => ACCEDER A TODO
"""

#! CONJUNTOS o SETS (con llaves{}): NO HAY ELEMENTOS REPETIDOS.
#METODOS:
"""
.add(). => AÑADIR UN ELEMENTO (se coloca donde sea ya que no hay ningún orden establecido)
.clear(). => ELIMINAR o LIMPIAR UN CONJUNTO
.pop => (elimnar un elemento cualquiera)
.remove(3) => (escribo entre parentesis la posicion del elemento que quiero eliminar)
.issubset() => COMPROBAR SI UN CONJUNTO o SET ES SUBCONJUNTO DE OTRO.
.union() => COMPROBAR LA UNIÓN DE 2 CONJUNTOS.
.intersection() => COMPROBAR SI HAY INTERSECCIÓN DE 2 CONJUNTOS.
.difference() => CALCULAR LA DIFERENCIA ENTRE 2 CONJUNTOS.
.symmetric_difference() => SE QUEDA CON LO QUE NO ESTÁ (LO CONTRARIO) EN NINGUNO DE LOS 2 CONJUNTOS.
"""