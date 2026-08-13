
print("=" * 60)

valores = [12, 23, 34, 243, 113, 1212]
print(f"Maior valor é {max(valores)}")
print(f"Menor valor é {min(valores)}")
print(f"A soma dos valores é {sum(valores)}")

print("=" * 60)

# For e suas caracteristicas
for i in range(1, 52, 10):
    print(f"O valor é {i}")

print("=" * 60)

arquivos = ["vendas.csv", "compras.csv", "funcionarios.csv"]
for indice, arquivo in enumerate(arquivos, start=1):
    print(f"{indice}: {arquivo}")

print("=" * 60)

funcionario = ["Enzo", "Emmilly", "Jose", "Rose"]
vendas = [1000, 4000, 10000]
metas = [1233, 1233]

for vendendor, venda, meta in zip(funcionario, vendas, metas):
    status = "Meta atingida" if venda > meta else "Meta não atingida"
    print(f"Vendendor: {vendendor}")
    print(f"Status: {status}")

print("=" * 60)
