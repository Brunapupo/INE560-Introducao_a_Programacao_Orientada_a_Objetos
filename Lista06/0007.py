num = 1
count = 0
somatorio = 0
while num != 0:
   num = int(input("Informe o valor: "))
   somatorio = somatorio + num

   count += 1

media =  somatorio / count

print(f"Quantidade de números digitados:{count}")
print(f"Quantidade dos números somados: {somatorio}")
print(f"Média dos números: {media}")