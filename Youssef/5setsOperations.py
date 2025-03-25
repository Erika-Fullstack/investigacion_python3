# Operaciones con sets
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Unión de dos sets (combina los elementos sin repetir)
union_set = set_a.union(set_b)  
print(union_set)  # {1, 2, 3, 4, 5}

# Intersección de dos sets (elementos en común)
interseccion_set = set_a.intersection(set_b)  
print(interseccion_set)  # {3}

# Diferencia entre dos sets (elementos en set_a que no están en set_b)
diferencia_set = set_a.difference(set_b)  
print(diferencia_set)  # {1, 2}
