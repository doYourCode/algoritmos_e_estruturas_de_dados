"""
Bogosort (também conhecido como StupidSort), é um algoritmo de ordenação extremamente ineficiente. É baseado na
reordenação aleatória dos elementos. Não é utilizado na prática, mas pode ser usado no ensino de algoritmos mais
eficientes. Seu nome veio do engraçado termo quantum bogodynamics.
"""

__author__ = ["Caio Henriques Sica Lamas"]
__date__ = "25/05/2023"
__credits__ = ["https://www.geeksforgeeks.org/bogosort-permutation-sort/"]
__license__ = "GPL"
__email__ = "caio.lamas@ifnmg.edu.br"

import random


def bogo_sort(nums):
    def is_sorted(nums):
        if len(nums) < 2:
            return True
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True

    while not is_sorted(nums):
        random.shuffle(nums)
    return nums
