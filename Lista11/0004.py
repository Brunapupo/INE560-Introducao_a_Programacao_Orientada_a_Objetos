def Menor(m):

   menor = 1000000
   menor_elemento = 0


   for linha in m:
       for elemento in linha:
           if elemento < menor:
               menor = elemento
               menor_elemento += elemento


   return menor_elemento

print(Menor([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
  ]
))
