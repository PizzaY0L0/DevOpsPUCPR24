import random
import string

# Função para gerar a senha aleatória
def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Função principal para interação com o usuário
def gerador_de_senhas():
    print("Bem-vindo ao Gerador de Senhas!")
    try:
        comprimento = int(input("Digite o comprimento desejado da senha (número de caracteres): "))
        if comprimento < 1:
            print("O comprimento deve ser um número positivo.")
        else:
            senha = generate_password(comprimento)
            print(f"A sua senha gerada é: {senha}")
            return senha
    except ValueError:
        print("Por favor, insira um número válido.")
        return None
