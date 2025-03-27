# Listas
mi_lista = [5, 3, 1, 4, 2]

# Agregar un elemento al final de la lista
mi_lista.append(6)  
print(mi_lista)  # [5, 3, 1, 4, 2, 6]

# Eliminar un elemento específico de la lista
mi_lista.remove(3)  
print(mi_lista)  # [5, 1, 4, 2, 6]

# Ordenar la lista en orden ascendente
mi_lista.sort()  
print(mi_lista)  # [1, 2, 4, 5, 6]

# Invertir el orden de la lista
mi_lista.reverse()  
print(mi_lista)  # [6, 5, 4, 2, 1]

# Eliminar y devolver el último elemento de la lista
mi_lista.pop()  
print(mi_lista)  # [6, 5, 4, 2]
