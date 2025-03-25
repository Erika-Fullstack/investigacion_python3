# Diccionarios
mi_diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

# Obtener un valor de una clave específica
nombre = mi_diccionario.get("nombre")  
print(nombre)  # Juan

# Obtener todas las claves del diccionario
claves = mi_diccionario.keys()  
print(claves)  # dict_keys(['nombre', 'edad', 'ciudad'])

# Obtener todos los valores del diccionario
valores = mi_diccionario.values()  
print(valores)  # dict_values(['Juan', 25, 'Madrid'])

# Obtener todos los pares clave-valor del diccionario
items = mi_diccionario.items()  
print(items)  # dict_items([('nombre', 'Juan'), ('edad', 25), ('ciudad', 'Madrid')])
