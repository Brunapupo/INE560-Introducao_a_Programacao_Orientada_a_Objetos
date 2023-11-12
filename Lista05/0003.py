engajamento = int(input("Informe o nivel de engajamento: "))
compra = float(input("Informe o total da compra: "))

total = 0.0
desconto = 0.0
if engajamento != 5 and engajamento != 8 and engajamento != 12 or compra < 100:
   print(f"Cliente não tem direito ao desconto")
else:
   if engajamento == 5:
       desconto = compra * 5 / 100
       total = compra - desconto
   elif engajamento == 8:
       desconto = compra * 8 / 100
       total = compra - desconto
   elif engajamento == 12:
       desconto = compra * 12 / 100
       total = compra - desconto
   print(f"Total da compra: R${total}, com desconto de: R${desconto}")
