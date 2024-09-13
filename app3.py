"""Ejercicios con Diccionarios
Estos 5 ejercicios te desafían a trabajar con diccionarios en Python.

1. Crear un diccionario de alumnos y sus notas:

Crea un programa que permita al usuario ingresar el nombre y la nota de un alumno, y almacene esta información en un diccionario. El programa debe permitir al usuario agregar varios alumnos y sus notas. Finalmente, el programa debe mostrar el diccionario con todos los alumnos y sus notas.

Pista: Puedes utilizar un bucle "while" para que el programa siga pidiendo datos hasta que el usuario decida salir.

2. Calcular el promedio de las notas de un diccionario:

Crea una función llamada promedio_notas que reciba un diccionario de alumnos y notas como parámetro y devuelva el promedio de todas las notas.

Pista: Puedes utilizar un bucle "for" para recorrer las notas del diccionario y calcular la suma de todas las notas.

3. Encontrar al alumno con la nota más alta:

Crea una función llamada alumno_con_mejor_nota que reciba un diccionario de alumnos y notas como parámetro y devuelva el nombre del alumno con la nota más alta.

Pista: Puedes utilizar un bucle "for" para recorrer las notas del diccionario y encontrar la nota más alta.

4. Crear un diccionario de palabras y sus definiciones:

Crea un programa que permita al usuario ingresar una palabra y su definición, y almacene esta información en un diccionario. El programa debe permitir al usuario agregar varias palabras y sus definiciones. Finalmente, el programa debe mostrar el diccionario con todas las palabras y sus definiciones.

Pista: Puedes utilizar un bucle "while" para que el programa siga pidiendo datos hasta que el usuario decida salir.

5. Buscar una palabra en un diccionario:

Crea una función llamada buscar_palabra que reciba un diccionario de palabras y definiciones como parámetro y una palabra a buscar. La función debe devolver la definición de la palabra si está presente en el diccionario, o un mensaje indicando que la palabra no se encontró.

Pista: Puedes utilizar la función get() para obtener el valor asociado a una clave en el diccionario.
"""

"""
#### punto 1 ###
notas_alumnos = {}
while True:
    que_hacer= input("Que quieres hacer? (A (Agregar), S (Salir)): ")
    if que_hacer == 'S': 
        print(f"Decidiste salir, las notas agregadas son: \n {notas_alumnos}")
        break

    alumno = input("Escribe el nombre del alumno: ")
    nota = float(input("Escribe la nota del alumno: "))
    notas_alumnos[alumno] = nota
    

### Punto 2 ###

def promedio_notas(): 
    suma_notas = 0
    for nota in notas_alumnos.values():
        suma_notas += nota

    promedio = suma_notas / len(notas_alumnos)
    print(f"El promedio de las notas es: {promedio}")
    
promedio_notas()
### punto 3 ###

def maxima_nota():
    mejor_nota = -1
    mejor_alumno = None
    for alumno, nota in notas_alumnos.items():
        if nota > mejor_nota:
            mejor_nota = nota
            mejor_alumno = alumno
    return print(f"El mejor alumno es: {mejor_alumno} y su nota es {mejor_nota}")

maxima_nota()
"""

"""
### Punto 4 ####

palabras = {}
while True:
    que_hacer= input("Que quieres hacer? (A (Agregar), S (Salir)): ")
    if que_hacer == 'S': 
        print(f"Decidiste salir, las palabras y sus definiciones agregadas son: \n {palabras}")
        break

    palabra = input("Escribe una palabra: ")
    frase = input("Escribe el signifiado de la palabra: ")
    palabras[palabra] = frase

"""
    
### Punto 5 ###

def buscar_palabra(diccionario, palabra):
    
    definicion = diccionario.get(palabra)
    
    if definicion:
        return f"La definición de '{palabra}' es: {definicion}"
    else:
        return f"La palabra '{palabra}' no se encontró en el diccionario."

diccionario = {
    "Comer": "Accion de ingerir alimentos",
    "Desarrollador": "Persona que programa software en algun o algunos lenguajes de programacion",
    "Variable": "Un espacio de memoria para almacenar datos."
}

palabra = input("Introduce la palabra que quieres buscar: ")
resultado = buscar_palabra(diccionario, palabra)
print(resultado)
