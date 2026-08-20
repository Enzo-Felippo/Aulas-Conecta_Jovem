print("=" * 60) # Questão 1

dada = [3, 7, 1, 9, 4]
print(f"Os três primeiros {dada[:3]}")
print(f"Os dois últimos {dada[-2:]}")

print("=" * 60) # Questão 2

resultado = []
resultado.extend([x*2 for x in range(10) if x % 3 == 0])
print(f"Multiplicação por: {resultado}")

print("=" * 60) # Questão 3

quadrados = [x*x for x in range(1, 21) if x % 3 == 0]
print(f"Quadrados: {quadrados}")

print("=" * 60) # Questão 4

vendas = [120.5, 89.9, 340.0, 15.0, 220.0]
media_vendas = sum(vendas) / len(vendas)
acima_media_vendas = [v for v in vendas if v > media_vendas]

print(f"Vendas média: {media_vendas:,.2f}")
print(f"Vendas acima da média: {acima_media_vendas}")

print("=" * 60) # Questão 5

