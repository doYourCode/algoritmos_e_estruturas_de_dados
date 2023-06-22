_author__ = ["Everton Sousa Oliveira",
             "Jônatas Pereira da Rocha",
             "Thaylon Ramon Ramos Ribeiro",
             "Gregory Almeida SilvaGregory Almeida Silva"]
__date__ = "28/05/2023"
__credits__ = [""]
__license__ = "GPL"
__email__ = "eso@aluno.ifnmg.edu.br, caio.lamas@ifnmg.edu.br"

# COMENTÁRIOS DO PROFESSOR (FAVOR APAGAR APÓS CORRIGIR)
# Não implementou os testes, favor ver o arquivo testes_filas.py
# A documentação deste arquivo não condiz com o padrão, você corrigiu isso no segundo arquivo, pode por naquele formato
class FilaPrioridade:
    def __init__(self, tamanho_maximo):
        self.fila_teste = []
        self.tamanho_maximo = tamanho_maximo

    def remover(self):
        if self.estaVazia():
            raise IndexError("A fila está vazia.")

        valor_removido = self.fila_teste[0]
        del self.fila_teste[0]

        return valor_removido

    def adicionar(self, valor):
        if self.estaCheia():
            print("A fila está cheia. Não é possível adicionar o elemento.")
            exit(-1)
        self.fila_teste.append(valor)
        self.fila_teste.sort(reverse=True) # Vou verificar se o procedimento é esse mesmo, entro em contato

    def peek(self):
        if self.estaVazia():
            raise IndexError("A fila está vazia.")
        return self.fila_teste[0]

    def tamanho(self):
        return len(self.fila_teste)

    def estaVazia(self):
        return self.tamanho() == 0

    def estaCheia(self):
        return self.tamanho() == self.tamanho_maximo