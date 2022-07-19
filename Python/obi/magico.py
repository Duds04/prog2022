N = int(input())
aux1 = -1
aux2 = -1
g_q1 = g_q2 = calculo = cont = 0
quadrado = []

for j in range(N):
    vetor = input().split(' ')
    for i in range(len(vetor)):
        vetor[i] = int(vetor[i])
    quadrado.append(vetor)

for i in range(N):
    for j in range(N):
        if(quadrado[i][j] == 0):
            aux1 = i
            aux2 = j
            break

g_q1 = sum(quadrado[aux1])
if (aux1>0):
    g_q2 = sum(quadrado[aux1-1])
else:
    g_q2 = sum(quadrado[aux1 + 1])

calculo = g_q2 - g_q1

print(calculo)
print(aux1+1)
print(aux2+1)
