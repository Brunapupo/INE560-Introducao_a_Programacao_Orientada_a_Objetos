def mostraMatriz(m):
   for i in m:
       for j in i:
           print(j, ' ', end='')
       print()

def criaMatrizSequencial(m, n):
   ret = []
   for i in range(m):
       noval = list(range(i, i+n))
       ret.append(noval)
   return ret

m = criaMatrizSequencial(5,5)
mostraMatriz(m)


ind = 0
soma = 0
while ind < len(m):
   soma = soma + (m[ind][ind])
   print(m[ind][ind])
   ind = ind + 1

media = soma / len(m)
print(media)
