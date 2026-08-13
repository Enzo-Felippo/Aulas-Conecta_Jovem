print("=" * 60)
while True:
    try:
        numero = float(input("Digite um numero: "))
        resposta = numero / 100
    except ValueError:
        print("Valor não compativel")
    except ZeroDivisionError:
        print("Não pode dividir por 0 (zero)")
    else:
        print(f"Para a conta {numero} / 100")
        print(f"A resposta é {resposta}")
        break

print("=" * 60)
print("Volte sempre!")
print("=" * 60)
