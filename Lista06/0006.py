superior = int(input("Informe o valor do produtório: "))

inferior = 1
count = 1
produto = 1
tamanho_sequecia = superior - inferior

while count <= tamanho_sequecia:
   produto *= inferior + count
   count = count + 1

print(produto)

calulo_par = produto % 2
if calulo_par == 0:
   print(f"O valor do produtório {produto} é par. ")
else:
   print(f"O valor do produtório {produto} não é par.")