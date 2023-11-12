m = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
   ]
soma = 0
for linha in m:
   for ele in linha:
       soma += ele
       print(f'{ele} ', end='')

   print()

print(f"A soma total dos elementos da matriz é: {soma}")