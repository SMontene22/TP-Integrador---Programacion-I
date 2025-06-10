import random

# FUNCIONES

# ORDENAMIENTO
def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # Caso base: lista de 1 elemento ya está ordenada
    else:
        pivot = arr[len(arr) // 2]  # Elegimos el pivote
        izquierda = [x for x in arr if x < pivot]  # Elementos menores al pivote
        centro = [x for x in arr if x == pivot]  # Elementos iguales al pivote
        derecha = [x for x in arr if x > pivot]  # Elementos mayores al pivote
        return quick_sort(izquierda) + centro + quick_sort(derecha)  # Ordenamos recursivamente

# BUSQUEDA
def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        centro = (izquierda + derecha) // 2
        if arr[centro] == objetivo:
            return centro  # Se encontró el elemento
        elif arr[centro] < objetivo:
            izquierda = centro + 1  # Buscar en la mitad derecha
        else:
            derecha = centro - 1  # Buscar en la mitad izquierda
    return -1  # Elemento no encontrado

# Prueba del algoritmo

lista = [random.randint(1, 1000) for _ in range(100)]

lista_ordenada = quick_sort(lista)
objetivo = int(input("Ingrese el elemento a buscar: "))
resultado = busqueda_binaria(lista_ordenada, objetivo)
print(f"La lista aleatoria es {lista}")
print(f"La lista ordenada es {lista_ordenada}")
print(f"El elemento {objetivo} está en la posición {resultado}" if resultado != -1 else "Elemento no se creo en la lista aleatoria")




