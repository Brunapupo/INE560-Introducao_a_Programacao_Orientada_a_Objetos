inferior = int(input("Informe o primeiro número: "))
superior = int(input("Informe o segundo número: "))


if inferior >= superior:
  print(f"O limite inferior não é menor ou igual ao limite superior. ")
else:
   count = 1
   soma = inferior
   tamanho_sequecia = superior - inferior
   while count <= tamanho_sequecia:
       soma += inferior + count
       count = count + 1

   print(f"{soma}")
