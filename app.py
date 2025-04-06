import os
# Programa Sabor Açaí

def exibir_logo():
    ''' Exibe o logo do programa encontrado
    digitando no google fsymbols'''

    print("""

    ███████╗░█████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    █████╗░░██║░░██║██║░░██║██║░░██║  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ██╔══╝░░██║░░██║██║░░██║██║░░██║  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██║░░░░░╚█████╔╝╚█████╔╝██████╔╝  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═╝░░░░░░╚════╝░░╚════╝░╚═════╝░  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      
    """)

def opcao_invalida():
    ''' 
    Exibe mensagem de opção inválida e retorna ao menu principal 
    '''
    # Exibe mensagem de opção inválida
    print('Opção inválida. Tente novamente.\n')
    print('Digite uma tecla para voltar ao menu principal')
    os.system('cls' if os.name == 'nt' else 'clear')
    main()

def exibir_menu():
    ''' 
    menu principal do programa 
    '''
    print("Menu de Opções:")
    print("1. Cadastrar Restaurantes")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurantes")
    print("4. Sair")
    print()

def entrada_usuario():
    '''
    Lê a entrada do usuário e retorna a opção escolhida'''
    try:
        escolha = int(input("Escolha uma opção: "))
        print(f"voce escolheu a opção {escolha}")
        print()
        return escolha
    except ValueError:
        opcao_invalida()

def opcao(escolha):
    '''
    Executa a opção escolhida pelo usuário

    Argumentos:
    - escolha (int): A opção escolhida pelo usuário
    Input:
    - escolha: int
    - A opção escolhida pelo usuário
    Output:
    - funcao correspondente

    '''
    if escolha < 1 or escolha > 4:
        print("Opção inválida. Tente novamente.")
    else:
        restaurantes = []
        while escolha != 4:
            if escolha == 1:
                  escolha_um(restaurantes)
            elif escolha == 2:
                # Lista os restaurantes cadastrados
                escolha_dois(restaurantes)
            elif escolha == 3:
                # Ativa um restaurante
                escolha_tres(restaurantes)
            elif escolha == 4:
                # Sai do programa
                print("Saindo do programa...")
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            else:
                print("Opção inválida. Tente novamente.")
            exibir_menu()
            escolha = entrada_usuario()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Saindo do programa...")

def escolha_um(restaurantes):
    '''
    Cadastra um novo restaurante
    Input:
    - restaurantes: list
    - Lista de restaurantes cadastrados
    Output:
    - update na lista de restaurantes
    '''
    nome = input("Digite o nome do restaurante: ")
    endereco = input("Digite o endereço do restaurante: ")
    telefone = input("Digite o telefone do restaurante: ")
    ativo = False
    restaurantes.append({"nome": nome, "endereco": endereco, "telefone": telefone, "ativo": ativo})
    print(f"Restaurante {nome} cadastrado com sucesso!")
    
def escolha_dois(restaurantes):
    '''
    Lista os restaurantes cadastrados
    '''
    print("Restaurantes cadastrados:")
    for i, restaurante in enumerate(restaurantes):
        status = "Ativo" if restaurante["ativo"] else "Inativo" # ternário
        print(f"{i + 1}. {restaurante['nome']} - {restaurante['endereco']} - {restaurante['telefone']} - {status}")
    print()

def escolha_tres(restaurantes):
    '''
    Ativa um restaurante'''
    nome = input("Digite o nome do restaurante a ser ativado: ")
    for restaurante in restaurantes:
        if restaurante["nome"] == nome:
            restaurante["ativo"] = True
            print(f"Restaurante {nome} ativado com sucesso!")
            break
    else:
        print(f"Restaurante {nome} não encontrado.")

def main():
    '''
    Função principal do programa
    '''
    exibir_logo()
    exibir_menu()
    escolha = entrada_usuario()
    opcao(escolha)
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    # Executa o programa
    main()
    