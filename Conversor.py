# Taxas de câmbio fixas para o exemplo
USD_TO_BRL = 5.00  # Exemplo: 1 USD = 5 BRL
KRW_TO_BRL = 0.0043  # Exemplo: 1 KRW = 0.0043 BRL
JPY_TO_BRL = 0.035  # Exemplo: 1 JPY = 0.035 BRL

BRL_TO_USD = 1 / USD_TO_BRL
BRL_TO_KRW = 1 / KRW_TO_BRL
BRL_TO_JPY = 1 / JPY_TO_BRL

# Função para converter Reais para outras moedas
def brl_to_currency(brl, currency):
    if currency == "USD":
        return brl * BRL_TO_USD
    elif currency == "KRW":
        return brl * BRL_TO_KRW
    elif currency == "JPY":
        return brl * BRL_TO_JPY
    else:
        return "Moeda não suportada."

# Função para converter outras moedas para Reais
def currency_to_brl(amount, currency):
    if currency == "USD":
        return amount * USD_TO_BRL
    elif currency == "KRW":
        return amount * KRW_TO_BRL
    elif currency == "JPY":
        return amount * JPY_TO_BRL
    else:
        return "Moeda não suportada."

# Função principal para interação com o usuário
def converter_moeda():
    print("Bem-vindo ao conversor de moedas!")
    print("Escolha a opção de conversão:")
    print("1. Converter BRL para outra moeda")
    print("2. Converter outra moeda para BRL")
    
    escolha = input("Digite o número da opção desejada (1 ou 2): ")

    if escolha == "1":
        brl = float(input("Digite o valor em Reais (BRL): "))
        print("Escolha a moeda de destino:")
        print("USD - Dólar Americano")
        print("KRW - Won Sul-Coreano")
        print("JPY - Iene Japonês")
        moeda = input("Digite o código da moeda (USD, KRW, JPY): ").upper()
        resultado = brl_to_currency(brl, moeda)
        print(f"O valor de R$ {brl} em {moeda} é: {resultado:.2f}")

    elif escolha == "2":
        moeda = input("Digite a moeda de origem (USD, KRW, JPY): ").upper()
        valor = float(input(f"Digite o valor em {moeda}: "))
        resultado = currency_to_brl(valor, moeda)
        print(f"O valor de {valor} {moeda} em BRL é: R$ {resultado:.2f}")

    else:
        print("Opção inválida. Tente novamente.")

# Chama a função principal
converter_moeda()
