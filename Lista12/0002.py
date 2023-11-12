def segundo_diagonal(m):
   tam = len(m)
   l = 0
   c = tam - 1
   numinicial = m[l][c]
   while l < tam:
       segunda_diagonal = m[l][c]
       if numinicial != segunda_diagonal:
           return False
       l = l + 1
       c = c - 1
   return True


m = [
   [0, 1, 2, 3],
   [2, 5, 3, 3],
   [5, 9, 5, 6],
   [3, 8, 9, 8]
   ]

print(segundo_diagonal(m))