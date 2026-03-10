import os

os.system("cls")

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma = A + B 

if soma < C:
    print("A soma de A + B é menor que C.")
else:
    print("A soma de A + B é maior ou igual a C.")
    