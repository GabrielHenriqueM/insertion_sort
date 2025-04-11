import time
import random

def insertion_sort(array):
    n = len(array)
    iteracoes = 0
    inicio = time.time()

    print("Vetor inicial", array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        print()
        print("Iteracao", i)
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            iteracoes += 1
        array[j + 1] = key
        print(array)

    fim = time.time()

    print()
    print("Vetor final ordenado", array)
    print("Total de iteracoes:", iteracoes)
    print("Tempo de execucao:", f"{fim - inicio:.6f}", "segundos")
    print()

vetor_teste = random.sample(range(100), 10)
vetor_ordenado = list(range(10))
vetor_invertido = list(range(10, 0, -1))

print("Teste vetor aleatorio")
insertion_sort(vetor_teste.copy())

print("Teste vetor ordenado")
insertion_sort(vetor_ordenado.copy())

print("Teste vetor invertido")
insertion_sort(vetor_invertido.copy())
