import os

os.system("cls")

morango = float(input("Digite o preço do quilo de morango: "))
maçã = float(input("Digite o preço do quilo de maçã: "))

if morango <= 5:
    preco_morango = morango * 2.50
else:
    preco_morango = morango * 2.50

if maçã <= 5:
    preco_maçã = maçã * 1.80
else:
    preco_maçã = maçã * 1.5

total = preco_morango + preco_maçã
peso_total = morango + maçã

if peso_total >= 10 or total > 15:
    total *= 0.90

print("Preço total: r$", total)
