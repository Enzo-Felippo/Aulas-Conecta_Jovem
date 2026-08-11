peso = float(input("Seu peso: "))
altura = float(input("Sua altura: "))

IMC = peso/(altura*altura)

print("===" * 20)
print("De acordo com os dados oferecidos,")
print(f"Seu IMC é {IMC:.2f}")
print("===" * 20)
