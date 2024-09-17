from src.Gerador_de_senhas import gerador_de_senhas, generate_password
from unittest import TestCase
from unittest.mock import patch
import string

class TestGeradorDeSenhas(TestCase):

    # Testando se a função de geração de senhas está funcionando corretamente
    def test_generate_password(self):
        password = generate_password(10)
        self.assertEqual(len(password), 10)  # Verifica se o comprimento da senha está correto
        self.assertTrue(any(char in string.ascii_letters for char in password))  # Verifica se há letras
        self.assertTrue(any(char in string.digits for char in password))  # Verifica se há dígitos
        self.assertTrue(any(char in string.punctuation for char in password))  # Verifica se há pontuação

    # Testando a função principal simulando entradas do usuário
    @patch('builtins.input', return_value='10')
    @patch('builtins.print')
    def test_gerador_de_senhas_valid_input(self, mock_print, mock_input):
        senha = gerador_de_senhas()
        mock_input.assert_called_once_with("Digite o comprimento desejado da senha (número de caracteres): ")
        self.assertEqual(len(senha), 10)  # Verifica se a senha gerada tem 10 caracteres
        mock_print.assert_any_call("Bem-vindo ao Gerador de Senhas!")
        mock_print.assert_any_call(f"A sua senha gerada é: {senha}")

    @patch('builtins.input', return_value='-5')
    @patch('builtins.print')
    def test_gerador_de_senhas_negative_length(self, mock_print, mock_input):
        gerador_de_senhas()
        mock_print.assert_called_with("O comprimento deve ser um número positivo.")

    @patch('builtins.input', return_value='abc')
    @patch('builtins.print')
    def test_gerador_de_senhas_invalid_input(self, mock_print, mock_input):
        gerador_de_senhas()
        mock_print.assert_called_with("Por favor, insira um número válido.")
