def fatorial(numero):
  resultado = 1
  cont = 1
  while cont <= numero:
      resultado *= cont
      cont += 1
  return resultado

n = int(input())
p = int(input())
soma = (fatorial(n) / fatorial(p)) * fatorial(n - p)
print(soma)
