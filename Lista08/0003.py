def fatorial(numero):
  resultado = 1
  cont = 1
  while cont <= numero:
      resultado *= cont
      cont += 1
  return resultado

def sequencia(n):
   somatorio = 0
   cont = 0
   while cont <= n:
       somatorio = somatorio + (1 / fatorial(cont))
       cont = cont + 1
   return somatorio

n = int(input())
print(sequencia(n))