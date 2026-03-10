import os

os.system("cls")

nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo (m/f): ")
estado_civil = input("Digite o seu estado civil: ")
tempo_de_casada = int(input("Digite o tempo de casada (em anos): "))

if sexo == "F" and estado_civil == "CASADA":
    tempo_de_casada = int(input("Digite o tempo de casada (em anos): "))

print("\n--- DADOS DO USUÁRIO ---")
print("Nome:", nome)
print("Sexo:", sexo)
print("Estado civil:", estado_civil)

if sexo == "F" and estado_civil == "CASADA":
    print("Tempo de casada:", tempo_de_casada, "anos")