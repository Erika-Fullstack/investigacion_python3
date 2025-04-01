#PARÁMETROS Y RETORNO DE VALORES

#Parámetros opcionales con valores por defecto
def saludar(nombre="Usuario"):
    print(f"Hola, {nombre}")

saludar()  # Salida: "Hola, Usuario"
saludar("Erika")  # Salida: "Hola, Erika"


#Retorno de múltiples valores
def operaciones(a, b):
    suma = a + b# Parámetros y retorno de valores
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