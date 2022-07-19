#13

num = 1
soma = 0
produto = 1

while (num>0):
    num = int(input("Digite um nº (maior que 0): "))
    if(num>0):
        if(num%2==0):
            soma += num
        else:
            produto *= num

print(f"Soma: {soma}")
print(f"Produto: {produto}")
