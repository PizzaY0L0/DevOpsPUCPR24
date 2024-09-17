# Função para contar palavras em um texto
def count_words(text):
    words = text.split()  # Divide o texto em uma lista de palavras
    return len(words)

# Função principal para interação com o usuário
def contador_de_palavras():
    print("Bem-vindo ao Contador de Palavras!")
    texto = input("Digite o texto ou frase que deseja contar as palavras: ")
    numero_de_palavras = count_words(texto)
    print(f"O número de palavras no texto é: {numero_de_palavras}")

# Chama a função principal
contador_de_palavras()

