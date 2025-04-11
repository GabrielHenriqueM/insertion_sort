import time
import random

def insertion_sort_otimizado(array):
    n = len(array)
    iteracoes = 0
    inicio = time.time()

    print("Vetor inicial", array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        trocou = False
        print()
        print("Iteracao", i)
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
            iteracoes += 1
            trocou = True
        array[j + 1] = key
        print(array)

        if not trocou and all(array[k] <= array[k + 1] for k in range(n - 1)):
            print("Sem movimentacoes, interrompendo o algoritmo.")
            break

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
insertion_sort_otimizado(vetor_teste.copy())

print("Teste vetor ordenado")
insertion_sort_otimizado(vetor_ordenado.copy())

print("Teste vetor invertido")
insertion_sort_otimizado(vetor_invertido.copy())
