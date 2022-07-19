n = int(input("Digite o nº de termos: "))
anterior, atual, prox = 0, n

if(n>2):
    anterior = int(input("Digite o 1º termo: "))
    atual = int(input("Digite o 2º termo: "))
    if(n>=1):
        print(anterior)
    if(n>=2):
        print(atual)

    for i in range(2, n):
        prox = anterior + atual
        print(prox)
        anterior = atual
        atual = prox
else:
    print("É necessário, pelo menos, três termos")