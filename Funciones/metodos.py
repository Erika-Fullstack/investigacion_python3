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

#-------------------------------------------------------------

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


#-------------------------------------------------------------

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