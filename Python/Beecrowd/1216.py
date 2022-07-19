try:
    distancia_total = 0
    cont = 0
    while True:
        nome = input()
        distancia = int(input())
        distancia_total += distancia
        cont +=1
except EOFError:
    print(f"{(distancia_total / cont):.1f}")
