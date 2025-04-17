# Passo 1- Coleta de dados:
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
profissao = input("Digite sua profissão: ")
cidade = input("Digite sua cidade: ")

# Passo 2 - Criação do dicionário:
perfil_usuario = {
    "nome": nome,
    "idade": idade,
    "profissão": profissao,
    "cidade": cidade
}

# Passo 3 - Exibição do dicionário:
print("\nPerfil cadastrado:")
print(perfil_usuario)

# Passo 4 - Atualizando a cidade:
perfil_usuario["cidade"] = input("\nVocê se mudou! Qual é sua nova cidade?")

# Passo 5 - Removendo a profissão:
del perfil_usuario["profissão"]

# Passo 6 - Mostrando perfil atualizado
print("\nPerfil atualizado:")
print(perfil_usuario)