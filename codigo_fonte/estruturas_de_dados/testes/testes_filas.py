from codigo_fonte.utilidades.utilidades import *
from codigo_fonte.estruturas_de_dados.fila_encadeada import FilaEncadeada
from codigo_fonte.estruturas_de_dados.fila import Fila
from codigo_fonte.estruturas_de_dados.fila_dupla import Fila_dupla
from codigo_fonte.estruturas_de_dados.fila_circular_encadeada import FilaCircularEncadeada
from codigo_fonte.estruturas_de_dados.fila_dupla_encadeada import FilaDuplaEncadeada

def fila_encadeada():
    fila_teste = FilaEncadeada()  # Iniciando a Fila sem valor algum.

    # Teste de inserção
    fila_teste.adicionar("Franck")
    fila_teste.adicionar("Allyson")
    fila_teste.adicionar("Ronaldinho")
    print(f'{HEADER} Teste Nº 1 (Inserções): {ENDC}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')

    # Teste de remoção
    fila_teste.remover()
    fila_teste.remover()  # Queremos verificar se o PEPS(Primeiro a Entrar, Primeiro a sair) está sendo cumprido.
    print(f'{HEADER} Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Leitura): {ENDC}')
    fila_teste.adicionar("Franck")
    fila_teste.adicionar("Caio")
    fila_teste.adicionar("Lamas")
    print(f'Elemento do inicio: {str(fila_teste.ler_inicio())}')
    print(f'Elemento do final: {str(fila_teste.ler_final())}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')

    # Teste de Erro
    print(f'{HEADER} Teste Nº 4 (Erro): {ENDC}')
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {str(len(fila_teste))}{ENDC}\n')


def fila():

    fila_teste = Fila(20)  # ............ Define o tamanho da fila

    # Testando inserção
    fila_teste.adicionar(1)  # ............ Insere o primeiro elemento
    fila_teste.adicionar(2)  # ............ Insere o segundo elemento
    fila_teste.adicionar(3)  # ............ Insere o terceiro elemento
    print(f'{HEADER}Teste Nº 1 (Inserções): {ENDC}')
    print(f'O tamanho da fila é: {fila_teste.tamanho()}')
    print(f'O elemento da frente é: {fila_teste.peek()}')

    # Teste de retorno
    print(f'{HEADER} Teste Nº 3 (Leitura): {ENDC}')
    fila_teste.adicionar(7)
    fila_teste.adicionar(75)
    fila_teste.adicionar(9)
    print(f'O elemento da frente é: {fila_teste.peek()}')
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {fila_teste.tamanho()}{ENDC}')

    # Testando a Exclusões
    fila_teste.remover()  # ............ Remove o elemento da frente da fila
    print(f'{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    print(f'O elemento da frente é: {fila_teste.peek()}')
    fila_teste.remover()  # ............ Remove o elemento da frente da fila
    print(f'{str(fila_teste.valores)} {OKBLUE} Tamanho da Fila: {fila_teste.tamanho()}{ENDC}')

    # Testando Erro
    print(f'{HEADER}Teste Nº 4 (Erro): {ENDC}')
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    fila_teste.remover()
    print(f'{fila_teste.valores} {OKBLUE} Tamanho da fila: {fila_teste.tamanho()} {ENDC}')

    # Verificando se a fila está vazia ou não
    if fila_teste.estaVazia():
        print('A fila está vazia!')
    else:
        print('A fila não está vazia!')


def fila_dupla():
    
    filaTeste = Fila_dupla(20)  # ............ Define o tamanho da fila

    # Testando inserção no inicio
    print(f'{HEADER}Teste Nº 1 (Inserções no incio): {ENDC}')
    filaTeste.adicionarInicio(3)  # ............ Adiciona o elemento no inicio da fila
    filaTeste.adicionarInicio(2)  # ............ Adiciona o elemento no inicio da fila
    filaTeste.adicionarInicio(1)  # ............ Adiciona o elemento no inicio da fila
    print(f'O tamanho da Fila é: {filaTeste.tamanho()}{ENDC}\n')

    # Testando inserção no final
    print(f'{HEADER}Teste Nº 2 (Inserções no final): {ENDC}')
    filaTeste.adicionarFinal(99)  # ............ Adiciona o elemento no final da fila
    filaTeste.adicionarFinal(75)  # ............ Adiciona o elemento no final da fila
    filaTeste.adicionarFinal(51)  # ............ Adiciona o elemento no final da fila
    print(f'O tamanho da fila é: {filaTeste.tamanho()}{ENDC}\n')

    # Testando a remoção
    print(f'{HEADER}Teste Nº 3 (Exclusões): {ENDC}')
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila
    filaTeste.removerFinal()  # ............ Remove o elemento do final da fila

    # Testando Erro
    print(f'{HEADER}Teste Nº 4 (Erro): {ENDC}')
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila
    filaTeste.removerInicio()  # ............ Remove o elemento da inicio da fila

    # Verificando se a fila está vazia ou não
    if filaTeste.estaVazia():
        print('A fila está vazia!')
    else:
        print('A fila não está vazia!')


def fila_circular_encadeada():
    fila_circular_teste = FilaCircularEncadeada()

    # Testando a inserção
    print(f'{HEADER}Teste Nº 1 (Inserções no final): {ENDC}')
    fila_circular_teste.enfileirar("Franck")
    fila_circular_teste.enfileirar("Pedro")
    fila_circular_teste.enfileirar("Ronaldo")
    fila_circular_teste.enfileirar("Pereira")
    fila_circular_teste.enfileirar("Ítalo")
    print(f'Primeiro elemento: {WARNING}{fila_circular_teste.primeiro_elemento()}{ENDC}\n'
          f'Último elemento: {WARNING}{fila_circular_teste.ultimo_elemento()}{ENDC}\n'
          f'Pra quem o último elemento está apontando: {WARNING}{fila_circular_teste.ultimo.proximo.valor}{ENDC}')

    print(f'{str(fila_circular_teste.valores)} {OKBLUE} Tamanho da Fila: {len(fila_circular_teste)}{ENDC}\n')
    # Testando a exclusão
    print(f'{HEADER}Teste Nº 2 (Exclusões): {ENDC}')
    print(f'{OKBLUE}Desenfileirando {fila_circular_teste.desenfileirar()}{ENDC}')
    print(f'{OKBLUE}Desenfileirando {fila_circular_teste.desenfileirar()}{ENDC}')

    print(f'Primeiro elemento: {WARNING}{fila_circular_teste.primeiro_elemento()}{ENDC}\n'
          f'Último elemento: {WARNING}{fila_circular_teste.ultimo_elemento()}{ENDC}\n'
          f'Pra quem o último elemento está apontando: {WARNING}{fila_circular_teste.ultimo.proximo.valor}{ENDC}')
    print(f'{str(fila_circular_teste.valores)} {OKBLUE} Tamanho da Fila: {len(fila_circular_teste)}{ENDC}\n')

    # Testando se está vazia
    print(f'{HEADER}Teste Nº 3 (Verificar se está vazia): {ENDC}')
    print(f'{WARNING}A fila está vazia: {fila_circular_teste.vazia()}{WARNING}')
    print(f'{str(fila_circular_teste.valores)} {OKBLUE} Tamanho da Fila: {len(fila_circular_teste)}{ENDC}\n')

    # Testando erros
    print(f'{HEADER}Teste Nº 4 (Erros): {ENDC}')
    print(f'{OKBLUE}Desenfileirando {fila_circular_teste.desenfileirar()}{ENDC}')
    print(f'{OKBLUE}Desenfileirando {fila_circular_teste.desenfileirar()}{ENDC}')
    print(f'{OKBLUE}Desenfileirando {fila_circular_teste.desenfileirar()}{ENDC}')
    fila_circular_teste.desenfileirar()
    print(f'{str(fila_circular_teste.valores)} {OKBLUE} Tamanho da Fila: {len(fila_circular_teste)}{ENDC}\n')


def fila_dupla_encadeada():
    fila_dupla_encadeada_teste = FilaDuplaEncadeada()
    # Testando a inserção

    print(f'{HEADER}Teste Nº 1 (Inserções no final): {ENDC}')
    fila_dupla_encadeada_teste.enfileirar("Franck")
    print(f'{str(fila_dupla_encadeada_teste.valores())}')
    fila_dupla_encadeada_teste.enfileirar("Pedro")
    print(f'{str(fila_dupla_encadeada_teste.valores())}')
    fila_dupla_encadeada_teste.enfileirar("Ronaldo")
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')

    print(f'\n{HEADER}Teste Nº 2 (Inserções no início): {ENDC}')
    fila_dupla_encadeada_teste.enfileirar_inicio("Siqueira")
    print(f'{str(fila_dupla_encadeada_teste.valores())}')
    fila_dupla_encadeada_teste.enfileirar_inicio("Roberto")
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')

    print(f'\n{HEADER}Teste Nº 3 (Ler Início e Fim): {ENDC}')
    print(f'Valor no início: {OKGREEN}{fila_dupla_encadeada_teste.ler_inicio()}{ENDC}\n'
          f'Valor do fim: {OKGREEN}{fila_dupla_encadeada_teste.ler_final()}{ENDC}')
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')

    print(f'\n{HEADER}Teste Nº 4 (Vazia): {ENDC}')
    if fila_dupla_encadeada_teste.vazia():
        print('A fila ESTÁ vazia!')
    else:
        print('A fila NÃO está vazia!')
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')

    print(f'\n{HEADER}Teste Nº 5 (Remoção no final): {ENDC}')
    print(f'{OKGREEN}{fila_dupla_encadeada_teste.desenfileirar_final()} removido!{ENDC}')
    print(f'{str(fila_dupla_encadeada_teste.valores())}')
    print(f'{OKGREEN}{fila_dupla_encadeada_teste.desenfileirar_final()} removido!{ENDC}')
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')

    print(f'\n{HEADER}Teste Nº 6 (Remoção no início): {ENDC}')
    print(f'{OKGREEN}{fila_dupla_encadeada_teste.desenfileirar()} removido!{ENDC}')
    print(f'{str(fila_dupla_encadeada_teste.valores())}')
    print(f'{OKGREEN}{fila_dupla_encadeada_teste.desenfileirar()} removido!{ENDC}')
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')

    print(f'\n{HEADER}Teste Nº 7 (Erro de remoção): {ENDC}')
    print(f'{OKGREEN}{fila_dupla_encadeada_teste.desenfileirar()} removido!{ENDC}')
    fila_dupla_encadeada_teste.desenfileirar()
    print(f'{str(fila_dupla_encadeada_teste.valores())} {OKBLUE} Tamanho da FIla: {len(fila_dupla_encadeada_teste)}{ENDC}')