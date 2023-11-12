num = 15
while num < 0 or num > 9:
   num = int(input("Informe um valor inteiro entre 1 a 9 ou 0 para sair: "))

if num >= 1 and num <= 9:
   divi = 0
   count = 1
   while count <= 1000:
       if count % num == 0:
           divi += 1

       count +=1

   print(divi)
