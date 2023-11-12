salario_atual = float(input("Qual o valor do salário atual?"))
porcentual = float(input("Qual o percentural de aumento?"))

aumento_porcentagem = salario_atual * (porcentual / 100)
salario_final = aumento_porcentagem + salario_atual
print(f"O salário com aumento de {porcentual}% é de R${salario_final:.2f}")
