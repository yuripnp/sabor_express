# Programa Sabor Açaí

# Exibe o nome da loja
print("""

███████╗░█████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░██║░░██║██║░░██║██║░░██║  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░██║░░██║██║░░██║██║░░██║  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██║░░░░░╚█████╔╝╚█████╔╝██████╔╝  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
      
      
      """)


# Exibe as opções do menu
print("1. Cadastrar Restaurantes")
print("2. Listar Restaurantes")
print("3. Ativar Restaurantes")
print("4. Sair")
print()

# Recebe a escolha do usuário
escolha = int(input("Escolha uma opção: "))
print(f"voc'e escolheu a opção {escolha}")
print()
# Verifica se a escolha é válida
if escolha < 1 or escolha > 4:
    print("Opção inválida. Tente novamente.")
else:
    # Cria uma lista para armazenar os restaurantes
    restaurantes = []

    # Loop para executar o menu até que o usuário escolha sair
    while escolha != 4:
        if escolha == 1:
            # Cadastra um novo restaurante
            nome = input("Digite o nome do restaurante: ")
            endereco = input("Digite o endereço do restaurante: ")
            telefone = input("Digite o telefone do restaurante: ")
            ativo = False
            restaurantes.append({"nome": nome, "endereco": endereco, "telefone": telefone, "ativo": ativo})
            print(f"Restaurante {nome} cadastrado com sucesso!")
        elif escolha == 2:
            # Lista os restaurantes cadastrados
            print("Restaurantes cadastrados:")
            for i, restaurante in enumerate(restaurantes):
                status = "Ativo" if restaurante["ativo"] else "Inativo"
                print(f"{i + 1}. {restaurante['nome']} - {restaurante['endereco']} - {restaurante['telefone']} - {status}")
        elif escolha == 3:
            # Ativa um restaurante
            nome = input("Digite o nome do restaurante a ser ativado: ")
            for restaurante in restaurantes:
                if restaurante["nome"] == nome:
                    restaurante["ativo"] = True
                    print(f"Restaurante {nome} ativado com sucesso!")
                    break
            else:
                print(f"Restaurante {nome} não encontrado.")
        else:
            print("Opção inválida. Tente novamente.")

        # Exibe as opções do menu novamente
        print()
        print("1. Cadastrar Restaurantes")
        print("2. Listar Restaurantes")
        print("3. Ativar Restaurantes")
        print("4. Sair")
        print()

        # Recebe a nova escolha do usuário
        escolha = int(input("Escolha uma opção: "))
