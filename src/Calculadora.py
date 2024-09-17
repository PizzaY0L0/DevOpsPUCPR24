# Funções de Operações Matemáticas
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

# Função para Executar a Calculadora
def calculator():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    
    while True:
        # Entrada da Operação
        operation = input("Digite o número da operação (1/2/3/4) ou 'q' para sair: ")
        
        if operation == 'q':
            print("Encerrando a calculadora.")
            break

        # Verifica se a operação é válida
        if operation not in ['1', '2', '3', '4']:
            print("Operação inválida. Tente novamente.")
            continue
        
        try:
            # Entrada dos números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Realiza a operação escolhida
        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")

# Chamar a função da calculadora
calculator()