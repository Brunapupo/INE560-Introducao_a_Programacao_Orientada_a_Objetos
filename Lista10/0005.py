def ePrimo(numero):
   if numero == 0 or numero == 1:
       return False
   else:
       divisor = 2
       contagem_divisoes = 0
       while divisor < numero:
           if numero % divisor == 0:
               contagem_divisoes += 1
           divisor += 1
       if contagem_divisoes == 0:
           return True
       else:
           return False


def proximoPrimo(n):
   primo = False
   resultado = n
   while not primo:
       resultado = resultado + 1
       primo = ePrimo(resultado)
   return resultado

def nextPrimo(n, inicio):
   cont = 0
   numeros_primos = []
   while cont < n:
       inicio = proximoPrimo(inicio)
       numeros_primos.append(inicio)
       cont += 1
   return numeros_primos


n = int(input("Informe quantidade de primos: "))
inicio = int(input("Informe um número de inicio: "))

print(nextPrimo(n, inicio))