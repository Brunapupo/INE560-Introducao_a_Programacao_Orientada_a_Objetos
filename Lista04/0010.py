altura = float(input("Informe a sua altura:"))
idade =  int(input("Informe a sua idade:"))
horas_voo = float(input("Informe horas de vôo:"))
peso = int(input("Informe o seu peso:"))

if altura >= 1.75:
   if idade >= 22 and idade <= 40:
       if horas_voo >= 1600:
           if peso >= 65 and peso <= 95:
               print("Você está apto para ingressar no curso de aviação.")
else:
   print("Você não está apto para ingressar no curso de aviação.")
