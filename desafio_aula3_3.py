# Criando uma lista de 1 até 10
numeros = list(range(1, 11))

# Filtrando os números ímpares e somando-os
soma_impares = sum(num for num in numeros if num % 2 != 0)

# Exibindo o resultado
print(f"A soma dos números ímpares de 1 a 10 é: {soma_impares}")