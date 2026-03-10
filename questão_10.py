import os

os.system("cls")

tipo = input("Digite o tipo de combustível (A ou G): ")
litros = float(input("Digite a quantidade de litros: "))

if tipo == "A":
    preco = 3.79
    if litros <= 25:
        desconto = 0.02
    else:
        desconto = 0.04
elif tipo == "G":
    preco = 6.59
    if litros <= 25:
        desconto = 0.03
    else:
        desconto = 0.05

valor_total = litros * preco * (1 - desconto)
print(f"Valor total a pagar: R$ {valor_total:.2f}")