valor_compra = float(input("Informe o valor da compra: "))
desconto = 0
if valor_compra >= 6999:
   desconto = valor_compra * 15 / 100
   total = valor_compra - desconto
   print(f"O valor do é de: {total:.2f}, com desconto de {desconto:.2f}")
else:
   desconto = valor_compra * 5 / 100
   total = valor_compra - desconto
   print(f"O valor total é de: {total:.2f}, com desconto de {desconto:.2f}")