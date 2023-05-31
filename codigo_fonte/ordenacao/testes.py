from codigo_fonte.ordenacao.selection_sort import *
from codigo_fonte.ordenacao.bogo_sort import *
from codigo_fonte.ordenacao.insertion_sort import *


def teste_selection_sort(lista):
    print("Selection sort")
    print("Lista não ordenada -> " + str(lista))

    selection_sort(lista)

    print("Lista ordenada -> " + str(lista))


def teste_bogo_sort(lista):
    print("Bogo sort")
    print("Lista não ordenada -> " + str(lista))

    bogo_sort(lista)

    print("Lista ordenada -> " + str(lista))


def teste_insertion_sort(lista):
    print("Insertion sort")
    print("Lista não ordenada -> " + str(lista))

    insertion_sort(lista)

    print("Lista ordenada -> " + str(lista))
