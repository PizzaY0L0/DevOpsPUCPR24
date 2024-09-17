from src.Gerador_de_senhas import *
from unittest.mock import patch

# Função para gerar a senha aleatória
def test_generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    assert password

# Função principal para interação com o usuário
def test_gerador_de_senhas():
    print("Bem-vindo ao Gerador de Senhas!")
    try:
        comprimento = int(input("Digite o comprimento desejado da senha (número de caracteres): "))
        if comprimento < 1:
            print("O comprimento deve ser um número positivo.")
        else:
            senha = test_generate_password(comprimento)
            print(f"A sua senha gerada é: {senha}")
    except ValueError:
        print("Por favor, insira um número válido.")

# Chama a função principal
test_gerador_de_senhas()
