valor_produto = float(input("Informe o valor do produto:"))
desconto_produto = float(input("Informe o valor do desconto:"))

desconto = valor_produto * (desconto_produto / 100)
valor_final = valor_produto - desconto
print(f"{valor_final:.2f}")
