primeiro = int(input("Informe o primeiro número:"))
segundo = int(input("Informe o segundo número:"))

maior = primeiro
if segundo > primeiro:
   maior = segundo
   print(maior)

if primeiro == segundo:
   print("Os números são iguais.")