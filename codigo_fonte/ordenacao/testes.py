from codigo_fonte.ordenacao.selection_sort import *
from codigo_fonte.ordenacao.bogo_sort import *
from codigo_fonte.ordenacao.insertion_sort import *

import time


def teste_selection_sort(lista):
    print("Selection sort")
    print("Lista não ordenada -> " + str(lista))

    _time = time_set()

    selection_sort(lista)

    _time = time_get(_time)

    print("Lista ordenada -> " + str(lista))
    print(str(_time) + " nanoseconds")


def teste_bogo_sort(lista):
    print("Bogo sort")
    print("Lista não ordenada -> " + str(lista))

    _time = time_set()

    bogo_sort(lista)

    _time = time_get(_time)

    print("Lista ordenada -> " + str(lista))
    print(str(_time) + " nanoseconds")


def teste_insertion_sort(lista):
    print("Insertion sort")
    print("Lista não ordenada -> " + str(lista))

    _time = time_set()

    insertion_sort(lista)

    _time = time_get(_time)

    print("Lista ordenada -> " + str(lista))
    print(str(_time) + " nanoseconds")


def time_set():
    return time.time_ns()


def time_get(_time):
    return time.time_ns() - _time
