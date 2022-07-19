n = int(input())
posicao = 1
primeiro = 1
segundo = 4
terceiro = 4

while posicao<n:
    if(n>=posicao):
        print(primeiro)
        primeiro +=1
        posicao +=1
    if (n >= posicao):
        print(segundo)
        segundo += 1
        posicao += 1
    if (n >= posicao):
        print(terceiro)
        terceiro += 1
        posicao += 1