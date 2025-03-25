mi_lista = [10, 20, 30, 40]
# Accediendo al segundo elemento (índice 1)
print(mi_lista[1])  # 20


mi_tupla = (10, 20, 30, 40)
# Accediendo al tercer elemento (índice 2)
print(mi_tupla[2])  # 30


mi_diccionario = {"nombre": "Juan", "edad": 25}
# Accediendo al valor usando la clave
print(mi_diccionario["nombre"])  # Juan


mi_set = {10, 20, 30, 40}
# Los sets no tienen índices, pero podemos iterar para acceder a los elementos
for item in mi_set:
    print(item)  # Imprime todos los elementos del set, pero sin un orden específico
