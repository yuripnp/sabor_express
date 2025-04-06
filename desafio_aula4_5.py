palavras = {'para': 0, 'o': 0, 'mundo': 0, 'de': 0, 'programação': 0, 'python': 0}
# Exibe a contagem de palavras
frase = 'Olá, mundo! Bem-vindo ao mundo da programação em Python. vamos saber mais de python?'

for palavra in palavras.keys():
    # Conta quantas vezes cada palavra aparece na frase
    palavras[palavra] = frase.lower().count(palavra)

print(palavras)