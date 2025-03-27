
# Convertir una:

	# list to tuple

	mi_lista = [1, 2, 3]
	mi_tupla = tuple(mi_lista)
	print(mi_tupla)


	# tuple to list

	mi_tupla = (10, 20, 30)
	mi_lista = list(mi_tupla)
	print(mi_lista)


	# dictionary to key lists

	mi_diccionario = {"a": 1, "b": 2, "c": 3}
	claves = list(mi_diccionario.keys())
	print(claves)  # ['a', 'b', 'c']


	# dictionary to key values

	valores = list(mi_diccionario.values())
	print(valores)  # [1, 2, 3]


	# tuple to list

	mi_tupla = (1, 2, 2, 3, 4)
	mi_set = set(mi_tupla)
	print(mi_set)  # {1, 2, 3, 4}


