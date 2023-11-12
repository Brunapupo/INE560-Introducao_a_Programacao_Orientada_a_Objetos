saque = float(input("Informe o valor do saque: "))

if saque % 5 == 0 or saque % 10 == 0 or saque % 50 == 0:
   print("Valor Disponível.")
   print("Quantidade mínina de cada tipo de cédula:")
   quant_minina_5 = int(saque // 5)
   print(f"É possivel sacar {quant_minina_5} notas de R$ 5,00 reais.")
   quant_minina_10 = int(saque // 10)
   print(f"É possivel sacar {quant_minina_10} notas de R$ 10,00 reais.")
   quant_minina_50 = int(saque // 50)
   print(f"É possivel sacar {quant_minina_50} notas de R$ 50,00 reais.")
else:
   print("Valor Indisponível, dirija-se a outro caixa.")