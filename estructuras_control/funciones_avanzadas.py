# Funciones avanzadas (lambda, map, filter, reduce, enumerate, zip)
# Importar functools para reduce
from functools import reduce



print("\nFunciones avanzadas:")
# Lambda
multiplicar = lambda x,y: x * y
print(multiplicar(3, 4))

print()

# Map
numeros = [1, 2, 3, 4, 5]
cuadrados= list(map(lambda x: x**2, numeros))
print(f"{cuadrados}")

print()

# Filter
numeros = range (-5, 6)
positivos = list(filter(lambda x: x > 0, numeros))
print(f"Números positivos: {positivos}")

print()

# Reduce
numeros = [1,2,3,4,5]
producto = reduce(lambda x, y: x * y, numeros)
print(f"Suma del producto: {producto}")

print()

# Enumerate
frutas = ["Manzana", "Cereza", "Banana"]
for indice, fruta in enumerate (frutas, start= 2): # empeza a contar desde 2 y le da al primer elemento el indice 2 es utli ciiando por ejemplo tienes un sistema 
    #en la cual quieres que se muestran los datos a partir de 1 en vez de contar a partir de 0
    print(f"Fruta {indice} es {fruta}")

print()

# Zip
nombres = ["Ana", "Bob", "Carlos"]
edades = [25, 30, 35]
for nombre, edad in zip (nombres, edades):
    print(f"{nombre} tiene {edad} años")