# Criando uma lista de compras:
lista_compras = ["pães", "hamburgueres", "bacon" "alface", "presunto", "queijo", "condimentos"]

# Imprimindo a lista:
print("Minha lista de compras: ")
print(lista_compras)

# Adicionando "refrigerante" à lista de compras:
lista_compras.append("refrigerante")

# Imprimindo a lista atualizada:
print("\nLista de compras atualizada:")
print(lista_compras)

# Removendo o item "condimentos" da lista:
lista_compras.remove("condimentos")

# Imprimindo a lista após a remoção:
print("\nLista de compras depois de remover condimentos:")
print(lista_compras)

# Verificando se "queijo" está na lista:
if "queijo" in lista_compras:
    print("\nO queijo está na lista.")
else:
    print("\nO queijo não está na lista.")

# Imprimindo todos os itens da lista de compras:
print("\nItens da lista de compras:")
for item in lista_compras:
    print("- " + item)

# Imprimindo apenas os 3 primeiros itens da lista de compras:
print("\nOs 3 primeiros itens da lista de compras:")
print(lista_compras[:3])

# Ordenando a lista de compras em ordem alfabética:
lista_compras.sort()

print("\nLista de compras ordenada:")
print(lista_compras)