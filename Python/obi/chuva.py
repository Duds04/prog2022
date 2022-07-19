N = int(input())
S = int(input())
aux = input().split(' ')
cont = 0
vetor = []
for i in range(len(aux)):
    vetor.append(int(aux[i]))

for i in range(len(vetor)):
    contando = 0
    if(vetor[i]==S):
        cont +=1
    if(i>0) and ((vetor[i]+vetor[i-1])==S):
        cont +=1
    elif i==0 and ((vetor[i]+vetor[i+1]) == S):
        cont += 1
    if(vetor[i]>0):
        while True:
            print(i, len(vetor)-(i+1))
            for j in (i, (len(vetor)-(i+1))):
                soma =+ vetor[j]
            print("soma ", soma)
            if (soma == S):
                cont += 1
                break
            if (contando > len(vetor)):
                break
            contando +=1
            soma = 0
if(sum(vetor) == S):
        cont +=1

print(cont)
