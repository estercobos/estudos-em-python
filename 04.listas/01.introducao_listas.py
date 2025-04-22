# Uma lista em Python é uma estrutura que pode guardar vários valores dentro de uma única variável. Os valores são armazenados em sequência, separados por vírgulas e entre colchetes [].

# Criando uma lista com alguns elementos:

ingredientes_lanche = ["pães", "manteira", "maionese", "hamburgueres", "requeijão", "alface", "tomate", "molho de alho", "bacon", "barbecue"]

# Exibindo a lista completa:
print("Lista de ingredientes do lanche:", ingredientes_lanche)

# Acessando elementos da lista (lembrando que a contagem começa do zero)
print("Primeiro ingrediente da lista: ", ingredientes_lanche[0])
print("Segundo ingrediente da lista: ", ingredientes_lanche[1])

# Adicionando um novo item à lista com .append()
ingredientes_lanche.append("ketchup")
print("Depois adicionar ketchup à lista:", ingredientes_lanche)

# Removento um item com .remove()
ingredientes_lanche.remove("tomate")
print("Depois remover o tomate:", ingredientes_lanche)

# Verificando o tamanho da lista com len()
print("Quantidade de itens da lista: ", len(ingredientes_lanche))

# O Laço For também é útil para percorrer a lista
for ingredientes_lanche in ingredientes_lanche:
    print("Itens: ", ingredientes_lanche)