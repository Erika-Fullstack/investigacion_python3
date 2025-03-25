#count() → Cuenta cuántas veces aparece un valor en una lista o cadena.
lista = [1, 2, 3, 1, 1, 4]
print(lista.count(1))  # Salida: 3

texto = "hola mundo hola"
print(texto.count("hola"))  # Salida: 2


#len() → Devuelve la cantidad de elementos en una lista, diccionario o caracteres en una cadena.
print(len([1, 2, 3]))  # Salida: 3
print(len("Python"))  # Salida: 6
print(len({"a": 1, "b": 2}))  # Salida: 2


#find() → Busca una subcadena dentro de una cadena y devuelve la posición de la primera coincidencia.
texto = "Bienvenido a Python"
print(texto.find("Python"))  # Salida: 13
print(texto.find("Java"))  # Salida: -1 (no encontrado)


#split() → Divide una cadena en una lista, separando por un delimitador.
frase = "Hola, cómo estás?"
print(frase.split())  # ['Hola,', 'cómo', 'estás?']
print(frase.split(","))  # ['Hola', ' cómo estás?']


#join() → Une elementos de una lista en una cadena con un separador.
palabras = ["Hola", "mundo"]
print(" ".join(palabras))  # Salida: "Hola mundo"


#replace() → Reemplaza una subcadena por otra en una cadena.
texto = "Hola mundo"
print(texto.replace("mundo", "Python"))  # Salida: "Hola Python"


#slice() → Extrae una parte de una cadena o lista usando índices.
texto = "Python"
print(texto[0:3])  # Salida: "Pyt" (de 0 a 2)
print(texto[-3:])  # Salida: "hon" (últimos 3 caracteres)


#strip() → Elimina espacios o caracteres específicos al inicio y final de una cadena.
texto = "  hola  "
print(texto.strip())  # Salida: "hola"

otro_texto = "---Python---"
print(otro_texto.strip("-"))  # Salida: "Python"


#upper() → Convierte una cadena a mayúsculas.
print("python".upper())  # Salida: "PYTHON"


#lower() → Convierte una cadena a minúsculas.
print("PYTHON".lower())  # Salida: "python"


#Otros métodos relevantes
#append() → Agrega un elemento al final de una lista.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Salida: [1, 2, 3, 4]


#pop() → Elimina y devuelve el último elemento de una lista (o un índice específico).
lista = [1, 2, 3]
print(lista.pop())  # Salida: 3
print(lista)  # Salida: [1, 2]


#keys() y values() en diccionarios
diccionario = {"nombre": "Erika", "edad": 38}
print(diccionario.keys())  # Salida: dict_keys(['nombre', 'edad'])
print(diccionario.values())  # Salida: dict_values(['Erika', 38])


#Funciones en Python
# Sintaxis de funciones
def saludar():
    print("Hola, mundo")

saludar()  # Salida: "Hola, mundo"


#Argumentos en funciones
def sumar(a, b):
    return a + b

print(sumar(3, 5))  # Salida: 8


#Funciones avanzadas: lambda y map()
#lambda → Función anónima de una sola línea.
doble = lambda x: x * 2
print(doble(4))  # Salida: 8

#map() → Aplica una función a cada elemento de una lista.
numeros = [1, 2, 3, 4]
print(list(map(lambda x: x * 2, numeros)))  # Salida: [2, 4, 6, 8]


#Alcance de variables
# Variables locales → Solo existen dentro de una función.
def funcion():
    x = 10  # Variable local
    print(x)

funcion()
# print(x)  # Error, x no existe fuera de la función


#Variables globales → Se pueden acceder desde cualquier parte del código.
x = 5  # Variable global

def mostrar():
    print(x)  # Accede a la variable global

mostrar()  # Salida: 5


#Modificando una variable global dentro de una función
contador = 0

def incrementar():
    global contador  # Se usa la variable global
    contador += 1

incrementar()
print(contador)  # Salida: 1


# Parámetros y retorno de valores
#Parámetros opcionales con valores por defecto
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}")

saludar()  # Salida: "Hola, Usuario"
saludar("Erika")  # Salida: "Hola, Erika"


#Retorno de múltiples valores
def operaciones(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado = operaciones(10, 5)
print(resultado)  # Salida: (15, 5)


#Funciones con argumentos indefinidos (*args y **kwargs)
#*args → Recibe una cantidad variable de argumentos posicionales.
def sumar_todo(*numeros):
    return sum(numeros)

print(sumar_todo(1, 2, 3, 4))  # Salida: 10

#**kwargs → Recibe una cantidad variable de argumentos de tipo clave-valor.
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Erika", edad=38, ciudad="Barakaldo")
# Salida:
# nombre: Erika
# edad: 38
# ciudad: Barakaldo