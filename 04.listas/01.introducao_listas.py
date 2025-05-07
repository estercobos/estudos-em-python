# Uma lista em Python é uma estrutura que pode guardar vários valores dentro de uma única variável. Os valores são armazenados em sequência, separados por vírgulas e entre colchetes [].

# Criando uma lista com alguns elementos:

ingredientes_lanche = ["pães", "manteiga", "maionese", "hamburgueres", "requeijão", "alface", "tomate", "molho de alho", "bacon", "barbecue"]

# Exibindo a lista completa:
print("Lista de ingredientes do lanche:", ingredientes_lanche)

# Acessando elementos da lista (lembrando que a contagem começa do zero)
print("Primeiro ingrediente da lista: ", ingredientes_lanche[0])
print("Segundo ingrediente da lista: ", ingredientes_lanche[1])

# Acessando elementos usando índices negativos
print("Último ingrediente da lista: ", ingredientes_lanche[-1])  # Último item
print("Penúltimo ingrediente da lista: ", ingredientes_lanche[-2])  # Penúltimo item

# Adicionando um novo item à lista com .append()
ingredientes_lanche.append("ketchup")
print("Depois adicionar ketchup à lista:", ingredientes_lanche)

# Removento um item com .remove()
ingredientes_lanche.remove("tomate")
print("Depois remover o tomate:", ingredientes_lanche)

# Verificando o tamanho da lista com len()
print("Quantidade de itens da lista: ", len(ingredientes_lanche))

# O Laço For também é útil para percorrer a lista
print("\nListando os ingredientes um por um:")
for ingrediente in ingredientes_lanche:
    # A variável 'ingrediente' vai assumir, a cada volta, o valor de um item da lista
    print("Ingrediente:", ingrediente)

# Criando uma lista de listas (listas dentro de uma lista)
ingredientes_varios_lanches = [
    ["pães", "manteiga", "maionese", "hamburgueres"],
    ["alface", "tomate", "molho de alho", "bacon"],
    ["barbecue", "requeijão", "ketchup"]
]

# Acessando elementos de uma lista dentro da lista principal
print("Primeiro conjunto de ingredientes:", ingredientes_varios_lanches[0])  # Primeiro conjunto de ingredientes
print("Segundo ingrediente do segundo conjunto:", ingredientes_varios_lanches[1][1])  # Segundo ingrediente do segundo conjunto

# Modificando um item de uma lista
ingredientes_lanche[0] = "pães de forma"
print("Lista após modificar o primeiro item:", ingredientes_lanche)

# Ordenando a lista em ordem alfabética
ingredientes_lanche.sort()
print("Lista ordenada:", ingredientes_lanche)

# Revertendo a ordem da lista
ingredientes_lanche.reverse()
print("Lista revertida:", ingredientes_lanche)