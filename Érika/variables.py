#ALCANCE DE VARIABLES

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