def eh_primo(numero):
   if numero == 0 or numero == 1:
       return False
   flag = False
   if numero > 1:
       for i in range(2, numero):
           if (numero % i) == 0:
               flag = True
               break
   if flag:
       return False
   else:
       return True

def matrix(m):
   lista_primos = []
   for linha in m:
       for elemento in linha:
           if eh_primo(elemento):
               lista_primos.append(elemento)
   return lista_primos


print(matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
