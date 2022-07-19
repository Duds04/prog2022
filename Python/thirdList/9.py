#09
i = 0
lista = []

while (i != -1):
     i = int(input("Digite um nº positivo (p/ parar digite -1): "))
     if(i>0):
        lista.append(i)

print(f"Media: {sum(lista)/len(lista)}")
