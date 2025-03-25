#Funciones avanzadas: lambda y map()
#lambda → Función anónima de una sola línea.
doble = lambda x: x * 2
print(doble(4))  # Salida: 8

#map() → Aplica una función a cada elemento de una lista.
numeros = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, numeros)))  # Salida: [2, 4, 6, 8]