# Lista de números de 1 a 10
numeros = list(range(1, 11))

# Lista com quatro nomes
nomes = ["Alice", "Bruno", "Carla", "Diego"]

# Lista com o ano que você nasceu e o ano atual
anos = [1990, 2023]

# Exibindo as listas usando for
listas = [("Números", numeros), ("Nomes", nomes), ("Anos", anos)]
for nome_lista, conteudo in listas:
    print(f"{nome_lista}:", conteudo)
