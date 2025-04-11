import time
import random
from insertion_sort import insertion_sort
from insertion_sort_otimizado import insertion_sort_otimizado

def comparar_algoritmos():
    vetores = {
        "Aleatorio": random.sample(range(100), 10),
        "Ordenado": list(range(10)),
        "Invertido": list(range(10, 0, -1))
    }

    for nome, vetor in vetores.items():
        print("Comparacao com vetor", nome)
        print()

        print("Simples")
        inicio = time.time()
        insertion_sort(vetor.copy())
        tempo_simples = time.time() - inicio

        print("Otimizado")
        inicio = time.time()
        insertion_sort_otimizado(vetor.copy())
        tempo_otimizado = time.time() - inicio

        print("Resumo", nome)
        print("Tempo Insertion Sort simples:", f"{tempo_simples:.6f}")
        print("Tempo Insertion Sort otimizado:", f"{tempo_otimizado:.6f}")
        print()

comparar_algoritmos()
