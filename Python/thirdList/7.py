#07

qnt_pares = 0
qnt_impares = 0

for i in range(200):
    num = float(input(f"Digite o {i+1} nº:"))
    if(num%2==0):
        qnt_pares +=1
    else:
        qnt_impares +=1

print(f"Quantidade de pares: {qnt_pares}")
print(f"Quantidade de impares: {qnt_impares}")