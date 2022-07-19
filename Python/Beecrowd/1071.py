X = int(input())
Y = int(input())

soma = 0
lista = []

if(X<Y):
    if(X%2!=0):
        X=+1
    lista = list(range(X+1, Y, 2))
else:
    if(Y%2!=0):
        Y+=1
    lista = list(range(Y+1, X, 2))

print(sum(lista))
