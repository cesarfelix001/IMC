# Cálculo do IMC 

nome = input("Olá! vamos verificar seu IMC. Informe seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))

calculo = peso//altura**2
print(f"Muito bem {nome}, seu IMC é: {calculo}")
