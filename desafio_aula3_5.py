# Lista de números
numeros = [10, 20, 30, 40, 50]

# Inicializa a soma
soma = 0

try:
    # Loop para calcular a soma
    for numero in numeros:
        soma += numero
    print(f"A soma de todos os números é: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")