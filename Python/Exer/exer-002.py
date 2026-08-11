print("Digite somente numeros")

preco_unidade = float(input("Preço unitário: "))
quantidade = int(input("Quantidade: "))
IPI = 1.12

sub_total = preco_unidade * quantidade

total = sub_total * IPI

print("=" * 60)
print(f"Preço total sem IPI: {sub_total}")
print(f"Preço total com IPI de 12%: {total:,.2f}")
print("=" * 60)