print("=" * 60)
def saudacoes(nome: str, saudacao="Ola"):
    print(f"{saudacao}, {nome}")

nome = input("Qual é seu nome: ")
saudacoes(nome=nome)
print("=" * 60)

def eh_maior_idade(idade: int, limite = 18):
    print(f"Você é {'menor' if idade < limite else 'maior'} de idade")

idade = int(input("Qual é sua idade: "))
eh_maior_idade(idade=idade)

print("=" * 60)

def calcular_frete(peso: float, distancia_km: float, expresso=False) -> float:
    return peso * 2 + distancia_km * 0.5 if expresso else (peso * 2 + distancia_km * 0.5) * 2

print("Vamos precisar saber alguns dados para a entrega: ")
peso = float(input("Qual é o peso da mercadoria: "))
distancia = float(input("Qual é a distancia em KM: "))
expresso = bool(input("É expresso? (Enter) para não e qualquer outro para sim: "))

print("=" * 60)
print(f"O valor do frete será R$: {calcular_frete(peso=peso, distancia_km=distancia, expresso=expresso):,.2f}")

print("=" * 60)

def dividir_seguro(a, b):
    if b == 0:
        return None
    else:
        return a/b
    
primeiro_numero = float(input("Digite um numero: ")) 
segundo_numero = float(input("Digite um numero: ")) 

resposta = dividir_seguro(primeiro_numero, segundo_numero)
print(f"A divisao dos dois numeros: {resposta if resposta else 'não existe'}")

print("=" * 60)

lista_numeros = (1, 2, 34, 543, 12, 453, 14, 102)

def operacoes(lista):
    return sum(lista), sum(lista) / len(lista), min(lista), max(lista)

operado = operacoes(lista_numeros)
print(f"Soma: {operado[0]}")
print(f"Média: {operado[1]}")
print(f"Minimo: {operado[2]}")
print(f"Maximo: {operado[3]}")

print("=" * 60)