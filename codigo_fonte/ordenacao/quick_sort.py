#Baseado no slide do professor Alison Zille: https://drive.google.com/file/d/1GVur92ff65Zf2hiOlVZz2PThRr8nlW6V/view.
#O exemplo de código em C se encontra nas páginas 16-19


def partition(vetor, inicio, fim):
    pivot = vetor[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]

    vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
    return i + 1

def quickSort1(vetor, inicio, fim):
    if inicio < fim:
        pi = partition(vetor, inicio, fim)
        quickSort1(vetor, inicio, pi - 1)
        quickSort1(vetor, pi + 1, fim)

vetor = [4, 2, 1, 6, 8, 5, 7, 75, 64, 32, 100, 3, 22, 9]
quickSort1(vetor, 0, len(vetor) - 1)
print(vetor)
