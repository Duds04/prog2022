N = int(input())
M = int(input())
S = int(input())
soma = 0
aux = -1

for i in range(N, M+1):
    atual = str(i)
    for j in range(len(atual)):
        soma += int(atual[j])
    if (soma == S):
        aux = i
    soma = 0

print(aux)

