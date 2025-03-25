
#hay que mirar eso 


# Importar functools para reduce
from functools import reduce

# Bucles (while, for in, range())
print("Bucles:")
i = 0
while i < 3:
    print(f"While: {i}")
    i += 1

for i in range(3):
    print(f"For with range: {i}")

# Break y Continue
print("\nBreak y Continue:")
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(f"Número: {i}")

# List comprehension
print("\nList comprehension:")
cuadrados = [x**2 for x in range(5)]
print(f"Cuadrados: {cuadrados}")

# Condicionales (if/else/elif, ternario)
print("\nCondicionales:")
x = 10
if x > 10:
    print("x es mayor que 10")
elif x < 10:
    print("x es menor que 10")
else:
    print("x es igual a 10")

# Operador ternario
resultado = "Par" if x % 2 == 0 else "Impar"
print(f"x es {resultado}")

# Funciones avanzadas (lambda, map, filter, reduce, enumerate, zip)
print("\nFunciones avanzadas:")
# Lambda
cubo = lambda x: x**3
print(f"Cubo de 3: {cubo(3)}")

# Map
numeros = [1, 2, 3, 4, 5]
cuadrados_map = list(map(lambda x: x**2, numeros))
print(f"Cuadrados con map: {cuadrados_map}")

# Filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")

# Reduce
suma = reduce(lambda x, y: x + y, numeros)
print(f"Suma de números: {suma}")

# Enumerate
for i, valor in enumerate(["a", "b", "c"]):
    print(f"Índice {i}: {valor}")

# Zip
nombres = ["Ana", "Bob", "Carlos"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
