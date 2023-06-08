import random
import time

def binary_search(arr, left, right, target):
    """Función de búsqueda binaria que devuelve el índice del valor buscado en el array arr"""
    if right >= left:
        mid = left + (right - left) // 2

        # Si el elemento está presente en el medio
        if arr[mid] == target:
            return mid

        # Si el elemento es menor que el valor medio, entonces se encuentra en la sub-lista izquierda
        elif arr[mid] > target:
            return binary_search(arr, left, mid - 1, target)

        # Si el elemento es mayor que el valor medio, entonces se encuentra en la sub-lista derecha
        else:
            return binary_search(arr, mid + 1, right, target)

    # El elemento no se encuentra en el array
    else:
        return -1


# Función de búsqueda secuencial o lineal
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Ejemplo de uso
n = int(input("Introduzca el rango del array: "))
arr = [random.randint(1, n) for i in range(n)]
print("Array generado:", arr)

target = int(input("Introduzca el valor a buscar: "))


arr.sort()  # Ordenamos el array para que sea más fácil buscar
start_time = time.time()
result = binary_search(arr, 0, len(arr) - 1, target)
end_time = time.time()
binary_time = end_time - start_time

start_time = time.time()
result_linear = linear_search(arr, target)
end_time = time.time()
linear_time = end_time - start_time

if result != -1:
    print("El elemento", target, "se encuentra en el índice", result, "encontrado en", binary_time, "segundos con búsqueda binaria")
else:
    print("El elemento", target, "no se encuentra en el array con búsqueda binaria")

if result_linear != -1:
    print("El elemento", target, "se encuentra en el índice", result_linear, "encontrado en", linear_time, "segundos con búsqueda lineal")
else:
    print("El elemento", target, "no se encuentra en el array con búsqueda lineal")


