# Criando a lista de compras:
lista_compras = ["pães", "hamburgueres", "bacon", "alface", "presunto", "queijo", "condimentos"]

# Imprimindo a lista:
print("Minha lista de compras:")
print(lista_compras)

# Adicionando "refrigerante" no final:
lista_compras.append("refrigerante")

# Adicionando "maionese" na terceira posição:
lista_compras.insert(2, "maionese")

# Verificando quantos itens tem na lista:
print(f"\nTotal de itens na lista: {len(lista_compras)}")

# Removendo o item "condimentos":
lista_compras.remove("condimentos")

# Removendo o último item da lista e mostrando ele:
ultimo = lista_compras.pop()
print(f"\nRemovi o último item da lista: {ultimo}")

# Mostrando posição do item "queijo":
if "queijo" in lista_compras:
    posicao = lista_compras.index("queijo")
    print(f"\nO queijo está na posição {posicao}")

# Contando quantas vezes "pães" aparece:
print(f"\n'Pães' aparece {lista_compras.count('pães')} vez(es) na lista")

# Imprimindo todos os itens:
print("\nItens atuais da lista:")
for item in lista_compras:
    print("- " + item)

# Copiando a lista para não mexer na original:
lista_backup = lista_compras.copy()

# Ordenando uma cópia da lista:
lista_ordenada = sorted(lista_compras)
print("\nLista ordenada (sem alterar a original):")
print(lista_ordenada)

# Invertendo a lista original:
lista_compras.reverse()
print("\nLista na ordem reversa:")
print(lista_compras)

# Limpando a cópia da lista (só pra mostrar o método):
lista_backup.clear()
print("\nBackup limpado:")
print(lista_backup)