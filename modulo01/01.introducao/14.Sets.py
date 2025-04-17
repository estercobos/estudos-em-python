# Características principais:
# 1. Não permite duplicatas: Se você tentar adicionar um valor que já existe, o Python vai ignorar.
# 2. Não é indexado: Você não pode acessar os elementos de um set por índice, como é feito em listas (não tem set[0] ou algo do tipo).
# 3. Mutable: Você pode adicionar ou remover elementos de um set depois que ele foi criado.
# 4. Desordenado: Os elementos não são armazenados em uma ordem específica.

# Set de itens comprados:
itens_comprados = {"pães", "hamburgueres", "bacon", "alface", "presunto", "queijo"}

# Set de itens que precisa comprar
itens_necessarios = {"pães", "queijo", "presunto", "refrigerante", "alface", "tomates", "condimentos"}

# Interseção: o que já comprei e também precisa comprar:
itens_comprados_necessarios = itens_comprados & itens_necessarios
print("Itens que você já comprou e precisa comprar: ", itens_comprados_necessarios)

# Diferença itens que preciso comprar, mas ainda não comprei:
itens_ainda_necessarios = itens_necessarios - itens_comprados
print("Itens que você ainda precisa comprar: ", itens_ainda_necessarios)

# Diferença simétrica: itens que já comprei ou preciso comprar, mas não os dois:
itens_comprados_ou_necessarios = itens_comprados ^ itens_necessarios
print("Itens que você já comprou ou precisa comprar, mas não ambos:", itens_comprados_ou_necessarios)