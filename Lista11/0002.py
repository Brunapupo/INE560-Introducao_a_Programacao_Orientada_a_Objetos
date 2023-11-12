m = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
   ]

linha = 0
qtLinhas = len(m)
while linha < qtLinhas:
   col = 0
   qtCol = len(m[linha])
   while col < qtCol:
       print(f"{m[linha][col]} ", end='  ')
       col = col + 1
   linha = linha + 1
   print()
