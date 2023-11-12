numero = int(input('Informe o número de estrelas: '))

count = 1
while count <= numero:
  count2 = 1
  while count2 <= count:
      print("*", end='')
      count2 = count2 + 1
  count = count + 1
  print()
count = numero - 1
while count >= 1:
   count2 = count
   while count2 >= 1:
       print("*", end='')
       count2 = count2 - 1
   count = count - 1
   print()
