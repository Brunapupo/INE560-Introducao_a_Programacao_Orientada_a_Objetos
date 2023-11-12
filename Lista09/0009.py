def palindromo(frase):
   frase_limpa = ''
   resultado = 0
   for caracter in frase.lower():
       if caracter.isalpha():
           frase_limpa += caracter
       if frase_limpa == frase_limpa[::-1]:
           resultado = True
       else:
           resultado = False
   return resultado


frase = input("Informe uma frase: ")
print(palindromo(frase))