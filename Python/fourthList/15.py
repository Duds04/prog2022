cont = 0
for i in range(10):
    N = float(input("Digite um número: "))
    if(N>=10 and N<=20):
        cont +=1

print(f"{cont} valores entre [10,20]")