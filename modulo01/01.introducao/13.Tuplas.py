# Cadastro de uma pessoa com tupla para data de nascimento:

# Entrada de dados:
nome = input("Digite seu nome: ")

# Coletando e armazenando a data de nascimento como tupla:
ano = int(input("Digite o ano do seu nascimento: "))
mes = int(input("Digite o mês do seu nascimento (número): "))
dia = int(input("Digite o dia do seu nascimento: "))

# Tupla rodando:
data_nascimento = (ano, mes, dia)

# Cidade atual (pode mudar, então é string comum)
cidade = input("Digite a cidade onde você mora atualmente: ")

# Imprimindo os resultados:
print("\nDados cadastrados:")
print(f"Nome: {nome}")
print(f"Data de nascimento: {data_nascimento[2]:02d}/{data_nascimento[1]:02d}/{data_nascimento[0]}")

# Tentando mudar a data de nascimento (irá dar erro):
# data_nascimento[0] = 2000  # Isso aqui daria erro se descomentado!

print("\n✅ Cadastro concluído com sucesso! ✅")
