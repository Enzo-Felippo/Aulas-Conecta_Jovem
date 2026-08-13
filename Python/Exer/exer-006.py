print("=" * 60)

peso = float(input("Qual é seu peso: "))
altura = float(input("Qual é sua altura: "))

imc = peso / (altura*altura)

print("=" * 60)

if imc <= 18.5:
    print(f"Seu imc de {imc} é de alguém abaixo do peso")
elif imc <= 24.9:
    print(f"Seu imc de {imc} é de alguém de peso normal")
else:
    print(f"Seu imc de {imc} é de alguém com sobrepeso")

print("=" * 60)