# Bucles (while, for in, range())
print("While:")

contador = 1
while contador <= 5:
    print(f"Día {contador}:")
    if contador % 2 == 0:
        print("  - Hacer ejercicio")
    else:
        print("  - Descansar")
    contador += 1
print("Fin del programa")

print()

print("for in")
for i in range(3):
    print(f"For with range: {i}")

print()

# Break y Continue
print("\nBreak y Continue:")
for i in range(1, 6):
    if i == 3:
        continue  # Salta el número 3
    if i == 5:
        print("Terminando el bucle")
        break  # Termina el bucle en el número 5
    print(f"El número es {i}")

print()

# List comprehension
print("\nList comprehension:")
numeros=[1,2,3,4,5]
cuadrados = [x**2 for x in numeros if x % 2==0]
print(f"Cuadrados: {cuadrados}")

print()

# Condicionales (if/else/elif, ternario)
print("\nCondicionales:")
edad = 18
if edad < 18:
    print("x es menor de edad")
elif edad == 18:
    print("acaba de alcanzar 18")
else:
    print("eres mayor de edad")

print()

# Operador ternario
temperatura = 25
estado = "calor" if temperatura > 20 else "frio"
print(f"Hace {estado}")

