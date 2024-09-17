import string
from src.Gerador_de_senhas import gerador_de_senhas, generate_password
from unittest import TestCase
from unittest.mock import patch

class TestGeradorDeSenhas(TestCase):

    def test_generate_password(self):
        password = generate_password(10)
        self.assertEqual(len(password), 10)
        self.assertTrue(any(char in string.ascii_letters for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    @patch('builtins.input', return_value='10')  # Simula o input do usuário
    @patch('builtins.print')  # Simula o print
    def test_gerador_de_senhas_valid_input(self, mock_print, mock_input):
        senha = gerador_de_senhas()
        mock_input.assert_called_once_with("Digite o comprimento desejado da senha (número de caracteres): ")
        self.assertEqual(len(senha), 10)
        mock_print.assert_any_call("Bem-vindo ao Gerador de Senhas!")
        mock_print.assert_any_call(f"A sua senha gerada é: {senha}")

    @patch('builtins.input', return_value='-5')  # Simula input de comprimento negativo
    @patch('builtins.print')
    def test_gerador_de_senhas_negative_length(self, mock_print, mock_input):
        gerador_de_senhas()
        mock_print.assert_called_with("O comprimento deve ser um número positivo.")

    @patch('builtins.input', return_value='abc')  # Simula input inválido
    @patch('builtins.print')
    def test_gerador_de_senhas_invalid_input(self, mock_print, mock_input):
        gerador_de_senhas()
        mock_print.assert_called_with("Por favor, insira um número válido.")
