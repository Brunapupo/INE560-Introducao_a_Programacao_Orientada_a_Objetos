def correcaoProva(prova):
   cont_acertos = 0
   gabarito = ['A','A','C','E','D','B','C','E','B','D']
   for numero_atual in range(len(prova)):
       if prova[numero_atual] == gabarito[numero_atual]:
           cont_acertos += 1
   return cont_acertos
