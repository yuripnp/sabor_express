# Solicita ao usuário um número e exibe a tabuada desse número

# Solicita o número ao usuário
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibe a tabuada do número
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")