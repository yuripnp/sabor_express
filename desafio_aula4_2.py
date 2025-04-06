from desafio_aula4_1 import usuario

# Importa o dicionário do arquivo desafio_aula4_1

# Atualiza no mínimo dois parâmetros do dicionário
usuario.update({'idade': 31})
usuario['endereco']['numero'] = 456
usuario['profissao'] = 'Engenheiro de Software'
# Adiciona um novo parâmetro ao dicionário

usuario.pop('email', None)
# Exibe o dicionário atualizado
print("Dicionário atualizado:", usuario)