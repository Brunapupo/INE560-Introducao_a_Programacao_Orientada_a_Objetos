def fatorial(numero):
 resultado = 1
 cont = 1
 while cont <= numero:
     resultado *= cont
     cont += 1
 return resultado


def cosseno(n):
   somatorio = 1
   cont = 0
   x = 2
   sinal_menos = True
   expoente = 2
   while cont < n:
       if sinal_menos:
           somatorio = somatorio - (x ** expoente) / fatorial(expoente)
           sinal_menos = False
       else:
           somatorio = somatorio + (x ** expoente) / fatorial(expoente)
           sinal_menos = True
		
       cont += 1


   return somatorio

n = int(input())
x = float(input())
print(cosseno(n))
