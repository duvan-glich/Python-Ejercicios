"""Ejercicios con While y Colecciones en Python
Estos 5 ejercicios te desafían a usar únicamente bucles while y colecciones (listas, diccionarios, conjuntos) para resolver los problemas.

1. Eliminar duplicados de una lista:

Crea un programa que reciba una lista de números como entrada y devuelva una nueva lista con los mismos números pero sin duplicados.

Pista: Puedes utilizar un conjunto (set) para almacenar los elementos únicos de la lista.

2. Adivinar un número con intentos limitados:

Crea un programa que genere un número aleatorio entre 1 y 100, y el usuario debe adivinarlo en un máximo de 7 intentos. El programa debe indicar si el número ingresado es mayor o menor que el número secreto, y cuántos intentos le quedan. Si el usuario adivina el número o se quedan sin intentos, el juego termina.

Pista: Puedes utilizar un bucle "while" que se ejecute mientras los intentos sean mayores que 0 y el usuario no haya adivinado el número.

3. Contar vocales en una frase:

Crea un programa que pida al usuario que ingrese una frase y cuente la cantidad de vocales que contiene. El programa debe usar un bucle while para recorrer la frase y un contador para las vocales.

Pista: Puedes utilizar un bucle "while" que se ejecute mientras no se llegue al final de la frase.

4. Calculadora básica:

Crea un programa que simule una calculadora básica. El usuario debe poder ingresar dos números y seleccionar una operación (+, -, *, /). El programa debe realizar la operación y mostrar el resultado. Utiliza un bucle while para que la calculadora funcione hasta que el usuario decida salir.

Pista: Puedes utilizar un bucle "while" que se ejecute hasta que el usuario ingrese una opción para salir.

5. Crear una lista de números pares:

Crea un programa que cree una lista con todos los números pares entre 1 y 100. Utiliza un bucle while para recorrer los números del 1 al 100 y agregar los pares a la lista.

Pista: Puedes utilizar un bucle "while" que se ejecute mientras el contador sea menor o igual a 100."""

#### PUNTO 1 ####
"""lista_numeros = []
cantidad_numeros = 10
while cantidad_numeros != 0:
    
    cantidad_numeros-= 1
    numero = int(input(f"Vuelta {cantidad_numeros + 1}, Escribe un numero entero: "))
    lista_numeros.append(numero)

lista_sin_duplicado = list(dict.fromkeys(lista_numeros))

print(f"La lista con duplicados es: {lista_numeros}")
print(f"La lista sin duplicados es: {lista_sin_duplicado}")"""

#### Punto 2 ####
"""import random
intentos = 7
numero_aleatorio= random.randint(0, 100)
while intentos > 0:
    
    intentos-= 1
    numero_pregunta = int(input(f"Escribe cual numero crees que es (intento {intentos + 1}): "))
    if numero_pregunta == numero_aleatorio:
        print("Es el numero correcto")
        break
    elif numero_aleatorio > numero_pregunta:
         print("El numero que escribiste es menor")
    elif numero_aleatorio < numero_pregunta: 
        print("El numero que escribiste es mayor")"""
        
### Punto 3 ####
"""

vocales = 'aeiou'
contador = 0
indice = 0
frase = input("Escribe una frase: ")
while indice < len(frase):
    if frase[indice] in vocales:
        contador += 1
    indice += 1
    
print (f"La cantidad de vocales encontradas son: {contador}") """

## Punto 4 ###

"""

while True: 
    
    operador = input("Escribe el operador que quieres usar (+, -, *, /, S (para salir)): ")
    numero1 = int(input("Escribe el numero 1: "))
    numero2 = int(input("Escribe el numero 2: "))
     
    if operador == '+':
        total = numero1 + numero2
        print(f"El total es: {total}")
    elif operador == '-': 
        total = numero1 - numero2
        print(f"El total es: {total}")
    elif operador == '*':
        total = numero1 * numero2
        print(f"El total es: {total}")
    elif operador == '/':
        if numero2 == 0:
            print("Error, no se puede calcular")
        else:    
            total = numero1 / numero2
            print(f"El total es: {total}")
    elif operador == 'S':
        break
        """
                
### Punto 5 ###
"""
lista_pares = []
contador = 1
while contador <= 100:
    if contador % 2 == 0:
        lista_pares.append(contador)
    contador +=1
    
print(f"La lista de numeros pares de 1 al 100 es: {lista_pares}")"""
    
    