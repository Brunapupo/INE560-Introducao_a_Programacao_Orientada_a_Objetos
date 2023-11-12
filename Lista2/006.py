from datetime import date
nome = input("Qual seu nome?")
ano_nascimento = int(input("Qual seu ano de nascimento?"))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f"{nome}, você tem {idade} anos de idade")