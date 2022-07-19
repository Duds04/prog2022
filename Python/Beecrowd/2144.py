w1 = 1
w2 = 1
r = 1
media_total = 0
cont = 0

while True:
    w1, w2, r = map(int, input().split(' '))
    if ((w1 != 0) and (w2 != 0) and (r != 0)):
        M = w1 * (1 + (r / 30))
        M += w2 * (1 + (r / 30))
        M = M / 2
        media_total += M
        cont += 1
        if (M >= 1 and M < 13):
            print("Nao vai da nao")
        elif (M < 14):
            print("E 13")
        elif (M < 40):
            print("Bora, hora do show! BIIR!")
        elif (M <= 60):
            print("Ta saindo da jaula o monstro!")
        elif (M > 60):
            print("AQUI E BODYBUILDER!!")
    else:
        break

media_total = media_total / cont
if (media_total > 40):
    print("\nAqui nois constroi friba rapaz! Nao e agua com musculo!")