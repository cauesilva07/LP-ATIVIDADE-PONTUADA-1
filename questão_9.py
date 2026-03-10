import os

os.system("cls")

renda = float(input("Digite a renda mensal: "))
emprestimo = float(input("Digite o valor do empréstimo: "))
prestacoes = int(input("Digite o número de prestações: "))

valor_prestacao = emprestimo / prestacoes

if emprestimo <= renda * 10 and valor_prestacao <= renda * 0.30:
    print("Empréstimo pode ser concedido.")
else:
    print("Empréstimo não pode ser concedido.")