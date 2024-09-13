""""inicio-1"""
def suma_elementos(lista_numeros):

  suma = 0
  for numero in lista_numeros:
    suma += numero
  return suma

mi_lista = [1, 2, 3, 4, 10]
resultado = suma_elementos(mi_lista)
print("El total de la suma es:", resultado)


""""inicio-2"""
def contar_pares(lista_numeros):

  contador_pares = 0
  for numero in lista_numeros:
    if numero % 2 == 0:
      contador_pares += 1
  return contador_pares

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8]
cantidad_pares = contar_pares(mi_lista)
print("Hay", cantidad_pares, "números pares en la lista.")


""""inicio-3"""
def elemento_mas_grande(lista_numeros):
 
  if not lista_numeros:
      return None  

  maximo = lista_numeros[0]  
  for numero in lista_numeros[1:]:
    if numero > maximo:
      maximo = numero
  return maximo

mi_lista = [3, 7, 2, 9, 5]
resultado = elemento_mas_grande(mi_lista)
print("El elemento más grande es:", resultado)

""""inicio-4"""
def multiplicar_elementos(lista_numeros):

  nueva_lista = []
  for numero in lista_numeros:
    nuevo_numero = numero * 2
    nueva_lista.append(nuevo_numero)
  return nueva_lista

mi_lista = [1, 2, 3, 4, 56]
resultado = multiplicar_elementos(mi_lista)
print("La nueva lista es:", resultado)

""""inicio-5"""
def invertir_lista(lista):
 
  lista_invertida = []
  for i in range(len(lista) - 1, -1, -1):
    lista_invertida.append(lista[i])
  return lista_invertida

mi_lista = [1, 2, 3, 4, 5]
lista_invertida = invertir_lista(mi_lista)
print("La lista invertida es:", lista_invertida)

""""FIN EJERCICIOS-1"""

""""INICIO EJERCICIOS-2"""

def eliminar_duplicados(lista_numeros):
    
    conjunto_numeros = set(lista_numeros)
    lista_sin_duplicados = list(conjunto_numeros)
    return lista_sin_duplicados

entrada = [1, 2, 2, 3, 4, 4, 5]
resultado = eliminar_duplicados(entrada)
print("Lista sin duplicados:", resultado)


