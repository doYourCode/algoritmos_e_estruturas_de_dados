from codigo_fonte.ordenacao.selection_sort import *
from codigo_fonte.ordenacao.bogo_sort import *

# COMENTARIO DO PROFESSOR
# observar como foram feitos os testes das EDs no repositório
def teste_selection_sort():
    num1 = input('Input  comma separated numbers:\n').strip()
    nums = [int(item) for item in num1.split(',')]
    print(selection_sort(nums))
    pass

def teste_bogo_sort():
    num1 = input('Input  comma separated numbers:\n').strip()
    nums = [int(item) for item in num1.split(',')]
    print(bogosort(nums))