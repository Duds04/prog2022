#03

lista = []

for i in range(1000):
    lista.append(float(input("Digite um número: ")))

print(f"Valor mínimo: {min(lista)}")
print(f"Valor máximo: {max(lista)}")