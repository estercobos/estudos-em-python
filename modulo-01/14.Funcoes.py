# É um bloco de código reutilizável que executa uma tarefa específica. Você define uma vez e chama quantas quiser.Imagina uma função como uma máquina de suco: você coloca frutas (parâmetros), ela processa (executa comandos) e te entrega suco (retorno).

def saudacao(nome):
    return f"Olá, {nome}! Bem-vinda(o) ao mundo as funções!"

mensagem = saudacao("Ester")
print(mensagem)