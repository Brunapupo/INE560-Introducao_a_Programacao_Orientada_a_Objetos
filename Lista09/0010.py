def classificacoesTexto(texto):
   qtd_vogais = 0
   qtd_consoantes = 0
   qtd_numeros = 0
   for caracter in texto:
       if caracter.lower() in ['a', 'e', 'i', 'o', 'u']:
           qtd_vogais += 1
       else:
           if caracter in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
               qtd_numeros += 1
           else:
               if caracter.lower() >= 'a' and caracter.lower() <= 'z':
                   qtd_consoantes += 1

   return [qtd_vogais, qtd_consoantes, qtd_numeros]

print(classificacoesTexto("123 abc"))