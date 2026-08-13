print("=" * 60)

idade = int(input("Qual é sua idade: "))

print("=" * 60)

if idade < 12 and idade > 0:
    print(f"Com {idade} é riança")
elif idade > 12 and idade < 18:
    print(f"Com {idade} é adolescente")
elif idade >= 18 and idade < 129:
    print(f"Com {idade} já é adulto")
else:
    print("Quer mentir para quem?")

print("=" * 60)