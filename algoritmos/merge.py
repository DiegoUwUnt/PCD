# Merge Sort 
# E S C O M
# I P N
# @autor: Diego Villagran
# @autor: Urrutia Quiroz

import random

def generar_numeros_aleatorios(n):
  return [random.randint(0, 10000) for _ in range(n)]

#Lsita desornenada 
def imprimir_lista(lista):
  for elemento in lista:
    print(elemento, end=" ")
  print()

#Ordenamiento
def merge_sort(arr):
  if len(arr) > 1:
    mitad = len(arr) // 2
    izquierda = arr[:mitad]
    derecha = arr[mitad:]

    merge_sort(izquierda)
    merge_sort(derecha)

    i = j = k = 0

    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
        arr[k] = izquierda[i]
        i += 1
      else:
        arr[k] = derecha[j]
        j += 1
      k += 1

    while i < len(izquierda):
      arr[k] = izquierda[i]
      i += 1
      k += 1

    while j < len(derecha):
      arr[k] = derecha[j]
      j += 1
      k += 1

print("\nMergeSort\n\n")

n = int(input("Ingrese el tamaño del arreglo: "))
array = generar_numeros_aleatorios(n)

print("\nArreglo original:")
imprimir_lista(array)

merge_sort(array)

print("\nArreglo ordenado:")
imprimir_lista(array)


